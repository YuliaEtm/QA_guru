import pprint

import requests


class HTTPClient:
    def __init__(self, base_url, headers):
        self.session = requests.session()
        self.base_url = base_url
        self.headers = headers

    def _logger_request(self, method, path, **kwargs):
        request = f"""
        method: (method)
        path: (path)
        kwargs: (kwargs)
        """
        print(request)
        response = self.session.request(method, self.base_url+path, **kwargs)
        response_massage = f"""
        status_code: {response.status_code}
        json: {pprint.pformat(response.json())}
        """
        print(response_massage)

        return response