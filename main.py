import tkinter as tk
from tkinter import messagebox
import time
import datetime
from socket import *
import time
from time import ctime
import _thread

class Server():

    def __init__(self, parent, controller):

        def runner():
            global after_id
            global secs
            secs += 1
            if secs % 2 == 0:  # every other second
                e_host_v = e_host.get()
                e_port_v = int(e_port.get())

        # after_id = self.after(1000, runner)  # check again in 1 second

        def connect():
            # CONNECT COM PORT
            e_host_v = e_host.get()
            e_port_v = int(e_port.get())
            _thread.start_new_thread(my_server, (show_1, e_host_v, e_port_v))
            # start_new_thread(my_server,(show_1,e_host_v,e_port_v))
            global secs
            secs = 0
            # runner()  # start repeated checking

        def disconnect():
            global after_id
            if after_id:
                self.after_cancel(after_id)
                after_id = None

def my_server(show_1,HOST,PORT):


    BUFSIZE = 1024
    ADDR = (HOST, PORT)

    tcpTimeSrvrSock = socket(AF_INET, SOCK_STREAM)
    tcpTimeSrvrSock.bind(ADDR)
    tcpTimeSrvrSock.listen(5)
    currentDT = datetime.datetime.now()


    while True:
        print('waiting for connection...')

        tcpTimeClientSock, addr = tcpTimeSrvrSock.accept()

        print('...connected from:', addr)

        filename = 'space_image.jpg'
        f = open(filename, 'rb')
        l = f.read(1024)

        while (l):
            tcpTimeClientSock.send(l)
            print('Sent ',repr(l))
            l = f.read(1024)

        f.close()
        print('Done sending')
        tcpTimeClientSock.send('Thank you for connecting')
        tcpTimeClientSock.close()



        '''while True:
            data = tcpTimeClientSock.recv(BUFSIZE)
            if not data:
                break

            tcpTimeClientSock.send(bytes(currentDT.strftime("%I:%M:%S %p"),'utf-8'))

            show_1.insert(tk.END,data.decode('utf-8'))
            show_1.insert(tk.END,"\n")
            print(data.decode('utf-8'))

        tcpTimeClientSock.close()
    tcpTimeSrvrSock.close()'''




