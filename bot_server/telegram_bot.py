import logging
import random
from telegram import *
from telegram.ext import *
import time

API_KEY = '1934407070:AAHYR-4tHwwm7Abtt-ZSWsXQ1QxWGbfab2E'
FAT_COUNT = 0
STUPID_COUNT = 0
DUMB_COUNT = 0

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def message_handler(update, context):
    text = str(update.message.text).lower()
    user_name = update['message']['chat']['first_name']
    update.message.reply_text(f"Hi {user_name},\n\nWelcome to Peekiri... Pwolikkulle appo..!\n\nUse /start for Jokes\nUse /help for Help")


def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Stupid", callback_data='1'),
            InlineKeyboardButton("Fat", callback_data='2'),
            InlineKeyboardButton("Dumb", callback_data='3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    
    update.message.reply_text('Please choose one for a Joke:', reply_markup=reply_markup)
    


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    jokes = {
         'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                    """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
         'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                    """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
         'dumb':   ["""THis is fun""",
                    """THis isn't fun"""] 
    }

    if '1' in query.data:
        text = random.choice(jokes['stupid'])
        global STUPID_COUNT
        STUPID_COUNT += 1

    elif '2' in query.data:
        text = random.choice(jokes['fat'])
        global FAT_COUNT
        FAT_COUNT += 1

    elif '3' in query.data:
        text = random.choice(jokes['dumb'])
        global DUMB_COUNT
        DUMB_COUNT += 1

    else:
        text = "I don't know any responses for that. If you're interested in yo mama jokes tell me fat, stupid or dumb."

    result_text = text + "\n\nUse /start for more Jokes\nUse /help for Help"
    query.edit_message_text(result_text)


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Hi ya, This is a Development Bot. \n\nYou can find the Github Repo at https://github.com/sandy85625/peekiri. \n\nFor more information please mail me at contact@zstream.in.")

def main() -> None:

    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(API_KEY, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

    if __name__ == '__main__':
        main()
