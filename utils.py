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
from twilio_config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, PHONE_NUMBER, API_KEY_WAPI

from pycoingecko import CoinGeckoAPI


''' CoinGecko'''
def get_crypto():
    cg = CoinGeckoAPI()
    coins=['bitcoin', 'ethereum']
    simplePriceRequest = cg.get_price(ids = coins, vs_currencies='usd')
    btc = simplePriceRequest['bitcoin']['usd']
    eth = simplePriceRequest['ethereum']['usd']
    crypto = [btc, eth]
    return crypto

''' Dolar API'''
def get_dolar():
    r = requests.get('https://api.bluelytics.com.ar/v2/latest')
    data = r.json()
    fecha = data['last_update'].split('T')[0]
    dolar_oficial = data['oficial']['value_avg']
    dolar_blue = data['blue']['value_avg']
    datos_dolar = [fecha, dolar_oficial, dolar_blue]
    return datos_dolar

''' Twilio Whatsapp'''
def send_message(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN):
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    
    from_whatsapp_number = 'whatsapp:+14155238886'
    to_whatsapp_number = 'whatsapp:+5492612539749'

    dolar = get_dolar()
    crypto = get_crypto()

    client.messages.create(body=f'Hola! ¿Cómo estás? \nLas cotizaciones para hoy {dolar[0]} son: \n \nDólar oficial ${dolar[1]} \nDólar blue ${dolar[2]} \nBTC: ${crypto[0]} \nETH: ${crypto[1]} \nHasta pronto!', 
                    from_=from_whatsapp_number, 
                    to=to_whatsapp_number)
    return print('Mensaje enviado!')
