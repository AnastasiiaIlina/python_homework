# 1. Калькулятор податків:
# Напишіть функцію, яка приймає суму доходу і обчислює загальну суму податку, враховуючи різні ставки податків на прибуток.

def get_taxes(income_sum):
    taxes_rate = 0.18
    return income_sum * taxes_rate

print(get_taxes(100))

# 2. Система обліку запасів:
# Створіть функцію, яка дозволяє додавати товари до системи обліку запасів, відстежує кількість товарів та повертає інформацію про наявність товарів на складі.
initial_goods = ['paper', 'pen', 'eraser']

def get_goods_in_stock(goods, new_good):
    if new_good:
        goods.append(new_good)
    
    return f'На складі є {len(goods)} товари(-ів) - {', '.join(goods)}.'


print(get_goods_in_stock(initial_goods, 'pencil'))


# 3. Обчислення вартості доставки:
# Напишіть функцію, яка приймає вагу товару та відстань до місця доставки і обчислює вартість доставки згідно з заданими тарифами.


def calculate_order_price(weight, distance):
    if weight <= 10:
        if distance <= 20:
            return f'Вартість доставки - 50 грн'
        else:  
            return f'Вартість доставки - 100 грн'  
    elif weight > 10:
        if distance > 20:
            return f'Вартість доставки - 70 грн'
        else:  
            return f'Вартість доставки - 140 грн'  


print(calculate_order_price(10, 100))


# 4. Система обліку вартості проекту:
# Напишіть функцію, яка приймає вартість робочих годин, кількість годин та додаткові витрати і розраховує загальну вартість проекту.

def calculate_project_price(hour_price, hour_amount, extra_costs):
    return hour_price * hour_amount + extra_costs

print(calculate_project_price(20, 2, 5))

# 5. Автоматизація операцій з банківським рахунком:
# Створіть функції для переведення грошей між рахунками, перевірки балансу та виведення історії транзакцій.
bill1 = {'id': 1, 'balance': 100, 'history': []}
bill2 = {'id': 2, 'balance': 15, 'history': [] }

def transfer_money(write_off_bill, received_bill, transfer_sum):
    write_off_bill['balance'] -= transfer_sum
    received_bill['balance'] += transfer_sum

    write_off_bill['history'].append({'type': 'withdrawal', 'sum': transfer_sum })
    received_bill['history'].append({'type': 'deposit', 'sum': transfer_sum })

def check_balance(bill):
    print(bill['balance'])

def print_transactions_history(bills):
    for bill in bills:
        for transaction in bill['history']:
            if transaction['type'] == 'withdrawal':
                print(f'З рахунку №{bill['id']} було списано {transaction['sum']} грн.')
            else:
                print(f'На рахунок №{bill['id']} було зараховано {transaction['sum']} грн.')


transfer_money(bill1, bill2, 5)
print_transactions_history([bill1, bill2])

check_balance(bill1)
check_balance(bill2)


# 6. Система відстеження завдань:
# Напишіть функції для додавання нових завдань, відзначення завершених та виведення списку активних завдань.
tasks_list = [{
    'id': 1,
    'text': 'Зробити уроки',
    'marked': False
}]

def add_task(task_text):
    # expect that tasks_list has at least one element
    tasks_list.append({'id': tasks_list[-1]['id'] + 1, 'text': task_text, 'marked': False})

add_task('Помити посуд')

def mark_task_done(task_id):
    for task in tasks_list:
       if(task_id == task['id']):
           task['marked'] = True

           break

mark_task_done(1)

# print(tasks_list)

def print_active_tasks(tasks):
    for task in tasks:
        if task['marked'] == False:
            print(task)

print_active_tasks(tasks_list)

# 7. Обчислення середньомісячного обороту:
# Розробіть функцію, яка приймає місячні продажі за останній рік і обчислює середньомісячний оборот.
sales_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

def calculate_turnover(sales):
    print(sum(sales) / len(sales_list))

calculate_turnover(sales_list)

# 8. Система керування клієнтами:
# Напишіть функції для додавання нових клієнтів, зміни контактної інформації та виведення списку клієнтів.
clients_list = [{
    'id': 1,
    'name': 'Ivan',
    'contacts': '+38096553454'
}]

def add_client(client_name, client_contacts):
    # expect that clients_list has at least one element
    clients_list.append({'id': clients_list[-1]['id'] + 1, 'name': client_name, 'contacts': client_contacts})

add_client('Nastya', '+38093522222')

def update_contacts(client_id, updated_contacts):
     for client in clients_list:
       if(client_id == client['id']):
           client['contacts'] = updated_contacts

           break
       
update_contacts(2, '+380000000')

def print_clients_list(clients):
    for client in clients:
        print(f"Client's name - {client['name']}. Client's contacts - {client['contacts']}")

print_clients_list(clients_list)

# 9. Система відомостей про співробітників:
# Розробіть функції для додавання нових співробітників, зміни їхніх робочих годин та розрахунку зарплати.

working_hours = {
    'day': '08-20',
    'night': '20-08'
}

salary_rates_per_shift = {
    'trainee': 40,
    'junior': 70,
    'middle': 120,
    'senior': 250
}

employees_list = [
    {
        'id': 1,
        'name': 'Ivan',
        'working_hours': working_hours['day'],
        'salary_per_shift': salary_rates_per_shift['junior'],
        'shifts_amount_per_mounth': 15
    }
]

def add_employee(employee):
     # expect that clients_list has at least one element
    employees_list.append(
        {
            'id': employees_list[-1]['id'] + 1, 
            'name': employee['name'], 
            'working_hours': employee['working_hours'], 
            'salary_per_shift': employee['salary_per_shift'],
            'shifts_amount_per_mounth': employee['shifts_amount_per_mounth'],
        }
    )

add_employee({
    'name': 'Nastya', 
    'working_hours': working_hours['night'], 
    'salary_per_shift': salary_rates_per_shift['middle'],
    'shifts_amount_per_mounth': 5
    })


def update_working_hours(employee_id, updated_hours):
    for employee in employees_list:
       if(employee_id == employee['id']):
           employee['working_hours'] = updated_hours
           break

update_working_hours(2, working_hours['day']) 

def calculate_salary(employees):
    for employee in employees:
        print(f"Monthly salary of {employee['name']}: {employee['salary_per_shift'] * employee['shifts_amount_per_mounth']}")


calculate_salary(employees_list)