import json

def count_local_vars():
    var1 = 0
    var2 = 1

    return locals()

def outside_fun(a):
    def inside_fun(b):
        return a * b

    return inside_fun

def choose_func(nums: list, func1, func2):
    if(all(element >= 0 for element in nums)):
        return func1(nums)
    else:
        return func2(nums)


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
                        phonebook = filtered_contacts
                        print(f'Ми знайшли контакти - {filtered_contacts}')

                elif operation == 'ESC':
                    json.dump(phonebook, file, indent=4)
                    print('Телефонна книга успішно закрита.')
                    return phonebook
                else:
                    print('Такий тип операції відсутній. Спробуйте знову.')
    except FileNotFoundError:
        print('Телефонна книга не знайдена!')





# def use_phonebook(phonebook_name, operation_type, user = None, user_identifier = None):
#     try:
#         with open(phonebook_name, 'r') as file:
#             phonebook = json.load(file)
            
#         with open(phonebook_name, 'w') as file:
#             if operation_type == 'add':

#                 phonebook.append(user)
#                 print('Новий контакт успішно доданий.')

#             elif operation_type == 'update':
#                 for index in range(len(phonebook)):
#                     if phonebook[index]['tel'] == user_identifier:
#                         index_for_updating = index
#                         break
                
#                 if index_for_updating:
#                     phonebook[index_for_updating] = user
#                     print(f'Контакт з номером телефону {user_identifier} оновлений.')
#                 else:
#                     print(f'Контакта з таким номером телефона не знайдено.')
#             elif operation_type == 'delete':
#                 for index in range(len(phonebook)):
#                     if phonebook[index]['tel'] == user_identifier:
#                         index_for_deleting = index

#                 if index_for_deleting:
#                     phonebook.pop(index_for_deleting)
#                     print(f'Контакт видалено з телефонної книги.')
#                 else:
#                     print(f'Контакта з таким номером телефона не знайдено.')

#             elif operation_type == 'search':
#                 filtered_contacts = list()

#                 for contact in phonebook:
#                     if user_identifier in contact.values():
#                         filtered_contacts.append(contact)

#                 if len(filtered_contacts) == 0:
#                     print(f'Ми не знайшли жодного контакту. Повторіть спробу.')

#                     return None
#                 else:
#                     print(f'Ми знайшли контакти - {filtered_contacts}')
#                     return filtered_contacts

#             else:
#                 print('Такий тип операції відсутній. Спробуйте знову.')
            
#             json.dump(phonebook, file, indent=4)
#     except FileNotFoundError:
#         return 'Телефонна книга не знайдена!'
