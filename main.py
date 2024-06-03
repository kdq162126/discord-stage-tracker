import os
from bot.bot import bot
from keep_alive import keep_alive
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    keep_alive()
    bot.run(os.getenv('BOT_TOKEN'))

