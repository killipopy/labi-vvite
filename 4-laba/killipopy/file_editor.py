def write_to_file(file_name, text):
    with open(f'{file_name}', 'w') as file:
        file.write(text)

    print('[module] The text has been written to file')

def append_to_file(file_name, text):
    with open(f'{file_name}', 'a') as file:
        file.write(text + '\n')

    print('[module] The text has been written to file')

def open_file(file_name):
    try:
        with open(file_name) as file:
            text = file.read()
        return print(text)
    except FileNotFoundError:
        print('[module] File not found')

def ui():
    while True:
        print('1. Open an existing file\n2. Write to a new file\n3. Add a new line\n0. Exit')

        choice = input('Enter your choice: ')

        if choice == '0':
            break

        file_name = input('Enter file name: ')

        if choice == '1':
            open_file(file_name)
            continue

        input_text = input('Enter your text: ')
        write_to_file(file_name, input_text)

        if choice == '2':
            write_to_file(file_name, input_text)
        elif choice == '3':
            append_to_file(file_name, input_text)
        else:
            print('Invalid choice')
