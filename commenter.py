# !/usr/bin/python

import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      if name.endswith('talon'):
        if os.path.join(root, name) == "./settings.talon":
           continue

        print(os.path.join(root, name))
        # Open the file as read
        f = open("text.txt", "r+")
        # Create an array to hold write data
        new_file = []
        # Loop the file line by line
        for line in f:
            # Split A,B on , and use first position [0], aka A, then add to the new array
            commented_line = f'# + {line}'
            # Add
            new_file.append(commented_line)
        # Open the file as Write, loop the new array and write with a newline
        with open("text.txt", "w+") as f:
            for i in new_file:
                f.write(i+"\n")
