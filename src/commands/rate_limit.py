import json
import datetime

from parser import subparser
from client import client

timestamp2str = lambda t: str(datetime.datetime.fromtimestamp(t))


def rate_limit(args):
    res = client.get("/rate_limit")
    rate = res["rate"]
    rate["reset"] = timestamp2str(rate["reset"])
    for item in res["resources"].values():
        item["reset"] = timestamp2str(item["reset"])

    print(json.dumps(res, indent=4))


markdown_parser = subparser.add_parser("rate-limit", help="show rate limit status")
markdown_parser.set_defaults(callback=rate_limit)
