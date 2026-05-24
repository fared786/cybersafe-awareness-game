import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from app import app


def test_login_page_loads():
    tester = app.test_client()
    response = tester.get("/login")
    assert response.status_code == 200
    assert b"CyberSafe Awareness Game" in response.data


def test_home_redirects_to_login():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 302


def test_student_dashboard_requires_login():
    tester = app.test_client()
    response = tester.get("/student/dashboard", follow_redirects=True)
    assert response.status_code == 200
    assert b"Secure Login Portal" in response.data


def test_teacher_dashboard_requires_login():
    tester = app.test_client()
    response = tester.get("/teacher/dashboard", follow_redirects=True)
    assert response.status_code == 200
    assert b"Secure Login Portal" in response.data


def test_valid_login_redirects_to_twofa():
    tester = app.test_client()
    response = tester.post(
        "/login",
        data={
            "username": "student1",
            "password": "Password123!"
        },
        follow_redirects=False
    )
    assert response.status_code == 302
    assert "/twofa" in response.headers["Location"]