import psutil

#psutil library is imported to fetch system information, such as CPU usage
#Install :- pip install psutil

import time

# Set the threshold (as 80%)


threshold = 80

print("Monitoring CPU usage...")

try:
    while True:
# Get the current CPU usage in percentage, below method returns the CPU usage percentage over a 1-second interval.
        cpu_percent = psutil.cpu_percent(interval=1) 

 # Get current CPU usage and check whether CPU usage exceeds than the 80% threshold

        if cpu_percent > threshold:
            print(f"Alert! CPU usage exceeds threshold: {cpu_percent:.2f}%")

# Wait for a short period before monitoring once again

        time.sleep(1) 

except KeyboardInterrupt:
# when use input is given as CTL+C

    print("\nMonitoring stopped. Program interrupted, stopped by user")
except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")
    