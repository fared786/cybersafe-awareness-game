# Testing Results - CyberSafe Awareness Game

## 1. Testing Overview

Testing was performed to validate both functionality and security. The project uses manual testing, automated functional testing, static application security testing, and dependency vulnerability scanning.

## 2. Functional Testing

| Test Case | Expected Result | Actual Result | Status ||---|---|---|---|
| Login page loads | Login page should display correctly | Page loaded successfully | Passed |
| Student login with valid credentials | User should proceed to 2FA page | Redirected to 2FA page | Passed |
| Teacher login with valid credentials | User should proceed to 2FA page | Redirected to 2FA page | Passed |
| Invalid login attempt | Error message should appear | Error displayed | Passed |
| Correct 2FA code | User should access role-based dashboard | Dashboard displayed | Passed |
| Student accesses teacher dashboard | Access should be denied | Redirected to login | Passed |
| Student submits quiz | Score and feedback should display | Score and instant feedback displayed | Passed |
| Teacher views progress | Student score should be visible | Score shown in teacher dashboard | Passed |

## 3. Automated Testing with Pytest

Pytest was used to confirm that core routes and access controls behave correctly.

Automated tests covered:

- Login page loading
- Home page redirect
- Protected student dashboard
- Protected teacher dashboard
- Valid login redirect to 2FA

Result:

```text
5 passed


## 9. Incident Response Simulation Result

A simulated failed-login incident was performed to test monitoring and response capability.

| Incident Test | Expected Result | Actual Result | Status | |---|---|---|---|
| Failed login attempt | Event should be logged | Event appeared in security.log | Passed |
| Teacher views logs | Recent security events should be visible | Logs displayed in teacher monitoring page | Passed |
| Unauthorized dashboard access | Access should be denied | User redirected to login page | Passed |

The incident simulation confirmed that the application can detect and record basic authentication-related security events.
