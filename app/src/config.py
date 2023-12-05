import os
import dotenv

class Config():
    dotenv.load_dotenv()
    CMS_URL = os.environ.get('CMS_URL', None)

    CMS_URL = CMS_URL.strip('/') if CMS_URL else None

    if any(x is None for x in [CMS_URL]):
        raise Exception('Missing environment variables. Check your .env file.')