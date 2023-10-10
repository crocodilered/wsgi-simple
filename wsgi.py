import typing


class Wsgi:
    def __init__(self) -> None:
        self.__endpoints = dict()

    @classmethod
    def encode_response_body(cls, response_body: str) -> bytes:
        return response_body.encode("utf-8")

    def __call__(self, environ, start_response):
        path_info = environ.get("PATH_INFO", "")
        try:
            endpoint = self.resolve_endpoint(path_info)
        except KeyError:
            start_response("404 Not found", [])
            return []

        response_body = endpoint(environ)
        encoded_response_body = self.encode_response_body(response_body)
        response_headers = [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(encoded_response_body))),
        ]
        start_response("200 OK", response_headers)
        return [encoded_response_body]

    def set_endpoint(self, uri, endpoint: typing.Callable) -> None:
        assert uri not in self.__endpoints
        self.__endpoints[uri] = endpoint

    def resolve_endpoint(self, uri) -> typing.Callable:
        return self.__endpoints[uri]
