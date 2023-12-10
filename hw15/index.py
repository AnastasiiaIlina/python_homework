# Task 1
# A Person class
# Make a class called Person. Make the __init__() method take firstname, 
# lastname, and age as parameters and add them as attributes. Make another method 
# called talk() which makes prints a greeting from the person containing, 
# for example like this: "Hello, my name is Carl Johnson and I’m 26 years old".

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f'Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old')

 
person1 = Person('Petro', 'Petrenko', 32)
person1.talk()

# Task 2
# Doggy age
# Create a class Dog with class attribute 'age_factor' equals to 7.
# Make __init__() which takes values for a dog’s age. Then create a method `human_age` 
# which returns the dog’s age in human equivalent.

class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age
 
    def human_age(self):
        return Dog.age_factor * self.age

dog1 = Dog(2)
print(dog1.human_age())

# Task 3
# TV controller
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:

# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel 
# numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is 
# the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, 
# turns on the last channel.
# current_channel() - returns the name of the current channel.
# exists(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", 
# if the channel N or 'name' exists in the list, or "No" - in the other case.
 
# The default channel turned on before all commands is №1.
# Your task is to create the TVController class and methods described above.

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:

    def __init__(self, channels):
        self.channels = channels
        self.current_channel = channels[0]

    def first_channel(self):
        self.current_channel = self.channels[0]
        return self.current_channel
    
    def last_channel(self):
        self.current_channel = self.channels[-1]
        return self.current_channel
    
    def turn_channel(self, N):
        try:
            self.current_channel = self.channels[N-1]
            return self.current_channel
        except IndexError:
            return f'There is no channel with number {N}'

    def next_channel(self):
        if self.current_channel == self.channels[-1]:
            self.first_channel()
        else:
            current_index = self.channels.index(self.current_channel)
            self.current_channel = self.channels[current_index + 1]

        return self.current_channel
    
    def previous_channel(self):
        if self.current_channel == self.channels[0]:
            self.last_channel()
        else:
            current_index = self.channels.index(self.current_channel)
            self.current_channel = self.channels[current_index - 1]

        return self.current_channel

    def get_current_channel(self):
        return self.current_channel

    def exists(self, number_or_name):
        if type(number_or_name) == int:
            try:
                element = self.channels[number_or_name]
                print(element)

                return 'Yes'
            except IndexError:
                return 'No'
        else:
            if number_or_name in self.channels:
                print(number_or_name)
                return 'Yes'
            else:
                return "No"
            
controller = TVController(CHANNELS)

assert controller.first_channel() == "BBC"
assert controller.last_channel() == "TV1000"
assert controller.turn_channel(1) == "BBC"
assert controller.next_channel() == "Discovery"
assert controller.previous_channel() == "BBC"
assert controller.get_current_channel() == "BBC"
assert controller.exists(4) == "No"
assert controller.exists("BBC") == "Yes"
