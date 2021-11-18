def get_user_data(data_name):
    return input(f"Enter your  {data_name} : ")


print("Hi, this is wizard to setup your lab environment")
user_choice = str(input("type 'yes' to proceed or enter any key for cancelation: "))

if user_choice == 'yes' or user_choice == 'Yes' or user_choice == 'YES':
    print('your choice YES! Lets GO')
    vsphere_server = get_user_data('Vcenter IP')
    vsphere_user = get_user_data('Vcenter username in format administrator@vsphere.local')
    vsphere_password = get_user_data('Vcenter password')
    print(f"you entered:\n vcenter IP: {vsphere_server}\n vcenter username: {vsphere_user}\n vcenter user password: {vsphere_password}\n")
else:
    print('all right lets do that manually')