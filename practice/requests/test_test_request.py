from unittest import TestCase

from practice.requests import test_request


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
