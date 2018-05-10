#!/usr/bin/env python
import subprocess
proc_list = ['ceilometer-agent-central',
                 'ceilometer-agent-notification',
                 'ceilometer-alarm-evaluator',
                 'ceilometer-alarm-notifier',
                 'glance-api']
for proc in proc_list:
    cmd = '''ps -ef | grep %s | grep -v grep''' % proc
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for i in result.stdout:
        if i.split()[2] == '1':
            pid = i.split()[1]
            print proc, pid