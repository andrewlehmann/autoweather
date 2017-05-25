import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from auto_weather import location
from auto_weather import getweather
from auto_weather import message
from auto_weather import mongo
