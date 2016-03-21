Ansible module used by OSAS to manage a set of servers using Ansible, over the salt bus.

The project started as a fun experiment during Pycon.fr to see if Ansible could run over the
Salt bus, like it can be done over Func.

While the system was working in theory, some weird behavior was triggered when the complex
shell command line from Ansible was sent over the bus to the Salt minion. After a few months
of hiatus, the problem was found to be linked to https://github.com/saltstack/salt/issues/28077 
and so a work-around was devised.

Then due to community familiarity and a need to reuse existing work, Gluster.org infrastructure decided
to migrate from Saltstack to Ansible. But in order to migrate cleanly and not having to change the 
current infra, the decision to reuse the Salt bus was made.

Using the bus from SaltStack provide some benefits:

  * Can work when ssh is down for whatever reason (such as a bad commit)
  * Work from behind a firewall that block ssh for security purpose
  * Leverage complex topology enabled by salt-syndic (https://docs.saltstack.com/en/latest/topics/topology/syndic.html)

In order to use the Salt bus, the role will install salt-master and open the firewall for it. Adding
the minions to the bus is out of the scope of this role.

Then once that role is applied, the usage on the Ansible side can be something like this:

```
$ cat hosts
[all:vars]
ansible_connection=saltstack

[syslog]
syslog01.rax.example.org

$ ansible syslog -m ping
syslog01.rax.example.org | SUCCESS => {
    "changed": false, 
    "ping": "pong"
}
```

Of course, Ansible can also use and mix with others type of transports.

For now, the role hardcode the use of ansible_admin user in the ACL. There is plan to
make it more generic later.

The role is made to integrate with the [ansible_bastion role](https://github.com/OSAS/ansible-role-ansible_bastion).
