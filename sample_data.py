import requests
import random
import time
from datetime import datetime

API = 'http://127.0.0.1:5000/api/events'

events = ['page_view', 'button_click', 'signup_click', 'form_submit']

def send(ev):
    payload = {
        'event_name': ev,
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'user_id': 'user' + str(random.randint(1,5)),
        'session_id': 'sess' + str(random.randint(1,3)),
        'url': 'http://example.com/page' + str(random.randint(1,3)),
        'referrer': 'http://google.com',
        'device': {'os':'Windows','browser':'Chrome','device_type': 'desktop'},
        'metadata': {'sample': True}
    }
    try:
        r = requests.post(API, json=payload, timeout=2)
        print(r.status_code, r.text)
    except Exception as e:
        print('failed', e)

if __name__=='__main__':
    for _ in range(30):
        send(random.choice(events))
        time.sleep(0.1)
