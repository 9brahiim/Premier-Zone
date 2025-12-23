# Deployment Guide

This guide will help you deploy your PremierZone application to production.

## Overview

- **Frontend**: Deploy to Vercel (free, easy)
- **Backend**: Deploy to Railway (free tier available)
- **Database**: Railway PostgreSQL (included with Railway)

## Step 1: Deploy Backend to Railway

### 1.1 Create Railway Account
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project"

### 1.2 Add PostgreSQL Database
1. In your Railway project, click "New"
2. Select "Database" → "PostgreSQL"
3. Railway will automatically create a PostgreSQL database
4. Copy the `DATABASE_URL` from the database service (it will be something like `postgresql://postgres:password@host:port/railway`)

### 1.3 Deploy Backend
1. In Railway project, click "New" → "GitHub Repo"
2. Select your `Premier-Zone` repository
3. Railway will detect it's a Python project
4. Set the **Root Directory** to `BackendPy`
5. Add environment variables:
   - `DATABASE_URL`: Paste the PostgreSQL URL from step 1.2
   - `ALLOWED_ORIGINS`: Will be set after frontend deployment (see Step 2.4)
6. Railway will automatically deploy your backend
7. Once deployed, copy your backend URL (e.g., `https://your-backend.railway.app`)

### 1.4 Update CORS
After deploying frontend, update `ALLOWED_ORIGINS` in Railway:
- Go to your backend service → Variables
- Update `ALLOWED_ORIGINS` to: `http://localhost:3000,https://your-frontend.vercel.app`

## Step 2: Deploy Frontend to Vercel

### 2.1 Create Vercel Account
1. Go to [vercel.com](https://vercel.com)
2. Sign up with GitHub
3. Click "Add New" → "Project"

### 2.2 Import Repository
1. Select your `Premier-Zone` repository
2. Set **Root Directory** to `Frontend`
3. Framework Preset: **Create React App**

### 2.3 Configure Environment Variables
Add this environment variable:
- **Name**: `REACT_APP_API_URL`
- **Value**: Your Railway backend URL (e.g., `https://your-backend.railway.app`)

### 2.4 Deploy
1. Click "Deploy"
2. Vercel will build and deploy your frontend
3. Once deployed, copy your frontend URL (e.g., `https://premier-zone.vercel.app`)

### 2.5 Update Backend CORS
Go back to Railway and update `ALLOWED_ORIGINS`:
```
http://localhost:3000,https://your-frontend.vercel.app
```

## Step 3: Update README

Update your README.md with your actual deployed URLs:
1. Replace `https://your-deployed-website-url.com/` with your Vercel frontend URL
2. Update the note about backend hosting

## Step 4: Populate Database (Optional)

If you have player data to import:
1. Connect to your Railway PostgreSQL database
2. Use the data scraping script or import your CSV file
3. Or use the API endpoints to add players

## Troubleshooting

### Backend Issues
- **Database connection errors**: Check `DATABASE_URL` is correct in Railway
- **CORS errors**: Make sure `ALLOWED_ORIGINS` includes your frontend URL
- **Port issues**: Railway sets `$PORT` automatically, don't hardcode it

### Frontend Issues
- **API calls failing**: Check `REACT_APP_API_URL` is set correctly in Vercel
- **Build errors**: Make sure all dependencies are in `package.json`
- **Routing issues**: Vercel config handles React Router automatically

## Free Tier Limits

- **Railway**: $5 free credit/month (usually enough for small projects)
- **Vercel**: Free tier is generous for personal projects
- **PostgreSQL**: Included with Railway

## Next Steps

- Set up custom domain (optional)
- Add CI/CD for automatic deployments
- Set up monitoring and logging
- Configure backups for database

