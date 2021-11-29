import os
import platform

# Defining variables
os_platform_name = platform.system()
win_terraform_url = 'https://releases.hashicorp.com/terraform/1.0.11/terraform_1.0.11_windows_amd64.zip'
mac_terraform_url = 'https://releases.hashicorp.com/terraform/1.0.11/terraform_1.0.11_darwin_amd64.zip'


# Defining functions

def check_terr_install(terraform_url):  #<<----CHECK IT  !!!!!! Передать значения переменных в функцию
    if os.system('terraform --version') == 0:  # В зависимости от операционной системы
        print("Terraform already installed")
    else:
        print("Terraform is not installed")
        user_choice = str(input("type 'yes' to proceed with install or enter any key for cancel: "))
        if user_choice == 'yes' or user_choice == 'Yes' or user_choice == 'YES':
            os.system(terraform_url)
            os.system('unzip terraform_*.zip')
            os.system('mv ./terraform /usr/local/bin/')
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
    y_terraform_url = 'wget https://releases.hashicorp.com/terraform/1.0.11/terraform_1.0.11_linux_amd64.zip'
    check_terr_install(terraform_url)
elif os_platform_name == 'nt':
    print("this is a Windows OS")
    os.chdir("../terraform")
    terraform_check = terraform_plan_output = os.system('terraform --version')
else:
    print("Unreconized or unsupported OS")
