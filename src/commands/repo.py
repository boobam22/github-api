from parser import subparser
from client import client


def list_repo(args):
    res = client.get("/user/repos")
    print(
        *[
            f"{repo['full_name']:<24}\t{repo['visibility']}\t{repo['id']}"
            for repo in res
        ],
        sep="\n",
    )


def delete_repo(args):
    client.delete(f"/repos/{args.full_name}")


def create_repo(args):
    res = client.post("/user/repos", data={"name": args.name, "private": args.private})
    print(f"{res['full_name']:<24}\t{res['visibility']}\t{res['id']}")


repo_parser = subparser.add_parser("repo", help="manage repo")
repo_parser.set_defaults(callback=list_repo)

repo_subparser = repo_parser.add_subparsers()

delete = repo_subparser.add_parser("delete")
delete.add_argument("-n", "--full-name", required=True)
delete.set_defaults(callback=delete_repo)

create = repo_subparser.add_parser("create")
create.add_argument("-n", "--name", required=True)
create.add_argument("-p", "--private", action="store_true", default=False)
create.set_defaults(callback=create_repo)
