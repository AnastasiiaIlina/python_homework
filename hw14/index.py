from functools import wraps

# Task 1
# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!

def logger(func):
    @wraps(func)

    def print_func(*args):
        print(f"{func.__name__} called with {','.join(str(x) for x in args)}")
        
        return func(*args)
    
    return print_func


@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(4,5)
square_all(6,4,7,7)

# Task 2
# Write a decorator that takes a list of stop words 
# and replaces them with * inside the decorated function

def stop_words(words: list):
    def replace_words(fn):
        @wraps(fn)
        def wrapped_fn(name):
            initial_str = fn(name)

            for word in words:
                if word in initial_str:
                    initial_str = initial_str.replace(word, '*')

            return initial_str
        return wrapped_fn
    return replace_words


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

create_slogan("Steve")
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

# Task 3
# Write a decorator "arg_rules" that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain

# If some of the rules' checks returns False, the function 
# should return False and print the reason it failed; otherwise, return the result.


def arg_rules(type_: type, max_length: int, contains: list):

    def chech_rules(fn):
        def wrapped_fn(name):
            if type(name) != type_:
                print('Name should be a string!')
                return False
            
            if len(name) > max_length:
                print('Long name!')
                return False
            
            is_required_symbol = True

            for contain in contains:
                if not(contain in name):
                    is_required_symbol = False

            if not is_required_symbol:
                print('Name doesn`t have required symbols')
                return False
            
            return fn(name)
        return wrapped_fn
    return chech_rules

 

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('05years') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'