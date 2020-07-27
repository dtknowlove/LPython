import schedule
import time

running=False;

def register(time_str,job):
    schedule.every().day.at(time_str).do(job)

def run():   
    running=True
    print("schedule runnnig...")
    while running:
        schedule.run_pending()
        time.sleep(1)
def stop():
    running=False
    print("stop schedule!")



