class HTTPRequest:

    def __init__(self):
        self.url = None
        self._state = 'NEW'

    def open(self, url):
        assert self._state == 'NEW', 'state of the request is invalid'
        self.url = url
        print(f'Connecting to {url}')
        self._state = 'OPEN'

    def send(self, method):
        assert self._state == 'OPEN', 'state of the request is invalid'
        accepted = ['GET', 'POST']
        if not isinstance(method, str) or method.upper() not in accepted:
            raise RuntimeError(f'method must be one of {accepted}')
        print(f'Sending {method.upper()}')
        self._state = 'SENT'


if __name__ == '__main__':
    request = HTTPRequest()
    request.open('http://test.com')
    request.send('get')
