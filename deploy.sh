#!/usr/bin/env bash
echo -e "Testing travis-encrypt"
echo -e "$VARNAME"

ghp-import output
git push -fq https://${GH_TOKEN}@github.com:gnureng/gnurenga.github.io.git gh-pages:master
