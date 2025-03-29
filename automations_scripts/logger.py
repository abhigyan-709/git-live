import psutil
import time
import logging

# Configure logging
logging.basicConfig(
    filename="system_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - CPU: %(cpu_usage)s%%, RAM: %(ram_usage)s%%, Disk: %(disk_usage)s%%"
)

def log_system_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    
    logging.info("", extra={
        "cpu_usage": cpu_usage,
        "ram_usage": ram_usage,
        "disk_usage": disk_usage
    })
    
    print(f"CPU: {cpu_usage}%, RAM: {ram_usage}%, Disk: {disk_usage}%")

if __name__ == "__main__":
    while True:
        log_system_usage()
        time.sleep(5)  # Log data every 5 seconds
