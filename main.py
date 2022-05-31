from ncclient import manager
import pyautogui
import ncBuilder
# L2
# inet
# na switchu speed na interface
if __name__ == '__main__':
    host = pyautogui.prompt("IP address of Juniper device you want to configure:")
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
                                     buttons=['Host name', 'Interface', 'Commit'])
        if response == 'Commit':
            in_configuration = False
            
        elif response == 'Host name':
            hostname = pyautogui.prompt("Hostname: ")
            cmd = ncBuilder.setHostnameCmd(hostname)
            print("Uploading hostname configuration...")
            result = dev_srxl.rpc(cmd)
            print(result)

        elif response == 'Interface':
            if_name = pyautogui.prompt("Which interface do you want to configure\n(give name ex. ge-0/0/1)")
            option = pyautogui.confirm(buttons=['L2', 'L3', 'Disable'])
            if (option == 'L2'):
                cmd = ncBuilder.l2InterfaceCmd(if_name)
            elif (option == 'L3'):
                vlanID = pyautogui.prompt("Give VlanID: ")
                ipAddr = pyautogui.prompt("Give IP Address with mask (e.g. 192.168.1.3/24): ")
                cmd = ncBuilder.l3InterfaceCmd(if_name, vlanID, ipAddr)
            else:
                cmd = ncBuilder.disableCmd(if_name)
            print("Uploading interface configuration...")
            result = dev_srxl.rpc(cmd)
            print(result)

    print("Trying to commit...")
    result = dev_srxl.commit()
    print(result)
    dev_srxl.close_session()