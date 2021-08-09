from django.shortcuts import render
import logging
import random
from telegram import *
from telegram.ext import *
from . import telegram_bot

def index(request):
    FAT_COUNT, STUPID_COUNT, DUMB_COUNT = telegram_bot.main()

    context = {
        'FAT_COUNT': FAT_COUNT, 
        'STUPID_COUNT': STUPID_COUNT, 
        'DUMB_COUNT':DUMB_COUNT
    }
    return render(request, 'bot_server/index.html', context=context)



