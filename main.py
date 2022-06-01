from ncclient import manager
import pyautogui
import ncBuilder


if __name__ == '__main__':
    host = pyautogui.prompt("IP address of Juniper device you want to configure:")
    if host == None:
        exit()
    print(f"Trying to connect to {host}...")
    dev_srxl = manager.connect(host=host,
                               port=830,
                               username='root',
                               password='Juniper',
                               device_params={'name': 'junos'},
                               timeout=300,
                               hostkey_verify=False,
                               allow_agent=False,
                               look_for_keys=False)
    pyautogui.alert(f"Connected to {host}!")

    in_configuration = True
    while in_configuration:
        response = pyautogui.confirm("What do you want to change?\n"
                                     "Press commit to commit changes",
                                     buttons=['Host name', 'Interface', 'Commit', 'Quit'])
        if response == 'Quit':
            in_configuration = False
        
        elif response == 'Commit':
            print("Trying to commit...")
            result = dev_srxl.commit()
            print(result)

        elif response == 'Host name':
            hostname = pyautogui.prompt("Hostname: ")
            if hostname == None: 
                continue
            cmd = ncBuilder.setHostnameCmd(hostname)
            print("Uploading hostname configuration...")
            result = dev_srxl.rpc(cmd)
            print(result)

        elif response == 'Interface':
            try:
                if_name = pyautogui.prompt("Which interface do you want to configure\n(give name ex. ge-0/0/1)")
                if if_name == None: 
                    continue

                option = pyautogui.confirm(buttons=['L2', 'L3', 'Enable', 'Disable'])
                if option == 'L2':
                    cmd = ncBuilder.l2InterfaceCmd(if_name)
                elif option == 'L3':
                    ipAddr = pyautogui.prompt("Give IP Address with mask (e.g. 192.168.1.3/24): ")
                    if ipAddr == None: 
                        continue
                    cmd = ncBuilder.l3InterfaceCmd(if_name, ipAddr)
                elif option == 'Enable':
                    cmd = ncBuilder.enableCmd(if_name)
                else:
                    cmd = ncBuilder.disableCmd(if_name)
                print("Uploading interface configuration...")
                result = dev_srxl.rpc(cmd)
                print(result)
            except:
                print("Already configured...")
    print(f"Disconnecting from {host}...")
    dev_srxl.close_session()