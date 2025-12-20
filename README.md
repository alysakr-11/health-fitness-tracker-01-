\# 🏃‍♂️ Health \& Fitness Tracker – Django Web Application



A web-based Health \& Fitness Tracker built using \*\*Django\*\* that helps users manage their fitness activities, goals, reminders, and personal profiles.  

This project was developed as part of a \*\*software engineering course\*\* and follows best practices in \*\*UI design, system architecture, and CI/CD integration\*\*.



---



\## 📌 Project Overview



The Health \& Fitness Tracker is a user-centered web application that allows users to:



\- Create an account and log in securely

\- Track daily check-ins and fitness progress

\- Set personal fitness goals

\- Manage reminders

\- View and update their user profile

\- Navigate through a clean and intuitive dashboard



The project is structured to be scalable and suitable for real-world extension.



---



\## 🚀 Features



\- 🔐 User Authentication (Sign up, Login, Logout, Forgot Password)

\- 🏠 Home Dashboard

\- ✅ Daily Check-in

\- 🎯 Goals Management

\- ⏰ Reminders

\- 👤 User Profile

\- ⚙️ Settings Page

\- 🧭 Connected Navigation Between Pages

\- 🔁 CI/CD Pipeline with GitHub Actions



---



\## 🧩 Project Structure



health-fitness-tracker/

│

├── tracker/ # Main Django app

│ ├── views.py

│ ├── urls.py

│

├── core/ # Project configuration

│ ├── settings.py

│ ├── urls.py

│

├── templates/

│ ├── home.html

│ ├── checkin.html

│ ├── goals.html

│ ├── reminders.html

│ ├── setting.html

│ ├── userprofile.html

│ └── registration/

│ ├── login.html

│ ├── signup.html

│ └── password\_reset\_form.html

│

├── .github/workflows/

│ └── django-ci.yml # CI pipeline

│

├── manage.py

├── db.sqlite3

└── README.md

---



\## ⚙️ Technologies Used



\- \*\*Backend:\*\* Python, Django

\- \*\*Frontend:\*\* HTML, CSS

\- \*\*Database:\*\* SQLite

\- \*\*Version Control:\*\* Git \& GitHub

\- \*\*CI/CD:\*\* GitHub Actions



---



\## 🔄 CI/CD Pipeline



This project uses \*\*GitHub Actions\*\* to implement Continuous Integration (CI).



\### Pipeline Features:

\- Automatically triggered on every push and pull request

\- Sets up Python environment

\- Installs Django dependencies

\- Runs Django system checks to ensure project integrity



📁 Pipeline configuration:



---



\## ▶️ How to Run the Project Locally



\### 1️⃣ Clone the Repository

```bash

git clone https://github.com/alysakr-11/health-fitness-tracker-01- 

cd health-fitness-tracker-01-

2️⃣ Create and Activate Virtual Environment 

&nbsp;    python -m venv venv

&nbsp;    venv\\Scripts\\activate   # Windows

3️⃣ Install Dependencies

&nbsp;   pip install django 

4️⃣ Run the Server 

&nbsp;  python manage.py runserver

5️⃣ Open in Browser 

&nbsp;  http://127.0.0.1:8000/

&nbsp;## 📐 UML Diagrams \& Design Documentation



The following UML and design diagrams were created to model and document the complete system:



\- \*\*Activity Diagram\*\*

\- \*\*Architecture Diagram\*\*

\- \*\*Class Diagram\*\*

\- \*\*Context Diagram\*\*

\- \*\*Sequence Diagram\*\*

\- \*\*State Diagram\*\*

\- \*\*Use Case Diagram\*\*

\- \*\*Wireframe Designs\*\*



These diagrams collectively describe the system structure, behavior, interactions, and user experience, and were developed according to the concepts covered in the course lectures.



--- 

📎 Notes

This project is intended for educational purposes.

The repository is structured and documented to be suitable for showcasing on GitHub and including in a resume. 



👤 Author

Ali

Computer Science Student

University Project – Health \& Fitness Tracker 



