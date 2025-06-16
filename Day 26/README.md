# Automating Tasks with Python - Daily Reminder to do TryHackMe Questions.

This is a simple automation script that reminds me daily at **10:00 AM** to complete my TryHackMe Questions for the day.

## What It Does:
- Sends a desktop notification at **10:00 AM** every day.
- Uses the `plyer` library for cross-platform notifications.
- Runs in the background using `schedule`.

## Installation:

Make sure Python is installed on your system. Then install the required libraries:

``bash
pip install schedule plyer
``

_Note: plyer works well for system notifications on Windows, macOS, and some Linux environments. If you face issues on Linux, you might need to install libnotify or run the script in a graphical session._
