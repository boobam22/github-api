import os
import json
import urllib.request


default_headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
    "User-Agent": os.getenv("USER_AGENT"),
    "X-GitHub-Api-Version": "2022-11-28",
}


class Client:
    def __init__(self, base_url=""):
        self.base_url = base_url

    def build_request(
        self,
        method,
        path,
        data=None,
    ):
        config = {
            "method": method,
            "url": f"{self.base_url}{path}",
            "headers": default_headers,
        }
        if data is not None:
            config["headers"] = default_headers | {"Content-Type": "application/json"}
            config["data"] = json.dumps(data).encode()
        return urllib.request.Request(**config)

    def request(
        self,
        method,
        path,
        data=None,
    ):
        req = self.build_request(method, path, data)

        with urllib.request.urlopen(req) as res:
            body = res.read().decode()
            if res.headers.get("Content-Type", "").split(";")[0] == "application/json":
                body = json.loads(body)
            return body

    def get(self, path):
        return self.request(method="GET", path=path)

    def post(self, path, data=None):
        return self.request(method="POST", path=path, data=data)

    def delete(self, path):
        return self.request(method="DELETE", path=path)


client = Client(base_url="https://api.github.com")
