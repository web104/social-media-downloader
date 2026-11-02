from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import yt_dlp
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Social Media Downloader API",
    description="Download videos and thumbnails from YouTube, Instagram, TikTok, Facebook, Twitter/X",
    version="1.0.0"
)

# Configure CORS - Allow all origins for public API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DownloadRequest(BaseModel):
    url: str
    format: str = "best"  # best, audio, video, thumbnail

class VideoInfo(BaseModel):
    title: str
    thumbnail: str
    duration: int
    uploader: str
    formats: list

@app.get("/")
async def root():
    return {
        "message": "Social Media Downloader API",
        "status": "active",
        "supported_platforms": [
            "YouTube",
            "Instagram",
            "TikTok",
            "Facebook",
            "Twitter/X",
            "and many more via yt-dlp"
        ],
        "endpoints": {
            "/info": "GET video information",
            "/download": "POST to get download URL",
            "/health": "API health check"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "running"}

@app.post("/info")
async def get_video_info(request: DownloadRequest):
    """Get video information without downloading"""
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            logger.info(f"Extracting info for URL: {request.url}")
            info = ydl.extract_info(request.url, download=False)
            
            # Extract formats information
            formats = []
            if 'formats' in info:
                for f in info['formats']:
                    formats.append({
                        'format_id': f.get('format_id', ''),
                        'ext': f.get('ext', ''),
                        'quality': f.get('format_note', 'unknown'),
                        'filesize': f.get('filesize', 0),
                        'url': f.get('url', '')
                    })
            
            return {
                "success": True,
                "data": {
                    "title": info.get('title', 'Unknown'),
                    "thumbnail": info.get('thumbnail', ''),
                    "duration": info.get('duration', 0),
                    "uploader": info.get('uploader', 'Unknown'),
                    "description": info.get('description', '')[:200],
                    "view_count": info.get('view_count', 0),
                    "formats": formats[:10]  # Limit to first 10 formats
                }
            }
    except Exception as e:
        logger.error(f"Error extracting info: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Failed to extract video info: {str(e)}")

@app.post("/download")
async def get_download_url(request: DownloadRequest):
    """Get direct download URL for the video"""
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
        }
        
        # Configure format based on request
        if request.format == "audio":
            ydl_opts['format'] = 'bestaudio/best'
        elif request.format == "video":
            ydl_opts['format'] = 'bestvideo+bestaudio/best'
        elif request.format == "thumbnail":
            ydl_opts['skip_download'] = True
        else:
            ydl_opts['format'] = 'best'
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            logger.info(f"Processing download for URL: {request.url}")
            info = ydl.extract_info(request.url, download=False)
            
            if request.format == "thumbnail":
                return {
                    "success": True,
                    "type": "thumbnail",
                    "data": {
                        "title": info.get('title', 'Unknown'),
                        "thumbnail_url": info.get('thumbnail', ''),
                        "thumbnails": info.get('thumbnails', [])
                    }
                }
            
            # Get the best format URL
            if 'formats' in info:
                # Try to get the requested format
                format_url = None
                for f in info['formats']:
                    if f.get('url'):
                        format_url = f['url']
                        break
                
                if not format_url and 'url' in info:
                    format_url = info['url']
                
                return {
                    "success": True,
                    "type": "video" if request.format != "audio" else "audio",
                    "data": {
                        "title": info.get('title', 'Unknown'),
                        "download_url": format_url,
                        "thumbnail": info.get('thumbnail', ''),
                        "duration": info.get('duration', 0),
                        "ext": info.get('ext', 'mp4')
                    }
                }
            else:
                raise HTTPException(status_code=400, detail="No suitable format found")
                
    except Exception as e:
        logger.error(f"Error processing download: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Failed to process download: {str(e)}")

@app.get("/supported-sites")
async def get_supported_sites():
    """Get list of supported websites"""
    try:
        extractors = yt_dlp.extractor.gen_extractors()
        sites = list(set([e.IE_NAME for e in extractors if hasattr(e, 'IE_NAME')]))
        return {
            "success": True,
            "count": len(sites),
            "sites": sorted(sites)[:50]  # Return first 50 popular ones
        }
    except Exception as e:
        logger.error(f"Error getting supported sites: {str(e)}")
        return {
            "success": False,
            "error": str(e)
        }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
