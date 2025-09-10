# copyfile() : copies contents of a file
# copy()     : copyfile() + permission mode + destination can be a directory
# copy2()    : copy + copies metadata
# arguments are all the same for all these functions

import shutil

shutil.copyfile('test.txt', 'copy.txt') # src (source path), dst (destination path)