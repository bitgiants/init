import os
import platform

# Defining variables
os_platform_name = platform.system()
win_terraform_url = 'https://releases.hashicorp.com/terraform/1.0.11/terraform_1.0.11_windows_amd64.zip'
mac_terraform_url = 'https://releases.hashicorp.com/terraform/1.0.11/terraform_1.0.11_darwin_amd64.zip'


# Defining functions

def check_terr_install(terraform_url,unzip,terraform_path):
    if os.system('terraform --version') == 0:
        print("Terraform already installed")
    else:
        print("Terraform is not installed")
        user_choice = str(input("type 'yes' to proceed with install or enter any key for cancel: "))
        if user_choice == 'yes' or user_choice == 'Yes' or user_choice == 'YES':
            os.system(terraform_url)
            os.system(unzip)
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
    linux_terraform_url = 'wget https://releases.hashicorp.com/terraform/1.0.11/terraform_1.0.11_linux_amd64.zip'
    linux_unzip = 'unzip terraform_*.zip'
    linux_terraform_path = 'mv ./terraform /usr/local/bin/'
    check_terr_install(linux_terraform_url,linux_unzip,linux_terraform_path)
elif os_platform_name == 'nt':
    print("this is a Windows OS")
    #os.chdir("../terraform")
    win_terraform_url = 'Invoke-WebRequest https://releases.hashicorp.com/terraform/1.0.11/terraform_1.0.11_windows_amd64.zip -OutFile terraform.zip'
    win_unzip = 'Expand-Archive -LiteralPath .\terraform.zip -DestinationPath 'C:\Program Files (x86)\''
    #$ENV:PATH
    #'$ENV:PATH="$ENV:PATH;'   
    win_terraform_path =()
    check_terr_install(win_terraform_url,win_unzip,win_terraform_path)
   
else:
    print("Unreconized or unsupported OS")
