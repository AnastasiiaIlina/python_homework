import json

# Task 1
# Files
# Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it. Then write another script that opens myfile.txt, and reads and prints its contents. Run your two scripts from the system command line. 
# Does the new file show up in the directory where you ran your scripts? - YES
# What if you add a different directory path to the filename passed to open? - FILE WILL BE CREATED IN A DIFFERENT PATH
# Note: file write methods do not add newline characters to your strings; add an explicit "\n" at the end of the string if you want to fully terminate the line in the file.

with open('myfile.txt', 'w') as file:
    file.write('Hello file world!\n')

with open('myfile.txt') as file:
    print(file.read())


# Task 2
# Extend Phonebook application
# Functionality of Phonebook application:

# Add new entries 
# Search by first name 
# Search by last name 
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
 

# The first argument to the application should be the name of the phonebook. Application should load JSON data, if it is present in the folder with application, else raise an error. After the user exits, all data should be saved to loaded JSON.

def use_phonebook(phonebook_name):
    try:
        with open(phonebook_name, 'r') as file:
            phonebook = json.load(file)
            
        with open(phonebook_name, 'w') as file:
            while True:
                operation = input('Оберіть, що хочете зробити - додати новий запис (ADD), видалити існуючий запис (DELETE), оновити існуючий запис (UPDATE) чи знайти потрібний запис (SEARCH)? Щоб закрити телефонну книгу, введіть ESC: ')

                if operation == 'ADD':
                    first_name = input('Введіть імʼя нового контакту: ')
                    last_name = input('Введіть прізвище нового контакту: ')
                    tel = input('Введіть телефон нового контакту: ')
                    city = input('Введіть місто нового контакту: ')

                    phonebook.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'tel': tel,
                        'city': city
                    })
                elif operation == 'UPDATE':
                    tel = input('Введіть телефон нового контакту, який хочете оновити: ')
                    index_for_updating = int()

                    for index in range(len(phonebook)):
                        if phonebook[index]['tel'] == tel:
                            index_for_updating = index
                            break

                    first_name = input('Введіть оновлене імʼя: ')
                    last_name = input('Введіть оновлене прізвище: ')
                    tel = input('Введіть оновлений телефон: ')
                    city = input('Введіть оновлене місто: ')

                    phonebook[index_for_updating] = {
                        'first_name': first_name,
                        'last_name': last_name,
                        'tel': tel,
                        'city': city
                    }
                elif operation == 'DELETE':
                    tel = input('Введіть телефон контакту, який хочете видалити: ')

                    for index in range(len(phonebook)):
                        if phonebook[index]['tel'] == tel:
                            index_for_deleting = index

                    phonebook.pop(index_for_deleting)
                    print(f'Контакт видено з телефонної книги.')
                elif operation == 'SEARCH':
                    search_string = input('Введіть імʼя, прізвище, номер телефону чи місто: ')
                    filtered_contacts = list()

                    for contact in phonebook:
                        if search_string in contact.values():
                            filtered_contacts.append(contact)

                    if len(filtered_contacts) == 0:
                        print(f'Ми не знайшли жодного контакту. Повторіть спробу.')
                    else:
                        print(f'Ми знайшли контакти - {filtered_contacts}')

                elif operation == 'ESC':
                    json.dump(phonebook, file, indent=4)
                    print('Телефонна книга успішно закрита.')
                    break
                else:
                    print('Такий тип операції відсутній. Спробуйте знову.')
    except FileNotFoundError:
        print('Телефонна книга не знайдена!')

use_phonebook('phonebook.json')