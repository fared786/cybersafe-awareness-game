# CyberSafe Awareness Game

## Project Overview

CyberSafe Awareness Game is a cybersecurity education web application designed
to teach students basic cybersecurity awareness through interactive quiz
challenges.

The project focuses on phishing detection, password security, social engineering
awareness, and secure browsing practices.

## Main Features

- Secure login system
- Role-Based Access Control for Student and Teacher roles
- Two-Factor Authentication demo
- Cybersecurity quiz challenges
- Scoring and progress tracking
- Teacher dashboard for viewing student progress
- DevSecOps pipeline with automated security checks

## Technology Stack

- Python
- Flask
- HTML/CSS
- Pytest
- Bandit
- pip-audit
- GitHub Actions

## Repository Structure

```text
/src      - Source code
/docs     - Documentation
/tests    - Test files
/ci-cd    - Pipeline notes and DevSecOps documentation
README.md - Setup and usage instructions
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/fared786/cybersafe-awareness-game
cd cybersafe-awareness-game



# Project Summary - CyberSafe Awareness Game

## Project Objective

CyberSafe Awareness Game is a web-based cybersecurity awareness training prototype. The objective is to teach users about phishing, password security, and social engineering through interactive quiz challenges.

## Why This Project Was Selected

This project was selected because it is safe, practical, achievable within the available time, and directly connected to cybersecurity education. It does not require testing against real external systems, which reduces ethical and technical risk.

## Implemented Features

- Secure login system
- Password hashing
- Two-factor authentication demo
- Role-based access control
- Student dashboard
- Teacher dashboard
- 15 cybersecurity awareness quiz challenges
- Instant feedback
- Score calculation
- Achievement badges
- SQLite progress tracking
- Security event logging
- Teacher security monitoring page
- Incident response simulation
- Security headers
- Automated testing
- DevSecOps GitHub Actions pipeline

## DevSecOps Implementation

The project follows DevSecOps principles by integrating security into development, testing, and deployment simulation.

Pipeline stages:


Build → Security Scan → Test → Deploy Simulation

## Team Members and Contributions

| Team Member | Student ID | Contribution | Main Contributions |
|---|---|---:|---|
| Farhad Hossain | cihe240509 | 33.34% | Lead technical implementation; Flask backend; login; RBAC; 2FA demo; quiz logic; SQLite progress tracking; security headers; GitHub Actions pipeline; Bandit, pip-audit, and Pytest integration; troubleshooting pipeline and security issues; incident response simulation. |
| Ujwal Paudel | cihe240544 | 33.33% | Documentation support; requirements review; testing evidence preparation; functional testing support; README review; report and presentation content support. |
| Samir Raut | cihe240444 | 33.33% | UI review; quiz content review; screenshot evidence support; testing results documentation; threat model and risk analysis support; presentation preparation. |

## Key Deliverables Completed

| Requirement | Status | Evidence |
|---|---|---|
| GitHub Repository | Completed | Source code, documentation, tests, CI/CD files |
| Required Structure | Completed | `/src`, `/docs`, `/tests`, `/ci-cd`, `README.md` |
| Authentication | Completed | Login system with hashed passwords |
| Authorization | Completed | Student and Teacher roles |
| 2FA | Completed | Demo two-factor authentication flow |
| Security Testing | Completed | Bandit, pip-audit, pytest |
| CI/CD Pipeline | Completed | GitHub Actions workflow |
| Documentation | Completed | Threat model, testing results, incident response simulation |
| Monitoring | Completed | Teacher security logs page |
| Incident Response | Completed | Failed-login incident simulation |
| Presentation Evidence | Ready | Screenshots and live demo flow |

## Live Demo Flow

During the presentation, the live demo will follow this sequence:

1. Open the CyberSafe Awareness Game login page.
2. Log in as a student using demo credentials.
3. Complete the 2FA verification step.
4. Open the student dashboard.
5. Start the cybersecurity quiz.
6. Submit answers and show score, instant feedback, and achievement badge.
7. Log out.
8. Log in as teacher.
9. Show teacher dashboard with saved student progress.
10. Open security logs page.
11. Show GitHub Actions DevSecOps pipeline.
12. Show automated testing and security scan evidence.

## Security Testing Summary

| Tool / Method | Purpose |
|---|---|
| Pytest | Automated functional testing |
| Bandit | Static Application Security Testing for Python code |
| pip-audit | Dependency vulnerability scanning |
| Manual Testing | Login, 2FA, RBAC, quiz, dashboard and monitoring validation |
| Security Headers Test | Checks browser-side security configuration |

## Future Improvements

Future versions of this project could include:

- Real 2FA using PyOTP or Google Authenticator
- Persistent user account database
- Account lockout after repeated failed login attempts
- Email alerts for suspicious activity
- More quiz categories and difficulty levels
- Student progress charts
- Deployment to a secure cloud platform
