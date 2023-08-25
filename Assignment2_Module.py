class Assignment2_Module:


    # Question no 1
    def list_to_dict(self):
        li1 = [int(x) for x in input("Enter your list of integers separated by spaces: ").split()]
        li2 = input("Enter your list of strings separated by spaces: ").split()
        print("hello")
        d = {}
        for i in range(len(li1)):
            d[li1[i]] = li2[i]
        print(d)

    # Question no 2
    def replace_dictionary(self):
        input_string = input("Enter a dictionary in the format {key1:value1, key2:value2, ...}: ")
        input_dict = eval(input_string) 
        for key,value in input_dict.items():
            if input_dict[key] == 'D':
                input_dict[key] = 'apple'
        return input_dict

    
    # Question no 3
    def update_dictionary(self):
        input_string = input("Enter a dictionary in the format {'key1': value1, 'key2': value2, ...}: ")
        input_dict = eval(input_string)
        for key,value in input_dict.items():
            if input_dict[key] == 7:
                input_dict[key] = 10
        return input_dict
  

    # Question no 4
    def find_common_elements(self):
        input_string1 = input("Enter the first list as comma-separated values: ")
        list1 = [int(x) for x in input_string1.split(',')]

        input_string2 = input("Enter the second list as comma-separated values: ")
        list2 = [int(x) for x in input_string2.split(',')]
        for item1 in list1:
            for item2 in list2:
                if item1 == item2:
                    print(item1, end=' ,')

    # Question no 5
    def use_of_continue(self):
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
        for i in range(start, end+1):
            if i % 2 == 0:
                continue
            else:
                print(i)
    
    # Question no 6
    def update_list_element(self):
        input_string = input("Enter a list containing different data types: ")
        input_list = eval(input_string) 

        index = int(input("Enter the index of the dictionary element in the list: "))
        key = int(input("Enter the key for the dictionary element: "))
        value = input("Enter the value to update with: ")
        
        input_list[index][key] = value

        print(input_list)

    # Question no 7
    def add_occupation_to_nested_dict(self):
        input_string = input("Enter a nested dictionary in the format {'person1': {'age': age1, 'city': 'city1'}, 'person2': {'age': age2, 'city': 'city2'}, ...}: ")
        input_dict = eval(input_string) 
        for person, details in input_dict.items():
            print("hi",details)
            details['occupation'] = 'Engineer'
            
            return input_dict
            
    # Question no 8
    def filter_age_above_18(self):
        input_string = input("Enter a dictionary of names and ages in the format {'name1': age1, 'name2': age2, ...}: ")
        input_dict = eval(input_string) 
        new_age_dict = {}
        for name, age in input_dict.items():
            if age >= 18:
                new_age_dict[name] = age
        return new_age_dict

    # Question no 9
    def sort_num_list(self):
        input_list = [int(x) for x in input("Enter your list of integers separated by spaces: ").split()]
        for i in range(len(input_list)):
            for j in range(i+1, len(input_list)):
                if input_list[i] > input_list[j]:
                    input_list[i], input_list[j] = input_list[j], input_list[i]
        return input_list
    
     # Question no 10
    def sort_string_list(self):
        input_list = input('Enter your list of Alphabets or words seperated by spaces').split()
        for i in range(len(input_list)):
            for j in range(i+1, len(input_list)):
                if input_list[i] > input_list[j]:
                    input_list[i], input_list[j] = input_list[j], input_list[i]
        return input_list
    
    # Question no 11
    def sort_alphanumeric_list(self):
        input_list = input('Enter your list of characters and integers seperated by spaces').split()
        for i in range(len(input_list)):
            for j in range(i+1, len(input_list)):
                if input_list[i] > input_list[j]:
                    input_list[i], input_list[j] = input_list[j], input_list[i]
        return input_list
    
    
    


    
