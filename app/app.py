from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os
import time
from . __init__ import celery
from app import nlp


app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)
