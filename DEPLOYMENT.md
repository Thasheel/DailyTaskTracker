# Deployment Guide for Daily Task Tracker

This guide provides step-by-step instructions for deploying the Daily Task Tracker on various platforms.

## 🚀 Quick Deployment Options

### Option 1: Render (Recommended)

1. **Fork the Repository**
   - Fork this repository to your GitHub account
   - Clone it locally if you want to make changes

2. **Create Render Account**
   - Go to [render.com](https://render.com)
   - Sign up with your GitHub account

3. **Deploy the Service**
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Configure settings:
     - **Name**: `flask-task-tracker` (or your preferred name)
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Instance Type**: Free tier is sufficient
   - Click "Create Web Service"

4. **Access Your App**
   - Render will provide a URL like: `https://your-app-name.onrender.com`
   - The app will be live in a few minutes

### Option 2: Railway

1. **Prepare Repository**
   - Ensure your code is pushed to GitHub

2. **Deploy on Railway**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway auto-detects Flask and deploys automatically

3. **Custom Domain (Optional)**
   - Railway provides a default domain
   - You can add a custom domain in the settings

### Option 3: PythonAnywhere

1. **Upload Code**
   - Create a PythonAnywhere account
   - Upload your files via the Files tab

2. **Create Web App**
   - Go to Web tab → "Add a new web app"
   - Choose Flask and Python 3.x
   - Set the source code directory

3. **Configure WSGI**
   - Edit the WSGI configuration file:
   ```python
   import sys
   import os
   
   # Add your project directory to sys.path
   project_home = '/home/yourusername/flask-task-tracker'
   if project_home not in sys.path:
       sys.path = [project_home] + sys.path
   
   from app import app as application
   ```

4. **Install Dependencies**
   - Open a Bash console
   - Navigate to your project directory
   - Run: `pip3.x install --user -r requirements.txt`

5. **Reload Web App**
   - Go back to Web tab and click "Reload"

## 🔧 Environment Configuration

### Environment Variables

For production deployment, consider setting these environment variables:

```bash
# Flask Configuration
FLASK_ENV=production
SECRET_KEY=your-super-secret-key-here

# Database (if using external database)
DATABASE_URL=sqlite:///tasks.db
```

### Security Considerations

1. **Change Secret Key**: Update the secret key in `app.py` for production
2. **Database Security**: Consider using PostgreSQL for production
3. **HTTPS**: Most platforms provide HTTPS by default

## 📊 Monitoring and Maintenance

### Health Checks

Most platforms provide built-in monitoring. You can also add a health check endpoint:

```python
@app.route('/health')
def health_check():
    return {'status': 'healthy', 'timestamp': datetime.now().isoformat()}
```

### Logs

- **Render**: View logs in the dashboard
- **Railway**: Check logs in the deployment tab
- **PythonAnywhere**: Access logs via the Web tab

## 🔄 Continuous Deployment

### Automatic Deployments

1. **Render & Railway**: Automatically deploy on git push
2. **PythonAnywhere**: Manual deployment or use git hooks

### Git Workflow

```bash
# Make changes locally
git add .
git commit -m "Update feature"
git push origin main

# Render/Railway will automatically deploy
```

## 🐛 Troubleshooting

### Common Issues

1. **Build Failures**
   - Check `requirements.txt` for correct package versions
   - Ensure Python version compatibility

2. **Database Issues**
   - SQLite database is created automatically
   - Check file permissions on PythonAnywhere

3. **Static Files**
   - Ensure `static/` directory is included in deployment
   - Check Flask static file configuration

### Debug Mode

For local debugging, set `debug=True` in `app.py`:

```python
if __name__ == '__main__':
    app.run(debug=True)  # Only for local development
```

## 📞 Support

If you encounter issues:

1. Check platform-specific documentation
2. Review application logs
3. Verify all files are properly uploaded
4. Ensure dependencies are correctly installed

## 🎯 Post-Deployment Checklist

- [ ] App loads without errors
- [ ] Can add new tasks
- [ ] Can edit existing tasks
- [ ] Can mark tasks as complete
- [ ] Can delete tasks
- [ ] Database persists data between requests
- [ ] Responsive design works on mobile
- [ ] All static files (CSS) load correctly

---

**Happy Deploying!** 🚀
