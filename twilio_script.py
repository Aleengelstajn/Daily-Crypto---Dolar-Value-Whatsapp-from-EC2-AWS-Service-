''' Libraries '''
import os
import time
import pandas as pd
from datetime import datetime

import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

from twilio.rest import Client
from twilio_config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

from pycoingecko import CoinGeckoAPI

from utils import get_dolar, get_crypto, send_message




send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
