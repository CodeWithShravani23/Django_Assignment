import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from django.conf import settings
import django
import logging

# Set up Django environment (to access models)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import TelegramUser

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    """Handle /start command from users."""
    user = update.effective_user
    chat_id = update.effective_chat.id
    
    # Save or update user in database
    TelegramUser.objects.update_or_create(
        chat_id=chat_id,
        defaults={
            'username': user.username or str(user.id),
        }
    )
    
    update.message.reply_text(f'👋 Hello {user.first_name}! You are now registered.')

def main() -> None:
    """Start the bot."""
    # Get token from environment variables
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN not set in environment variables!")
        return

    updater = Updater(token)
    dispatcher = updater.dispatcher
    
    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    
    # Start polling
    updater.start_polling()
    logger.info("Bot is now running...")
    updater.idle()

if __name__ == '__main__':
    main()