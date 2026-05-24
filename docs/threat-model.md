# Threat Model - CyberSafe Awareness Game

## 1. Project Context

CyberSafe Awareness Game is a web-based cybersecurity awareness training application. It allows students to log in, complete cybersecurity quiz challenges, view instant feedback, and track their score. Teachers can access a dashboard to review student progress.

The application includes authentication, role-based access control, two-factor authentication, logging, automated testing, and DevSecOps pipeline checks.

## 2. Assets

| Asset | Description | Security Importance ||---|---|---|
| User accounts | Student and teacher login details | Must be protected from unauthorized access |
| Student scores | Quiz progress and learning outcomes | Must be protected from unauthorized modification |
| Teacher dashboard | Progress monitoring area | Must only be accessible by teacher role |
| Application source code | Flask app and templates | Must be scanned for vulnerabilities |
| Logs | Login, 2FA, logout, and quiz completion records | Useful for monitoring and incident response |

## 3. Threat Actors

| Threat Actor | Motivation ||---|---|
| Unauthorized student | Attempts to access teacher dashboard |
| External attacker | Attempts to bypass login or exploit input fields |
| Malicious user | Attempts to manipulate score or session |
| Accidental user | Enters incorrect details or triggers errors unintentionally |

## 4. Main Threats

| Threat | Risk | Mitigation ||---|---|---|
| Brute-force login attempts | Medium | Login attempt logging and strong password requirement |
| Broken access control | High | Role checks before accessing student or teacher pages |
| Session misuse | Medium | Server-side session validation before protected routes |
| Plain-text password storage | High | Passwords are hashed using Werkzeug security functions |
| Input manipulation | Medium | Form inputs are validated and stripped where relevant |
| Dependency vulnerabilities | Medium | pip-audit is included in CI/CD pipeline |
| Insecure code patterns | Medium | Bandit SAST scan is included in CI/CD pipeline |

## 5. OWASP Top 10 Coverage

| OWASP Area | Project Mitigation ||---|---|
| Broken Access Control | RBAC prevents students from accessing teacher dashboard |
| Identification and Authentication Failures | Login uses password hashing and 2FA flow |
| Security Misconfiguration | GitHub Actions pipeline checks the app automatically |
| Vulnerable and Outdated Components | pip-audit checks dependency vulnerabilities |
| Software and Data Integrity Failures | CI/CD pipeline validates code before deployment simulation |
| Cross-Site Scripting | Content-Security-Policy restricts script execution sources |
| Security Misconfiguration | Security headers reduce unsafe default browser behaviour |

## 6. Ethical Scope

This project is a defensive cybersecurity awareness tool. It does not attack real systems or collect real user data. All users and credentials are demo-based for educational purposes only.

## 7. Risk Rating Summary

| Risk | Likelihood | Impact | Rating ||---|---|---|---|
| Unauthorized dashboard access | Medium | High | High |
| Weak user awareness | High | Medium | High |
| Dependency vulnerability | Medium | Medium | Medium |
| Failed login attempts | Medium | Low | Medium |
| Data loss in prototype memory storage | Low | Low | Low |

## 8. Conclusion

The threat model shows that access control, authentication, dependency management, and secure coding are the main security priorities for this project. The implemented controls reduce the major risks and support the DevSecOps approach required for the assessment.
