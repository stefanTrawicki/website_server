import requests
from ..config import Config

class HttpClient():
    _session = requests.Session()
    _base_url = Config.CMS_URL

    @staticmethod
    def get(url):
        return HttpClient._session.get(HttpClient._base_url + url).json()