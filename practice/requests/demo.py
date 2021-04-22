import requests
from jsonpath import jsonpath


class TestDemo:
    # get请求，获取网络地址信息
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r)
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    # query请求，带参数查询
    def test_query(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    # form请求 以表单形式发送请求，常用于请求登录
    def test_form(self):
        payload = {
            "login": "name",
            "password": "passwd"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200

    # headers 发送请求的同时，附带上自定义信息，同时发出去的信息能返回，体现在headers内
    def test_headers(self):
        r = requests.get('https://httpbin.testing-studio.com/get', headers={"abc": "headers_case"})
        # print(r.status_code)
        # print(r.text)
        # print(r.json())
        # print(r.headers)
        # print(r.cookies)
        # print(r.url)
        # print(r.raw.read(10))
        assert r.status_code == 200
        assert r.json()['headers']["Abc"] == "headers_case"

    # json 以json的结构体发送请求
    def test_json(self):
        payload = {
            "login": "name",
            "password": "passwd"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        # print(r.json())
        print(r.text)
        assert r.json()['headers']["Content-Length"] == "39"
        assert r.json()['json']['password'] == "passwd"

    # xml 以sml的结构体发送请求，和json类似，但以data形式发出，并且需要定义headers
    def test_xml(self):
        xml = """<?xml version = '1.0' encoding = 'utf-8'? >
        <a>6</a>"""
        headers = {'Content-Type': 'application/xml'}
        r = requests.post('https://httpbin.testing-studio.com/post', data=xml, headers=headers)
        print(r.text)
        assert r.json()['data'] == "<?xml version = '1.0' encoding = 'utf-8'? >\n        <a>6</a>"

    # jsonpath 断言
    def test_jsonpath(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.text)
        assert r.json()['category_list']['categories'][0]['name'] == "开源项目"
        print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[0] == "开源项目"