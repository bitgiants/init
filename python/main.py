import os
import platform

ter_path = "../../terraform/"
ter_vars = "../../terraform/variables.tf"
vsphere_user_name = str('default = "vsphere_user_name"')
win_terraform_url = 'https://releases.hashicorp.com/terraform/1.0.11/terraform_1.0.11_windows_amd64.zip'
mac_terraform_url = 'https://releases.hashicorp.com/terraform/1.0.11/terraform_1.0.11_darwin_amd64.zip'

os_platform_name = platform.system()


def check_terr_install(terraform_url, unzip, terraform_path):
    if os.system('terraform --version') == 0:
        print("Terraform already installed")
    else:
        print("Terraform is not installed")
        user_choice = str(input("type 'yes' to proceed with install or enter any key for cancel: "))
        if user_choice == 'yes' or user_choice == 'Yes' or user_choice == 'YES':
            # download terraform binary
            os.system(terraform_url)
            # unzip terraform binary to workdir
            os.system(unzip)
            # mv terraform binary to os binary directory
            os.system(terraform_path)
        else:
            print("Try to install Terraform manually")


if os_platform_name == 'Darwin':
    print("this is a mac OS")
    os.chdir("../terraform")
    print("Executing terraform init")
    terraform_init_output = os.system('terraform init')
    print(terraform_init_output)
    terraform_plan_output = os.system('terraform plan')
    print(terraform_plan_output)
    terraform_url_mac = 'https://releases.hashicorp.com/terraform/1.0.11/terraform_1.0.11_darwin_amd64.zip'
    check_terr_install(terraform_url_mac)
elif os_platform_name == 'Linux':
    print("this is a Linux OS")
    # download terraform binary:
    linux_terraform_url = 'wget https://releases.hashicorp.com/terraform/1.0.11/terraform_1.0.11_linux_amd64.zip'
    # unzip terraform binary to workdir:
    linux_unzip = 'unzip terraform_*.zip'
    # mv terraform binary to os binary directory
    linux_terraform_path = 'mv ./terraform /usr/local/bin/'
    # check terraform installation and install if not:
    check_terr_install(linux_terraform_url, linux_unzip, linux_terraform_path)
elif os_platform_name == 'Windows':
    print("this is a Windows OS")
    if os.system('terraform --version') == 0:
        print("Terraform already installed")
    else:
        print("Terraform is not installed")
        win_user_choice = str(input("type 'yes' to proceed with install or enter any key for cancel: "))
        if win_user_choice == 'yes' or win_user_choice == 'Yes' or win_user_choice == 'YES':
            print('Download Terraform binary')
            power_shell = '"powershell.exe"'
            # This block is ok, tested and working---------------------------------------------------
            win_terraform_url = str('Invoke-WebRequest '
                                    'https://releases.hashicorp.com/terraform/1.0.11/terraform_1.0'
                                    '.11_windows_amd64.zip -OutFile terraform.zip')
            download_terraform = f'{power_shell} {win_terraform_url}'
            os.system(download_terraform)
            install_dirpath = 'C:\\Windows\\System32'
            filepath = f'{install_dirpath}\\terraform.exe'
            if not os.path.isfile(filepath):
                print(f'Unzip terraform bin into {install_dirpath}')
                archive_path = r'.\terraform.zip'
                win_unzip = str(
                    f'{power_shell} Expand-Archive -LiteralPath {archive_path} -DestinationPath {install_dirpath}')
                os.system(win_unzip)
        else:
            print(os.environ.get('PATH'))
else:
    print("Unreconized or unsupported OS")


def get_user_data(data_name):  # function to get user input
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

should_exec_t_init = str(input("type 'yes(y)' if you would like to execute terraform init and plan and or enter "
                               "any key for cancelation: "))
if should_exec_t_init == 'yes' or should_exec_t_init == 'Yes' or should_exec_t_init == 'YES' or should_exec_t_init == 'y':
    print(os.system(f'terraform -chdir="{ter_path}" init'))
    print(os.system(f'terraform -chdir="{ter_path}" plan'))
else:
    print('ok, next time!!!')

should_exec_t_apply = str(input("type 'yes(y)' if you would like to execute terraform apply or enter "
                                "any key for cancelation: "))
if should_exec_t_apply == 'yes' or should_exec_t_apply == 'Yes' or should_exec_t_apply == 'YES' or should_exec_t_init == 'y':
    print(os.system(f'terraform -chdir="{ter_path}" apply'))
else:
    print('ok, next time!!!')
