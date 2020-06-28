from paramiko import SSHClient
from scp import SCPClient
ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('127.0.0.1')
with SCPClient(ssh.get_transport()) as scp:
    scp.put('my_file.txt', 'my_file.txt')
