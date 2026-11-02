# Automated Render.com Deployment Script
# Usage: .\auto-deploy-render.ps1 -RenderApiKey "your_render_api_key_here"

param(
    [Parameter(Mandatory=$true)]
    [string]$RenderApiKey
)

Write-Host "🚀 Starting Automated Render.com Deployment..." -ForegroundColor Cyan
Write-Host ""

# Configuration
$apiUrl = "https://api.render.com/v1/services"
$headers = @{
    "Authorization" = "Bearer $RenderApiKey"
    "Content-Type" = "application/json"
}

# Service configuration
$serviceConfig = @{
    type = "web_service"
    name = "social-media-downloader-api"
    repo = "https://github.com/web104/social-media-downloader"
    branch = "main"
    runtime = "python"
    buildCommand = "pip install -r requirements.txt"
    startCommand = "uvicorn main:app --host 0.0.0.0 --port `$PORT"
    envVars = @(
        @{
            key = "PYTHON_VERSION"
            value = "3.11.0"
        }
    )
    region = "oregon"
    plan = "free"
    autoDeploy = "yes"
} | ConvertTo-Json -Depth 10

Write-Host "📦 Creating Render service..." -ForegroundColor Yellow

try {
    $response = Invoke-RestMethod -Uri $apiUrl -Method Post -Headers $headers -Body $serviceConfig
    
    Write-Host "✅ Service created successfully!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Service Details:" -ForegroundColor Cyan
    Write-Host "  Name: $($response.service.name)" -ForegroundColor White
    Write-Host "  ID: $($response.service.id)" -ForegroundColor White
    Write-Host "  URL: https://$($response.service.name).onrender.com" -ForegroundColor Green
    Write-Host ""
    Write-Host "🔄 Deployment started. This may take 3-5 minutes..." -ForegroundColor Yellow
    Write-Host "📊 Monitor progress at: https://dashboard.render.com/web/$($response.service.id)" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "⚠️  IMPORTANT: Update index.html with your backend URL:" -ForegroundColor Magenta
    Write-Host "   const API_BASE_URL = 'https://$($response.service.name).onrender.com';" -ForegroundColor White
    
} catch {
    Write-Host "❌ Error creating service: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please check:" -ForegroundColor Yellow
    Write-Host "  1. Your Render API key is valid" -ForegroundColor White
    Write-Host "  2. You have permission to create services" -ForegroundColor White
    Write-Host "  3. The repository is accessible" -ForegroundColor White
    exit 1
}

Write-Host ""
Write-Host "✨ Deployment initiated successfully!" -ForegroundColor Green
