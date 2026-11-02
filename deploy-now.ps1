$apiKey = "rnd_dbnNNmCgrmr8asIimKudyVxVTzq4"
$headers = @{
    "Authorization" = "Bearer $apiKey"
    "Content-Type" = "application/json"
}

$body = @"
{
  "type": "web_service",
  "name": "social-media-downloader",
  "ownerId": "tea-dbhiu0o473hc73a4ff2g",
  "repo": "https://github.com/web104/social-media-downloader",
  "autoDeploy": "yes",
  "branch": "main",
  "serviceDetails": {
    "env": "python",
    "region": "oregon",
    "plan": "free",
    "buildCommand": "pip install -r requirements.txt",
    "startCommand": "uvicorn main:app --host 0.0.0.0 --port \$PORT",
    "envSpecificDetails": {
      "buildCommand": "pip install -r requirements.txt",
      "startCommand": "uvicorn main:app --host 0.0.0.0 --port \$PORT"
    }
  }
}
"@

Write-Host "🚀 Deploying to Render.com..." -ForegroundColor Yellow
Write-Host ""

try {
    $response = Invoke-RestMethod -Uri "https://api.render.com/v1/services" -Method Post -Headers $headers -Body $body
    Write-Host "✅ SUCCESS! Service deployed!" -ForegroundColor Green
    Write-Host ""
    Write-Host "📦 Service Details:" -ForegroundColor Cyan
    Write-Host "   Name: $($response.service.name)" -ForegroundColor White
    Write-Host "   ID: $($response.service.id)" -ForegroundColor White
    
    # Extract URL
    $serviceUrl = "https://$($response.service.name).onrender.com"
    Write-Host "   URL: $serviceUrl" -ForegroundColor Green
    Write-Host ""
    Write-Host "📊 Dashboard: https://dashboard.render.com/web/$($response.service.id)" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "⏳ Deployment in progress... This may take 3-5 minutes" -ForegroundColor Yellow
    Write-Host ""
    
    # Save URL for later use
    $serviceUrl | Out-File -FilePath "c:\Users\Admin\Desktop\render\backend-url.txt" -Encoding UTF8
    
} catch {
    Write-Host "❌ ERROR: $($_.Exception.Message)" -ForegroundColor Red
    if ($_.Exception.Response) {
        $stream = $_.Exception.Response.GetResponseStream()
        $reader = New-Object System.IO.StreamReader($stream)
        $reader.BaseStream.Position = 0
        $errorBody = $reader.ReadToEnd()
        Write-Host "Details: $errorBody" -ForegroundColor Yellow
    }
}
