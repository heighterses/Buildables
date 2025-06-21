# Buildables Website 🚀

Welcome to the official repository for the Buildables community website!
![image](https://github.com/user-attachments/assets/f161f6c1-0480-4a49-ac1f-7f30cf694d4f)

## 🌟 Features

### Frontend
-   **Home Page**: An overview of what Buildables is all about.
-   **About Us**: Learn about our mission, vision, and the team behind Buildables.
-   **Events**: Stay updated with our latest events and workshops.
-   **Programs**: Detailed information about our Hackathons and Fellowships.
    -   **Hackathons**: Challenges, schedules, and registration.
    -   **Fellowships**: Various tracks like Data Engineering, Web Development, AI, and more.
-   **Community**: Join our community and connect with other builders.
-   **Contact**: Get in touch with us.
-   **Responsive Design**: Looks great on desktops, tablets, and mobile devices. 📱💻

### Backend
-   **Flask API**: RESTful API endpoints for form handling
-   **Email Integration**: Automatic email notifications for form submissions
-   **Form Processing**: Fellowship applications and contact form handling
-   **Database Ready**: Designated space for future database integration
-   **Error Handling**: Comprehensive error handling and logging
-   **Security**: Input validation and sanitization

## 🛠️ Tech Stack

### Frontend
-   **HTML5**: For the structure of the web pages.
-   **CSS3**: For styling and making it look beautiful.
-   **JavaScript**: For interactivity and dynamic features.
-   **Font Awesome**: For icons.
-   **Google Fonts**: For clean and modern typography.

### Backend
-   **Flask**: Python web framework for the backend API
-   **Flask-CORS**: Cross-origin resource sharing support
-   **SMTP**: Email functionality for notifications
-   **Python-dotenv**: Environment variable management

## 🏃‍♂️ Getting Started

### Prerequisites

1.  **Python 3.7+**: Make sure you have [Python](https://www.python.org/downloads/) installed on your computer.
2.  **Email Configuration**: For email functionality, you'll need Gmail credentials.

### Installation & Setup

1.  **Clone this repository:**
    ```sh
    git clone <repository-url>
    cd Buildables
    ```

2.  **Install Python dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**
    Create a `.env` file in the root directory (use `env_example.txt` as a template):
    ```sh
    # Flask Configuration
    SECRET_KEY=your-secret-key-here
    FLASK_ENV=development

    # Email Configuration (Gmail)
    MAIL_SERVER=smtp.gmail.com
    MAIL_PORT=587
    MAIL_USERNAME=your-email@gmail.com
    MAIL_PASSWORD=your-app-password

    # Admin Email for notifications
    ADMIN_EMAIL=admin@buildables.pk
    ```

4.  **Configure Gmail for sending emails:**
    - Enable 2-factor authentication on your Gmail account
    - Generate an App Password (Google Account → Security → App Passwords)
    - Use the App Password in your `.env` file

### Running the Application

#### Option 1: Full Stack (Recommended)
Run the Flask backend which serves both the API and static files:

```sh
python app.py
```

Then open your browser and navigate to:
-   `http://localhost:5000`

#### Option 2: Frontend Only (Development)
If you want to run just the frontend for development:

```sh
cd website
python -m http.server 8000
```

Then open your browser and navigate to:
-   `http://localhost:8000`

## 📧 Email Features

The backend automatically sends emails for:

### Fellowship Applications
- **To Applicant**: Confirmation email with application details
- **To Admin**: Notification of new application with all details

### Contact Form Submissions
- **To Admin**: Notification of new contact form submission

## 🔧 API Endpoints

- `POST /api/fellowship/apply` - Submit fellowship application
- `POST /api/contact` - Submit contact form
- `GET /api/health` - Health check endpoint

## 🗄️ Database Integration Space

The backend includes a designated space for future database integration:

- **Location**: `app.py` - `DatabaseManager` class
- **Future Options**: SQLAlchemy, MongoDB, Google Sheets API
- **Ready for**: User management, application tracking, analytics

## 🚀 Deployment

### Local Development
```sh
python app.py
```

### Production Deployment
1. Set `FLASK_ENV=production` in your environment variables
2. Use a production WSGI server like Gunicorn:
   ```sh
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

## 🙏 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again! ⭐

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details. 
