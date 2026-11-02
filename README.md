# Social Media Video Downloader

An all-in-one social media video and thumbnail downloader supporting YouTube, Instagram, TikTok, Facebook, Twitter/X, and 1000+ more websites.

## Features

- ✅ Download videos from 1000+ websites
- ✅ Support for YouTube, Instagram, TikTok, Facebook, Twitter/X
- ✅ Multiple format options (Best Quality, Video Only, Audio Only, Thumbnail)
- ✅ Fast and efficient powered by yt-dlp
- ✅ Clean and modern UI
- ✅ No registration required
- ✅ Completely free

## Architecture

### Backend (Python FastAPI + yt-dlp)
- Deployed on Render.com
- RESTful API endpoints
- Powered by yt-dlp for video extraction

### Frontend (Static HTML/CSS/JS)
- Hosted on GitHub Pages
- Responsive design
- Modern UI/UX

## API Endpoints

### GET `/`
Health check and API information

### GET `/health`
Service health status

### POST `/info`
Get video information without downloading

Request body:
```json
{
  "url": "https://youtube.com/watch?v=..."
}
```

### POST `/download`
Get download URL for video/audio/thumbnail

Request body:
```json
{
  "url": "https://youtube.com/watch?v=...",
  "format": "best"  // Options: best, video, audio, thumbnail
}
```

### GET `/supported-sites`
Get list of supported websites

## Local Development

### Backend Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Update the API URL in `index.html`:
```javascript
const API_BASE_URL = 'http://localhost:8000';
```

2. Open `index.html` in your browser

## Deployment

### Backend (Render.com)

1. Push code to GitHub
2. Connect your GitHub repository to Render.com
3. Render will automatically detect `render.yaml` and deploy

### Frontend (GitHub Pages)

1. Push `index.html` to your GitHub repository
2. Enable GitHub Pages in repository settings
3. Update the API_BASE_URL in `index.html` with your Render backend URL

## Technologies Used

- **Backend**: Python, FastAPI, yt-dlp, uvicorn
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Hosting**: Render.com (Backend), GitHub Pages (Frontend)

## Supported Platforms

YouTube, Instagram, TikTok, Facebook, Twitter/X, Vimeo, Dailymotion, Reddit, LinkedIn, Pinterest, Twitch, and 1000+ more websites.

Full list available via `/supported-sites` endpoint.

## License

MIT License - Feel free to use and modify

## Credits

Powered by [yt-dlp](https://github.com/yt-dlp/yt-dlp)
