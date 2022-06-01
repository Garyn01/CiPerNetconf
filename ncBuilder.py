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
            <system>
                <host-name>{hostname}</host-name>
            </system>
            ''' + CMD_CLOSE

def l2InterfaceCmd (interfaceID: str) -> str:
    return CMD_OPEN + f'''
            <interfaces>
                <interface>
                    <name>{interfaceID}</name>
                    <ether-options>
                        <link-mode>automatic</link-mode>
                        <speed>
                            <auto-negotiation>
                            </auto-negotiation>
                        </speed>
                    </ether-options>
                    <unit>
                        <name>0</name>
                        <family>
                            <ethernet-switching>
                            </ethernet-switching>
                            <inet operation="delete"/>
                        </family>
                    </unit>
                </interface>
            </interfaces>
            ''' + CMD_CLOSE

def l3InterfaceCmd (interfaceID: str, ipAddr: str) -> str:
    return CMD_OPEN + f'''
            <interfaces>
                <interface>
                    <name>{interfaceID}</name>
                    <ether-options>
                        <link-mode>automatic</link-mode>
                        <speed>
                            <auto-negotiation>
                            </auto-negotiation>
                        </speed>
                    </ether-options>
                    <unit>
                        <name>0</name>
                        <family>
                            <inet>
                            <address>
                                <name>{ipAddr}</name>
                            </address>
                            </inet>
                            <ethernet-switching operation="delete"/>
                        </family>
                    </unit>
                </interface>
            </interfaces>
            ''' + CMD_CLOSE

def disableCmd(interfaceID: str) -> str: 
    return CMD_OPEN + f'''
            <interfaces>
                <interface>
                    <name>{interfaceID}</name>
                    <disable/>
                </interface>
            </interfaces>
            ''' + CMD_CLOSE

def enableCmd(interfaceID: str) -> str: 
    return CMD_OPEN + f'''
            <interfaces>
                <interface>
                    <name>{interfaceID}</name>
                    <disable operation="delete"/>
                </interface>
            </interfaces>
            ''' + CMD_CLOSE