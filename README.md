# Infrastructure Health Prediction

> A hands-on DevOps project demonstrating infrastructure monitoring, health analysis, predictive reporting, and observability using Python, Docker, Prometheus, Grafana, and Node Exporter.

---

## Project Overview

Modern production environments require continuous monitoring to maintain high availability and prevent unexpected failures.

Infrastructure Health Prediction demonstrates how DevOps engineers can deploy a monitoring stack, collect infrastructure metrics, analyze system health, detect potential infrastructure risks, and generate automated health reports.

This project combines Python automation with industry-standard monitoring tools to simulate a real-world infrastructure monitoring workflow.

---

# Architecture

![Architecture](screenshots/architecture.png)

---

# Technologies Used

- Python 3
- Docker
- Docker Compose
- Prometheus
- Grafana
- Node Exporter
- Pandas
- Psutil
- Git
- GitHub

---

# Features

- Infrastructure Health Monitoring
- Historical Failure Analysis
- CPU Monitoring
- Memory Monitoring
- Disk Space Prediction
- Network Monitoring
- Security Detection
- Infrastructure Cost Optimization
- Automated Health Reporting
- Docker-based Monitoring Stack

---

# Project Structure

```text
Infrastructure-Health-Prediction/

├── screenshots/
├── scripts/
├── data/
├── reports/
├── docker-compose.yml
├── prometheus.yml
├── requirements.txt
├── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/feranzeey/Infrastructure-Health-Prediction.git
```

Move into the project

```bash
cd Infrastructure-Health-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Start the Monitoring Stack

```bash
docker compose up -d
```

The following services will start:

- Prometheus
- Grafana
- Node Exporter

---

# Run the Prediction Modules

Failure Prediction

```bash
python scripts/failure_prediction.py
```

Resource Prediction

```bash
python scripts/resource_prediction.py
```

Disk Prediction

```bash
python scripts/disk_prediction.py
```

Network Prediction

```bash
python scripts/network_prediction.py
```

Security Detection

```bash
python scripts/security_detection.py
```

Cost Optimization

```bash
python scripts/cost_optimizer.py
```

Generate Health Report

```bash
python scripts/health_report.py
```

---

# Project Demonstration

## Docker Monitoring Stack

Docker Compose successfully deploys Prometheus, Grafana, and Node Exporter.

![Docker Stack](screenshots/docker-stack.png)

---

## Infrastructure Failure Prediction

The prediction module analyzes historical infrastructure metrics and identifies high-risk periods.

![Failure Prediction](screenshots/failure-prediction.png)

---

## Generated Infrastructure Health Report

The project automatically generates an infrastructure health report.

![Health Report](screenshots/health-report.png)

---

## Prometheus Monitoring

Prometheus collects and stores infrastructure metrics.

![Prometheus Dashboard](screenshots/prometheus-dashboard.png)

---

## Grafana Dashboard

Grafana visualizes infrastructure metrics for real-time monitoring.

![Grafana Dashboard](screenshots/grafana-dashboard.png)

---

## VS Code Project

Development environment used for the project.

![VS Code](screenshots/project-structure.png)

---

# Example Health Report

```
Infrastructure Health Report

CPU Usage: 62.9%

Memory Usage: 88.4%

Disk Usage: 97.1%

Overall Status:
Attention Required
```

---

# Skills Demonstrated

- Infrastructure Monitoring
- Docker Compose
- Prometheus
- Grafana
- Node Exporter
- Python Automation
- Linux Monitoring
- Observability
- Infrastructure Reporting
- DevOps Best Practices

---

# Learning Outcomes

After completing this project, learners will understand how to:

- Deploy monitoring infrastructure
- Configure Prometheus
- Build Grafana dashboards
- Monitor Linux resources
- Automate infrastructure health analysis
- Generate health reports
- Apply observability concepts

---

# Future Improvements

- Email Alerts
- Slack Notifications
- Microsoft Teams Integration
- Kubernetes Monitoring
- AWS CloudWatch Integration
- Azure Monitor Integration
- Machine Learning Predictions
- Grafana Alert Rules
- Multi-Server Monitoring

---

# Author

**Oluwaferanmi Dada**

GitHub: https://github.com/feranzeey

If you found this project useful, consider giving it a ⭐ on GitHub.
