# Django_Assignment
# Django Internship Project

## Setup Instructions

1. Clone the repository
2. Create and activate virtual environment
3. Install requirements: `pip install -r requirements.txt`
4. Create `.env` file with required variables
5. Run migrations: `python manage.py migrate`
6. Start development server: `python manage.py runserver`

## Environment Variables

- `SECRET_KEY`: Django secret key
- `DB_*`: Database credentials
- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token

## Running Locally

1. Start Redis server
2. Start Celery worker: `celery -A yourproject worker --loglevel=info`
3. Start Telegram bot: `python telegram_bot.py`
4. Start Django server: `python manage.py runserver`

## API Documentation

- Public endpoint: `GET /api/public/`
- Protected endpoint: `GET /api/protected/` (requires authentication)
