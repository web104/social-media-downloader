# 🎬 Social Media Video Downloader

A professional, all-in-one social media video and thumbnail downloader with an integrated admin panel for complete control.

## ✨ Features

### Core Functionality
- ✅ Download videos from **1000+ websites**
- ✅ Support for YouTube, Instagram, TikTok, Facebook, Twitter/X, and more
- ✅ Multiple format options (Best Quality, Video Only, Audio/MP3, Thumbnail)
- ✅ Fast and efficient powered by yt-dlp
- ✅ Modern, responsive UI with mobile support

### Admin Panel
- 🔐 Secure login system (default: admin/admin)
- ⚙️ Full site customization (name, tagline, logo)
- 💰 Google AdSense integration
- 💵 Download monetization with click-based redirects
- 📝 Ads.txt management
- 🔒 Password change functionality
- ⏰ Automated cron job for cache cleanup
- 📊 Dashboard with statistics

### SEO & Monetization
- 🔍 SEO-optimized with dynamic meta tags
- 📄 Legal pages (Privacy, Terms, About, Contact, Disclaimer)
- 💰 AdSense auto-ads support
- 💵 Monetization link override system
- 📊 Google Search Console ready

## 🚀 Deployment

### Backend (Render.com)

The backend is automatically configured via `render.yaml`:

1. Connect your GitHub repository to Render
2. Render will auto-detect the configuration
3. Deploy and copy your backend URL

### Frontend (GitHub Pages or Any Static Host)

1. Enable GitHub Pages in repository settings
2. Update `API_BASE_URL` in `index.html` with your Render backend URL
3. Your site will be live

## 🔧 Configuration

### First-Time Setup

1. **Access Admin Panel**: Navigate to `/admin.html`
2. **Login**: Use default credentials
   - Username: `admin`
   - Password: `admin`
3. **Change Password**: Immediately change the default password
4. **Configure Site**:
   - Website name and tagline
   - Upload logo (URL)
   - Add AdSense code
   - Set up ads.txt
   - Enable monetization (optional)

### Admin Panel URL

Access at: `https://your-domain.com/admin.html` or `https://your-domain.com/admin500.html`

### Cron Job Setup

1. Go to Admin Panel → Cron Job section
2. Copy the cron URL
3. Create a cron job at [cron-job.org](https://cron-job.org) or similar
4. Schedule: Every 12 hours
5. Test using the "Test Cron Job" button

## 📡 API Endpoints

### Public Endpoints

- `GET /` - API information
- `GET /health` - Health check
- `GET /api/config` - Public configuration
- `POST /api/info` - Get video information
- `POST /api/download` - Get download URL
- `GET /ads.txt` - AdSense ads.txt file

### Admin Endpoints (Requires Authentication)

- `POST /api/admin/login` - Admin login
- `GET /api/admin/config` - Get admin configuration
- `POST /api/admin/config` - Update configuration
- `POST /api/admin/password` - Change password
- `POST /api/admin/test-cron` - Test cron job
- `GET /api/cron/cleanup?key=SECRET` - Automated cleanup

## 💰 Monetization System

The admin panel includes a powerful monetization system:

1. **Enable Monetization**: Toggle in admin panel
2. **Set Redirect Link**: Add your offer/sponsor link
3. **Configure Clicks**: Set how many clicks before direct download (default: 2)
4. **User Experience**: Users are redirected to your link for N clicks, then get direct download

## 🎨 Customization

### Site Branding
- Change website name and tagline
- Upload custom logo
- All updates reflect immediately on frontend

### AdSense Integration
- Add your AdSense script in admin panel
- Configure ads.txt for ad verification
- Strategic ad placements: header, sidebar, footer

## 📋 Supported Platforms

YouTube, Instagram, TikTok, Facebook, Twitter/X, Vimeo, Dailymotion, Reddit, LinkedIn, Pinterest, Twitch, Snapchat, and 1000+ more websites.

Full list available at: `/api/supported-sites`

## 🔒 Security

- Password hashing with SHA-256
- Session-based authentication
- Token expiration (24 hours)
- Secure admin endpoints
- Cron job key protection

## 🛠️ Technical Stack

- **Backend**: Python, FastAPI, yt-dlp
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Hosting**: Render.com (Backend), GitHub Pages (Frontend)
- **Admin**: Custom-built admin panel

## 📖 Legal Pages

The application includes essential legal pages:

- Privacy Policy
- Terms of Service
- About Us
- Contact
- Disclaimer
- DMCA Policy

## ⚡ Performance

- Fast video extraction with yt-dlp
- Cached responses for better performance
- Automatic cleanup to manage storage
- Mobile-optimized and responsive

## 🆘 Troubleshooting

### Backend Not Starting
- Check Render logs
- Verify Python version 3.11+
- Ensure all dependencies installed

### Download Not Working
- Some videos may be geo-restricted
- Platform may have changed API
- Check backend logs for errors

### Admin Panel Access
- Use `/admin.html` to access
- Clear browser cache if issues persist
- Check session token validity

## 📞 Support

For issues and questions:
- Check the admin panel dashboard
- Review backend logs on Render
- Test cron job functionality

## 📄 License

MIT License - Free to use and modify

---

**Built with ❤️ for creators and developers**

Powered by [yt-dlp](https://github.com/yt-dlp/yt-dlp)
