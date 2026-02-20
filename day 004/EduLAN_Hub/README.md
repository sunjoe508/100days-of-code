# 🚀 EduLAN Hub

> Offline-First School File Distribution & LAN Dashboard

EduLAN Hub is a lightweight web-based file sharing system designed for schools operating in low or no internet environments. It enables centralized distribution of learning materials across devices connected to the same local network (LAN).

Built with FastAPI and SQLite, the system is optimized for simple deployment on a laptop or local server within a school setting.

---

## 📌 Problem It Solves

Many educational institutions face:

- Unreliable internet connectivity  
- Limited cloud infrastructure  
- Difficulty distributing digital learning materials  
- Lack of centralized local device coordination  

EduLAN Hub provides a practical solution by enabling file distribution entirely within a local network.

---

## 🧱 Technology Stack

- Backend: FastAPI  
- Database: SQLite  
- ORM: SQLAlchemy  
- Authentication: Passlib (bcrypt)  
- Template Engine: Jinja2  
- ASGI Server: Uvicorn  

---

## 📁 Project Structure

edulan-hub/
│
├── main.py
├── database.py
├── models.py
├── auth.py
├── templates/
│   ├── login.html
│   └── dashboard.html
├── static/
├── uploads/
├── requirements.txt
└── README.md

---

## ✨ Features (MVP)

- User authentication system  
- Default admin account generation  
- File upload through dashboard  
- File listing interface  
- Local network deployment  
- Offline-first architecture  

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/edulan-hub.git
cd edulan-hub
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 🔐 Admin Setup

Open your browser and visit:

http://localhost:8000/register

This generates the default admin account:

- Username: admin  
- Password: admin123  

Then log in at:

http://localhost:8000

---

## 🌐 Access from Other Devices

1. Identify the server’s local IP address  
   Example: 192.168.1.5  

2. On connected devices, open:

http://192.168.1.5:8000

All devices must be connected to the same LAN.

---

## 🎯 Intended Deployment Environment

EduLAN Hub is suitable for:

- Digital Learning Programs (DLP)  
- Computer laboratories  
- Tablet classrooms  
- Offline ICT training sessions  
- Local content distribution hubs  

---

## 🔒 Security Notice

This MVP is designed for controlled internal environments.

For production-level deployment, consider adding:

- Secure session handling  
- Role-based access enforcement  
- HTTPS configuration  
- File type validation  
- File size restrictions  
- Activity logging  
- Token-based authentication validation  

---

## 🛣 Roadmap

Planned enhancements:

- Role-based access control (Admin / Teacher / Student)  
- File download button with permissions  
- Device activity monitoring  
- Storage analytics dashboard  
- Modern responsive UI  
- Docker containerization  
- REST API documentation expansion  

---

## 🤝 Contributing

1. Fork the repository  
2. Create a feature branch  
3. Commit your changes  
4. Submit a Pull Request  

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

Developed as a practical LAN-based education technology solution focused on offline digital learning environments.
