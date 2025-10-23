from modules.miniTools import init_parser, log_time
from SinCity.colors import RED, RESET, GREEN, BLUE, YELLOW
from modules.config import status_type_error, status_type_warning
import sys

def parse_params(params:list[str]) -> dict[str | None]:

    commands = ['--test-url', '--recording']
    parsed_argv = {}
    
    for command in commands:
        for param in params:
            if command in param:
                try:
                    value = param.split('=', 1)[1].strip()
                    if command not in parsed_argv:
                        parsed_argv[command] = value
                except IndexError:
                    print(
                            f'{log_time()} {status_type_error} '
                            f'необходимо передать значение: {YELLOW}{param}{RESET}=<url>')
    return parsed_argv

if __name__ == '__main__':
    #инит парсера - создаем директории и подобное
    init_parser()
    #убрать имя скрипта
    params = sys.argv[1:]
    
    args = parse_params(params=params)
    
    if len(args) != 0:
        print(args)
    if len(args) == 0:
        print(f'{log_time()} {status_type_warning} необходимо передать параметры')
