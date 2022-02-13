# pip install schedule 설치

from datetime import datetime
import schedule
import time

def job():
    now = datetime.now()
    print(now)

schedule.every().minutes.do(job)    # 매 분마다 해당 job을 실행시켜라

schedule.every().hour.do(job)

schedule.every().day.at('17:41').do(job)

schedule.every().monday.do(job)

while True:
    schedule.run_pending()
    time.sleep(0.5)
