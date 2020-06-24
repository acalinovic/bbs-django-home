import os

from bbs.settings import BASE_DIR


class CommandRegistry:
    print('CommandRegistry invoked')
    _app_commands = dict()

    com_path = os.path.join(BASE_DIR, 'home', 'gui', 'commands', 'home_commands.py')



    @classmethod
    def register(cls, module):
        try:
            com_path = os.path.join(BASE_DIR, module, 'commands.py')
            with open(com_path) as f:
                print(f.name)
        except FileNotFoundError:
            raise(FileNotFoundError('command file not found'))
        print(f'commands found for module {module}')
        return cls
