#!/usr/bin/python 
# -*- coding: utf-8 -*-

from ansible.module_utils.dell5548 import dell5548 #import dell5548
from ansible.module_utils.basic import *  
import os

def main(): 

    fields = {
        "ansible_become_method": {"required": False, "type": "str"},
        "ansible_ssh_user": {"required": True, "type": "str"},
        "ansible_ssh_pass": {"required": True, "type": "str"},
        "ansible_pathtoswitch_inventory": {"required": True, "type": "str"},
        "commands": {"required": True, "type": "str"}
    }

    
    module = AnsibleModule( argument_spec=fields )
    ansible_pathtoswitch_inventory = module.params.get("ansible_pathtoswitch_inventory")
    ansible_ssh_pass = module.params.get("ansible_ssh_pass")
    ansible_ssh_user = module.params.get("ansible_ssh_user")
    commands = module.params.get("commands")
    ansible_become_method = module.params.get("ansible_become_method")

#--------------recuperation de l'inventaire et parsage------------
    hostdict = {}
    hostfile =  open(ansible_pathtoswitch_inventory,'r')
    in_powerconnectlist = False

    for hostname in hostfile:
        if (hostname[0] == '['):
            in_powerconnectlist = False
        if ("[powerconnect]" in hostname):
            in_powerconnectlist = True
        if (in_powerconnectlist == True and hostname[0] != '[') :
            hostdict[hostname.split()[0]]= hostname.split()[1][13:]
    hostfile.close()
    returned["hostdict"]=hostdict
    returned["ansible_become_method"]=ansible_become_method
#------------------------------------------------------------------
#-------------execution de la commande pour chaque host------------

    for cle in hostdict.keys():
        switch=dell5548(hostdict[cle],ansible_ssh_user,ansible_ssh_pass)
        if (ansible_become_method=="enable"):
            switch.exec_cmd_in_enable(commands)
        else:
            switch.exec_cmd(commands)


#------------------------------------------------------------------
#--------récuperation des retours et affichage de celui------------

    #returned = {"hostdict": hostdict}
    module.exit_json(changed=False, meta=returned)

#------------------------------------------------------------------


if __name__ == '__main__':
    main()


