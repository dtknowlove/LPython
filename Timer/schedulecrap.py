import schedule
import time

running=False;

def run(time_str,job):
    schedule.every().day.at(time_str).do(job)
    running=True
    print("schedule runnnig...")
    while running:
        schedule.run_pending()
        time.sleep(1)
def stop():
    running=False
    print("stop schedule!")



