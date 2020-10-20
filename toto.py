def fonction(test: int, *args, **kwargs):
    if isinstance(test, int):
        print(test)
        for each in args:
            print(each)
    for i in kwargs:
        print(i.__str__())
        print(i.__repr__())
    for key, value in kwargs.items():
        print(f'{key} === {value} of type {type(value)}')
    print(kwargs)
    print(f'fonction exécutée avec argument : {args}')
    print(kwargs['brol'])
    with open('toto.txt', 'w') as f:
        print('sur ligne 1\n','sur ligne 2\n','sur ligne 3', sep='', end='\n\n', file=f) 

fonction(5, 'toto', 'tata', 'titi', arg3='coin', brol=False)
