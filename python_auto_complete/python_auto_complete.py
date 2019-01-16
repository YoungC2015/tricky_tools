# A tool that can auto complete python methods in python shell
# Test past at "Linux ubuntu 4.15.0-42-generic"
# YoungC, at 2019-01-16

import atexit, os
try:
    import readline
except ImportError:
    pass
else:
    import rlcompleter
    rl = 1
    readline.parse_and_bind("tab: complete")

if 'HOME' in os.environ.keys():
    home_path = 'HOME'
else:
    home_path = 'HOMEPATH'

histfile = os.path.join(os.environ[home_path], '.python_history')
if not os.path.isfile(histfile):
    histfile = os.path.join(os.environ[home_path], '.pythonhistory')

try:
    readline.read_history_file(histfile)
except IOError:
    pass

atexit.register(readline.write_history_file, histfile)

del os, histfile, readline, 
