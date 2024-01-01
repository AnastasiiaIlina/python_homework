import unittest
import json
from functions import count_local_vars, outside_fun, choose_func, use_phonebook

# Task 1
# Pick your solution to one of the exercises in this module.
# Design tests for this solution and write tests using unittest library. 

# let's test functions from homework 13
class TestHW13(unittest.TestCase):
    def test_count_local_vars(self):    
        self.assertEqual(count_local_vars(), {'var1': 0, 'var2': 1})

    def test_outside_fun(self):
        self.assertEqual(outside_fun(2)(3), 6)
        self.assertEqual(outside_fun(3)(0), 0)

    def test_choose_func(self):
        def square_nums(nums):
            return [num ** 2 for num in nums]

        def remove_negatives(nums):
            return [num for num in nums if num > 0]
        
        self.assertEqual(choose_func([1, 2, 3, 4, 5], square_nums, remove_negatives), [1, 4, 9, 16, 25])
        self.assertEqual(choose_func([1, -2, 3, -4, 5], square_nums, remove_negatives), [1, 3, 5])


# Task 2
# Write tests for the Phonebook application, which you have implemented 
# in module 1. Design tests for this solution and write tests using unittest library
    
class PhonebookTest(unittest.TestCase):
    def test_use_phonebook(self):
        with open('phonebook.json', 'r') as file:
            phonebook = json.load(file)
         
        # add
        phonebook.append({
            'first_name': 'Anastasiia',
            'last_name': 'Ilina',
            'city': 'Lviv',
            'tel': '+3805656656565'
        })

        self.assertEqual(use_phonebook('phonebook.json'), phonebook)

        # update
        # change users city with +3805656656565 phone from Lviv to Kyiv
        updated_user = {
            'first_name': 'Anastasiia',
            'last_name': 'Ilina',
            'city': 'Kyiv',
            'tel': '+3805656656565'
        }
        for index, user in enumerate(phonebook):
            if user['tel'] == '+3805656656565':
                phonebook[index] = updated_user
                break

        self.assertEqual(use_phonebook('phonebook.json'), phonebook)

        # delete
        # delete user with phone number +3805656656565
        for index, user in enumerate(phonebook):
            if user['tel'] == '+3805656656565':
                phonebook.pop(index)
                break
        self.assertEqual(use_phonebook('phonebook.json'), phonebook)
            
        # search
        # search by last_name 'Ilina'
        filtered_phonebook = []

        for user in phonebook:
            if user['last_name'] == 'Ilina':
                filtered_phonebook.append(user)

        self.assertEqual(use_phonebook('phonebook.json'), filtered_phonebook)  


if __name__ == '__main__':
    unittest.main()

