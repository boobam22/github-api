#!/bin/sh

dirs=$(find src -name __pycache__)
if [ -n "$dirs" ]; then
    rm -r $dirs
fi

mkdir -p dist
python3 -m zipapp src -p '/bin/env python3' -o dist/github-api.pyz
