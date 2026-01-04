# QR_HealthCare🏥📱

A hospital-driven digital health platform that enables **secure, instant access to verified patient medical information** using QR codes — especially critical during medical emergencies.

---

## 🚩 Problem Statement

In real-world emergency scenarios, patients are often unconscious or unable to communicate their medical history. Doctors and emergency responders are forced to make treatment decisions without knowing:
- Blood group
- Allergies
- Chronic conditions
- Ongoing medications

This lack of verified information can lead to **incorrect treatment and loss of life**.

---

## 💡 Solution Overview

**QR Health Access System** solves this problem by introducing a **hospital-managed, centralized medical record system** where:

- Only **hospitals** can register and update patient medical data
- Each patient receives a **unique QR code**
- QR scan provides **limited emergency-safe information**
- **Doctors** can securely access **complete medical history** after authentication

The system is designed as an **MVP** with scalability toward a **national health platform**.

---

## 🔐 Key Features

### 🏥 Hospital Portal
- Hospital registration & login
- Role-based access control
- Structured patient registration (Basic, Medical, Clinical sections)
- Upload medical reports (PDFs, images, documents)
- QR code generation for each patient

### 🚑 Emergency Mode
- QR scan shows **only critical information**:
  - Blood group
  - Allergies
  - Chronic conditions
  - Emergency contact
- Designed for ambulance and first responders

### 👨‍⚕️ Doctor Access
- Separate doctor login
- Secure access to **full patient medical records**
- QR-based patient lookup

### 🔒 Security & Privacy
- Hospital-only data entry (patients cannot self-edit)
- Doctors require authentication
- Emergency view is restricted and minimal
- No public access to full records

---

## 🧱 Tech Stack

| Layer        | Technology |
|-------------|------------|
| Backend     | Python (Flask) |
| Database    | SQLite (MVP) |
| ORM         | SQLAlchemy |
| Frontend    | HTML, CSS, JavaScript |
| QR Handling | Python `qrcode` library |
| File Upload | Flask + local storage |

---

## 📁 Project Structure
QR-health_access/
├── app.py
├── models.py
├── qr_health.db
├── frontend/
│ ├── register.html
│ ├── login.html
│ ├── home.html
│ ├── dashboard.html
│ ├── doctor.html
│ ├── about.html
│ └── styles.css
├── uploads/
│ ├── reports/
│ └── team/
└── README.md


---

## 🚀 Getting Started

1️⃣ Clone the Repository

git clone https://github.com/your-username/qr-health-access-system.git

cd qr-health-access-system

2️⃣ Install Dependencies

pip install flask flask-sqlalchemy qrcode

3️⃣ Run the Application

python app.py

4️⃣ Open in Browser

http://127.0.0.1:5000 

🧪 Demo Credentials (MVP)
Doctor Accounts
doctor1@demo.com | doc123
doctor2@demo.com | doc123
doctor3@demo.com | doc123


Hospitals can register dynamically.

👥 Team & Contributions

Naveen Kumar B – Backend architecture, database design, QR generation, authentication

Yashwin Gowda K – Frontend UI/UX design, multi-page navigation

Shalini M G – Healthcare research, emergency workflow analysis

Priya K – Documentation, presentation, testing & validation

(Team images are stored locally under uploads/team/)

🔮 Future Scope

National-level centralized health registry

Aadhaar / Government health ID integration

AI-assisted emergency decision support

Camera-based QR scanning inside the web app

Cloud deployment with Azure (planned)

Encrypted medical data storage


⚠️ Disclaimer

This is an MVP prototype developed for academic and competition purposes.
Not intended for real-world clinical use without regulatory approvals.

📜 License

MIT License
