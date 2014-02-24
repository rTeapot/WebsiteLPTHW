import web

urls = (
    '/', 'Index',
    '/Foo', 'Foo'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        greeting_Index = "Hello World"
        return render.index(greeting = greeting_Index)

class Foo(object):
    def GET(self):
        greeting_Foo = 'FooBAR'
        return render.foo(greeting = greeting_Foo)

if __name__ == "__main__":
    app.run()