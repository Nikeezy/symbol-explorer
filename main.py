import os
import subprocess
from pywinauto import Application


def explorer() -> None:
    while True:
        char: str = input('Введите символ: ')
        print(f'Бинарный код введённого символа: {bin(ord(char))}')

        if bin(ord(char)) == bin(ord('s')):
            subprocess.Popen('explorer')
        elif bin(ord(char)) == bin(ord('f')):
            path: str = input('Введите путь к папке: ')
            subprocess.Popen(['explorer', path])
            os.chdir(path)
        elif bin(ord(char)) == bin(ord('k')):
            filename: str = input('Введите имя файла: ')
            with open(filename, 'w+') as f:
                f.write('Hello World!')
                f.close()
        elif bin(ord(char)) == bin(ord('w')):
            filename: str = input('Введите имя файла: ')
            os.remove(filename)
        elif bin(ord(char)) == bin(ord('e')):
            app = Application(backend="uia").connect(path="explorer.exe")
            windows = app.windows()
            explorer_windows = [window for window in windows if window.class_name() == 'CabinetWClass']
            if explorer_windows:
                explorer_windows[0].close()
        elif bin(ord(char)) == bin(ord('q')):
            print('Выполнение программы завершено!')
            return None
        else:
            print('Неопознанная команда!')


if __name__ == "__main__":
    explorer()
