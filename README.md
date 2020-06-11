# ANSIBLE MODULE FOR DELLOS4.1.0.x


[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)

this project has been made to use ansible on old switch who are not supported by the dell library for ansible because there is an issue with the ssh implementation from those old dell switch who are using.

## To begin

has been tested on DELL 5548 switch with OS Version = 4.1.0.x and should work with any dell switch under this OS Version.


### Needed

you will need to have ansible installed on you're computer and who is working.
``https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html``

### Instal

you need to :
 - git clone this repository. ``git clone https://github.com/Lexios4/ansible_module_dellOS4.1.0.x.git``
 - to add an inventory from the example.
 - to create the playbook from the example.

## Démarrage

you can execute you're playbook like this ``ansible-playbook  exempleplaybook.yml``.

## Contributing

if you want to contribute you will need to understand python and expect.

it could be usefull to know that i dynamically create expect script _(in the dell 5548 class)_ and execute it form the information in the playbook


## Authors
* **Gaetan GIANQUINTIERI**


