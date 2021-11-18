print("Hi, this is wizard to setup your lab environment")

user_choice = str(input("type 'yes' to proceed or enter any key for cancelation: "))

if user_choice == 'yes' or user_choice == 'Yes' or user_choice == 'YES':
    print('your choice YES! Lets GO')
else:
    print('all right lets do that manually')