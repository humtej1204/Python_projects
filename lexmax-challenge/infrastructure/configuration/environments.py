from dotenv import load_dotenv
import os

load_dotenv('.env')

env = {
    "database": {
        "url": os.environ.get('DATABASE_URL')
    }
}