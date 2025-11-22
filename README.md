# Daily Task Tracker 📝

A simple and elegant Flask-based web application for managing your daily tasks. Built as part of a Python Developer Screening Task.

**🌐 Live Demo**: [https://dailytasktracker.up.railway.app/](https://dailytasktracker.up.railway.app/)

## 🌟 Features

- ✅ **Add Tasks**: Create new tasks with title and optional description
- ✏️ **Edit Tasks**: Modify existing tasks anytime
- 🗑️ **Delete Tasks**: Remove tasks you no longer need
- ✔️ **Mark Complete**: Toggle task completion status
- 📊 **Task Statistics**: View total, completed, and pending tasks
- 💾 **SQLite Database**: Persistent storage for all your tasks
- 📱 **Responsive Design**: Works great on desktop and mobile devices
- 🎨 **Modern UI**: Clean interface built with Bootstrap 5

## 🚀 Live Demo

**Hosted App URL**: [https://dailytasktracker.up.railway.app/]

## 🛠️ Technology Stack

- **Backend**: Flask (Python 3.11)
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Template Engine**: Jinja2
- **Icons**: Font Awesome
- **Deployment**: Ready for Render, Railway, or PythonAnywhere

## 📁 Project Structure

```
flask-task-tracker/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment configuration
├── runtime.txt           # Python version specification
├── README.md             # Project documentation
├── .gitignore           # Git ignore rules
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Main page
│   └── edit.html        # Edit task page
└── static/              # Static files
    └── style.css        # Custom CSS styles
```

## 🏃‍♂️ Running Locally

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/flask-task-tracker.git
   cd flask-task-tracker
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

The SQLite database (`tasks.db`) will be created automatically when you first run the application.

## 🎯 Features Implemented

### Core Requirements ✅
- [x] Add, edit, and delete daily tasks
- [x] Mark tasks as completed
- [x] View all tasks in a simple list
- [x] Flask framework with Python 3.x
- [x] Jinja2 template engine
- [x] SQLite database for persistent storage
- [x] Clean and responsive UI

### Bonus Features ✅
- [x] SQLite database integration
- [x] Dynamic task display
- [x] Task statistics dashboard
- [x] Modern, responsive design
- [x] Flash messages for user feedback
- [x] Task creation timestamps
- [x] Confirmation dialogs for deletions

## 🎨 UI/UX Features

- **Responsive Design**: Works seamlessly on all device sizes
- **Modern Interface**: Clean, professional look with Bootstrap 5
- **Interactive Elements**: Hover effects and smooth transitions
- **Visual Feedback**: Color-coded task status and flash messages
- **Intuitive Navigation**: Clear action buttons with icons
- **Statistics Dashboard**: Quick overview of task progress

## 🔧 Code Quality

- **Clean Code**: Well-structured and commented Python code
- **Error Handling**: Proper error messages and user feedback
- **Security**: Flask secret key and SQL injection prevention
- **Database Design**: Efficient SQLite schema with proper indexing
- **Responsive Templates**: Mobile-first design approach

## 🚧 Challenges Faced & Solutions

1. **Database Initialization**: Ensured automatic database creation on first run
2. **Responsive Design**: Implemented mobile-first approach with Bootstrap
3. **User Experience**: Added confirmation dialogs and flash messages
4. **Deployment Configuration**: Created proper Procfile and requirements.txt

## 🔮 Future Enhancements

- [ ] User authentication and multiple user support
- [ ] Task categories and tags
- [ ] Due dates and reminders
- [ ] Task priority levels
- [ ] Search and filter functionality
- [ ] Export tasks to CSV/PDF
- [ ] Dark mode toggle
- [ ] API endpoints for mobile app integration

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Developer

Created by Mohammed Thasheel as part of a Python Developer Screening Task.

**Contact**: mohdthasheelok@gmail.com  
**GitHub**: (https://github.com/thasheel)  



