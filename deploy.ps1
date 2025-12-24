# PremierZone Deployment Script
# This script will guide you through deploying your project

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "PremierZone Deployment Helper" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if CLIs are installed
Write-Host "Checking CLI tools..." -ForegroundColor Yellow
$railwayInstalled = Get-Command railway -ErrorAction SilentlyContinue
$vercelInstalled = Get-Command vercel -ErrorAction SilentlyContinue

if (-not $railwayInstalled) {
    Write-Host "Installing Railway CLI..." -ForegroundColor Yellow
    npm install -g @railway/cli
}

if (-not $vercelInstalled) {
    Write-Host "Installing Vercel CLI..." -ForegroundColor Yellow
    npm install -g vercel
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Step 1: Deploy Backend to Railway" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "1. Open your browser and go to: https://railway.app" -ForegroundColor White
Write-Host "2. Sign up/login with GitHub" -ForegroundColor White
Write-Host "3. Click 'New Project' -> 'Deploy from GitHub repo'" -ForegroundColor White
Write-Host "4. Select your 'Premier-Zone' repository" -ForegroundColor White
Write-Host "5. Set Root Directory to: BackendPy" -ForegroundColor White
Write-Host "6. Add PostgreSQL database: New -> Database -> PostgreSQL" -ForegroundColor White
Write-Host "7. Copy the DATABASE_URL from the database service" -ForegroundColor White
Write-Host "8. Add environment variable in backend service:" -ForegroundColor White
Write-Host "   - Name: DATABASE_URL" -ForegroundColor Cyan
Write-Host "   - Value: (paste the PostgreSQL URL)" -ForegroundColor Cyan
Write-Host ""
$backendReady = Read-Host "Press Enter when backend is deployed and you have the backend URL"

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Step 2: Deploy Frontend to Vercel" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "1. Open your browser and go to: https://vercel.com" -ForegroundColor White
Write-Host "2. Sign up/login with GitHub" -ForegroundColor White
Write-Host "3. Click 'Add New' -> 'Project'" -ForegroundColor White
Write-Host "4. Import your 'Premier-Zone' repository" -ForegroundColor White
Write-Host "5. Set Root Directory to: Frontend" -ForegroundColor White
Write-Host "6. Framework Preset: Create React App" -ForegroundColor White
Write-Host "7. Add Environment Variable:" -ForegroundColor White
Write-Host "   - Name: REACT_APP_API_URL" -ForegroundColor Cyan
Write-Host "   - Value: (your Railway backend URL from Step 1)" -ForegroundColor Cyan
Write-Host "8. Click 'Deploy'" -ForegroundColor White
Write-Host ""
$frontendReady = Read-Host "Press Enter when frontend is deployed and you have the frontend URL"

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Step 3: Update CORS Settings" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Go back to Railway and update ALLOWED_ORIGINS:" -ForegroundColor White
Write-Host "Add your Vercel frontend URL to the allowed origins" -ForegroundColor White
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Deployment Complete!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Your website should now be live!" -ForegroundColor Green
Write-Host "Don't forget to update README.md with your actual URLs" -ForegroundColor Yellow

