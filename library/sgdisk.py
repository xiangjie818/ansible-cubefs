#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ansible.module_utils.basic import *
import commands

def newpartition(disk, **kwargs):
    zap = kwargs.get('zap', False)
    fstype = kwargs.get('fstype', 'xfs')
    status, check_output = commands.getstatusoutput('blkid -o value -s UUID {}1'.format(disk))
    if zap or status != 0:
        zap_cmd = 'sgdisk -Z {}'.format(disk)
        commands.getoutput(zap_cmd)
        cmd = 'sgdisk -n 0:0:0 {}'.format(disk)
        commands.getoutput(cmd)
        commands.getoutput('mkfs.xfs {}1 -f'.format(disk))

    output = dict(disk=disk, zap=zap, fstype=fstype)
    return output
    
def main():
    module = AnsibleModule(
                argument_spec = dict(
                  disk = dict(type='str', required=True),
                  fstype = dict(type='str', default='xfs', required=False),
                  zap = dict(type='bool', default=False, required=False)
                ),
    )
    disk = module.params['disk']
    fstype =  module.params['fstype']
    zap = module.params['zap']
    result = newpartition(disk, zap=zap, fstype=fstype)
    module.exit_json(**result)

if __name__ == '__main__':
    main()
