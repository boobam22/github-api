#!/bin/sh

set -eux

python3 src/main.py repo create -n test-999
python3 src/main.py repo create -n test-998 -p
python3 src/main.py repo
python3 src/main.py repo delete -n boobam22/test-999
python3 src/main.py repo delete -n boobam22/test-998

python3 src/main.py gist -f qwe
python3 src/main.py gist

python3 src/main.py gitignore | head -n 3
python3 src/main.py gitignore -t Python | head -n 3

python3 src/main.py license | head -n 3
python3 src/main.py license -l mit | head -n 3

ssh-keygen -t ed25519 -f id_test -N ""
python3 src/main.py ssh create -t test-999 -k "`cat id_test.pub`"
python3 src/main.py ssh
python3 src/main.py ssh delete -t test-999
rm id_test id_test.pub

python3 src/main.py markdown < README.md | (head -c 30; echo "")

python3 src/main.py rate-limit | head -n 5
