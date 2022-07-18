#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from threading import Thread

import socket


#!/usr/bin/python3

import sys, time
import threading


def start_daemon():
    thread_con = Thread(target = thread_socket_server)
    thread_con.start()

def stop_daemon():
    param_hu.run_thread_socket = False

def thread_socket_server():
    port_hubi = param_hu.state_hu["self"]["sock_server_port"]
    port_pywa = param_hu.state_hu["pywardium"]["sock_server_port"]
    ip = param_hu.state_hu["pywardium"]["ip"]

    param_hu.sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_hu.sock_server.bind(("127.0.0.1", port_hubi))
    param_hu.sock_server.settimeout(1)
    param_hu.run_thread_socket = True

    while param_hu.run_thread_socket:
        try:
            print("wait")
            print(port_hubi)
            data, (address, port) = param_hu.sock_server.recvfrom(4096)
            msg = data.decode('utf-8')
            print(msg)
            if(msg == "test"):
                param_hu.sock_server.sendto(str.encode("ok"), (ip, port_pywa))
            if(msg == "ok"):
                param_hu.state_hu["velodium"]["connected"] = True
        except:
            a=1
        pass
    param_hu.sock_server.close()