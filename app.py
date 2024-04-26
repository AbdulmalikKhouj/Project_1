from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Email Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Gmail SMTP server
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nnewdummy@gmail.com'  # Update this with your email
app.config['MAIL_PASSWORD'] = 'mquk tkuv uwvi bbkj'  # Update this with your app password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

official_email = 'dummy4project123@gmail.com'  # Update this with your official email

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
    send_email('New Message from Contact Form', message)
    
    return redirect(url_for('index'))

def send_email(subject, body):
    msg = Message(subject, sender='nnewdummy@gmail.com', recipients=[official_email])
    msg.body = body
    mail.send(msg)

if __name__ == "__main__":
    app.run(debug=True)
