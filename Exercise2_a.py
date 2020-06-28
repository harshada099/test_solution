import getpass
import sys
import telnetlib
host = "192.168.1.101"
port=22
timeout =10
user = raw_input("Enter your remote account: ")
password = getpass.getpass()
tn = telnetlib.Telnet(host)
tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")
tn.write("ls\n")
tn.write("exit\n")
print tn.read_all()