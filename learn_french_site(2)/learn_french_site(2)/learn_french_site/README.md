# Learn French! — Project
This is a beginner-friendly Flask + MySQL project that teaches French vocabulary, grammar, short stories and quizzes.

## Learning Goal
Learn backend basics in Python: variables, routing, error handling, and relational DB CRUD operations using MySQL and SQLAlchemy.

## Product Goal
Create an interactive website that helps students aged 7-12 learn French through vocabulary, grammar, short stories, and quizzes.

## Requirements
- Python 3.10+
- MySQL Server
- VS Code (recommended)

## Setup (quick)
1. Clone or extract this folder.
2. Create and activate a virtualenv:
   - `python -m venv venv`
   - Windows: `venv\Scripts\activate`
   - Linux/macOS: `source venv/bin/activate`
3. Install dependencies:
   - `pip install -r requirements.txt`
4. Create a MySQL database and user (example):
   - `CREATE DATABASE learn_french;`
   - `CREATE USER 'lf_user'@'localhost' IDENTIFIED BY 'lf_password';`
   - `GRANT ALL PRIVILEGES ON learn_french.* TO 'lf_user'@'localhost';`
5. Update `app/config.py` if your DB credentials differ.
6. Option A: Let SQLAlchemy create tables automatically. Start the app:
   - `python run.py`
   - Open `http://127.0.0.1:5000/`

## Admin pages (demo)
- Add vocabulary: `/admin/vocab/new`
- Edit/Delete demo pages available (see `app/routes.py`)

## Notes
- This project is for demo/college submission. Do not use debug settings in production.
