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
'''

EXAMPLES = '''

'''

RETURN = '''

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
