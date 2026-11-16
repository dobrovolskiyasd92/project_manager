from commands.help import help_commands

MY_CONST = 1
print(__name__)

def main():
    print('Task manager. help - для справки')
    try:
        while True:
            raw = input('> ').strip('').lower()
            parts = raw.split()
            cmd, args = parts[0], parts[1:]
            match cmd:
                case 'help':
                    help_commands()
                case 'list':
                    pass
                case 'done':
                    pass

                case 'add':
                    pass

                case 'remove':
                    pass

                case 'edit':
                    pass

                case 'tags':
                    pass

                case 'exit':
                    break

                case _:
                    print('Неизвестная команда')

    except KeyboardInterrupt:
        print('\nЗавершение работы...')
        exit()

    except Exception as e:
        print(f'ERROR: {e}')


if __name__ == '__main__':
    main()
