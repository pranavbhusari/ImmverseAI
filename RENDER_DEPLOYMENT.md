# Render Deployment Guide - ImmverseAI

This guide walks you through deploying the **ImmverseAI** Multilingual QnA Generation System on **Render**, a modern cloud platform supporting Docker containers.

---

## Prerequisites

### Local Setup
- **Docker & Docker Compose** installed ([Download Docker Desktop](https://www.docker.com/products/docker-desktop))
- **Render Account** ([Free at render.com](https://render.com))
- **GitHub Account** with repository pushed (see GITHUB_SETUP.md)
- **Groq API Key** (get free 10k req/day tier from [console.groq.com](https://console.groq.com))

---

## Part 1: Test Deployment Locally

### 1.1 Build and Run Docker Container Locally

```powershell
# Navigate to project directory
cd c:\Users\Rutika\Desktop\ImmverseAI

# Build Docker image (first time only)
docker build -t immverse-ai:latest .

# Run with environment variable
docker run -p 8501:8501 -e GROQ_API_KEY="your-groq-api-key-here" immverse-ai:latest
```

App will be available at: **http://localhost:8501**

### 1.2 Use Docker Compose (Easier)

```powershell
# Create .env in project root with your API key
# Add this line:
# GROQ_API_KEY=your-groq-api-key-here

# Then run:
docker-compose up --build

# App runs at http://localhost:8501
```

### 1.3 Stop Docker Container

```powershell
# Using docker-compose
docker-compose down

# Or manually
docker stop immverse-ai
```

---

## Part 2: Deploy to Render

### 2.1 Create Render Account & Connect GitHub

1. Go to [render.com](https://render.com) and sign up (free tier available)
2. Click **Dashboard** in top-right
3. Click **Connect GitHub** in "Deployment" section
4. Authorize Render to access your GitHub repos
5. Grant `ImmverseAI` repo access

### 2.2 Create Web Service on Render

1. In Render Dashboard, click **New +** → **Web Service**
2. Select your `ImmverseAI` repository
3. Fill in settings:

| Setting | Value |
|---------|-------|
| **Name** | immverse-ai |
| **Environment** | Docker |
| **Region** | Select closest to you |
| **Branch** | main |

4. Click **Create Web Service**
   - Render will detect `Dockerfile` automatically
   - Takes ~5-10 minutes for first deployment

### 2.3 Add Environment Variables

1. In Render Dashboard → Your Service → **Environment**
2. Click **Add a New Variable**
3. Add these variables:

| Key | Value |
|-----|-------|
| `GROQ_API_KEY` | `<your-10k-free-tier-key-from-console.groq.com>` |
| `OUTPUT_DIR` | `./output` |

4. Click **Save**
5. Service will auto-redeploy with new variables

### 2.4 Access Your Deployed App

- **URL Format**: `https://immverse-ai.onrender.com`
- Exact URL shown in Render Dashboard under "Service URL"
- App accessible immediately after deployment completes

---

## Part 3: GitHub Integration & Auto-Deploy

### 3.1 Enable Auto-Deployment

- Render automatically redeploys when you push to `main` branch
- No additional setup needed after initial connection

### 3.2 Manual Redeploy (if needed)

1. Render Dashboard → Your Service
2. Click **Manual Deploy** → **Deploy latest commit**
3. Service redeploys from current repository state

---

## Part 4: Monitoring & Troubleshooting

### 4.1 View Logs

1. Render Dashboard → Your Service → **Logs**
2. Shows real-time application output
3. Check here if app fails to start

### 4.2 Common Issues & Solutions

#### Issue: "GROQ_API_KEY not found"
**Solution**: 
- Go to Environment variables in Render
- Verify `GROQ_API_KEY` is set
- Redeploy service

#### Issue: "Port is already in use"
**Solution** (Render handles this automatically):
- Render provides port 8501
- Remove any hardcoded port settings

#### Issue: "Build failing" or "Service not running"
**Solution**:
- Check Logs tab for errors
- Verify requirements.txt has all dependencies
- Ensure Dockerfile is in repository root
- Try Manual Redeploy

#### Issue: "App runs locally but not on Render"
**Solution**:
- Check that all files (app.py, translator.py, etc.) are in repository root
- Verify .env variables are set in Render, not committed to Git
- Check that paths are relative, not absolute Windows paths
- Ensure .streamlit/config.toml exists

### 4.3 Performance Optimization

For Render's free tier:
- File uploads may take longer over network
- First QnA generation request may be slower (Groq API warms up)
- Acceptable performance: ~6-8 seconds for small documents

### 4.4 Upgrade Service Tier (if needed)

For production use:
1. Render Dashboard → Your Service → **Settings**
2. Under "Plan", select paid tier
3. Options: Starter ($7/month), Standard ($12/month), etc.
4. Supports higher concurrency and guaranteed resources

---

## Part 5: Advanced - Custom Domain (Optional)

1. Dashboard → Your Service → **Settings** → **Custom Domain**
2. Add your domain (requires domain ownership)
3. Update DNS records per Render's instructions

---

## File Structure for Deployment

For successful Render deployment, ensure your repository has:

```
ImmverseAI/
├── Dockerfile              ← Docker configuration
├── docker-compose.yml      ← Local testing config
├── .dockerignore          ← Files to exclude from build
├── .streamlit/
│   └── config.toml        ← Streamlit server config
├── app.py                 ← Main application
├── qna_generator.py       ← QnA generation logic
├── translator.py          ← Translation module
├── document_parser.py     ← Document parsing
├── excel_exporter.py      ← Excel export
├── requirements.txt       ← Python dependencies
├── .env.example           ← Template (not deployed)
├── .env                   ← Local only (in .gitignore)
├── .gitignore            ← Protects .env
├── README.md             ← Project documentation
└── RENDER_DEPLOYMENT.md  ← This file
```

---

## Deployment Checklist

- [ ] Docker installed locally
- [ ] Docker runs successfully locally: `docker-compose up`
- [ ] All code pushed to GitHub main branch
- [ ] Render account created
- [ ] GitHub connected to Render
- [ ] Web Service created on Render
- [ ] GROQ_API_KEY added to Render environment variables
- [ ] Service deployment completed (check Render dashboard)
- [ ] Service URL accessible in browser
- [ ] Test upload & QnA generation works on deployed service

---

## Summary

| Step | Time | Status |
|------|------|--------|
| Local Docker test | 5-10 min | Quick validation |
| Push to GitHub | 1 min | Already done |
| Create Render service | 2-3 min | Connect & config |
| First deployment | 5-10 min | Automatic |
| Environment setup | 2 min | Add API key |
| **Total Time** | **~20-30 min** | **Ready!** |

---

## Support & Next Steps

**Got issues?**
- Check Render Logs tab (Service → Logs)
- Verify all environment variables are set
- Try Manual Redeploy
- Check Streamlit documentation for config options

**Want to improve?**
- Set up custom domain for professional URL
- Upgrade to paid tier for production workloads
- Add GitHub Actions for automated testing before deploy

**Questions?**
- Render Docs: https://render.com/docs
- Streamlit Docs: https://docs.streamlit.io
- Groq Docs: https://console.groq.com/docs
