#!/usr/bin/python

import socket
import select
import signal

# intercept signal
def sigint_handler(signal, frame):
    print "Cleaning up sockets..."
    # TODO close sockets in other lists
    msock.close()
    print "Done!"
    exit(0)
signal.signal(signal.SIGINT, sigint_handler)

# create server socket
msock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
msock.bind(("", 1024))
print "Successfully binded to:", msock.getsockname()

readable = [msock]
writable = []
errable = []

while 1:
    select.select(
        readable,
        writable,
        errable,
        60)

    # TODO handle socket read either
    #   1. accept() new connection
    #   2. read data from socket
