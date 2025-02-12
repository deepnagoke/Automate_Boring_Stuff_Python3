import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
        print('You have exited')
    elif response != 'exit':
        print('Type exit to leave this prompt.')