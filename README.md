# 🌐 Analatica – Real-Time Event Tracking & Analytics Demo

Analatica is a lightweight, real-time event tracking platform that captures user interactions such as clicks, page views, and device information — and visualizes them in a beautiful dashboard.

This project is built as a **demo analytics system**, perfect for learning how tracking, logging, and visual dashboards work under the hood.

---

## 🚀 Live Demo

🔗 **Website:** https://analatica.onrender.com  
🔗 **Dashboard:** https://analatica.onrender.com/dashboard

---

## 🖼 Screenshots

_Add your screenshots in a folder named `/screenshots` and reference them like this:_



### **Launch Page**
![Clicks](https://raw.githubusercontent.com/AnshPandey74/analatica/main/ss2/Click.png)

### **Homepage Overview**
![Homepage](https://raw.githubusercontent.com/AnshPandey74/analatica/main/ss2/Home.png)

### **Insight**
![Insight](https://raw.githubusercontent.com/AnshPandey74/analatica/main/ss2/Insights.png)

### **Stats**
![Stats](https://raw.githubusercontent.com/AnshPandey74/analatica/main/ss2/stats2.png)
---


---

## ✨ Features

### **🎯 Real-Time Event Tracking**
- Tracks page views
- Tracks custom events (like button clicks)
- Captures metadata such as:
  - URL
  - Referrer
  - Device Type
  - Browser
  - Timestamp

---

### **📊 Live Analytics Dashboard**
Built using Chart.js, showing:
- Event Count Overview
- Device Type Breakdown
- Hourly Activity Chart

---

### **💻 Beautiful Modern UI (with Dark Mode)**
- Clean landing page  
- Three-section design  
- Light/Dark theme toggle  
- Mobile responsive  

---

### **📝 Tech Stack**
| Layer       | Technology |
|------------|------------|
| Backend API | Flask |
| Frontend UI | HTML, Bootstrap 5, CSS |
| Charts | Chart.js |
| Tracking Script | Custom JS (`tracker.js`) |
| Database | SQLite |
| Hosting | Render |

---

## 📌 API Endpoints

### **1️⃣ POST /api/events**
Send a new event to the backend.

**Example Payload**
```json
{
  "event_name": "signup_click",
  "user_id": "u_f91k73d",
  "device": { "device_type": "desktop" },
  "metadata": { "page": "demo" }
}


Analatica/
│── app.py                # Flask backend
│── init_db.py            # Database setup
│── migrate_db.py         # Optional DB migration
│── requirements.txt      # Dependencies
│── render.yaml           # Render deployment config
│── static/
│     └── tracker.js      # Event tracking script
│── templates/
│     ├── index.html      # Landing page
│     └── dashboard.html  # Analytics dashboard
└── screenshots/          # Add screenshots for README


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
