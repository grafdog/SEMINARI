#!/usr/bin/env python3

import sys

d = 0

#sys.argv.pop(0)
for arg in sys.argv[1:]:
    if len(arg) % 3 == 0:
        d +=1
print(d)
