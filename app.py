from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import json
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='website', template_folder='website')
CORS(app)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'your-email@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', 'your-app-password')

# Track mapping for better email formatting
TRACK_MAPPING = {
    'data-engineering': 'Data Engineering',
    'data-science': 'Data Science',
    'web-development': 'Web Development',
    'app-development': 'App Development',
    'cloud-engineering': 'Cloud Engineering',
    'machine-learning': 'Machine Learning',
    'ai': 'AI',
    'ui-ux': 'UI/UX'
}

def send_email(subject, body, to_email, attachment_path=None):
    """
    Send email with optional attachment
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = app.config['MAIL_USERNAME']
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'html'))

        # Attach file if provided
        if attachment_path and os.path.exists(attachment_path):
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {os.path.basename(attachment_path)}'
            )
            msg.attach(part)

        # Create SMTP session
        server = smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT'])
        server.starttls()
        server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        
        text = msg.as_string()
        server.sendmail(app.config['MAIL_USERNAME'], to_email, text)
        server.quit()
        
        logger.info(f"Email sent successfully to {to_email}")
        return True
    except Exception as e:
        logger.error(f"Failed to send email: {str(e)}")
        return False

def create_fellowship_email_content(data):
    """
    Create HTML email content for fellowship application
    """
    track_name = TRACK_MAPPING.get(data.get('fellowshipTrack', ''), 'Not specified')
    
    html_content = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background-color: #007bff; color: white; padding: 20px; text-align: center; }}
            .content {{ padding: 20px; background-color: #f8f9fa; }}
            .field {{ margin-bottom: 15px; }}
            .field-label {{ font-weight: bold; color: #007bff; }}
            .footer {{ text-align: center; padding: 20px; color: #666; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🎉 Fellowship Application Received!</h1>
            </div>
            <div class="content">
                <p>Dear <strong>{data.get('firstName', '')} {data.get('lastName', '')}</strong>,</p>
                
                <p>Thank you for applying to the Buildables Fellowship Program! We have received your application and are excited to review it.</p>
                
                <h3>📋 Application Details:</h3>
                
                <div class="field">
                    <span class="field-label">Full Name:</span> {data.get('firstName', '')} {data.get('middleName', '')} {data.get('lastName', '')}
                </div>
                
                <div class="field">
                    <span class="field-label">Email:</span> {data.get('email', '')}
                </div>
                
                <div class="field">
                    <span class="field-label">Contact Number:</span> {data.get('contactNo', '')}
                </div>
                
                <div class="field">
                    <span class="field-label">Selected Track:</span> {track_name}
                </div>
                
                <div class="field">
                    <span class="field-label">Why do you want to join Buildables?</span><br>
                    {data.get('whyJoin', '')}
                </div>
                
                <div class="field">
                    <span class="field-label">Why should we choose you?</span><br>
                    {data.get('whyChoose', '')}
                </div>
                
                <div class="field">
                    <span class="field-label">What perspective will you bring?</span><br>
                    {data.get('perspective', '')}
                </div>
                
                <div class="field">
                    <span class="field-label">Additional Information:</span><br>
                    {data.get('anythingElse', '')}
                </div>
                
                <p><strong>Next Steps:</strong></p>
                <ul>
                    <li>Our team will review your application within 5-7 business days</li>
                    <li>You will receive an email with the next steps if selected</li>
                    <li>Keep an eye on your email for updates</li>
                </ul>
                
                <p>If you have any questions, feel free to reach out to us at contact@buildables.pk</p>
                
                <p>Best regards,<br>
                The Buildables Team</p>
            </div>
            <div class="footer">
                <p>This is an automated message. Please do not reply to this email.</p>
                <p>&copy; 2024 Buildables. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html_content

# ============================================================================
# DATABASE INTEGRATION SPACE - FUTURE IMPLEMENTATION
# ============================================================================
# TODO: Add database models and integration here
# This space is reserved for future database integration (SQLAlchemy, MongoDB, etc.)
# or Google Sheets API integration

class DatabaseManager:
    """
    Placeholder class for future database operations
    """
    def __init__(self):
        self.connection = None
    
    def connect(self):
        """
        TODO: Implement database connection
        """
        pass
    
    def save_fellowship_application(self, data):
        """
        TODO: Save fellowship application to database
        """
        # Placeholder for future implementation
        logger.info(f"Would save application to database: {data.get('email', '')}")
        return True
    
    def save_contact_form(self, data):
        """
        TODO: Save contact form to database
        """
        # Placeholder for future implementation
        logger.info(f"Would save contact form to database: {data.get('email', '')}")
        return True

# Initialize database manager
db_manager = DatabaseManager()

# ============================================================================
# ROUTES
# ============================================================================

@app.route('/')
def index():
    """Serve the main index page"""
    return send_from_directory('website', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files from the website directory"""
    return send_from_directory('website', filename)

@app.route('/api/fellowship/apply', methods=['POST'])
def fellowship_application():
    """
    Handle fellowship application form submission
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['firstName', 'lastName', 'email', 'contactNo', 'whyJoin', 
                          'whyChoose', 'perspective', 'anythingElse', 'fellowshipTrack']
        
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Add timestamp
        data['timestamp'] = datetime.now().isoformat()
        
        # Send email to applicant
        email_content = create_fellowship_email_content(data)
        email_sent = send_email(
            subject="🎉 Your Buildables Fellowship Application Has Been Received!",
            body=email_content,
            to_email=data['email']
        )
        
        # TODO: Save to database (future implementation)
        db_manager.save_fellowship_application(data)
        
        # Send notification email to admin (optional)
        admin_email = os.environ.get('ADMIN_EMAIL', app.config['MAIL_USERNAME'])
        admin_content = f"""
        <h3>New Fellowship Application</h3>
        <p><strong>Name:</strong> {data['firstName']} {data['lastName']}</p>
        <p><strong>Email:</strong> {data['email']}</p>
        <p><strong>Track:</strong> {TRACK_MAPPING.get(data['fellowshipTrack'], 'Not specified')}</p>
        <p><strong>Applied at:</strong> {data['timestamp']}</p>
        """
        
        send_email(
            subject=f"New Fellowship Application - {data['firstName']} {data['lastName']}",
            body=admin_content,
            to_email=admin_email
        )
        
        return jsonify({
            'success': True,
            'message': 'Application submitted successfully! Check your email for confirmation.',
            'email_sent': email_sent
        }), 200
        
    except Exception as e:
        logger.error(f"Error processing fellowship application: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/contact', methods=['POST'])
def contact_form():
    """
    Handle contact form submission
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'subject', 'message']
        
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Add timestamp
        data['timestamp'] = datetime.now().isoformat()
        
        # TODO: Save to database (future implementation)
        db_manager.save_contact_form(data)
        
        # Send email to admin
        admin_email = os.environ.get('ADMIN_EMAIL', app.config['MAIL_USERNAME'])
        admin_content = f"""
        <h3>New Contact Form Submission</h3>
        <p><strong>Name:</strong> {data['name']}</p>
        <p><strong>Email:</strong> {data['email']}</p>
        <p><strong>Subject:</strong> {data['subject']}</p>
        <p><strong>Message:</strong></p>
        <p>{data['message']}</p>
        <p><strong>Submitted at:</strong> {data['timestamp']}</p>
        """
        
        email_sent = send_email(
            subject=f"New Contact Form - {data['subject']}",
            body=admin_content,
            to_email=admin_email
        )
        
        return jsonify({
            'success': True,
            'message': 'Message sent successfully! We will get back to you soon.',
            'email_sent': email_sent
        }), 200
        
    except Exception as e:
        logger.error(f"Error processing contact form: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 