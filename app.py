from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# Database setup
DATABASE = 'tasks.db'

def init_db():
    """Initialize the database with tasks table"""
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                completed BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database when app starts (works with both direct run and gunicorn)
init_db()

@app.route('/')
def index():
    """Display all tasks"""
    conn = get_db_connection()
    tasks = conn.execute('''
        SELECT * FROM tasks 
        ORDER BY completed ASC, created_at DESC
    ''').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """Add a new task"""
    title = request.form.get('title')
    description = request.form.get('description', '')
    
    if not title:
        flash('Task title is required!', 'error')
        return redirect(url_for('index'))
    
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO tasks (title, description) 
        VALUES (?, ?)
    ''', (title, description))
    conn.commit()
    conn.close()
    
    flash('Task added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    """Toggle task completion status"""
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    
    if task:
        new_status = not task['completed']
        conn.execute('''
            UPDATE tasks 
            SET completed = ?, updated_at = CURRENT_TIMESTAMP 
            WHERE id = ?
        ''', (new_status, task_id))
        conn.commit()
        
        status_text = 'completed' if new_status else 'marked as pending'
        flash(f'Task {status_text}!', 'success')
    else:
        flash('Task not found!', 'error')
    
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    """Edit an existing task"""
    conn = get_db_connection()
    
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description', '')
        
        if not title:
            flash('Task title is required!', 'error')
            return redirect(url_for('edit_task', task_id=task_id))
        
        conn.execute('''
            UPDATE tasks 
            SET title = ?, description = ?, updated_at = CURRENT_TIMESTAMP 
            WHERE id = ?
        ''', (title, description, task_id))
        conn.commit()
        conn.close()
        
        flash('Task updated successfully!', 'success')
        return redirect(url_for('index'))
    
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    conn.close()
    
    if not task:
        flash('Task not found!', 'error')
        return redirect(url_for('index'))
    
    return render_template('edit.html', task=task)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Delete a task"""
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    
    if task:
        conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        flash('Task deleted successfully!', 'success')
    else:
        flash('Task not found!', 'error')
    
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    # Use 0.0.0.0 for deployment (Render/Railway), 127.0.0.1 for local dev
    host = '0.0.0.0' if os.environ.get('PORT') else '127.0.0.1'
    debug_mode = not bool(os.environ.get('PORT'))  # Disable debug in production
    
    if not os.environ.get('PORT'):
        # Only print this message in local development
        print(f"\n{'='*50}")
        print(f"Daily Task Tracker is running!")
        print(f"Access it at: http://localhost:{port}")
        print(f"{'='*50}\n")
    
    app.run(debug=debug_mode, host=host, port=port)
