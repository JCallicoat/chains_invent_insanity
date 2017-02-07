#!/bin/env python
# coding: utf-8

# ls -Q dah-cards/ | fgrep -v -e Reject -e Ladies -e README -e scripts | xargs python wordlist_from_yaml.py > custom_wordlist.txt

# python wordlist_from_yaml.py Base.yaml Box.yaml CAHe1.yaml CAHe2.yaml CAHe3.yaml CAHe4.yaml CAHe5.yaml CAHe6.yaml CAHgrognards.yaml CAHweeaboo.yaml CAHxmas.yaml christmas2013.yaml HACK.yaml NEIndy.yaml NSFH.yaml PAXE13.yaml PAXE14PP.yaml PAXE14.yaml PAXP13.yaml PAXP14PP.yaml PAXP15FP.yaml www.yaml > fun_wordlist.txt

import sys
import yaml

answers = []
for f in (sys.argv[1:]):
  d = yaml.load(open('dah-cards/' + f))
  map(answers.append, d['answers'])

print('\n'.join(list(set(answers))).encode('utf-8'))
