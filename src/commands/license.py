import datetime
import subprocess

from parser import subparser
from client import client


def list_license(args):
    if license := args.license:
        year = str(datetime.datetime.now().year)
        fullname = subprocess.run(
            "git config --global user.name",
            shell=True,
            stdout=subprocess.PIPE,
            text=True,
            check=True,
        ).stdout.strip()

        res = client.get(f"/licenses/{license}")
        template: str = res["body"]
        print(template.replace("[year]", year).replace("[fullname]", fullname).strip())
    else:
        res = client.get("/licenses")
        print(*[f"{license['key']:<16}{license['name']}" for license in res], sep="\n")


license_parser = subparser.add_parser("license", help="get license")
license_parser.add_argument("-l", "--license")
license_parser.set_defaults(callback=list_license)
