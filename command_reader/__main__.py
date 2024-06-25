import sys
from pathlib import Path

from collect_commands import collect_commands
from sort_commands import sort_commands
from execute_commands import execute_commands

debug = False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Enter a path to folder')
        sys.exit(1)
    try:
        if sys.argv[2] == '--debug':
            debug = True
    except:
        pass



    collected = collect_commands(sys.argv[1], debug)
    if not collected:
        print('Not found folder or py files')
        exit(0)
    collected = sort_commands(collected, debug)
    execute_commands(collected, debug)
