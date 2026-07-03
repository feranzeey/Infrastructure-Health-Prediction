import psutil

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent

print("CPU:", cpu)
print("Memory:", memory)

if cpu > 80:
    print("Warning: CPU exhaustion predicted")

if memory > 80:
    print("Warning: Memory exhaustion predicted")
