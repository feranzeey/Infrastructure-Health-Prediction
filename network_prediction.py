import psutil

network = psutil.net_io_counters()

print("Bytes Sent:", network.bytes_sent)
print("Bytes Received:", network.bytes_recv)

if network.bytes_recv > 100000000:
    print("High Network Usage Predicted")
else:
    print("Network Healthy")
