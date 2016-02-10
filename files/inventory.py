#!/usr/bin/env python

# (c) 2015, Michael Scherer <misc@zarb.org>
#
# This file is part of Ansible,
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

DOCUMENTATION = '''
---
inventory: saltstack
short_description: Saltstack minion inventory script
description:
  - Generates inventory of Salt managed minions
version_added: 2.0
author: Michael Scherer
'''
import sys
import json
try:
    import salt
    import salt.key
    import salt.config
except ImportError:
    print("failed=True msg='`salstack` is required for this script'")
    sys.exit(1)

if len(sys.argv) == 2 and sys.argv[1] == '--list':
    c = salt.config.master_config('/etc/salt/master')
    c['__role'] = 'master'
    print(json.dumps(salt.key.Key(c).list_keys()['minions']))
elif len(sys.argv) == 3 and sys.argv[1] == '--host':
    print(json.dumps({}))
else:
    print("Need an argument, either --list or --host <host>")
