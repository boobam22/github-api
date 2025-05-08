from parser import subparser
from client import client


def list_template(args):
    if template := args.template:
        res = client.get(f"/gitignore/templates/{template}")
        print(res["source"], end="")
    else:
        res = client.get("/gitignore/templates")
        print(*res, sep="\n")


gitignore_parser = subparser.add_parser("gitignore", help="get gitignore template")
gitignore_parser.add_argument("-t", "--template")
gitignore_parser.set_defaults(callback=list_template)
