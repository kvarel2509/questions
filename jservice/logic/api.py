from urllib.parse import urljoin

import requests


class FetchError(Exception):
    pass


class JServiceAPI:
    URL = 'https://jservice.io/api/'

    def get_questions(self, count: int) -> list:
        suffix = 'random'
        params = {'count': count}
        url = self._get_url(suffix)
        response = self._get_response(url, params)
        return response

    def _get_response(self, url: str, params: dict):
        try:
            response = requests.get(url, params, timeout=10)
            return response.json()
        except requests.RequestException:
            raise FetchError()

    def _get_url(self, suffix: str) -> str:
        return urljoin(self.URL, suffix)
