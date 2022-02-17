from aiohttp import web


class ApiClass:
    def __init__(self, web):
        self.routes = [web.get('/api/foo', handler=self.handle), web.post('/api/throw', self.throw)]

    async def handle(self, request):
        return web.Response(text='Hello')

    async def throw(self):
        pass


if __name__ == '__main__':
    print('PyCharm')
