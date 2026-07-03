# Infrastructure Health Prediction

## Overview

Infrastructure Health Prediction is a DevOps monitoring project that demonstrates how predictive analytics can be used to monitor infrastructure health, detect potential issues, and generate automated health reports.

The project combines Docker, Prometheus, Grafana, Python, and system monitoring techniques to analyze infrastructure metrics and provide recommendations before failures occur.

---

## Objectives

- Analyze historical infrastructure failures
- Predict potential infrastructure issues
- Forecast disk space exhaustion
- Monitor CPU and memory utilization
- Detect possible network congestion
- Identify security anomalies
- Recommend infrastructure cost optimization
- Generate automated infrastructure health reports

---

## Technologies Used

- Python 3
- Docker
- Prometheus
- Grafana
- Node Exporter
- Pandas
- Psutil
- Git
- GitHub

---

## Project Structure

```
Infrastructure-Health-Prediction/
│
├── data/
│   └── infrastructure_metrics.csv
│
├── reports/
│   └── health_report.txt
│
├── screenshots/
│
├── scripts/
│   └── failure_prediction.py
│
├── cost_optimizer.py
├── disk_prediction.py
├── docker-compose.yml
├── health_report.py
├── network_prediction.py
├── resource_prediction.py
├── security_detection.py
├── requirements.txt
└── README.md
```

---

## Features

### Historical Failure Analysis

Analyzes historical infrastructure metrics and identifies periods with increased failure risk.

### Disk Space Forecasting

Monitors disk utilization and predicts possible storage exhaustion.

### Resource Monitoring

Tracks CPU and memory usage and generates warnings when usage exceeds predefined thresholds.

### Network Monitoring

Monitors network traffic and predicts possible congestion.

### Security Monitoring

Checks authentication logs for failed login attempts to identify potential security anomalies.

### Cost Optimization

Provides recommendations to scale infrastructure resources based on current utilization.

### Automated Health Reports

Generates infrastructure reports containing:

- CPU Usage
- Memory Usage
- Disk Usage
- Overall Infrastructure Health Status

---

## Installation

Clone the repository.

```bash
git clone https://github.com/feranzeey/Infrastructure-Health-Prediction.git
cd Infrastructure-Health-Prediction
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Failure Prediction

```bash
python scripts/failure_prediction.py
```

### Disk Prediction

```bash
python disk_prediction.py
```

### Resource Prediction

```bash
python resource_prediction.py
```

### Network Prediction

```bash
python network_prediction.py
```

### Security Detection

```bash
python security_detection.py
```

### Cost Optimization

```bash
python cost_optimizer.py
```

### Generate Infrastructure Health Report

```bash
python health_report.py
```

The generated report will be saved in:

```
reports/health_report.txt
```

---

## Docker Monitoring Stack

Start the monitoring environment.

```bash
docker compose up -d
```

Services:

- Prometheus
- Grafana
- Node Exporter

---

## Example Health Report

```
Infrastructure Health Report

CPU Usage: 62.9%

Memory Usage: 88.4%

Disk Usage: 97.1%

Overall Status:
Attention Required
```

---

## Future Improvements

- Email notifications
- Slack alert integration
- Machine learning-based predictions
- Kubernetes monitoring
- Cloud infrastructure monitoring
- Grafana dashboards with predictive analytics
- Automated scheduling using cron or Task Scheduler

---

## Learning Outcomes

This project demonstrates practical knowledge of:

- Infrastructure Monitoring
- Predictive Maintenance
- Python Automation
- Docker
- Prometheus
- Grafana
- System Health Reporting
- DevOps Monitoring Practices

---

## Author

**Oluwaferanmi Dada**

GitHub: https://github.com/feranzeey