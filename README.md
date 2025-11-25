Skill Bridge: Voice-First Internship Portal for Rural India

Skill Bridge is a full-stack web application designed to connect rural youth to internship opportunities. With a voice-first, multilingual interface, it provides an accessible platform for users with limited digital literacy to register profiles and receive personalized internship recommendations.

Core Features
Voice-First Onboarding: Multi-step conversational UI enabling users to register their name, skills, education, and location entirely through voice commands.

Multilingual Support: English, Hindi, and Tamil supported throughout the interface, including voice prompts and all UI text.

Personalized Recommendations: Backend engine matches user profiles (skills and location) to a curated database of internships, providing custom opportunity lists.

Accessible Fallback: Full traditional form-based registration available as fallback for accessibility.

Mobile-First PWA: Progressive Web App installable on smartphones, featuring high accessibility, large touch targets, and high contrast for all users.

Technology Stack
Skill Bridge is built as a modern full-stack application with a React frontend and FastAPI backend.

Area	Technology
Frontend	React, Vite, React Router, i18next, Axios
Backend	Python, FastAPI, Uvicorn
Database	MongoDB (for user profiles & internships)
Cache	Redis (match scores & session management)
Voice API	Web Speech API (react-speech-recognition)
Snapshots
See live screenshots and demos here:
Google Drive Snapshots

Getting Started
To set up the full project locally, you’ll need to configure both backend and frontend in separate terminals.

Prerequisites
Node.js (v18+) & npm

Python (v3.10+) & pip

MongoDB instance

Redis instance

Backend Setup
Navigate to the backend folder and create/activate a Python virtual environment:

bash
python -m venv venv
.\venv\Scripts\activate # Windows
source venv/bin/activate # macOS/Linux
Install backend dependencies:

bash
pip install -r requirements.txt
Configure environment variables in backend/.env:

text
MONGO_URI=mongodb://localhost:27017/skillbridge_db
REDIS_HOST=your-redis-host.com
REDIS_PORT=6379
REDIS_PASSWORD=your-redis-password
Run the backend server:

bash
uvicorn main:app --reload
The API will be live at http://127.0.0.1:8000.

Frontend Setup
Open a new terminal and navigate to the frontend folder.

Install frontend dependencies:

bash
npm install
Configure environment variables in frontend/.env:

text
VITE_API_URL=http://127.0.0.1:8000
Run the frontend app:

bash
npm run dev
The app will open at http://localhost:5173.

Future Scope
Enhanced AI matching algorithms for internships.

Full offline capability leveraging PWA features.

Real-time notifications for new high-match opportunities.

License
This project is under the MIT License.

For any questions or contributions, please open an issue or submit a pull request!

