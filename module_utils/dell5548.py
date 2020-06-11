#!/usr/bin/env python
# coding: utf-8

import os

class dell5548:
    def __init__(self,adress,user,passwd):
        self.adress = adress
        self.passwd = passwd
        self.user = user
        self.execscript = ["#!/usr/bin/expect\n\r\n\r"]

    def connect(self):
        self.execscript.append("set user [lindex $argv 1]\n\r")
        self.execscript.append("set password [lindex $argv 2]\n\r")
        self.execscript.append("set ipaddr [lindex $argv 0]\n\rset prompt \"#\" \n\r")
        self.execscript.append("spawn ssh $user@$ipaddr"+"\n\r")
#        self.execscript.append('expect "*?ame:*"'+"\n\r"+'send -- "$user\\r"'+"\n\r")
#        self.execscript.append('expect "*?assword:*"'+"\n\r"+'send -- "$password\\r"'+"\n\r")
        self.execscript.append('\n\rexpect {\n\r   Name: {\n\r        send "$user\\r"\n\r        expect Password: {\n\r            send "$password\\r"\n\r            }        \n\r    } incorrect {\n\r        send_user "invalid password or account\\n"\n\r        exit\n\r    } timeout {\n\r        send_user "connection to $ipaddr timed out\\n"\n\r        exit\n\r    } eof {\n\r        send_user "connection to host failed: $expect_out(buffer)"\n\r        exit\n\r    } \n\r}\n\r\n\r')

    def prntexecscript(self):
        for i in self.execscript:
            print(i)
    
    def command(self,command):
        self.execscript.append('expect -re $prompt\n\r')
        self.execscript.append('send -- "'+command+'\\r"'+"\n\r")

    def verbose(self):
        self.execscript.append('\
            \n\rwhile { 1 } {\
            \n\r    expect {\
            \n\r        "*More*" { send " " }\
            \n\r        -re $prompt { break }\
            \n\r    }\
            \n\r}')



    def createxec(self):
        self.execscript.append('\n\rsend "exit\\r"')
        file=open("tmp.exec","w")
        for i in self.execscript:
            file.write(i)
        os.system("chmod +x tmp.exec")

    def execf(self):
        os.system("expect tmp.exec "+self.adress+" "+self.user+" "+self.passwd+" > log/"+self.adress)
        os.system("rm -f tmp.exec ")

    def exec_cmd_in_enable(self,command):
        self.connect()
        self.command(command)
        self.verbose()
        self.createxec()
        #self.prntexecscript()
        self.execf()

    def exec_cmd(self,command):
        self.connect()
        self.command("configure terminal")
        self.command(command)
        self.verbose()
        self.createxec()
        #self.prntexecscript()
        self.execf()
        

