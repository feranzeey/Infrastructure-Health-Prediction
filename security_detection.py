import subprocess

logs = subprocess.getoutput("sudo cat /var/log/auth.log | grep Failed")

count = logs.count("Failed")

print("Failed Login Attempts:", count)

if count > 5:
    print("Security Anomaly Detected")
else:
    print("Normal Activity")
