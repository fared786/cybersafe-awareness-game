from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import logging
import os
import sqlite3

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-demo-secret-key")  # nosec B105

@app.after_request
def add_security_headers(response):
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "style-src 'self' 'unsafe-inline'; "
        "script-src 'self'; "
        "img-src 'self' data:;"
    )
    return response

logging.basicConfig(
    filename="security.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DEMO_PASSWORD = os.getenv("DEMO_PASSWORD", "Password123!")  # nosec B105
DEMO_2FA_CODE = os.getenv("DEMO_2FA_CODE", "123456")  # nosec B105

DATABASE = "cybersafe.db"

quiz_questions = [
    {
        "id": 1,
        "category": "Phishing",
        "question": "Which email is most likely to be a phishing attempt?",
        "options": [
            "An email from your teacher using the official school domain",
            "An urgent email asking you to verify your bank account through a suspicious link",
            "A weekly newsletter you subscribed to",
            "A password reset email you requested"
        ],
        "answer": "An urgent email asking you to verify your bank account through a suspicious link",
        "explanation": "Phishing emails often use urgency and suspicious links to trick users."
    },
    {
        "id": 2,
        "category": "Phishing",
        "question": "What should you check before clicking a link in an email?",
        "options": [
            "The colour of the email",
            "The sender address and actual link destination",
            "The email font size",
            "The number of images"
        ],
        "answer": "The sender address and actual link destination",
        "explanation": "Checking the sender and link destination helps identify suspicious emails."
    },
    {
        "id": 3,
        "category": "Phishing",
        "question": "A phishing email may contain:",
        "options": [
            "Urgent language",
            "Suspicious attachments",
            "Fake login links",
            "All of the above"
        ],
        "answer": "All of the above",
        "explanation": "Phishing attempts often combine urgency, attachments, and fake links."
    },
    {
        "id": 4,
        "category": "Phishing",
        "question": "What is the safest action when receiving a suspicious email?",
        "options": [
            "Reply and ask if it is real",
            "Click the link quickly",
            "Report it or verify through official channels",
            "Forward it to all friends"
        ],
        "answer": "Report it or verify through official channels",
        "explanation": "Suspicious emails should be reported or verified safely."
    },
    {
        "id": 5,
        "category": "Phishing",
        "question": "Which URL looks suspicious?",
        "options": [
            "https://www.microsoft.com",
            "https://login.microsoft-security-alert.example.ru",
            "https://www.google.com",
            "https://www.apple.com"
        ],
        "answer": "https://login.microsoft-security-alert.example.ru",
        "explanation": "Attackers often use misleading subdomains and unusual domains."
    },
    {
        "id": 6,
        "category": "Password Security",
        "question": "Which password is strongest?",
        "options": [
            "password123",
            "Farhad2024",
            "Qz!8vL#2pM@9",
            "12345678"
        ],
        "answer": "Qz!8vL#2pM@9",
        "explanation": "Strong passwords are long, random, and use mixed character types."
    },
    {
        "id": 7,
        "category": "Password Security",
        "question": "What is password reuse?",
        "options": [
            "Using a different password for each account",
            "Using the same password on multiple accounts",
            "Changing a password every day",
            "Using a password manager"
        ],
        "answer": "Using the same password on multiple accounts",
        "explanation": "Password reuse is risky because one breach can affect many accounts."
    },
    {
        "id": 8,
        "category": "Password Security",
        "question": "What is the purpose of multi-factor authentication?",
        "options": [
            "To make websites load faster",
            "To add another layer of identity verification",
            "To delete old passwords",
            "To avoid using usernames"
        ],
        "answer": "To add another layer of identity verification",
        "explanation": "MFA improves security by requiring more than just a password."
    },
    {
        "id": 9,
        "category": "Password Security",
        "question": "Which is a good password practice?",
        "options": [
            "Writing passwords on a public whiteboard",
            "Sharing passwords with classmates",
            "Using a password manager",
            "Using your birthdate as a password"
        ],
        "answer": "Using a password manager",
        "explanation": "Password managers help generate and store strong unique passwords."
    },
    {
        "id": 10,
        "category": "Password Security",
        "question": "Why should passwords be hashed before storage?",
        "options": [
            "To make them easier to read",
            "To protect them if the database is exposed",
            "To remove the need for login",
            "To make the website colourful"
        ],
        "answer": "To protect them if the database is exposed",
        "explanation": "Hashing protects passwords by avoiding plain-text storage."
    },
    {
        "id": 11,
        "category": "Social Engineering",
        "question": "What is social engineering?",
        "options": [
            "A method of building websites",
            "A technique that manipulates people into revealing information",
            "A type of antivirus software",
            "A database backup process"
        ],
        "answer": "A technique that manipulates people into revealing information",
        "explanation": "Social engineering targets human behaviour rather than only technology."
    },
    {
        "id": 12,
        "category": "Social Engineering",
        "question": "Which is an example of social engineering?",
        "options": [
            "A caller pretending to be IT support and asking for your password",
            "Installing official updates",
            "Using a secure VPN",
            "Backing up your files"
        ],
        "answer": "A caller pretending to be IT support and asking for your password",
        "explanation": "Impersonation is a common social engineering technique."
    },
    {
        "id": 13,
        "category": "Social Engineering",
        "question": "What should you do if someone asks for your password?",
        "options": [
            "Share it if they sound professional",
            "Share only half of it",
            "Never share it and report the request",
            "Send it by email"
        ],
        "answer": "Never share it and report the request",
        "explanation": "Passwords should never be shared, even with people claiming authority."
    },
    {
        "id": 14,
        "category": "Social Engineering",
        "question": "Tailgating means:",
        "options": [
            "Following someone into a restricted area without permission",
            "Changing your password",
            "Encrypting files",
            "Updating antivirus software"
        ],
        "answer": "Following someone into a restricted area without permission",
        "explanation": "Tailgating is a physical social engineering attack."
    },
    {
        "id": 15,
        "category": "Social Engineering",
        "question": "Which habit reduces social engineering risk?",
        "options": [
            "Trusting all urgent requests",
            "Verifying identities through official channels",
            "Posting passwords online",
            "Ignoring security training"
        ],
        "answer": "Verifying identities through official channels",
        "explanation": "Verification helps prevent impersonation-based attacks."
    }
]

users = {
    "student1": {
        "password": generate_password_hash(DEMO_PASSWORD),
        "role": "student",
        "score": 0
    },
    "teacher1": {
        "password": generate_password_hash(DEMO_PASSWORD),
        "role": "teacher",
        "score": 0
    }
}


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_db_connection()
    connection.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            category TEXT NOT NULL,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL,
            completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    connection.close()


def save_progress(username, category, score, total):
    connection = get_db_connection()
    connection.execute(
        "INSERT INTO progress (username, category, score, total) VALUES (?, ?, ?, ?)",
        (username, category, score, total)
    )
    connection.commit()
    connection.close()


def get_all_progress():
    connection = get_db_connection()
    progress = connection.execute(
        """
        SELECT username, category, score, total, completed_at
        FROM progress
        ORDER BY completed_at DESC
        """
    ).fetchall()
    connection.close()
    return progress


def get_badge(score):
    if score >= 13:
        return "Cybersecurity Champion"
    if score >= 10:
        return "Security Smart Learner"
    if score >= 7:
        return "Cyber Awareness Beginner"
    return "Needs More Practice"


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        user = users.get(username)

        if user and check_password_hash(user["password"], password):
            session["pending_user"] = username
            logging.info("Successful password check for user: %s", username)
            return redirect(url_for("twofa"))

        logging.warning("Failed login attempt for username: %s", username)
        flash("Invalid username or password.", "error")

    return render_template("login.html")


@app.route("/twofa", methods=["GET", "POST"])
def twofa():
    if "pending_user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        code = request.form.get("code", "").strip()

        if code == DEMO_2FA_CODE:
            username = session.pop("pending_user")
            session["user"] = username
            session["role"] = users[username]["role"]

            logging.info("2FA success for user: %s", username)

            if session["role"] == "teacher":
                return redirect(url_for("teacher_dashboard"))

            return redirect(url_for("student_dashboard"))

        logging.warning("Failed 2FA attempt")
        flash("Invalid 2FA code. Use demo code: 123456", "error")

    return render_template("twofa.html")


@app.route("/student/dashboard")
def student_dashboard():
    if session.get("role") != "student":
        flash("Access denied. Student role required.", "error")
        return redirect(url_for("login"))

    username = session.get("user")
    return render_template("student_dashboard.html", username=username)


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if session.get("role") != "student":
        flash("Access denied. Student role required.", "error")
        return redirect(url_for("login"))

    if request.method == "POST":
        score = 0
        feedback = []

        for question in quiz_questions:
            selected_answer = request.form.get(str(question["id"]))
            is_correct = selected_answer == question["answer"]

            if is_correct:
                score += 1

            feedback.append({
                "question": question["question"],
                "selected": selected_answer,
                "correct": question["answer"],
                "is_correct": is_correct,
                "explanation": question["explanation"]
            })

        username = session.get("user")
        users[username]["score"] = score

        save_progress(
            username,
            "Cybersecurity Awareness Quiz",
            score,
            len(quiz_questions)
        )

        badge = get_badge(score)

        logging.info(
            "Quiz completed by %s. Score: %s/%s",
            username,
            score,
            len(quiz_questions)
        )

        return render_template(
            "quiz.html",
            questions=quiz_questions,
            feedback=feedback,
            score=score,
            badge=badge,
            submitted=True
        )

    return render_template(
        "quiz.html",
        questions=quiz_questions,
        feedback=None,
        score=None,
        badge=None,
        submitted=False
    )


@app.route("/reset-score")
def reset_score():
    if session.get("role") != "student":
        flash("Access denied. Student role required.", "error")
        return redirect(url_for("login"))

    username = session.get("user")
    users[username]["score"] = 0
    logging.info("Score reset by user: %s", username)

    return redirect(url_for("student_dashboard"))


@app.route("/teacher/dashboard")
def teacher_dashboard():
    if session.get("role") != "teacher":
        flash("Access denied. Teacher role required.", "error")
        return redirect(url_for("login"))

    progress_records = get_all_progress()

    return render_template(
        "teacher_dashboard.html",
        users=users,
        progress_records=progress_records
    )


@app.route("/teacher/security-logs")
def security_logs():
    if session.get("role") != "teacher":
        flash("Access denied. Teacher role required.", "error")
        return redirect(url_for("login"))

    logs = []

    try:
        with open("security.log", "r", encoding="utf-8") as log_file:
            logs = log_file.readlines()[-20:]
    except FileNotFoundError:
        logs = ["No security logs available yet."]

    return render_template("security_logs.html", logs=logs)


@app.route("/logout")
def logout():
    user = session.get("user", "unknown")
    session.clear()
    logging.info("User logged out: %s", user)
    return redirect(url_for("login"))


if __name__ == "__main__":
    init_db()
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug_mode)