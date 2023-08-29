from Assignment2_Module import Assignment2_Module

def main():
    obj = Assignment2_Module()
    

    while True:

        print('Enter your question num')
        print('Enter 1 to convert lists to dictionary')
        print('Enter 2 to replace the specific values of dictionary')
        print('Enter 3 to update the specific values of dictionary')
        print('Enter 4 to find the common elements in the ;lists')
        print('Enter 5 to check the use of continue in python')
        print("Enter 6 to replace the dictionary's value in a list")
        print('Enter 7 to add new key value pair in nested dictionary')
        print('Enter 8 to filter out the persons having age above or equal to 18')
        print('Enter 9 to sort a list numbers in asscending order ')
        print('Enter 10 to sort a list of alphabets or strings in asscending order ')
        print('Enter 11 to sort a list of strings and integers in asscending order ')
        print("Enter 12 to check how single inheritance works")
        print("Enter 13 to check how multiple inheritance works")
        print("Enter 14 to check how multilevel inheritance works")
        print("Enter 15 to check how herarchical inheritance works")
        print('Enter 16 to Exit')
        
        ques = int(input('Enter the question number (1 to 16): '))
        if ques == 1 :
            result = obj.list_to_dict()
            print(result)
        elif ques == 2 :
            result = obj.replace_dictionary()
            print(result)
        elif ques == 3 :
            result = obj.update_dictionary()
            print(result)
        elif ques == 4 :
            result = obj.find_common_elements()
            print(result)
        elif ques == 5 :
            result = obj.use_of_continue()
            print(result)
        elif ques == 6 :
            result = obj.update_list_element()
            print(result)
        elif ques == 7 :
            result = obj.add_occupation_to_nested_dict()
            print(result)
        elif ques == 8 :
            result = obj.filter_age_above_18()
            print(result)
        elif ques == 9:
            result = obj.sort_num_list()
            print(result)
        elif ques == 10:
            result = obj.sort_string_list()
            print(result)
        elif ques == 11:
            result = obj.sort_alphanumeric_list()
            print(result)
        elif ques == 12:
            object = obj.Child()
            object.func1()
            object.func2()
        elif ques == 13:
            s1 = obj.Beta()
            s1.beta()
        elif ques == 14:
            v1 = obj.Son()
            v1.son()
        elif ques == 15:
            object1 = obj.Child1()
            object2 = obj.Child2()
            object1.function1()
            object1.function2()
            object2.function1()
            object2.function3()
        elif ques == 16:
            break
        else:
            print("Invalid question number.")

if __name__ == "__main__":
    main()








   
