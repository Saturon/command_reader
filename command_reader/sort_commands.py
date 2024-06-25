def sort_commands(commands_list, debug):
    if debug: print('Stated sorting')
    if debug: print(commands_list) 
    commands_list = dict( sorted(commands_list.items(), key=lambda x: x[0].lower()) )
    if debug: print(commands_list) 
    if debug: print('Finished sorting')
    return commands_list