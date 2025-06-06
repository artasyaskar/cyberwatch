import schedule
import threading
import time

class LogScheduler:
    def __init__(self, func, interval=10):
        self.job = schedule.every(interval).seconds.do(func)

    def start(self):
        def run_scheduler():
            while True:
                schedule.run_pending()
                time.sleep(1)
        thread = threading.Thread(target=run_scheduler)
        thread.daemon = True
        thread.start()
