import os

def execute_commands(commands_list, debug):
    if debug: print('Started executing')
    executed_commands = set()
    if debug: print(commands_list)

    try:
        for CMDS, commands in commands_list.items():
            if debug: print(CMDS, commands)
            if len(commands) <= 0: continue
            commands = eval( commands[commands.find('=')+1:] )
            for command in commands:
                if command in executed_commands:
                    print(command, 'already was executed')
                else:
                    if debug: print(command)
                    executed_commands.add(command)
                    os.system(command)
    except NameError:
        if debug: print(NameError)
        pass

    if debug: print('Finished executing')
    return