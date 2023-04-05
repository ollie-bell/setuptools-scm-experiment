import requests


def hello():
    print("Hello, world!")


if __name__ == "__main__":
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get('https://httpbin.org/get', params=payload)
    hello()
    print(r.url)
