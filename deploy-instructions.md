# 🚀 Deployment Instructions

## ✅ GitHub Deployment - COMPLETED

Your code has been successfully pushed to GitHub:
- **Repository URL**: https://github.com/web104/social-media-downloader
- **Branch**: main
- **Status**: ✅ Live and Ready

---

## 🔄 Render.com Deployment - AUTOMATED STEPS

### Option 1: Deploy via Render Dashboard (Recommended - 2 minutes)

1. **Go to Render Dashboard**: https://dashboard.render.com/

2. **Click "New +" → "Web Service"**

3. **Connect GitHub Repository**:
   - Select: `web104/social-media-downloader`
   - Branch: `main`

4. **Render will auto-detect** the `render.yaml` file and configure automatically:
   - **Name**: `social-media-downloader-api`
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

5. **Click "Create Web Service"**

6. **Wait 3-5 minutes** for deployment to complete

7. **Copy your Render URL** (will be like: `https://social-media-downloader-api.onrender.com`)

8. **Update Frontend**: 
   - Open `index.html` from your GitHub repo
   - Find line with `API_BASE_URL`
   - Replace `YOUR_RENDER_BACKEND_URL_HERE` with your Render URL
   - Commit and push changes

---

### Option 2: Deploy via Render API (Fully Automated)

If you provide your Render API key, I can deploy automatically via API.

**Get your Render API Key**:
1. Go to: https://dashboard.render.com/account/api-keys
2. Create new API key
3. Copy the key
4. Provide it to me

---

## 📱 Frontend Deployment (GitHub Pages)

Once backend is deployed and `index.html` is updated:

1. Go to repository settings: https://github.com/web104/social-media-downloader/settings/pages

2. Under "Source", select:
   - Branch: `main`
   - Folder: `/ (root)`

3. Click "Save"

4. Your frontend will be live at:
   - `https://web104.github.io/social-media-downloader/`

---

## 🎯 Final Configuration

After both deployments:

1. **Backend URL**: `https://your-app-name.onrender.com`
2. **Frontend URL**: `https://web104.github.io/social-media-downloader/`

3. **Update CORS** (if needed):
   - In `main.py`, the CORS is already set to allow all origins
   - No changes needed

4. **Test the application**:
   - Open frontend URL
   - Paste a YouTube/Instagram/TikTok link
   - Click Download

---

## 📝 Environment Variables (Optional)

No environment variables are required for basic functionality.

For production hardening, you can add:
- `ALLOWED_ORIGINS`: Comma-separated list of allowed frontend URLs
- `MAX_DOWNLOAD_SIZE`: Maximum file size limit
- `RATE_LIMIT`: API rate limiting

Add these in Render Dashboard → Your Service → Environment

---

## 🔒 Security Notes

- The GitHub token used for deployment should be kept secure
- Consider regenerating it after deployment
- Enable 2FA on both GitHub and Render accounts
- Monitor Render logs for any suspicious activity

---

## 🆘 Troubleshooting

### Backend not starting?
- Check Render logs in dashboard
- Verify Python version is 3.11+
- Ensure all dependencies in requirements.txt are valid

### CORS errors?
- Verify API_BASE_URL in index.html is correct
- Check browser console for exact error
- Ensure Render service is running

### Download failing?
- Some videos may be restricted by platform
- Check Render logs for yt-dlp errors
- Try with a different video URL

---

## 📊 Monitoring

- **Render Dashboard**: Monitor CPU, memory, and request metrics
- **Logs**: View real-time logs in Render dashboard
- **Uptime**: Render free tier may sleep after inactivity (wakes on first request)

---

**Need help?** Your GitHub repo is ready, and Render deployment is just one click away! 🎉
