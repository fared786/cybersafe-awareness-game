# DevSecOps Pipeline Notes

## Pipeline Platform

GitHub Actions is used as the CI/CD platform.

## Pipeline Stages

### 1. Build

- Checks out the source code.
- Sets up Python 3.11.
- Installs project dependencies from requirements.txt.

### 2. Security Scan

Security scanning includes:

#### Bandit SAST

Bandit scans the Python source code for common security issues.

#### Dependency Audit

pip-audit checks installed Python packages for known vulnerabilities.

### 3. Test

Pytest runs automated functional tests to confirm the application behaves correctly.

### 4. Deploy Simulation

A deployment simulation confirms that the pipeline reaches the final stage successfully.

## DevSecOps Value

This pipeline integrates security checks directly into the software development lifecycle. Security testing runs automatically when code is pushed, helping the team identify issues early.
