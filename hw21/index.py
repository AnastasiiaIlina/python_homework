# Task 1
# File Context Manager class
# Create your own class, which can behave like a built-in function 'open'. 
# Also, you need to extend its functionality with counter and logging. 
# Pay special attention to the implementation of '__exit__' method, 
# which has to cover all the requirements to context managers

class FileContextManager:
    counter = 0

    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.file_name, self.mode)

        with open('log.txt', 'a') as logger_file:
            logger_file.write(f'File {self.file_name} is opened\n')

        FileContextManager.counter += 1
        return self.file

    def __exit__(self, ex_type, ex_val, traceback):
        with open('log.txt', 'a') as logger_file:
            logger_file.write(f'File {self.file_name} is closed\n')
            logger_file.write(f'Total closed files -  {self.counter}\n')
            logger_file.write(f'-----------------\n')

        self.file.close()

# with FileContextManager('my_file.txt', 'a+') as file:
#     file.write('\nNew string!')

# with FileContextManager('my_file.txt', 'r') as file:
#     print(file.read())

