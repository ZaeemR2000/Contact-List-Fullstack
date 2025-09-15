# 📇 Contact List Fullstack App

A simple fullstack contact list application built with:

- **Frontend**: React  
- **Backend**: Python + Flask (REST API)  
- **Database**: SQLAlchemy + SQLite (local)  
- **Environment**: Virtualenv (`venv`) + `requirements.txt`  

---

## ✨ Features
- Create new contacts  
- Update existing contacts  
- Delete contacts  
- Real-time updates between frontend and backend  
- SQLite database stored in `backend/instance/`  

---

# Getting Started

## 1 Clone the Repository

git clone https://github.com/your-username/contact-list-app.git
cd contact-list-app


## 2 Backend Setup (Flask + Python)
### Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

### Install dependencies
pip install -r requirements.txt

### Run backend
cd backend
python main.py



## 3 Frontend Setup (React)
cd frontend

### Install dependencies
npm install

### Run frontend
npm run dev

```bash