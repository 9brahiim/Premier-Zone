# Quick Deployment Guide

Follow these steps to deploy your project in about 15 minutes!

## 🚀 Step 1: Deploy Backend (Railway)

1. **Go to Railway**: https://railway.app
2. **Sign up** with GitHub
3. **Create New Project** → "Deploy from GitHub repo"
4. **Select** your `Premier-Zone` repository
5. **Set Root Directory** to: `BackendPy`
6. **Add PostgreSQL Database**:
   - Click "New" → "Database" → "PostgreSQL"
   - Copy the `DATABASE_URL` (you'll need this)
7. **Add Environment Variable**:
   - Go to your backend service → Variables
   - Add: `DATABASE_URL` = (paste the PostgreSQL URL)
8. **Wait for deployment** (takes 2-3 minutes)
9. **Copy your backend URL** (e.g., `https://your-backend.railway.app`)

## 🎨 Step 2: Deploy Frontend (Vercel)

1. **Go to Vercel**: https://vercel.com
2. **Sign up** with GitHub
3. **Add New Project** → Import your `Premier-Zone` repo
4. **Configure**:
   - Root Directory: `Frontend`
   - Framework Preset: **Create React App**
5. **Add Environment Variable**:
   - Name: `REACT_APP_API_URL`
   - Value: Your Railway backend URL from Step 1
6. **Click Deploy** (takes 1-2 minutes)
7. **Copy your frontend URL** (e.g., `https://premier-zone.vercel.app`)

## 🔗 Step 3: Update CORS

1. **Go back to Railway**
2. **Backend service** → Variables
3. **Add/Update** `ALLOWED_ORIGINS`:
   ```
   http://localhost:3000,https://your-frontend.vercel.app
   ```
   (Replace with your actual Vercel URL)

## ✅ Done!

Your website is now live! Update your README.md with the actual URLs.

**Need help?** Check `DEPLOYMENT.md` for detailed troubleshooting.

