from . __init__ import celery
from app import app

import spacy
import time

@celery.task(bind=True)
def nlp_process(self, a_type=None):
    # self.update_state(state="STARTED")
    time.sleep(15)
    # self.update_state(state="SUCCESS")

    print('it happened!')

    return {'current': 100, 'total': 100, 'status': 'Task completed!',
            'result': 42}
