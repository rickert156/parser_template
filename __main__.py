from SinCity.colors import RED, RESET, GREEN, BLUE, YELLOW
from modules.miniTools import (
        init_parser, 
        log_time, 
        parse_params
        )
from modules.config import (
        status_type_error, 
        status_type_warning
        )
import sys


if __name__ == '__main__':
    #инит парсера - создаем директории и подобное
    init_parser()
    #убрать имя скрипта
    params = sys.argv[1:]
    
    args = parse_params(params=params)
    
    if len(args) != 0:
        print(args)
        test_url = args['--test-url'] if args.get('--test-url') else False 
        recording = args['--recording'] if args.get('--recording') else False
    if len(args) == 0:
        print(f'{log_time()} {status_type_warning} необходимо передать параметры')
