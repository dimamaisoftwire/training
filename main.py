from account import AccountManager
from command_handler import CommandHandler

def main():
    accounts = AccountManager()
    command_handler = CommandHandler(accounts)

    command_handler.show_command_info()
    while True:
        command = input()
        command_handler.process_command(command)

if __name__ == '__main__':
    main()

