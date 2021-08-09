from django.shortcuts import render
import logging
import random
from telegram import *
from telegram.ext import *
from . import telegram_bot
from bot_server import telegram_bot

def index(request):
    FAT_COUNT, DUMB_COUNT, STUPID_COUNT = res()
    context = {
        'FAT_COUNT'     : FAT_COUNT,
        'DUMB_COUNT'    : DUMB_COUNT,
        'STUPID_COUNT'  : STUPID_COUNT
    }
    
    return render(request, 'bot_server/index.html', context=context)

def res():
    FAT_COUNT    = telegram_bot.FAT_COUNT
    DUMB_COUNT   = telegram_bot.DUMB_COUNT
    STUPID_COUNT = telegram_bot.STUPID_COUNT
    return FAT_COUNT, DUMB_COUNT, STUPID_COUNT

def execute(request):
    telegram_bot.main()
    return render(request, 'bot_server/data.html')


