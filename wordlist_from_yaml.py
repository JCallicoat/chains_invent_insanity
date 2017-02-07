#!/bin/env python
# coding: utf-8

# ls -Q dah-cards/ | fgrep -v -e Reject -e Ladies -e README -e scripts | xargs python wordlist_from_yaml.py > custom_wordlist.txt

import sys
import yaml

answers = []
for f in (sys.argv[1:]):
  d = yaml.load(open('dah-cards/' + f))
  map(answers.append, d['answers'])

print('\n'.join(list(set(answers))).encode('utf-8'))
