# !/usr/bin/python

import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      if name.endswith('talon'):
        pathfull = os.path.join(root, name)
        if name == "settings.talon" or pathfull == "./cheatsheet/cheatsheet.talon" or pathfull == "./core/modes/wake_and_sleep.talon":
           continue

        print(pathfull)
        # Open the file as read
        f = open(pathfull, "r+")
        # Create an array to hold write data
        new_file = []
        # Loop the file line by line
        for line in f:
            if line.strip() == "\n":
               continue
            # Split A,B on , and use first position [0], aka A, then add to the new array
            commented_line = f'# {line}'
            # Add
            new_file.append(commented_line)
        # Open the file as Write, loop the new array and write with a newline
        with open(pathfull, "w+") as f:
            for i in new_file:
                f.write(i)
