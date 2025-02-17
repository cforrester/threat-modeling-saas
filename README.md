# 🚀 Threat Modeling SaaS - FastAPI Backend

## 🔹 Project Vision & Concept

In today's cybersecurity landscape, **proactive threat modeling** is crucial for identifying and mitigating security risks **before** they become vulnerabilities. This project is a **Threat Modeling SaaS** that enables **security teams, developers, and organizations** to **visualize, analyze, and mitigate threats** in their software architectures.

### **🌟 Key Features**
- **Threat Detection Engine**: Automatically analyzes system components and applies known threat models (**OWASP Top 10**, **STRIDE**).
- **Predefined Threat Catalog**: Integrates a database of common security threats and recommended mitigations.
- **Threat Modeling Reports**: Generates detailed PDF/CSV reports for compliance and risk assessment.
- **User Authentication & Role Management**: Supports **JWT-based authentication**, **OAuth2**, and **RBAC**.
- **Real-time Collaboration** (Upcoming): Allow teams to work on threat models together via **WebSockets**.

---

## 🛠 **Tech Stack**
- **Backend**: FastAPI + SQLAlchemy + Alembic
- **Database**: PostgreSQL
- **Authentication**: JWT (PyJWT) + Passlib for password hashing
- **Security Best Practices**: OAuth2, Role-Based Access Control (RBAC)
- **Infrastructure**: Docker, Kubernetes (Optional for scaling)

---

## 🚀 **Getting Started**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/threat-modeling-backend.git
cd threat-modeling-backend
```

### **2️⃣ Set Up a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up PostgreSQL**
1. Install PostgreSQL (if not already installed):
   ```bash
   sudo apt update && sudo apt install postgresql postgresql-contrib
   ```
2. Create the database & user:
   ```sql
   CREATE DATABASE threat_db;
   CREATE USER threat_user WITH PASSWORD 'secure_password';
   ALTER ROLE threat_user SET client_encoding TO 'utf8';
   GRANT ALL PRIVILEGES ON DATABASE threat_db TO threat_user;
   ```
3. Update the **`.env`** file:
   ```ini
   DATABASE_URL=postgresql://threat_user:secure_password@localhost/threat_db
   JWT_SECRET=your_secret_key
   ```

### **5️⃣ Apply Migrations (Using Alembic)**
```bash
alembic upgrade head
```

### **6️⃣ Run the FastAPI Application**
```bash
uvicorn app.main:app --reload
```
Your API will be available at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc Documentation**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔥 **API Endpoints**
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/auth/register` | Register a new user |
| `POST` | `/auth/login` | Authenticate and get a JWT token |
| `GET`  | `/threat-catalog` | Retrieve predefined security threats |
| `POST` | `/threat-models` | Create a new threat model |
| `GET`  | `/threat-models/{id}/report` | Generate a PDF report for a threat model |

---

## 🐳 **Running with Docker**
If you prefer using Docker, you can run the project using:
```bash
docker-compose up --build
```

---

## 🤝 **Contributing**
We welcome contributions! Feel free to fork this repository and submit a **pull request**.

---

## 📜 **License**
This project is licensed under the **MIT License**.

---

## 📬 **Contact**
For any inquiries, feel free to reach out via [GitHub Issues](https://github.com/your-username/threat-modeling-backend/issues).

---
