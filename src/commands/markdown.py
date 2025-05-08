import sys

from parser import subparser
from client import client


def markdown2html(args):
    res = client.post("/markdown", data={"text": sys.stdin.read()})
    print(res, end="")


markdown_parser = subparser.add_parser("markdown", help="markdown to html")
markdown_parser.set_defaults(callback=markdown2html)
