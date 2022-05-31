CMD_OPEN = '''
        <edit-config>
            <target>
                <candidate />
            </target>
            <default-operation>merge</default-operation>
            <config>
                <configuration>
        '''
CMD_CLOSE = '''
                </configuration>
            </config>
        </edit-config>
    '''

def setHostnameCmd(hostname: str) -> str:
    return CMD_OPEN + f'''
            "<system>
                <host-name>"{hostname}"</host-name>
            </system>"
            ''' + CMD_CLOSE
#TODO check if <ethernet-auto/> is correct and add link to auto negotiate
def l2InterfaceCmd (interfaceID: int, ) -> str:
    return CMD_OPEN + f'''
            <interfaces>
                <interface>
                    <name>ge-0/0/{interfaceID}</name>
                    <ether-options>
                        <speed>
                            <ethernet-auto/>
                        </speed>
                    </ether-options>
                    <unit>
                        <name>0</name>
                        <family>
                            <ethernet-switching>
                            </ethernet-switching>
                        </family>
                    </unit>
                </interface>
            </interfaces>
            ''' + CMD_CLOSE
#TODO check if <ethernet-auto/> is correct and add link to auto negotiate
#TODO check if it's all for l3
def l3InterfaceCmd (interfaceID: int, vlanUnit: int, ipAddr: str) -> str:
    return f'''
            <interfaces>
                <interface>
                    <name>ge-0/0/{interfaceID}</name>
                    <ether-options>
                        <speed>
                            <ethernet-auto/>
                        </speed>
                    </ether-options>
                    <unit>
                        <name>{vlanUnit}</name>
                        <family>
                            <ethernet-switching>
                            </ethernet-switching>
                        </family>
                    </unit>
                </interface>
                <interface>
                    <unit>
                        <name>{vlanUnit}</name>
                        <family>
                            <inet>
                                <address>
                                    <name>{ipAddr}</name>
                                </address>
                            </inet>
                        </family>
                    </unit>
                </interface>
            </interfaces>
            '''
