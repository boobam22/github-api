from parser import subparser
from client import client


def list_ssh(args):
    res = client.get("/user/keys")
    print(*[f"{ssh['title']:<16}\t{ssh['id']}" for ssh in res], sep="\n")


def delete_ssh(args):
    if id := args.id:
        client.delete(f"/user/keys/{id}")
    else:
        res = client.get("/user/keys")
        for ssh in res:
            if ssh["title"] == args.title:
                client.delete(f"/user/keys/{ssh['id']}")
                break
        else:
            raise Exception("Not Found")


def create_ssh(args):
    res = client.get("/user/keys")
    for ssh in res:
        if ssh["title"] == args.title:
            client.delete(f"/user/keys/{ssh['id']}")

    ssh = client.post("/user/keys", data={"title": args.title, "key": args.key})
    print(f"{ssh['title']:<16}\t{ssh['id']}")


ssh_parser = subparser.add_parser("ssh", help="manage git ssh keys")
ssh_parser.set_defaults(callback=list_ssh)

ssh_subparser = ssh_parser.add_subparsers()

delete = ssh_subparser.add_parser("delete")
group = delete.add_mutually_exclusive_group(required=True)
group.add_argument("-t", "--title")
group.add_argument("--id")
delete.set_defaults(callback=delete_ssh)

create = ssh_subparser.add_parser("create")
create.add_argument("-t", "--title", required=True)
create.add_argument("-k", "--key", required=True)
create.set_defaults(callback=create_ssh)
