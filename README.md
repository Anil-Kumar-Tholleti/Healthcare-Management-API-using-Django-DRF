 🏥 Healthcare Management API Using (Django + DRF)

A production-ready backend system built using **Django** and **Django REST Framework** for managing doctor-patient records securely. This system includes **JWT-based authentication**, PostgreSQL-ready config, and modular CRUD APIs. Developed as part of a full-stack internship assignment, the project demonstrates RESTful design, authentication, database modeling, and deployment practices.

---

## ✨ Project Highlights

✅ REST API with Django REST Framework  
✅ JWT Authentication using `SimpleJWT`  
✅ User registration and token-based login  
✅ CRUD operations for Patients, Doctors, and their Mappings  
✅ PostgreSQL-ready setup via `.env` file  
✅ Secure, modular, and scalable codebase  
✅ Fully containerizable and deployable  
✅ Auto-filtering patients by user (created_by)  
✅ Logs and error handling integrated  
✅ GitHub version controlled

---

## 📁 Project Structure

healthcare-backend/
├── core/
│ ├── models.py # Database models
│ ├── serializers.py # DRF serializers
│ ├── views.py # ViewSets and APIs
│ └── urls.py # App-specific routes
├── healthcare/
│ ├── settings.py # Project settings
│ └── urls.py # Global routes
├── env/ # Virtual environment (excluded in Git)
├── manage.py
├── requirements.txt
├── .env
└── README.md

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 🔁 1. Clone the Repository


git clone https://github.com/yourusername/healthcare-backend.git
cd healthcare-backend
🐍 2. Create & Activate Virtual Environment
python -m venv env
env\Scripts\activate    # Windows
📦 3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔑 4. Configure Environment
Create a .env file in the root directory:

SECRET_KEY=your_django_secret
DEBUG=True
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
PostgreSQL is optional — you can use SQLite for local testing.

⚡ 5. Apply Migrations & Run Server

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
Server is live at: http://127.0.0.1:8000/

🔐 Authentication
Endpoint	Method	Description
/api/auth/register/	POST	Create new user
/api/auth/login/	POST	Generate JWT tokens

Use JWT token in header:
Authorization: Bearer <access_token>

🧑 Patient APIs
Endpoint	Method	Description
/api/patients/	GET	List user’s patients
/api/patients/	POST	Add a patient
/api/patients/<id>/	PUT	Update patient
/api/patients/<id>/	DELETE	Remove patient

👨‍⚕️ Doctor APIs
Endpoint	Method	Description
/api/doctors/	GET	List all doctors
/api/doctors/	POST	Add new doctor
/api/doctors/<id>/	PUT	Update doctor
/api/doctors/<id>/	DELETE	Remove doctor

🔗 Patient–Doctor Mappings
Endpoint	Method	Description
/api/mappings/	GET	View all mappings
/api/mappings/	POST	Create mapping
/api/mappings/<id>/	DELETE	Delete mapping
/api/mappings/<patient_id>/	GET	View mappings for patient

🔃 Sample Flow
✅ Register → /api/auth/register/

🔓 Login → /api/auth/login/

🔐 Add JWT token to headers

🧑 Add Doctors & Patients

🔗 Create mappings

🎯 Build Frontend or consume API

📃 Logs
You can integrate Django logging and store logs in logs/:

lua
Copy
Edit
logs/
├── api.log
└── errors.log
(Add log handlers in settings.py if needed)

🚀 Deployment
You can deploy this app on Render, Heroku, or Docker.

Tips:

DEBUG=False

Add ALLOWED_HOSTS

Use gunicorn

Set static root: STATIC_ROOT = os.path.join(BASE_DIR, 'static')

collectstatic before deploying

🛡️ License
This project is for technical demonstration and open educational use only.
MIT License © 2025 Anil Kumar T.
