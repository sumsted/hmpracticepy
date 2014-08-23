__author__ = 'scottumsted'
from flask import Flask

app = Flask(__name__)
app.config.from_envvar('HMPRACTICEPY_SETTINGS', silent=False)
import hmpracticepy.views
