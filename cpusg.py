import psutil
import time

# Set the threshold (e.g., 80%)
threshold = 80

print("Monitoring CPU usage...")

try:
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)  # Get current CPU usage
        if cpu_percent > threshold:
            print(f"Alert! CPU usage exceeds threshold: {cpu_percent:.2f}%")
        time.sleep(1)  # Wait for 1 second before checking again

except KeyboardInterrupt:
    print("\nMonitoring stopped. Program interrupted.")