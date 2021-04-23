import requests
from jsonpath import jsonpath
from requests.auth import HTTPBasicAuth


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

    # cookie 两种传递方法：
    # 1.通过header传递Cookie，修改User-Agent
    # 2.通过cookies传递(两种方法不可同时存在，cookie只能传一次)
    def test_cookie(self):
        url = 'https://httpbin.testing-studio.com/cookies'
        header = {"Cookie": "adc"}
        # header = {'User-Agent': 'fight'}
        cookie_data = {"position": "mid"}
        r = requests.get(url=url, headers=header, cookies=cookie_data)
        print(r.request.headers)
        # print(r.text)

    # 认证体系
    # 执行python时，需要关闭Charles，代码和工具两者是冲突的，同时抓取会失效
    # url为网页中的Request URL
    def test_auth(self):
        r = requests.get(url='https://httpbin.testing-studio.com/basic-auth/abc/123',
                         auth=HTTPBasicAuth("abc", "123"))
        print(r.text)
