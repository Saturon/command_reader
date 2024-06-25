import os
#Function for collecting all commands from python files in folder tree
def collect_commands(path, debug):
    if debug: print('Started collecting commands')
    executed_commands = set()
    commands = {} #commands storage for future execution

    for folder, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                founded_file = os.path.join(folder, file)
                if debug : print(founded_file)
                with open(founded_file, 'r') as opened_file:
                    try:
                        CMDS = opened_file.read()
                        if debug : print(CMDS)
                        commands[founded_file] = CMDS
                    except:
                        print("Error in opened file")
    if debug: 
        for k, v in commands.items(): 
            print(k, v)  
    if debug: print('Finished collecting commands')  
    return commands