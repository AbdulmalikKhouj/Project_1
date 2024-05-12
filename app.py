import os
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import sqlite3
from waitress import serve  # Import serve function from Waitress
import logging
from flask import jsonify

app = Flask (__name__)

# Email Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Gmail SMTP server
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nnewdummy@gmail.com'  # Update this with your email
app.config['MAIL_PASSWORD'] = 'yxwq arip xxbx bzsy'  # Update this with your app password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

official_email = 'dummy4project123@gmail.com'  # Update this with your official email

# Routes for index, about, and contact
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact_us():
    return render_template('contact-us.html')

@app.route('/submit-message', methods=['POST'])
def submit_message():
    message = request.form.get('message')
    
    # Send email
    if send_email('New Message from Contact Form', message):
        return jsonify({'success': True, 'message': 'Email sent successfully'})
    else:
        return jsonify({'success': False, 'message': 'Failed to send email'})
      
def send_email(subject, body):
    try:
        msg = Message(subject, sender='nnewdummy@gmail.com', recipients=[official_email])
        msg.body = body
        mail.send(msg)
    except Exception as e:
        logging.error(f"Error occurred while sending email: {e}")


# Routes for mobiles and recqres-data
@app.route("/mobiles")
def mobiles():
    return render_template("mobiles.html")

@app.route("/recqres-data")
def recqres_data():
    return render_template("recqres-data.html")

# Fetch posts data from the database
def get_posts_data():
    conn = sqlite3.connect('posts.db')
    c = conn.cursor()
    c.execute('SELECT * FROM posts')
    posts_data = c.fetchall()  # Fetch all posts from the database
    conn.close()
    return posts_data

# Route for displaying all posts
@app.route('/posts')
def all_posts():
    posts_data = get_posts_data()
    return render_template('postall.html', posts=posts_data)

# Fetch post data by ID from the database
def get_post_by_id(post_id):
    conn = sqlite3.connect('posts.db')
    c = conn.cursor()
    c.execute('SELECT * FROM posts WHERE id=?', (post_id,))
    post_data = c.fetchone()  # Fetch the post with the specified ID
    conn.close()
    return post_data
"""
# Test route for Get Single User
@app.route('/api/users/1', methods=['GET'])
def single_post():
    return jsonify({'data': {'id': 1, 'email': 'AbdulmalikKhouj@reqres.in', 'first_name': 'Abdulmalik', 'last_name': 'Khouj'}}), 200
"""

# Route for displaying a single post by ID
@app.route('/posts/<int:post_id>')
def single_post(post_id):
    post_data = get_post_by_id(post_id)
    if post_data:
        return render_template('postsingle.html', post=post_data)
    else:
        return "Post not found", 404

# Route for fetching a single post by ID via GET request
@app.route('/get_single_post', methods=['GET'])
def get_single_post():
    post_id = request.args.get('post_id')
    post_data = get_post_by_id(post_id)
    if post_data:
        return render_template('postsingle.html', post=post_data)
    else:
        return render_template('postsingle.html', post=None)

if __name__ == "__main__":
    # Set FLASK_ENV to development for debug mode
    os.environ['FLASK_ENV'] = 'development'
    
    # Run Flask app using Waitress
    serve(app, host='0.0.0.0', port=5000)
