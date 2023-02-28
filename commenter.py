# !/usr/bin/python

import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      if name.endswith('talon'):
        print(os.path.join(root, name))
        