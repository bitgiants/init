ter_vars = "../../terraform/variables.tf"
vsphere_user_name = str('default = "vsphere_user_name"')


def get_user_data(data_name):
    return input(f"Enter your  {data_name} : ")


print("This Wizard will setup your lab environment")
user_choice = str(input("type 'yes' to proceed or enter any key for cancelation: "))

if user_choice == 'yes' or user_choice == 'Yes' or user_choice == 'YES':
    vsphere_server = get_user_data('Vcenter IP')
    vsphere_user = get_user_data('Vcenter username in format administrator@vsphere.local')
    vsphere_password = get_user_data('Vcenter password')
    print(f"you entered:\n vcenter IP: {vsphere_server}\n vcenter username: {vsphere_user}\n "
          f"vcenter user password: {vsphere_password}\n")
    concat_server = str('  default = ' + '"' + vsphere_server + '"')
    concat_username = str('  default = ' + '"' + vsphere_user + '"')
    concat_password = str('  default = ' + '"' + vsphere_password + '"')
    lines = ['variable "vsphere_server" {', '  type = string', concat_server, '}', '',
             'variable "vsphere_user" {', '  type = string', concat_username, '}', '',
             'variable "vsphere_password" {', '  type = string', concat_password, '}']
    with open(ter_vars, 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')
else:
    print('all right lets do that manually')





