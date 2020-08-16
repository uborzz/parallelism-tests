from time import sleep
from asyncio import sleep as asleep
from fastapi import FastAPI
from flask import Flask, request
from datetime import datetime, timedelta
from uuid import uuid4
import requests


flsk = Flask("flask app")
fapi = FastAPI()

# sync instant request
@flsk.route("/")
@fapi.get("/")
def main_call():
    ended = f"{datetime.now()} - 🆗 Main call"
    print(ended)
    return ended + "\n"


# sleep
# -----

# flask
@flsk.route("/sleep")
def sync_sleep():
    t = request.args.get('t')
    s = request.args.get('s')
    s = s if s else 10
    print(f"{datetime.now()} - {t} - ⛔ Sync started")
    sleep(int(s))
    ended = f"{datetime.now()} - {t} - ✅ Sync ended"
    print(ended)
    return ended + "\n"

# fastapi
@fapi.get("/sleep")
def fastapi_sync_sleep(t=0, s=10):
    print(f"{datetime.now()} - {t} - ⛔ Sync started")
    sleep(int(s))
    ended = f"{datetime.now()} - {t} - ✅ Sync ended"
    print(ended)
    return ended + "\n"

@fapi.get("/asleep")
async def async_sleep(t=0, s=10):
    print(f"{datetime.now()} - {t} - ⛔ Async started")
    await asleep(int(s))
    ended = f"{datetime.now()} - {t} - ✅ Async ended"
    print(ended)
    return ended + "\n"


# busy
# ----

def keep_busy(iterations):
    multiplier = 10000000
    total = iterations*multiplier
    for i in range(total):
        ...


async def async_keep_busy(iterations):
    multiplier = 10000000
    total = iterations*multiplier
    for i in range(total):
        ...


# flask
@flsk.route("/busy")
def sync_busy():
    t = request.args.get('t')
    s = request.args.get('s') 
    s = s if s else 10
    print(f"{datetime.now()} - {t} - ⛔ Sync started")
    keep_busy(int(s))
    ended = f"{datetime.now()} - {t} - ✅ Sync ended"
    print(ended)
    return ended + "\n"

# fastapi
@fapi.get("/busy")
def fastapi_sync_busy(t=0, s=10):
    print(f"{datetime.now()} - {t} - ⛔ Sync started")
    keep_busy(int(s))
    ended = f"{datetime.now()} - {t} - ✅ Sync ended"
    print(ended)
    return ended + "\n"

@fapi.get("/abusy")
async def async_busy(t=0, s=10):
    print(f"{datetime.now()} - {t} - ⛔ Async started")
    await async_keep_busy(int(s))
    ended = f"{datetime.now()} - {t} - ✅ Async ended"
    print(ended)
    return ended + "\n"
