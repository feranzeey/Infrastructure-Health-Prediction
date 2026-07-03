import psutil

cpu = psutil.cpu_percent(interval=1)

memory = psutil.virtual_memory().percent

print("CPU:", cpu)
print("Memory:", memory)

if cpu < 20:
    print("Recommendation:")
    print("Reduce VM Size")

elif cpu > 80:
    print("Recommendation:")
    print("Increase VM Size")

else:
    print("Current VM Size is Appropriate")
