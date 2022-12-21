def prompt(info, default=None, parser=None):
    if default != None:
        info += ' [{}]'.format(default)
    info += ': '
    
    answer = input(info)
    
    if answer == '':
        if default == None:
            raise ValueError('Please input a value')
        answer = default

    if parser:
        answer = parser(answer)

    return answer
