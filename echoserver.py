#!/usr/bin/python

import socket
import select
import signal

# intercept signal
def sigint_handler(signal, frame):
    print "Cleaning up sockets..."
    # close all open sockets
    for sock in readable:
        sock.close()
    for sock in writable:
        sock.close()
    for sock in errable:
        sock.close()
    print "Done!"
    exit(0)
signal.signal(signal.SIGINT, sigint_handler)

# create server socket
msock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
msock.bind(("", 1024))
print "Successfully binded to:", msock.getsockname()

# start listening
msock.listen(5)
print "Listening on:", msock.getsockname()

# open socket lists
readable = [msock]
writable = []
errable = []

while 1:
    tmpr, tmpw, tmpe = select.select(
                        readable,
                        writable,
                        errable,
                        60)

    # handle socket read either
    #   1. accept() new connection
    #   2. read data from socket

    if msock in tmpr:
        newconn, addr = msock.accept()
        readable.append(newconn)
        tmpr.remove(msock)

    # read from every connection and echo
    for sock in tmpr:
        sock.send(sock.recv(1024))
