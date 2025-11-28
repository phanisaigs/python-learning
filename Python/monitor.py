import shutil
import psutil
import smtplib

# config
THRESHOLD = 80
check_paths = ["/data"]

def check_diskusage(path)
    percent_used = (usage.used / usage.total) * 100
    return percent_used