from . __init__ import celery
from app import app
# from flask_socketio import SocketIO, emit, send

# socketio = SocketIO(app, engineio_logger=True)



import spacy
import time

@celery.task(bind=True)
def nlp_process(self, a_type=None):
    self.update_state(state="STARTED")
    time.sleep(8)
    self.update_state(state="SUCCESS")

    print('it happened!')

    return True


# @socketio.on('status', namespace='/events')
# def test_message(message):
#     socketio.emit('my response', {'data': message}, broadcast=True)

# @socketio.on('my response')
# def responded():
#     print("Actually received successfully")
