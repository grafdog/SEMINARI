#!/usr/bin/env python3

import argparse
import sys
import os

#sys.argv.pop(0)
for arg in sys.argv[1:]:
    if os.path.exists(arg):
        file_input = open(arg, 'r')
        print(file_input.read())
    else:
        print('plohoi put')
if len(sys.argv) == 1:
    print('vvedite dannie')




