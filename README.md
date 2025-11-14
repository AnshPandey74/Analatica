# 🧠 Analatica – Event Tracking & Analytics Dashboard  
A lightweight end-to-end **event analytics engine** built using **Flask**, **SQLite**, **Chart.js**, and a custom **JavaScript tracker**.  
This project demonstrates how user actions can be collected, stored, and visualized in a clean dashboard — similar to how Mixpanel, Amplitude, and other analytics tools work internally.

---

## 📸 Screenshots  
Create a folder in your repo:  

Upload your PNG/JPG images there and replace the links below.

### **Demo Page**
![Demo Page](https://raw.githubusercontent.com/YOUR-USERNAME/analatica/main/screenshots/demo_page.png)

### **Dashboard Overview**
![Dashboard](https://raw.githubusercontent.com/YOUR-USERNAME/analatica/main/screenshots/dashboard.png)

### **Dark Mode**
![Dark Mode](https://raw.githubusercontent.com/YOUR-USERNAME/analatica/main/screenshots/dark_mode.png)

---

## 🚀 Features  
- 📩 Tracks user actions (page views, signup clicks, custom events)  
- 📱 Detects device type (mobile/desktop)  
- 🗃 Stores all events in SQLite  
- 📊 Dashboard includes:
  - Event count chart  
  - Device breakdown (pie)  
  - Hourly activity chart  
- 🌙 Light Mode & Dark Mode toggle  
- 🔌 Clean ingestion API  
- 🧩 Frontend tracking script (`tracker.js`)  
- 💡 Fully customizable and beginner-friendly  

---

## 📁 Project Structure
analatica/
│
├── app.py # Flask backend API + routes
├── init_db.py # Create SQLite event table
├── requirements.txt # Python dependencies
│
├── static/
│ └── tracker.js # Frontend event tracking script
│
└── templates/
├── index.html # Demo page (with event triggers + dark mode)
└── dashboard.html # Analytics dashboard with charts

---

## 🛠️ Getting Started

### **1. Clone your repository**
```sh
git clone https://github.com/YOUR-USERNAME/analatica.git
cd analatica
## **Create a virtual environment (Windows)**
python -m venv venv
venv\Scripts\activate
### **Install dependencies**
pip install -r requirements.txt

### **Initialize the database**
python init_db.py

### **Start the server**
python app.py

### **Open in browser**
Demo → http://127.0.0.1:5000
Dashboard → http://127.0.0.1:5000/dashboard

## 📊 API Endpoints

### **POST /api/events**
Send events to backend.

**Example payload:**
```json
{
  "event_name": "signup_click",
  "user_id": "u_f91k73d",
  "device": { "device_type": "desktop" },
  "metadata": { "page": "demo" }
}

GET /api/analytics/event_counts

Returns:

[
  { "event_name": "page_view", "count": 10 },
  { "event_name": "signup_click", "count": 3 }
]

GET /api/analytics/device_breakdown
[
  { "device_type": "desktop", "count": 12 },
  { "device_type": "mobile", "count": 1 }
]

GET /api/analytics/hourly
[
  { "hour": "09", "count": 5 },
  { "hour": "10", "count": 3 }
]
