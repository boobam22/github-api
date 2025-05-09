from parser import parser
import commands.repo
import commands.gist
import commands.gitignore
import commands.license
import commands.ssh
import commands.markdown
import commands.rate_limit


def main():
    args = parser.parse_args()
    args.callback(args)


if __name__ == "__main__":
    main()
