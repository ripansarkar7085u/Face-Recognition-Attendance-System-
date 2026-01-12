# Face Recognition Attendance System
This project is a Face Recognition–based Attendance System created by following and learning from a YouTube tutorial. It demonstrates how Artificial Intelligence and Computer Vision can be used to automate the attendance process using a webcam.

# Project Files
- ├── Face_Recognition.ipynb # Main project notebook (face recognition logic)
- ├── attendance.db # SQLite database for attendance storage
- ├── practice.py # Extra Python practice file
- ├── tempCodeRunnerFile.python # Temporary file (can be ignored)
- └── README.md # Project documentation

# Project Objective
1.To detect human faces using webcam,
2.To recognize known faces,
3.To automatically mark attendance,
4.To store attendance records in a database,
5.To understand real-world use of Python, OpenCV, and AI .

# Concepts Used
- Face Detection
- Face Recognition
- Computer Vision
- Database (SQLite)
- Real-time webcam processing

# Technologies Used
- Python 3
- OpenCV (cv2)
- face_recognition library
- NumPy
- SQLite3
- Jupyter Notebook.

# How the Project Works
- The webcam opens using OpenCV
- The system detects faces from live video
- Known faces are compared with stored encodings
- If a match is found, attendance is marked
- Attendance is saved with name, date, and time

# Database (attendance.db)
The SQLite database stores attendance records.
Example fields:
- id (Primary Key)
- name (Person name)
- date (Attendance date)
- time (Attendance time)

# How to Run This Project
### - Step 1: Install Required Libraries
  - " pip install opencv-python face_recognition numpy "
### - Step 2: Run Jupyter Notebook
  - "jupyter notebook Face_Recognition.ipynb"
### - Step 3: Allow Webcam Access
  - Run the cells and make sure your webcam is working properly.

# Learning Outcome
Through this project, I learned:
- How face recognition works
- How to use OpenCV with Python
- How to connect Python with SQLite database
- How real-world AI projects are built

# Future Improvements
- Add GUI interface (Tkinter or Web App)
- Improve face accuracy
- Add login system for admin
- Store face encodings in database
- Deploy as a web application
