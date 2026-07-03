import psutil
import datetime

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent

disk = psutil.disk_usage("/").percent

report = f"""
Infrastructure Health Report

Date: {datetime.datetime.now()}

CPU Usage: {cpu}%

Memory Usage: {memory}%

Disk Usage: {disk}%

Overall Status:
"""

if cpu < 80 and memory < 80 and disk < 80:
    report += "Healthy"

else:
    report += "Attention Required"

with open("reports/health_report.txt","w") as file:
    file.write(report)

print(report)
