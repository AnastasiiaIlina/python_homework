

# 1. Читання та виведення даних:
# Зчитайте дані з JSON файлу та виведіть на екран інформацію про всі VM (віртуальні машини) у зручному форматі.


# 2. Фільтрація та пошук:
# Знайдіть всі VM, які розташовані в певному регіоні.
# Пошукайте VM, які мають більше ніж 16GB оперативної пам'яті.

# 3. Додавання та видалення даних:
# Додайте нову VM у файл та збережіть зміни.

import json


# with open('virtual_machines.json', 'r') as json_file:
#     vm_list = json.load(json_file)

#     vm_list.append({
#       "name": "VM51",
#       "processor": "AMD Ryzen2",
#       "memory": "16GB",
#       "storage": "256GB",
#       "location": "Frankfurt, Germany Cloud Hub",
#       "region": "Europe (Germany)",
#       "provider": "Provider XX"
#     })

# with open('virtual_machines.json', 'w') as json_file:
#     json.dump(vm_list, json_file, indent=4)


# 4. Оновлення та редагування:
# Видаліть всі VM у росії та "перенесіть" їх у іншу країну та оновіть файл.
# Змініть обсяг пам'яті для всіх VM у Франції та оновіть файл.

# with open('virtual_machines.json', 'r') as file:
#     vms = json.load(file)
    
#     for vm in vms:
#         if vm['region'] == 'Europe (Russia)':
#             vm['region'] = 'UNKNOWN_COUNTRY'

# with open('virtual_machines.json', 'w') as file:
#     json.dump(vms, file, indent=4)

# with open('virtual_machines.json', 'r') as file:
#     vms = json.load(file)

#     for vm in vms:
#         if vm['region'] == 'Europe (France)':
#             vm['memory'] = "99GB"
    
# with open('virtual_machines.json', 'w') as file:
#     json.dump(vms, file, indent=4)

# 5. Збереження в новий файл:
# Створіть новий JSON файл та збережіть туди інформацію лише про VM, 
# які розташовані в певному регіоні (Азія, до прикладу).

# def save_vms_by_region(region):
#     vms_by_region = list()

#     with open('virtual_machines.json', 'r') as file:
#         vms = json.load(file)

#         for vm in vms:
#             if(vm['region'] == region):
#                 vms_by_region.append(vm)

#     with open(f'vm_by_region_{region}.json', 'w') as file:
#         json.dump(vms_by_region, file, indent = 4)
    

# save_vms_by_region('Europe (France)')


# 6. Аналіз та Статистика:
# Знайдіть найбільш поширений обсяг пам'яті серед VM.

# with open('virtual_machines.json', 'r') as file:
#     vm_memories_dict = dict()

#     vms = json.load(file)

#     for vm in vms:
#         if vm['memory'] in vm_memories_dict:
#             vm_memories_dict[vm['memory']] += 1
#         else:
#             vm_memories_dict[vm['memory']] = 1

#     max_value = 0
#     message = ''
#     for key in vm_memories_dict:
#         if vm_memories_dict[key] > max_value:
#            max_value = vm_memories_dict[key]
#            message = f'Найбільш поширений обсяг пам\'яті серед VM - {key}'

#     print(message)

# 7. Застосування Умов:
# Створіть функцію, яка приймає обсяг пам'яті та повертає список VM, які мають цей обсяг.

# def get_vms_by_memory(memory):
#     vms_by_memory = list()

#     with open('virtual_machines.json', 'r') as file:
#         vms = json.load(file)

#         for vm in vms:
#             if vm['memory'] == memory:
#                 vms_by_memory.append(vm)
    
#     return vms_by_memory

# print(get_vms_by_memory("64GB"))