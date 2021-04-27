from unittest import TestCase

from practice.requests import test_request, env_demo


class TestApiRequest(TestCase):
    req_data = {
        "method": "get",
        "url": "http://192.168.64.129:9999/demo.txt",
        "headers": None,
        "encoding": "base64"
    }

    def test_send(self):
        ar = test_request.ApiRequest()
        print(ar.send(self.req_data))


class TestApi(TestCase):
    data = {
        "method": "get",
        "url": "http://localhost:9999/demo.txt",
        "headers": None
    }
    def test_send(self):
        api = env_demo.Api()
        print(api.send(self.data).text)