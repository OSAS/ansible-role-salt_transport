#!/usr/bin/python
#coding: utf-8 -*-

# (c) 2016, Michael Scherer <mscherer@redhat.com>
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.

DOCUMENTATION = '''
---
module: salt_grains_facts
short_description: Retrieve grains from the local salt minion to use as ansible facts
version_added: None
options:
  path:
    required: False
    description: path to the minion config, if not using the default
'''

EXAMPLES = '''
- name: Gather information from the local salt minion
  salt_grains_facts:

- name: Display a grain (kernel)
  debug: msg="Salt kernel grain is {{ grains['kernel'] }}"
'''

RETURN = '''
grains:
  description: Saltstack grains, see saltstack doc for complete list
  type: dict
  returned: always
'''

try:
    import salt.config
    import salt.loader
    HAS_SALT = True
except ImportError:
    HAS_SALT = False


def main():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(required=False, type='path', default='/etc/salt/minion')
        )
    )
    params = module.params

    if not HAS_SALT:
        module.fail_json(msg="Missing required salt modules")

    grains = salt.loader.grains(salt.config.minion_config(params['path']))
    module.exit_json(changed=False, ansible_facts=dict(grains=grains))

# this is magic, see lib/ansible/module_common.py
from ansible.module_utils.basic import *
main()
