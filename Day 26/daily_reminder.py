import schedule
import time
from plyer import notification

def send_reminder():
    notification.notify(
        title="Daily Cyber Security Training Reminder",
        message="Remember to do your daily TryHackMe Questions!",
        timeout=10  #how many seconds the notification stays
    )

# Scheduling the reminder at 10:00 AM every day
schedule.every().day.at("10:00").do(send_reminder)

print("Daily reminder set for 10:00 AM. Keep this script running...")

while True:
    schedule.run_pending()
    time.sleep(1)
