from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import logging

app = Flask(__name__)
app.secret_key = "change-this-secret-key-for-production"

# Basic logging for security monitoring evidence
logging.basicConfig(
    filename="security.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Demo users for prototype
# Password for both users: Password123!
users = {
    "student1": {
        "password": generate_password_hash("Password123!"),
        "role": "student",
        "score": 0
    },
    "teacher1": {
        "password": generate_password_hash("Password123!"),
        "role": "teacher",
        "score": 0
    }
}


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
            logging.info(f"Successful password check for user: {username}")
            return redirect(url_for("twofa"))

        logging.warning(f"Failed login attempt for username: {username}")
        flash("Invalid username or password.", "error")

    return render_template("login.html")


@app.route("/twofa", methods=["GET", "POST"])
def twofa():
    if "pending_user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        code = request.form.get("code", "").strip()

        # Demo 2FA code for educational prototype
        if code == "123456":
            username = session.pop("pending_user")
            session["user"] = username
            session["role"] = users[username]["role"]

            logging.info(f"2FA success for user: {username}")

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


@app.route("/teacher/dashboard")
def teacher_dashboard():
    if session.get("role") != "teacher":
        flash("Access denied. Teacher role required.", "error")
        return redirect(url_for("login"))

    return render_template("teacher_dashboard.html", users=users)


@app.route("/logout")
def logout():
    user = session.get("user", "unknown")
    session.clear()
    logging.info(f"User logged out: {user}")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
    