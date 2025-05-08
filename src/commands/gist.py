from parser import subparser
from client import client


def list_gist(args):
    filename = args.filename

    res = client.get("/gists")
    for gist in res:
        for file in gist["files"].values():
            if filename is None or filename in file["filename"]:
                print(file["raw_url"])


gist_parser = subparser.add_parser("gist", help="get gist")
gist_parser.add_argument("-f", "--filename")
gist_parser.set_defaults(callback=list_gist)
