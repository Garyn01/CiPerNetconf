from ncclient import manager
import pyautogui
# L2
# inet
# na switchu speed na interface
if __name__ == '__main__':
    host_ = pyautogui.prompt("IP address of Juniper device you want to configure:")
    print(f"Trying to connect to {host_}...")
    dev_srxl = manager.connect(host=host_,
                               port=830,
                               username='root',
                               password='Juniper',
                               device_params={'name': 'junos'},
                               timeout=300,
                               hostkey_verify=False,
                               allow_agent=False,
                               look_for_keys=False)
    pyautogui.alert(f"Connected to {host_}!")

    cmd_open = '''
        <edit-config>
            <target>
                <candidate />
            </target>
            <default-operation>merge</default-operation>
            <config>
                <configuration>
        '''
    cmd_close = '''
                </configuration>
            </config>
        </edit-config>
    '''

    in_configuration = True
    while in_configuration:
        response = pyautogui.confirm("What do you want to change?\n"
                                     "Press commit to commit changes",
                                     buttons=['Host name', 'Interface', 'Commit'])
        if response == 'Commit':
            in_configuration = False
        elif response == 'Host name':
            hostname = pyautogui.prompt("Hostname: ")
            cmd = cmd_open + "<system><host-name>" + hostname + "</host-name></system>" + cmd_close
            print("Uploading configuration...")
            result = dev_srxl.rpc(cmd)
            print(result)
        elif response == 'Interface':
            if_name = pyautogui.prompt("Which interface do you want to configure\n(give name ex. ge-0/0/1)")
            option = pyautogui.confirm(buttons=['L2', 'L3', 'Disable'])
            #TODO if l3 add unit (user input unit number) -> add to this unit inet address -> add unit to chosen interface
            #TODO l3 = l2 + to co wyzej
            #TODO dodac disable

    print("Trying to commit...")
    result = dev_srxl.commit()
    print(result)
    dev_srxl.close_session()