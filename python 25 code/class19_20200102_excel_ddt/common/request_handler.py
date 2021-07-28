import requests


class RequestHandler:

    def __init__(self):
        self.session = requests.Session()

    def visit(self, url, method, params=None, data=None, json=None, **kwargs):
        res = self.session.request(url, method, params=params, data=data, json=json, **kwargs)
        try:
            return res.json()
        except ValueError:
            print("not json")
