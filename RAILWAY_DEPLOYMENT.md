# Railway Deployment Guide - Daily Task Tracker

Complete step-by-step guide to deploy your Flask Task Tracker on Railway.

## Prerequisites

1. ✅ GitHub account
2. ✅ Railway account (free tier available)
3. ✅ Your code pushed to GitHub

## Step-by-Step Deployment

### Step 1: Prepare Your Code

Make sure your project has these files in the root directory:
- ✅ `app.py` (your Flask app)
- ✅ `requirements.txt` (dependencies)
- ✅ `Procfile` (deployment command)
- ✅ `runtime.txt` (optional, specifies Python version)
- ✅ `templates/` folder
- ✅ `static/` folder

**All files should be in your repository!**

### Step 2: Push to GitHub

If you haven't already, push your code to GitHub:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Daily Task Tracker"

# Add your GitHub repository (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/flask-task-tracker.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Sign Up for Railway

1. Go to [railway.app](https://railway.app)
2. Click **"Start a New Project"** or **"Login"**
3. Sign up using your GitHub account (recommended for easy repo access)
4. Complete the verification process

### Step 4: Deploy from GitHub

1. **Click "New Project"** on your Railway dashboard
2. Select **"Deploy from GitHub repo"**
3. If prompted, authorize Railway to access your GitHub repositories
4. **Select your repository** (`flask-task-tracker` or whatever you named it)
5. Railway will automatically:
   - Detect it's a Python project
   - Install dependencies from `requirements.txt`
   - Run the command from `Procfile`

### Step 5: Configure Environment (Optional)

Railway should auto-detect everything, but you can verify:

1. Click on your project
2. Go to **"Settings"** tab
3. Check **"Build Command"**: Should be empty (uses default `pip install -r requirements.txt`)
4. Check **"Start Command"**: Should use your `Procfile` which contains `web: gunicorn app:app`

### Step 6: Get Your Public URL

1. Go to **"Settings"** tab
2. Scroll to **"Networking"** section
3. Click **"Generate Domain"** (if not auto-generated)
4. Railway will provide a URL like: `https://your-app-name.up.railway.app`
5. **Copy this URL** - this is your live app!

### Step 7: Test Your Deployment

1. Open the Railway-provided URL in your browser
2. Test adding a task
3. Verify database persistence works
4. Check if all features are working

### Step 8: Custom Domain (Optional)

1. Go to **"Settings"** → **"Networking"**
2. Click **"Custom Domain"**
3. Add your domain name
4. Follow Railway's DNS configuration instructions

## Important Configuration Files

### Procfile
```
web: gunicorn app:app
```

### requirements.txt
Make sure gunicorn is included:
```
Flask==2.3.3
gunicorn==21.2.0
...
```

### runtime.txt (Optional)
```
python-3.11.5
```

## Troubleshooting

### Common Issues

#### 1. App Crashes on Startup
- **Check logs**: Go to **"Deployments"** tab → Click on latest deployment → View logs
- **Verify Procfile**: Ensure it says `web: gunicorn app:app`
- **Check app.py**: Make sure `app` variable is defined correctly

#### 2. Database Issues
- SQLite should work fine on Railway
- Database file will be created automatically on first run
- Note: Database resets on redeploy unless using persistent storage

#### 3. Static Files Not Loading
- Ensure `static/` folder is in your repository
- Check Flask's `url_for('static', ...)` paths
- Verify files are committed to git

#### 4. Port Issues
- Railway sets `PORT` environment variable automatically
- Your `app.py` should use: `port=int(os.environ.get('PORT', 5000))`
- ✅ Already configured in your app!

### Viewing Logs

1. Go to your project on Railway
2. Click **"Deployments"** tab
3. Click on the latest deployment
4. View **"Build Logs"** or **"Deploy Logs"**

### Redeploying

Every time you push to GitHub, Railway automatically redeploys!

```bash
# Make changes
git add .
git commit -m "Update app"
git push origin main
# Railway will automatically deploy
```

## Railway Free Tier Limits

- ✅ 500 hours/month free compute time
- ✅ $5 credit per month
- ✅ Automatic deployments from GitHub
- ✅ Custom domains
- ⚠️ Apps sleep after 5 minutes of inactivity (free tier)
- ⚠️ SQLite database resets on redeploy

## Production Tips

### 1. Environment Variables
Add secrets in Railway:
- Go to **"Variables"** tab
- Add environment variables like:
  - `SECRET_KEY=your-secret-key-here`
  - `FLASK_ENV=production`

### 2. Persistent Database
For production, consider using:
- PostgreSQL (Railway provides this)
- Update your app to use PostgreSQL instead of SQLite

### 3. Monitoring
- Use Railway's built-in metrics
- Monitor CPU and memory usage
- Set up alerts if needed

## Quick Checklist

Before deploying, ensure:
- [ ] Code is pushed to GitHub
- [ ] `Procfile` exists with correct command
- [ ] `requirements.txt` includes all dependencies
- [ ] `gunicorn` is in requirements.txt
- [ ] `app.py` uses `PORT` environment variable
- [ ] All templates and static files are in repo
- [ ] `.gitignore` excludes unnecessary files (but includes necessary ones)

## Your App URL

After successful deployment, your app will be live at:
```
https://your-app-name.up.railway.app
```

Share this URL in your submission! 🚀

---

**Need Help?**
- Railway Documentation: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- Check deployment logs for error messages

Happy Deploying! 🎉
