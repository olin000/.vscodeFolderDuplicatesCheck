from os import walk
import os

dirs = []
for (dirpath, dirnames, filenames) in walk(os.path.abspath(os.getcwd())):
    dirs.extend(dirnames)
    break

newdirs = []
for dir in dirs:
    newdirs.append(''.join([i for i in dir if not i.isdigit()]))

wasRunOnce = False
i = 0
for dir in newdirs:
    if(newdirs.count(dir) > 1):
        if not wasRunOnce:
            print("Duplicate folders:")
            wasRunOnce = True
        print("    " + dirs[i])
    i += 1
if not wasRunOnce:
    print("No duplicate folders found.")