import shutil

total, used, free = shutil.disk_usage("/")

percent = used / total * 100

print("Disk Usage")

print(f"{percent:.2f}%")

if percent > 80:
    print("Prediction: Disk may become full soon.")
else:
    print("Disk Healthy")
