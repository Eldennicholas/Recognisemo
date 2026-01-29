
# 💜 Sense (Recognisemo)

A simple **Emotion Tracking & Mood Logging Web App** built using **Python, Streamlit, and SQLite**.  
This project allows users to register, log in, and track their emotional moods over time.

---

## 🚀 Features

- ✅ User Registration & Login System
- 🧠 Emotion / Mood Tracking
- 📊 Mood History Visualization
- 🔒 Secure local database using SQLite
- ⚡ Fast UI using Streamlit
- 🤖 Emotion model integration (Pickle Model)

---

## 🛠️ Tech Stack

- **Python 3**
- **Streamlit**
- **SQLite**
- **Pickle (ML Model)**
- **VS Code / Any IDE**

---

## 📂 Project Structure

```
📁 project-root
 ┣ 📄 app.py                # Main Streamlit App (Login Page)
 ┣ 📄 database.py           # Database functions
 ┣ 📄 setup_db.py           # Database initialization
 ┣ 📄 alter_users.py        # Database schema update
 ┣ 📄 data.db               # SQLite Database
 ┣ 📄 Eldens_Emotion_Model.pkl # Trained Emotion Model
 ┣ 📄 README.md             # Project Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Install Dependencies

```bash
pip install streamlit
```

### 2️⃣ Initialize Database

```bash
python setup_db.py
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 🔐 How It Works

1. User registers with username, email, and password.
2. User logs in using email and password.
3. Mood data is saved into SQLite database.
4. User can view their recent mood history.

---

## 📌 Future Improvements

- 🌈 Better UI Design
- 📈 Mood Analytics Dashboard
- ☁️ Cloud Database Integration
- 🔑 Password Encryption
- 📱 Mobile Responsive UI

---

## 👨‍💻 Author

**Elden Nicholas**  
Java & Python Developer | ML Enthusiast

---

⭐ If you like this project, give it a star!
