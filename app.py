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
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

load_dotenv()


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='website', template_folder='website')
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'your-email@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', 'your-app-password')

app.config['UPLOAD_FOLDER'] = 'uploads'  # Local temp folder for uploads
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

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
    Creates a nice 'Thank You' email with specific application details.
    """
    full_name = f"{data.get('firstName', '')} {data.get('middleName', '')} {data.get('lastName', '')}".strip()
    track_name = TRACK_MAPPING.get(data.get('fellowshipTrack', ''), 'Not specified')
    why_join_reason = data.get('whyJoin', 'N/A')

    html_content = f"""
    <html>
    <head>
        <style>
            body {{ font-family: 'Poppins', sans-serif; line-height: 1.6; color: #333; background-color: #f4f4f4; margin: 0; padding: 0; }}
            .container {{ max-width: 600px; margin: 20px auto; padding: 30px; background-color: #ffffff; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }}
            .header {{ text-align: center; border-bottom: 1px solid #e9ecef; padding-bottom: 20px; margin-bottom: 30px; }}
            .header h1 {{ font-size: 28px; color: #4e73df; margin: 0; }}
            .content p {{ font-size: 16px; color: #555; }}
            .field {{ margin-bottom: 20px; padding: 15px; background-color: #f8f9fc; border-left: 4px solid #4e73df; border-radius: 4px; }}
            .field-label {{ font-weight: 600; color: #333; display: block; margin-bottom: 5px; }}
            .field-value {{ color: #555; }}
            .footer {{ text-align: center; margin-top: 30px; font-size: 12px; color: #999; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Thank You For Applying!</h1>
            </div>
            <div class="content">
                <p>Dear <strong>{full_name}</strong>,</p>
                <p>We've successfully received your application for the Buildables Fellowship Program. We're thrilled to see your interest and appreciate you taking the time to apply.</p>
                <p>Here's a summary of the information you submitted:</p>

                <div class="field">
                    <span class="field-label">Full Name:</span>
                    <span class="field-value">{full_name}</span>
                </div>

                <div class="field">
                    <span class="field-label">Track Applied For:</span>
                    <span class="field-value">{track_name}</span>
                </div>

                <div class="field">
                    <span class="field-label">Your reason for wanting to join Buildables:</span>
                    <blockquote class="field-value" style="margin: 0; padding-left: 10px; border-left: 2px solid #ccc;">
                        {why_join_reason}
                    </blockquote>
                </div>

                <p>Our team will review your application carefully. You can expect to hear from us within the next two weeks. Stay tuned!</p>
                <p>Best regards,<br>The Buildables Team</p>
            </div>
            <div class="footer">
                &copy; 2024 Buildables. All rights reserved.
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

@app.route('/apply', methods=['POST'])
def apply():
    """
    Accepts form data and a resume upload.
    Saves text data to Azure SQL and uploads resume to Blob Storage.
    Stores resume URL in SQL with form data.
    """
    try:
        # Get text fields (assuming multipart/form-data)
        text_data = request.form.get('text_data')
        if not text_data or not (1000 <= len(text_data) <= 1500):
            return jsonify({'error': 'Text data must be 1000-1500 characters.'}), 400

        # Get file
        if 'resume' not in request.files:
            return jsonify({'error': 'Resume file is required.'}), 400
        resume = request.files['resume']
        if resume.filename == '':
            return jsonify({'error': 'No selected file.'}), 400

        # Save file locally (temp)
        filename = secure_filename(resume.filename)
        local_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        resume.save(local_path)

        # Upload to Azure Blob Storage (placeholder)
        # resume_url = upload_resume_to_blob(local_path, filename)
        # Use placeholder values if config is not set
        blob_account = globals().get('AZURE_BLOB_ACCOUNT_NAME', 'your-storage-account')
        blob_container = globals().get('AZURE_BLOB_CONTAINER_NAME', 'your-container')
        resume_url = f"https://{blob_account}.blob.core.windows.net/{blob_container}/{filename}"  # Placeholder

        # Save form data + resume_url to Azure SQL (placeholder)
        # conn = get_sql_connection()
        # cursor = conn.cursor()
        # cursor.execute("INSERT INTO applications (text_data, resume_url, submitted_at) VALUES (?, ?, ?)",
        #                (text_data, resume_url, datetime.utcnow()))
        # conn.commit()
        # cursor.close()
        # conn.close()

        # Clean up local file
        os.remove(local_path)

        return jsonify({'success': True, 'resume_url': resume_url}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

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
            subject=f"Thank You for Applying to Buildables, {data['firstName']}!",
            body=email_content,
            to_email=data['email']
        )
        
        # TODO: Save to database (future implementation)
        db_manager.save_fellowship_application(data)
        
        # Send notification email to admin (optional)
        admin_email = os.environ.get('ADMIN_EMAIL', app.config['MAIL_USERNAME'])
        if admin_email:
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

# =========================
# Azure SQL Connection Setup
# =========================
def get_sql_connection():
    """
    Returns a connection to Azure SQL Database.
    Fill in the connection string with your credentials.
    """
    # Example using pyodbc (uncomment when ready)
    # conn_str = (
    #     f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    #     f"SERVER={AZURE_SQL_SERVER};"
    #     f"DATABASE={AZURE_SQL_DATABASE};"
    #     f"UID={AZURE_SQL_USERNAME};"
    #     f"PWD={AZURE_SQL_PASSWORD}"
    # )
    # return pyodbc.connect(conn_str)
    pass  # Placeholder

# =========================
# Azure Blob Storage Setup
# =========================
def get_blob_service_client():
    """
    Returns a BlobServiceClient for Azure Blob Storage.
    """
    # Example (uncomment when ready)
    # connect_str = f"DefaultEndpointsProtocol=https;AccountName={AZURE_BLOB_ACCOUNT_NAME};AccountKey={AZURE_BLOB_KEY};EndpointSuffix=core.windows.net"
    # return BlobServiceClient.from_connection_string(connect_str)
    pass  # Placeholder

def upload_resume_to_blob(file_path, filename):
    """
    Uploads the resume to Azure Blob Storage and returns the blob URL.
    """
    # Example (uncomment when ready)
    # blob_service_client = get_blob_service_client()
    # blob_client = blob_service_client.get_blob_client(container=AZURE_BLOB_CONTAINER_NAME, blob=filename)
    # with open(file_path, "rb") as data:
    #     blob_client.upload_blob(data)
    # # Generate SAS token for secure access (see below)
    # resume_url = f"https://{AZURE_BLOB_ACCOUNT_NAME}.blob.core.windows.net/{AZURE_BLOB_CONTAINER_NAME}/{filename}"
    # return resume_url
    pass  # Placeholder

# =========================
# SAS Token Generation
# =========================
def generate_sas_token(blob_name):
    """
    Generates a SAS token for the given blob.
    """
    # Example (uncomment when ready)
    # sas_token = generate_blob_sas(
    #     account_name=AZURE_BLOB_ACCOUNT_NAME,
    #     container_name=AZURE_BLOB_CONTAINER_NAME,
    #     blob_name=blob_name,
    #     account_key=AZURE_BLOB_KEY,
    #     permission=BlobSasPermissions(read=True),
    #     expiry=datetime.utcnow() + timedelta(hours=1)
    # )
    # return sas_token
    pass  # Placeholder

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)