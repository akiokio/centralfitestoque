# encoding: utf-8
# module UpdateManager.fdsend
# from /usr/lib/python2.7/dist-packages/UpdateManager/fdsend.so
# by generator 1.130
"""
fdsend allows the passing of open files between unrelated processes via
local sockets (using SCM_RIGHTS), a process known as file descriptor
passing.  The following functions are available:

  sendfds()
  recvfds()
  socketpair()

Unlike some other simplifications of the sendmsg()/recvmsg() interface,
fdsend allows multiple files to be transferred in a single operation, and
permits ordinary socket messages to accompany the files.  Additionally,
fdsend understands bona fide Python sockets and files, as well as objects
implementing fileno() methods and integers representing file descriptors.

Errors are raised via the socket.error exception object.
"""
# no imports

# functions

def recvfds(fd, len, flags=0, numfds=64): # real signature unknown; restored from __doc__
    """
    recvfds(fd, len, flags=0, numfds=64) -> (message, fd_tuple)
    
    Receive a message of up to length len and up to numfds new files from socket
    object fd.
    
    Though the socket object may be given as any of the representations listed
    in the module docstring, new files returned in fd_tuple are always integral
    file descriptors.  See os.fdopen for a means of transforming them into
    Python file objects.
    
    There is presently no way to detect msg_flags values (e.g., MSG_CTRUNC).
    """
    pass

def sendfds(fd, msg, flags=0, fds=None): # real signature unknown; restored from __doc__
    """
    sendfds(fd, msg, flags=0, fds=None) -> bytes_sent
    
    Send msg across the socket represented by fd, optionally accompanied by a
    sequence (tuple or list) of open file handles.  For centralfitestoque:
    
      >>> devnull = file("/dev/null")
      >>> sendfds(the_socket, "null device", (devnull,))
    
    The socket fd and members of the fds sequence may be any representation
    described in the module docstring.
    
    Note that most underlying implementations require at least a one byte msg
    to transmit open files.
    """
    pass

def socketpair(family, type, proto=0): # real signature unknown; restored from __doc__
    """
    socketpair(family, type, proto=0) -> (fd, fd)
    
    Provided as a convenience for Python versions lacking a socket.socketpair
    implementation.
    """
    pass

# no classes
