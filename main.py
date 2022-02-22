from aiohttp import web
import requirements

class ApiClass:
    def __init__(self, web):
        self.routes = [web.get('/api/foo', handler=self.handle), web.post('/api/throw', self.throw)]

    async def handle(self, request):
        return web.Response(text='Hello')

    async def throw(self):
        pass


if __name__ == '__main__':
    filename = '/home/ohad/PycharmProjects/PyReq/dum.txt'
    with open(filename, 'r') as fd:
        for req in requirements.parse(fd):
            print(req.name)
