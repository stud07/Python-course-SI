from data import values_input, percentage, value_check_USD, value_check_EUR, delete_resource, new_resource, change_the_quantity, resource, clear, check_condition

def programm():
    while True:
        print('What do you want to do? \n', "1. Enter your resources.\n", "2. Check the condition of your resources. \n", "3. Percentage. \n", "4. Value. \n", "5. Add new resource. \n", "6. Delete given resource. \n", "7. Change quantity of a resource. \n", "8. Clear all resources. \n", "Q: Press to quit.")
        action = input("\n SELECT NUMBER: ")

        if action == '1':
            values_input()
        elif action == '2':
            if check_condition() is True:
                print("You have no resources")
            else:
                resource()
        elif action == '3':
            if check_condition() is True:
                print("You have no resources")
            else:
                percentage()
        elif action == '4':
            if check_condition() is True:
                print("You have no resources")
            else:
                currency = input('Choose currency USD / EUR:')
                if currency == 'USD':
                    value_check_USD()
                elif currency == 'EUR':
                    value_check_EUR()
                else:
                    print('Something went wrong')
        elif action == '5':
            new_resource()
        elif action == '6':
            if check_condition() is True:
                print("You have no resources")
            else:
                delete_resource()
        elif action == '7':
            if check_condition() is True:
                print("You have no resources")
            else:
                change_quantity()
        elif action == '8':
            clear()
        elif action.upper() == 'Q':
            break
        else:
            print('Something went wrong')


programme()