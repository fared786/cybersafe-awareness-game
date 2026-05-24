# Incident Response Simulation

## 1. Incident Scenario

A simulated security incident was performed to test the CyberSafe Awareness Game monitoring and response process.

The scenario involved repeated failed login attempts against the application using an incorrect password. This represented a basic brute-force style authentication threat in a controlled educational environment.

## 2. Incident Type

| Field | Description ||---|---|
| Incident Name | Repeated Failed Login Attempt |
| Incident Category | Authentication Security Incident |
| Severity | Medium |
| Environment | Local Flask development environment |
| Affected Asset | Login system |
| Detection Method | security.log and Teacher Security Logs page |

## 3. Detection

The failed login attempt was detected through application logging.

The Flask application records failed login events using the Python logging module. The teacher dashboard includes a Security Logs page where recent authentication events can be reviewed.

Example event:

```text
WARNING - Failed login attempt for username: student1
