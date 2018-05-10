#!/usr/bin/env python
import subprocess


def find_port(pid):
    cmd = '''netstat -ntlp | grep %s | awk '{print $4}' | awk -F':' '{print $NF}' | uniq''' % pid
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    port_list = []
    for port in result.stdout:
        port_list.append(port)
    return port_list

def find_proc(proc_list):
    for proc in proc_list:
        cmd = '''ps -ef | grep %s | grep -v grep''' % proc
        result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        for i in result.stdout:
            if i.split()[2] == '1':
                pid = i.split()[1]
                port_list = find_port(pid)
                return proc, port_list

if __name__ == '__main__':
    proc_list = ['ceilometer-agent-central',
                 'ceilometer-agent-notification',
                 'ceilometer-alarm-evaluator',
                 'ceilometer-alarm-notifier',
                 'ceilometer-api',
                 'ceilometer-collector',
                 'cinder-api',
                 'cinder-backup',
                 'cinder-scheduler',
                 'cinder-volume',
                 'glance-api',
                 'glance-registry',
                 'gnocchi',
                 'haproxy',
                 'heat-api',
                 'heat-api-cfn',
                 'heat-engine',
                 'keepalived',
                 'keystone',
                 'nova-api',
                 'nova-cert',
                 'nova-conductor',
                 'nova-console',
                 'nova-consoleauth',
                 'nova-novncproxy',
                 'nova-scheduler',
                 'senlin',
                 'senlin-api',
                 'senlin-engine',
                 'redis',
                 'rabbitmq',
                 'mysql',
                 'memcached']
    for proc in proc_list:
        proc, port_list = find_proc(proc_list)
        if port_list == None:
            print proc, port_list
        else:
            pass