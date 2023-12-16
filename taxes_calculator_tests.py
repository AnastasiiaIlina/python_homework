import unittest

# 1. Калькулятор податків:
# Напишіть функцію, яка приймає суму доходу і обчислює загальну суму податку, враховуючи різні ставки податків на прибуток.

# Перевірте, чи функція правильно обчислює податок для суми доходу в межах одного діапазону ставок.
# Додайте тест для випадку, коли сума доходу знаходиться в межах кількох діапазонів ставок.
# Впевніться, що функція правильно обробляє великі суми доходу.

# 2. Система обліку запасів:
# Створіть функцію, яка дозволяє додавати товари до системи обліку запасів, відстежує кількість товарів та повертає інформацію про наявність товарів на складі.

# Створіть тест для додавання нового товару до системи обліку.
# Перевірте, чи функція правильно відстежує кількість товарів.
# Впевніться, що функція виводить коректну інформацію про наявність товарів на складі.

# 3. Обчислення вартості доставки:
# Напишіть функцію, яка приймає вагу товару та відстань до місця доставки і обчислює вартість доставки згідно з заданими тарифами.

# Перевірте, чи функція правильно обчислює вартість доставки для різних вагових та відстаневих категорій.
# Додайте тест для випадку, коли вага або відстань дорівнює нулю.
# Впевніться, що функція правильно обробляє великі значення ваги та відстані.

# 4. Система обліку вартості проекту:
# Напишіть функцію, яка приймає вартість робочих годин, кількість годин та додаткові витрати і розраховує загальну вартість проекту.

# Створіть тест для перевірки правильності розрахунку загальної вартості проекту.
# Перевірте, чи функція коректно обробляє додаткові витрати та різні кількості годин роботи.
# Впевніться, що функція працює правильно для проектів з мінімальними часовими та фінансовими обмеженнями.

# 5. Автоматизація операцій з банківським рахунком:
# Створіть функції для переведення грошей між рахунками, перевірки балансу та виведення історії транзакцій.

# Створіть тест для перевірки можливості переведення грошей між рахунками.
# Перевірте, чи функція правильно обробляє різні сценарії балансу та транзакцій.
# Впевніться, що функція правильно виводить історію транзакцій.

# 6. Система відстеження завдань:
# Напишіть функції для додавання нових завдань, відзначення завершених 
# та виведення списку активних завдань.

# Створіть тест для додавання нового завдання.
# Перевірте, чи функція коректно відзначає завершені завдання та виводить список активних завдань.
# Впевніться, що функція працює правильно для різних типів завдань.

def calculate_tax(income):
    if income < 1000:
        return income * 0.05
    elif income < 5000:
        return income * 0.1
    elif income < 10000:
        return income * 0.2
    else:
        return income * 0.3

goods_in_store = [{'name': 'Pen', 'amount': 1}]

def add_good(good_name):
    new_good = {}
    new_good_index = None

    for index, good in enumerate(goods_in_store):
        if good.get('name') == good_name:
            new_good = {'name': good.get('name'), 'amount': good.get('amount') + 1 }
            new_good_index = index
        else:
            new_good = {'name': good_name, 'amount': 1}
    
    if new_good_index != None:
        goods_in_store[new_good_index] = new_good
    else:
        goods_in_store.append(new_good)

    return goods_in_store


def calculate_delivery_cost(weight, distance):
    base_price = 60

    if weight < 10:
        if distance < 50:
            return base_price
        elif distance < 200:
            return base_price + base_price * 0.2
        else:
            return base_price + base_price * 0.3
    elif weight < 50:
        if distance < 50:
            return base_price + base_price * 0.1
        elif distance < 200:
            return base_price + base_price * 0.3
        else:
            return base_price + base_price * 0.4
    else:
        if distance < 50:
              return base_price + base_price * 0.2
        elif distance < 200:
            return base_price + base_price * 0.4
        else:
            return base_price + base_price * 0.5


def calculate_project_cost(hour_cost, hours, extra_costs):
    return hour_cost * hours + extra_costs

bill1 = {'id': 1, 'balance': 100, 'history': []}
bill2 = {'id': 2, 'balance': 15, 'history': [] }

def transfer_money(write_off_bill, received_bill, transfer_sum):
    write_off_bill['balance'] -= transfer_sum
    received_bill['balance'] += transfer_sum

    write_off_bill['history'].append({'type': 'withdrawal', 'sum': transfer_sum })
    received_bill['history'].append({'type': 'deposit', 'sum': transfer_sum })

    return {'write_off_bill': write_off_bill, 'received_bill': received_bill }

def check_balance(bill):
    return bill['balance']

def print_transactions_history(bills):
    for bill in bills:
        for transaction in bill['history']:
            if transaction['type'] == 'withdrawal':
                print(f'З рахунку №{bill['id']} було списано {transaction['sum']} грн.')
            else:
                print(f'На рахунок №{bill['id']} було зараховано {transaction['sum']} грн.')

tasks_list = [{
    'id': 1,
    'text': 'Зробити уроки',
    'marked': False
}]

def add_task(task_text):
    tasks_list.append({'id': tasks_list[-1]['id'] + 1, 'text': task_text, 'marked': False})

def mark_task_done(task_id):
    for task in tasks_list:
       if(task_id == task['id']):
           task['marked'] = True

           break

def print_active_tasks(tasks):
    for task in tasks:
        if task['marked'] == False:
            print(task)


class MyTest(unittest.TestCase):
    goods_in_store = [{'name': 'Pen', 'amount': 1}]

    # def test_calculate_tax(self):
    #     self.assertEqual(calculate_tax(100), 5)
    #     self.assertEqual(calculate_tax(200), 10)

    #     self.assertEqual(calculate_tax(4000), 400)
    #     self.assertEqual(calculate_tax(100000), 30000)

    # def test_add_good(self):
    #     self.assertEqual(add_good('Pen'), [{'name': 'Pen', 'amount': 2}])
    #     self.assertEqual(add_good('Pencil'), [{'name': 'Pen', 'amount': 2}, {'name': 'Pencil', 'amount': 1}])

    # def test_calculate_delivery_cost(self):
    #     self.assertEqual(calculate_delivery_cost(8, 70), 72)
    #     self.assertEqual(calculate_delivery_cost(0, 70), 72)
    #     self.assertEqual(calculate_delivery_cost(15, 0), 66)
    #     self.assertEqual(calculate_delivery_cost(10000, 1500), 90)

    # def test_calculate_project_cost(self):
    #     self.assertEqual(calculate_project_cost(100, 160, 500), 16500)
    #     self.assertEqual(calculate_project_cost(100, 8, 0), 800)
    #     self.assertEqual(calculate_project_cost(2, 1, 4), 6)

    # def test_transfer_money(self):
    #     self.maxDiff = None
    #     result = transfer_money(bill1, bill2, 10)

    #     self.assertEqual(result['write_off_bill']['history'][0]['sum'], 10)
    #     self.assertEqual(result['received_bill']['history'][0]['sum'], 10)
        

    # def test_check_balance(self):
    #     self.assertEqual(check_balance(bill1), 100)

    def test_add_task(self):
        self.assertEqual(add_task('pass exam'), tasks_list)




if __name__ == '__main__':
    unittest.main()
