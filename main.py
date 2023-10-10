from wsgiref.simple_server import make_server

from endpoints import asd, index, qwe
from wsgi import Wsgi


def get_app():
    app = Wsgi()
    app.set_endpoint("/", index)
    app.set_endpoint("/asd", asd)
    app.set_endpoint("/qwe", qwe)
    return app


def main():
    app = get_app()
    httpd = make_server("", 8051, app)
    print("Server started.")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
