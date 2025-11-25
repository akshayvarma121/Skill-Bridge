# PMIO: A Voice-First Internship Portal for Rural India 🇮🇳

PMIO is a full-stack web application designed to bridge the gap between rural youth and internship opportunities. Leveraging a voice-first, multilingual interface, it provides an accessible platform for users with limited digital literacy to register their profiles and receive personalized internship recommendations.



## ✨ Core Features

* **🎤 Voice-First Onboarding:** A multi-step conversational UI that allows users to register their name, skills, education, and location entirely through voice commands.
* **🌐 Multilingual Support:** Fully functional in English, Hindi, and Tamil, including voice prompts and UI text.
* **🤖 Personalized Recommendations:** A backend engine that matches user profiles (skills and location) to a database of internships, providing a tailored list of opportunities.
* **🛡️ Accessible Fallback:** A traditional form-based registration is available as a fallback, ensuring no user is left behind.
* **📱 Mobile-First PWA:** Built as a Progressive Web App, it's installable on low-cost smartphones and designed for accessibility with large touch targets and high contrast.

---


## 🛠️ Technology Stack

The project is a modern full-stack application composed of a React frontend and a FastAPI backend.

| Area      | Technology                                    |
| :-------- | :-------------------------------------------- |
| **Frontend** | React, Vite, React Router, i18next, Axios     |
| **Backend** | Python, FastAPI, Uvicorn                      |
| **Database** | MongoDB (for user profiles & internships)     |
| **Cache** | Redis (for match scores & session management) |
| **Voice API** | Web Speech API (`react-speech-recognition`)   |

---
## Snapshots:
https://drive.google.com/drive/folders/1TZ9i1Nc9T3HrXNdiVkUrkLO_0kOgSmG9?usp=drive_link

## 🚀 Getting Started

To get the full project running locally, you'll need to set up both the backend and the frontend in separate terminals.

### Prerequisites

* Node.js (v18+) & npm
* Python (v3.10+) & pip
* A running MongoDB instance
* A running Redis instance

### Step 1: Backend Setup ⚙️

1.  **Navigate to the `backend` folder** and create/activate a Python virtual environment:
    ```bash
    # Create virtual environment
    python -m venv venv
    # Activate on Windows
    .\venv\Scripts\activate
    # Activate on macOS/Linux
    source venv/bin/activate
    ```

2.  **Install backend dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment:** Create a `.env` file in the `backend` folder and add your database credentials:
    ```
    MONGO_URI=mongodb://localhost:27017/pmio_db
    REDIS_HOST=your-redis-host.com
    REDIS_PORT=12345
    REDIS_PASSWORD=your-redis-password
    ```

4.  **Run the Backend Server:**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be live at `http://127.0.0.1:8000`. Keep this terminal running.

### Step 2: Frontend Setup 🌐

1.  **Open a new terminal** and navigate to the `frontend` folder.

2.  **Install frontend dependencies:**
    ```bash
    npm install
    ```

3.  **Configure Environment:** Create a `.env` file in the `frontend` folder and point it to your running backend:
    ```
    VITE_API_URL=[http://127.0.0.1:8000](http://127.0.0.1:8000)
    ```

4.  **Run the Frontend App:**
    ```bash
    npm run dev
    ```
    The application will open in your browser at `http://localhost:5173`.

---

## 🔮 Future Scope

* **Enhanced AI Model:** Integrate a more sophisticated machine learning model for calculating match scores.
* **Offline Support:** Fully leverage PWA capabilities for offline browsing of saved recommendations.
* **Real-time Notifications:** Add push notifications for new, high-match internship opportunities.

---

This project was built late one night in Bhopal, Madhya Pradesh, as a part of SIH project 
