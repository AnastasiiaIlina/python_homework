import random

# 1. Генератор RandomTasks:
# Напишіть генератор, який генерує рандомні завдання для користувача. 
# Кожне завдання повинно мати опис та приблизний час виконання. 
# Генератор може створити, наприклад, список завдань на тиждень.

# my mock data
# time value is presented in minutes
tasks = [
    {
        'description': 'Почитати книгу',
        'time': 60 
    },
    {
        'description': 'Зробити зарядку',
        'time': 30
    },
    {
        'description': 'Помити посуд',
        'time': 20
    },
    {
        'description': 'Зробити домашнє завдання',
        'time': 90
    },
    {
        'description': 'Вигуляти собаку',
        'time': 40
    },
]

def RandomTasks(days):
    counter = 1
    while counter <= days:
        task_index = random.randint(0, len(tasks) - 1)

        yield tasks[task_index]
        counter += 1
   
for task in RandomTasks(3):
    print(task)


# 2. Ітератор для обліку використання робочого часу.
# Створіть клас WorkHoursCounter, який буде ітератором для обліку 
# витраченого робочого часу. Користувач може додавати витрачений час 
# на різні завдання, і ітератор буде підраховувати загальний витрачений 
# час та виводити повідомлення про продуктивність.
        
    
class WorkHoursCounter:
    def __init__(self):  
        self.tasks = [
            { 'name': 'coding', 'hours': 4 },
            { 'name': 'meeting', 'hours': 2 }, 
            { 'name': 'code review', 'hours': 1 }  
        ]

    def add_task(self, name, hours):
        self.tasks.append({ 'name': name, 'hours': hours })
    
    def __iter__(self):
        self.total_time = 0
        self.index = 0

        return self
    
    def __next__(self):
        if self.index < len(self.tasks):
            current_task =  self.tasks[self.index]

            self.total_time += current_task['hours']
            self.index +=1

            return f'На {current_task['name']} було витрачено {current_task['hours']} годин. На всі завдання було витрачено {self.total_time} годин.'
        else:
            raise StopIteration


developer_hours_counter = WorkHoursCounter()
developer_hours_counter.add_task('analytics', 4)


for task in developer_hours_counter:
    print(task)
