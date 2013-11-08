# encoding: utf-8
# module _dbus_bindings
# from /usr/lib/python2.7/dist-packages/_dbus_bindings.so
# by generator 1.130
"""
Low-level Python bindings for libdbus. Don't use this module directly -
the public API is provided by the `dbus`, `dbus.service`, `dbus.mainloop`
and `dbus.mainloop.glib` modules, with a lower-level API provided by the
`dbus.lowlevel` module.
"""

# imports
import dbus.lowlevel as __dbus_lowlevel


# Variables with simple values

BUS_DAEMON_IFACE = 'org.freedesktop.DBus'
BUS_DAEMON_NAME = 'org.freedesktop.DBus'
BUS_DAEMON_PATH = '/org/freedesktop/DBus'

BUS_SESSION = 0
BUS_STARTER = 2
BUS_SYSTEM = 1

DBUS_INTROSPECT_1_0_XML_DOCTYPE_DECL_NODE = '<!DOCTYPE node PUBLIC "-//freedesktop//DTD D-BUS Object Introspection 1.0//EN"\n"http://www.freedesktop.org/standards/dbus/1.0/introspect.dtd">\n'

DBUS_INTROSPECT_1_0_XML_PUBLIC_IDENTIFIER = '-//freedesktop//DTD D-BUS Object Introspection 1.0//EN'

DBUS_INTROSPECT_1_0_XML_SYSTEM_IDENTIFIER = 'http://www.freedesktop.org/standards/dbus/1.0/introspect.dtd'

DBUS_START_REPLY_ALREADY_RUNNING = 2

DBUS_START_REPLY_SUCCESS = 1

DICT_ENTRY_BEGIN = 123
DICT_ENTRY_END = 125

HANDLER_RESULT_HANDLED = 0

HANDLER_RESULT_NEED_MEMORY = 2

HANDLER_RESULT_NOT_YET_HANDLED = 1

INTROSPECTABLE_IFACE = 'org.freedesktop.DBus.Introspectable'

LOCAL_IFACE = 'org.freedesktop.DBus.Local'
LOCAL_PATH = '/org/freedesktop/DBus/Local'

MESSAGE_TYPE_ERROR = 3
MESSAGE_TYPE_INVALID = 0

MESSAGE_TYPE_METHOD_CALL = 1
MESSAGE_TYPE_METHOD_RETURN = 2

MESSAGE_TYPE_SIGNAL = 4

NAME_FLAG_ALLOW_REPLACEMENT = 1

NAME_FLAG_DO_NOT_QUEUE = 4

NAME_FLAG_REPLACE_EXISTING = 2

PEER_IFACE = 'org.freedesktop.DBus.Peer'

PROPERTIES_IFACE = 'org.freedesktop.DBus.Properties'

RELEASE_NAME_REPLY_NON_EXISTENT = 2

RELEASE_NAME_REPLY_NOT_OWNER = 3

RELEASE_NAME_REPLY_RELEASED = 1

REQUEST_NAME_REPLY_ALREADY_OWNER = 4

REQUEST_NAME_REPLY_EXISTS = 3

REQUEST_NAME_REPLY_IN_QUEUE = 2

REQUEST_NAME_REPLY_PRIMARY_OWNER = 1

STRUCT_BEGIN = 40
STRUCT_END = 41

TYPE_ARRAY = 97
TYPE_BOOLEAN = 98
TYPE_BYTE = 121

TYPE_DICT_ENTRY = 101

TYPE_DOUBLE = 100
TYPE_INT16 = 110
TYPE_INT32 = 105
TYPE_INT64 = 120
TYPE_INVALID = 0

TYPE_OBJECT_PATH = 111

TYPE_SIGNATURE = 103
TYPE_STRING = 115
TYPE_STRUCT = 114
TYPE_UINT16 = 113
TYPE_UINT32 = 117
TYPE_UINT64 = 116

TYPE_UNIX_FD = 104

TYPE_VARIANT = 118

WATCH_ERROR = 4
WATCH_HANGUP = 8
WATCH_READABLE = 1
WATCH_WRITABLE = 2

_python_version = 34013936

__docformat__ = 'restructuredtext'

__version__ = '1.0.0'

# functions

def get_default_main_loop(): # real signature unknown; restored from __doc__
    """
    get_default_main_loop() -> object
    
    Return the global default dbus-python main loop wrapper, which is used
    when no main loop wrapper is passed to the Connection constructor.
    
    If None, there is no default and you should always pass the mainloop
    parameter to the constructor - if you don't, then asynchronous calls,
    connecting to signals and exporting objects will raise an exception.
    There is no default until set_default_main_loop is called.
    """
    return object()

def set_default_main_loop(p_object): # real signature unknown; restored from __doc__
    """
    set_default_main_loop(object)
    
    Change the global default dbus-python main loop wrapper, which is used
    when no main loop wrapper is passed to the Connection constructor.
    
    If None, return to the initial situation: there is no default, and you
    must always pass the mainloop parameter to the constructor.
    
    Two types of main loop wrapper are planned in dbus-python.
    Native main-loop wrappers are instances of `dbus.mainloop.NativeMainLoop`
    supplied by extension modules like `dbus.mainloop.glib`: they have no
    Python API, but connect themselves to ``libdbus`` using native code.
    Python main-loop wrappers are not yet implemented. They will be objects
    supporting the interface defined by `dbus.mainloop.MainLoop`, with an
    API entirely based on Python methods.
    """
    pass

def validate_bus_name(name, allow_unique=True, allow_well_known=True): # real signature unknown; restored from __doc__
    """
    validate_bus_name(name, allow_unique=True, allow_well_known=True)
    
    Raise ValueError if the argument is not a valid bus name.
    
    By default both unique and well-known names are accepted.
    
    :Parameters:
       `name` : str
           The name to be validated
       `allow_unique` : bool
           If False, unique names of the form :1.123 will be rejected
       `allow_well_known` : bool
           If False, well-known names of the form com.centralfitestoque.Foo
           will be rejected
    :Since: 0.80
    """
    pass

def validate_error_name(name): # real signature unknown; restored from __doc__
    """
    validate_error_name(name)
    
    Raise ValueError if the given string is not a valid error name.
    
    :Since: 0.80
    """
    pass

def validate_interface_name(name): # real signature unknown; restored from __doc__
    """
    validate_interface_name(name)
    
    Raise ValueError if the given string is not a valid interface name.
    
    :Since: 0.80
    """
    pass

def validate_member_name(name): # real signature unknown; restored from __doc__
    """
    validate_member_name(name)
    
    Raise ValueError if the argument is not a valid member (signal or method) name.
    
    :Since: 0.80
    """
    pass

def validate_object_path(name): # real signature unknown; restored from __doc__
    """
    validate_object_path(name)
    
    Raise ValueError if the given string is not a valid object path.
    
    :Since: 0.80
    """
    pass

# classes

class Array(list):
    """
    An array of similar items, implemented as a subtype of list.
    
    As currently implemented, an Array behaves just like a list, but
    with the addition of a ``signature`` property set by the constructor;
    conversion of its items to D-Bus types is only done when it's sent in
    a Message. This might change in future so validation is done earlier.
    
    Constructor::
    
        dbus.Array([iterable][, signature][, variant_level])
    
    ``variant_level`` must be non-negative; the default is 0.
    
    ``signature`` is the D-Bus signature string for a single element of the
    array, or None. If not None it must represent a single complete type, the
    type of a single array item; the signature of the whole Array may be
    obtained by prepending ``a`` to the given signature.
    
    If None (the default), when the Array is sent over
    D-Bus, the item signature will be guessed from the first element.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing an array, this is represented in Python by an
        Array with variant_level==2.
    """
    def __init__(self, iterable=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The D-Bus signature of each element of this Array (a Signature instance)"""

    variant_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of nested variants wrapping the real data. 0 if not in a variant."""



class _IntBase(int):
    """
    Base class for int subclasses with a ``variant_level`` attribute.
    Do not rely on the existence of this class outside dbus-python.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    variant_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of nested variants wrapping the real data. 0 if not in a variant."""



class Boolean(_IntBase):
    """
    A boolean, represented as a subtype of `int` (not `bool`, because `bool`
    cannot be subclassed).
    
    Constructor::
    
        dbus.Boolean(value[, variant_level]) -> Boolean
    
    ``value`` is converted to 0 or 1 as if by ``int(bool(value))``.
    
    ``variant_level`` must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing a boolean, this is represented in Python by a
        Boolean with variant_level==2.
    """
    def __init__(self, value, variant_level=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass


class Byte(_IntBase):
    """
    An unsigned byte: a subtype of int, with range restricted to [0, 255].
    
    A Byte b may be converted to a str of length 1 via str(b) == chr(b).
    
    Most of the time you don't want to use this class - it mainly exists
    for symmetry with the other D-Bus types. See `dbus.ByteArray` for a
    better way to handle arrays of Byte.
    
    Constructor::
    
       dbus.Byte(integer or str of length 1[, variant_level])
    
    ``variant_level`` must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing a byte, this is represented in Python by a
        Byte with variant_level==2.
    """
    def __init__(self, integer_or_str_of_length, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass


class _StrBase(str):
    """
    Base class for str subclasses with a ``variant_level`` attribute.
    Do not rely on the existence of this class outside dbus-python.
    """
    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


class ByteArray(_StrBase):
    """
    ByteArray is a subtype of str which can be used when you want an
    efficient immutable representation of a D-Bus byte array (signature 'ay').
    
    By default, when byte arrays are converted from D-Bus to Python, they
    come out as a `dbus.Array` of `dbus.Byte`. This is just for symmetry with
    the other D-Bus types - in practice, what you usually want is the byte
    array represented as a string, using this class. To get this, pass the
    ``byte_arrays=True`` keyword argument to any of these methods:
    
    * any D-Bus method proxy, or ``connect_to_signal``, on the objects returned
      by `Bus.get_object`
    * any D-Bus method on a `dbus.Interface`
    * `dbus.Interface.connect_to_signal`
    * `Bus.add_signal_receiver`
    
    Import via::
    
       from dbus import ByteArray
    
    Constructor::
    
       ByteArray(str)
    """
    def __init__(self, p_str): # real signature unknown; restored from __doc__
        pass


class Connection(object):
    """
    A D-Bus connection.
    
    ::
    
       Connection(address, mainloop=None) -> Connection
    """
    def add_message_filter(self, callable): # real signature unknown; restored from __doc__
        """
        add_message_filter(callable)
        
        Add the given message filter to the internal list.
        
        Filters are handlers that are run on all incoming messages, prior to the
        objects registered to handle object paths.
        
        Filters are run in the order that they were added. The same handler can
        be added as a filter more than once, in which case it will be run more
        than once. Filters added during a filter callback won't be run on the
        message being processed.
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        close()
        
        Close the connection.
        """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """
        flush()
        
        Block until the outgoing message queue is empty.
        """
        pass

    def get_is_authenticated(self): # real signature unknown; restored from __doc__
        """
        get_is_authenticated() -> bool
        
        Return true if this Connection was ever authenticated.
        """
        return False

    def get_is_connected(self): # real signature unknown; restored from __doc__
        """
        get_is_connected() -> bool
        
        Return true if this Connection is connected.
        """
        return False

    def get_peer_unix_process_id(self): # real signature unknown; restored from __doc__
        """
        get_peer_unix_process_id() -> long or None
        
        Get the UNIX process ID at the other end of the connection, if it has been
        authenticated. Return None if this is a non-UNIX platform or the
        connection has not been authenticated.
        """
        return 0

    def get_peer_unix_user(self): # real signature unknown; restored from __doc__
        """
        get_peer_unix_user() -> long or None
        
        Get the UNIX user ID at the other end of the connection, if it has been
        authenticated. Return None if this is a non-UNIX platform or the
        connection has not been authenticated.
        """
        return 0

    def get_unique_name(self): # real signature unknown; restored from __doc__
        """
        get_unique_name() -> str
        
        Return this application's unique name on this bus.
        
        :Raises DBusException: if the connection has no unique name yet
           (for Bus objects this can't happen, for peer-to-peer connections
           this means you haven't called `set_unique_name`)
        """
        return ""

    def get_unix_fd(self): # real signature unknown; restored from __doc__
        """
        get_unix_fd() -> int or None
        
        Get the connection's UNIX file descriptor, if any.
        
        This can be used for SELinux access control checks with ``getpeercon()``
        for centralfitestoque. **Do not** read or write to the file descriptor, or try to
        ``select()`` on it.
        """
        return 0

    def list_exported_child_objects(self, path): # real signature unknown; restored from __doc__
        """
        list_exported_child_objects(path: str) -> list of str
        
        Return a list of the names of objects exported on this Connection as
        direct children of the given object path.
        
        Each name returned may be converted to a valid object path using
        ``dbus.ObjectPath('%s%s%s' % (path, (path != '/' and '/' or ''), name))``.
        For the purposes of this function, every parent or ancestor of an exported
        object is considered to be an exported object, even if it's only an object
        synthesized by the library to support introspection.
        """
        return []

    def remove_message_filter(self, callable): # real signature unknown; restored from __doc__
        """
        remove_message_filter(callable)
        
        Remove the given message filter (see `add_message_filter` for details).
        
        :Raises LookupError:
           The given callable is not among the registered filters
        """
        pass

    def send_message(self, msg): # real signature unknown; restored from __doc__
        """
        send_message(msg) -> long
        
        Queue the given message for sending, and return the message serial number.
        
        :Parameters:
           `msg` : dbus.lowlevel.Message
               The message to be sent.
        """
        return 0

    def send_message_with_reply(self, msg, reply_handler, timeout_s=-1, require_main_loop=False): # real signature unknown; restored from __doc__
        """
        send_message_with_reply(msg, reply_handler, timeout_s=-1, require_main_loop=False) -> dbus.lowlevel.PendingCall
        
        Queue the message for sending; expect a reply via the returned PendingCall,
        which can also be used to cancel the pending call.
        
        :Parameters:
           `msg` : dbus.lowlevel.Message
               The message to be sent
           `reply_handler` : callable
               Asynchronous reply handler: will be called with one positional
               parameter, a Message instance representing the reply.
           `timeout_s` : float
               If the reply takes more than this many seconds, a timeout error
               will be created locally and raised instead. If this timeout is
               negative (default), a sane default (supplied by libdbus) is used.
           `require_main_loop` : bool
               If True, raise RuntimeError if this Connection does not have a main
               loop configured. If False (default) and there is no main loop, you are
               responsible for calling block() on the PendingCall.
        """
        pass

    def send_message_with_reply_and_block(self, msg, timeout_s=-1): # real signature unknown; restored from __doc__
        """
        send_message_with_reply_and_block(msg, timeout_s=-1) -> dbus.lowlevel.Message
        
        Send the message and block while waiting for a reply.
        
        This does not re-enter the main loop, so it can lead to a deadlock, if
        the called method tries to make a synchronous call to a method in this
        application. As such, it's probably a bad idea.
        
        :Parameters:
           `msg` : dbus.lowlevel.Message
               The message to be sent
           `timeout_s` : float
               If the reply takes more than this many seconds, a timeout error
               will be created locally and raised instead. If this timeout is
               negative (default), a sane default (supplied by libdbus) is used.
        :Returns:
           A `dbus.lowlevel.Message` instance (probably a `dbus.lowlevel.MethodReturnMessage`) on success
        :Raises dbus.DBusException:
           On error (including if the reply arrives but is an
           error message)
        """
        pass

    def set_allow_anonymous(self, bool): # real signature unknown; restored from __doc__
        """
        set_allow_anonymous(bool)
        
        Allows anonymous clients. Call this on the server side of a connection in a on_connection_added callback
        """
        pass

    def set_exit_on_disconnect(self, bool): # real signature unknown; restored from __doc__
        """
        set_exit_on_disconnect(bool)
        
        Set whether the C function ``_exit`` will be called when this Connection
        becomes disconnected. This will cause the program to exit without calling
        any cleanup code or exit handlers.
        
        The default is for this feature to be disabled for Connections and enabled
        for Buses.
        """
        pass

    def set_unique_name(self, p_str): # real signature unknown; restored from __doc__
        """
        set_unique_name(str)
        
        Set this application's unique name on this bus. Raise ValueError if it has
        already been set.
        """
        pass

    @classmethod
    def _new_for_bus(cls, address_or_int=None): # real signature unknown; restored from __doc__
        """
        Connection._new_for_bus([address: str or int]) -> Connection
        
        If the address is an int it must be one of the constants BUS_SESSION,
        BUS_SYSTEM, BUS_STARTER; if a string, it must be a D-Bus address.
        The default is BUS_SESSION.
        """
        return Connection

    def _register_object_path(self, *args, **kwargs): # real signature unknown
        """
        register_object_path(path, on_message, on_unregister=None, fallback=False)
        
        Register a callback to be called when messages arrive at the given
        object-path. Used to export objects' methods on the bus in a low-level
        way. For the high-level interface to this functionality (usually
        recommended) see the `dbus.service.Object` base class.
        
        :Parameters:
           `path` : str
               Object path to be acted on
           `on_message` : callable
               Called when a message arrives at the given object-path, with
               two positional parameters: the first is this Connection,
               the second is the incoming `dbus.lowlevel.Message`.
           `on_unregister` : callable or None
               If not None, called when the callback is unregistered.
           `fallback` : bool
               If True (the default is False), when a message arrives for a
               'subdirectory' of the given path and there is no more specific
               handler, use this handler. Normally this handler is only run if
               the paths match exactly.
        """
        pass

    def _require_main_loop(self): # real signature unknown; restored from __doc__
        """
        _require_main_loop()
        
        Raise an exception if this Connection is not bound to any main loop -
        in this state, asynchronous calls, receiving signals and exporting objects
        will not work.
        
        `dbus.mainloop.NULL_MAIN_LOOP` is treated like a valid main loop - if you're
        using that, you presumably know what you're doing.
        """
        pass

    def _unregister_object_path(self, *args, **kwargs): # real signature unknown
        """
        unregister_object_path(path)
        
        Remove a previously registered handler for the given object path.
        
        :Parameters:
           `path` : str
               The object path whose handler is to be removed
        :Raises KeyError: if there is no handler registered for exactly that
           object path.
        """
        pass

    def __init__(self, address, mainloop=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Dictionary(dict):
    """
    An mapping whose keys are similar and whose values are similar,
    implemented as a subtype of dict.
    
    As currently implemented, a Dictionary behaves just like a dict, but
    with the addition of a ``signature`` property set by the constructor;
    conversion of its items to D-Bus types is only done when it's sent in
    a Message. This may change in future so validation is done earlier.
    
    Constructor::
    
        Dictionary(mapping_or_iterable=(), signature=None, variant_level=0)
    
    ``variant_level`` must be non-negative; the default is 0.
    
    ``signature`` is either a string or None. If a string, it must consist
    of exactly two complete type signatures, representing the 'key' type
    (which must be a primitive type, i.e. one of "bdginoqstuxy")
    and the 'value' type. The signature of the whole Dictionary will be
    ``a{xx}`` where ``xx`` is replaced by the given signature.
    
    If it is None (the default), when the Dictionary is sent over
    D-Bus, the key and value signatures will be guessed from an arbitrary
    element of the Dictionary.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing an array of DICT_ENTRY, this is represented in
        Python by a Dictionary with variant_level==2.
    """
    def __init__(self, mapping_or_iterable=(), signature=None, variant_level=0): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The D-Bus signature of each key in this Dictionary, followed by that of each value in this Dictionary, as a Signature instance."""

    variant_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of nested variants wrapping the real data. 0 if not in a variant."""



class _FloatBase(float):
    """
    Base class for float subclasses with a ``variant_level`` attribute.
    Do not rely on the existence of this class outside dbus-python.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    variant_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of nested variants wrapping the real data. 0 if not in a variant."""



class Double(_FloatBase):
    """ A double-precision floating point number (a subtype of float). """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Message(object):
    """ A message to be sent or received over a D-Bus Connection. """
    def append(self, *args, **kwargs): # real signature unknown
        """
        set_args(*args[, **kwargs])
        
        Set the message's arguments from the positional parameter, according to
        the signature given by the ``signature`` keyword parameter.
        
        The following type conversions are supported:
        
        =============================== ===========================
        D-Bus (in signature)            Python
        =============================== ===========================
        boolean (b)                     any object (via bool())
        byte (y)                        string of length 1
                                        any integer
        any integer type                any integer
        double (d)                      any float
        object path                     anything with a __dbus_object_path__ attribute
        string, signature, object path  str (must be UTF-8) or unicode
        dict (a{...})                   any mapping
        array (a...)                    any iterable over appropriate objects
        struct ((...))                  any iterable over appropriate objects
        variant                         any object above (guess type as below)
        =============================== ===========================
        
        Here 'any integer' means anything on which int() or long()
        (as appropriate) will work, except for basestring subclasses.
        'Any float' means anything on which float() will work, except
        for basestring subclasses.
        
        If there is no signature, guess from the arguments using
        the static method `Message.guess_signature`.
        """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """
        message.copy() -> Message (or subclass)
        Deep-copy the message, resetting the serial number to zero.
        """
        return Message

    def get_args_list(self, **kwargs): # real signature unknown; restored from __doc__
        """
        get_args_list(**kwargs) -> list
        
        Return the message's arguments. Keyword arguments control the translation
        of D-Bus types to Python:
        
        :Keywords:
           `byte_arrays` : bool
               If true, convert arrays of byte (signature 'ay') into dbus.ByteArray,
               a str subclass. In practice, this is usually what you want, but
               it's off by default for consistency.
        
               If false (default), convert them into a dbus.Array of Bytes.
           `utf8_strings` : bool
               If true, return D-Bus strings as Python 8-bit strings (of UTF-8).
               If false (default), return D-Bus strings as Python unicode objects.
        
        Most of the type mappings should be fairly obvious:
        
        ===============  ===================================================
        D-Bus            Python
        ===============  ===================================================
        byte (y)         dbus.Byte (int subclass)
        bool (b)         dbus.Boolean (int subclass)
        Signature (g)    dbus.Signature (str subclass)
        intNN, uintNN    dbus.IntNN, dbus.UIntNN (int or long subclasses)
        double (d)       dbus.Double
        string (s)       dbus.String (unicode subclass)
                         (or dbus.UTF8String, str subclass, if utf8_strings set)
        Object path (o)  dbus.ObjectPath (str subclass)
        dict (a{...})    dbus.Dictionary
        array (a...)     dbus.Array (list subclass) containing appropriate types
        byte array (ay)  dbus.ByteArray (str subclass) if byte_arrays set; or
                         list of Byte
        struct ((...))   dbus.Struct (tuple subclass) of appropriate types
        variant (v)      contained type, but with variant_level > 0
        ===============  ===================================================
        """
        return []

    def get_auto_start(self): # real signature unknown; restored from __doc__
        """
        message.get_auto_start() -> bool
        Return true if this message will cause an owner for the destination name
        to be auto-started.
        """
        return False

    def get_destination(self): # real signature unknown; restored from __doc__
        """
        get_destination() -> str or None
        
        Return the message's destination bus name, or None if none.
        """
        return ""

    def get_error_name(self): # real signature unknown; restored from __doc__
        """ get_error_name() -> str or None """
        return ""

    def get_interface(self): # real signature unknown; restored from __doc__
        """ get_interface() -> str or None """
        return ""

    def get_member(self): # real signature unknown; restored from __doc__
        """ get_member() -> str or None """
        return ""

    def get_no_reply(self): # real signature unknown; restored from __doc__
        """
        message.get_no_reply() -> bool
        Return true if this message need not be replied to.
        """
        return False

    def get_path(self): # real signature unknown; restored from __doc__
        """
        get_path() -> ObjectPath or None
        
        Return the message's destination object path (if it's a method call) or
        source object path (if it's a method reply or a signal) or None (if it
        has no path).
        """
        return ObjectPath

    def get_path_decomposed(self): # real signature unknown; restored from __doc__
        """
        get_path_decomposed() -> list of str, or None
        
        Return a list of path components (e.g. /foo/bar -> ['foo','bar'], / -> [])
        or None if the message has no associated path.
        """
        return []

    def get_reply_serial(self): # real signature unknown; restored from __doc__
        """
        message.get_reply_serial() -> long
        Returns the serial that the message is a reply to or 0 if none.
        """
        return 0

    def get_sender(self): # real signature unknown; restored from __doc__
        """
        get_sender() -> str or None
        
        Return the message's sender unique name, or None if none.
        """
        return ""

    def get_serial(self): # real signature unknown; restored from __doc__
        """
        message.get_serial() -> long
        Returns the serial of a message or 0 if none has been specified.
        
        The message's serial number is provided by the application sending the
        message and is used to identify replies to this message. All messages
        received on a connection will have a serial, but messages you haven't
        sent yet may return 0.
        """
        return 0

    def get_signature(self): # real signature unknown; restored from __doc__
        """ get_signature() -> Signature or None """
        return Signature

    def get_type(self): # real signature unknown; restored from __doc__
        """
        message.get_type() -> int
        
        Returns the type of the message.
        """
        return 0

    def guess_signature(self, *args): # real signature unknown; restored from __doc__
        """
        guess_signature(*args) -> Signature [static method]
        
        Guess a D-Bus signature which should be used to encode the given
        Python objects.
        
        The signature is constructed as follows:
        
        +-------------------------------+---------------------------+
        |Python                         |D-Bus                      |
        +===============================+===========================+
        |D-Bus type, variant_level > 0  |variant (v)                |
        +-------------------------------+---------------------------+
        |D-Bus type, variant_level == 0 |the corresponding type     |
        +-------------------------------+---------------------------+
        |anything with a                |object path                |
        |__dbus_object_path__ attribute |                           |
        +-------------------------------+---------------------------+
        |bool                           |boolean (y)                |
        +-------------------------------+---------------------------+
        |any other int subclass         |int32 (i)                  |
        +-------------------------------+---------------------------+
        |any other long subclass        |int64 (x)                  |
        +-------------------------------+---------------------------+
        |any other float subclass       |double (d)                 |
        +-------------------------------+---------------------------+
        |any other str subclass         |string (s)                 |
        +-------------------------------+---------------------------+
        |any other unicode subclass     |string (s)                 |
        +-------------------------------+---------------------------+
        |any other tuple subclass       |struct ((...))             |
        +-------------------------------+---------------------------+
        |any other list subclass        |array (a...), guess        |
        |                               |contents' type according to|
        |                               |type of first item         |
        +-------------------------------+---------------------------+
        |any other dict subclass        |dict (a{...}), guess key,  |
        |                               |value type according to    |
        |                               |types for an arbitrary item|
        +-------------------------------+---------------------------+
        |anything else                  |raise TypeError            |
        +-------------------------------+---------------------------+
        """
        return Signature

    def has_destination(self, bus_name): # real signature unknown; restored from __doc__
        """ has_destination(bus_name: str) -> bool """
        return False

    def has_interface(self, interface_or_None): # real signature unknown; restored from __doc__
        """ has_interface(interface: str or None) -> bool """
        return False

    def has_member(self, name_or_None): # real signature unknown; restored from __doc__
        """ has_member(name: str or None) -> bool """
        return False

    def has_path(self, name_or_None): # real signature unknown; restored from __doc__
        """ has_path(name: str or None) -> bool """
        return False

    def has_sender(self, unique_name): # real signature unknown; restored from __doc__
        """ has_sender(unique_name: str) -> bool """
        return False

    def has_signature(self, signature): # real signature unknown; restored from __doc__
        """ has_signature(signature: str) -> bool """
        return False

    def is_error(self, error): # real signature unknown; restored from __doc__
        """ is_error(error: str) -> bool """
        return False

    def is_method_call(self, interface, member): # real signature unknown; restored from __doc__
        """ is_method_call(interface: str, member: str) -> bool """
        return False

    def is_signal(self, interface, member): # real signature unknown; restored from __doc__
        """ is_signal(interface: str, member: str) -> bool """
        return False

    def set_auto_start(self, bool): # real signature unknown; restored from __doc__
        """
        message.set_auto_start(bool) -> None
        Set whether this message will cause an owner for the destination name
        to be auto-started.
        """
        pass

    def set_destination(self, bus_name_or_None): # real signature unknown; restored from __doc__
        """ set_destination(bus_name: str or None) """
        pass

    def set_error_name(self, name_or_None): # real signature unknown; restored from __doc__
        """ set_error_name(name: str or None) """
        pass

    def set_interface(self, name_or_None): # real signature unknown; restored from __doc__
        """ set_interface(name: str or None) """
        pass

    def set_member(self, unique_name_or_None): # real signature unknown; restored from __doc__
        """ set_member(unique_name: str or None) """
        pass

    def set_no_reply(self, bool): # real signature unknown; restored from __doc__
        """
        message.set_no_reply(bool) -> None
        Set whether no reply to this message is required.
        """
        pass

    def set_path(self, name_or_None): # real signature unknown; restored from __doc__
        """ set_path(name: str or None) """
        pass

    def set_reply_serial(self, bool): # real signature unknown; restored from __doc__
        """
        message.set_reply_serial(bool) -> None
        Set the serial that this message is a reply to.
        """
        pass

    def set_sender(self, unique_name_or_None): # real signature unknown; restored from __doc__
        """ set_sender(unique_name: str or None) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class ErrorMessage(__dbus_lowlevel.Message):
    """
    An error message.
    
    Constructor::
    
       dbus.lowlevel.ErrorMessage(reply_to: Message, error_name: str,
                                  error_message: str or None)
    """
    def __init__(self, reply_to, error_name, error_message_or_None): # real signature unknown; restored from __doc__
        pass


class Int16(_IntBase):
    """
    A signed 16-bit integer between -0x8000 and +0x7FFF, represented as
    a subtype of `int`.
    
    Constructor::
    
        dbus.Int16(value: int[, variant_level: int]) -> Int16
    
    value must be within the allowed range, or OverflowError will be
    raised.
    
        variant_level must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing an int16, this is represented in Python by an
        Int16 with variant_level==2.
    """
    def __init__(self, value, variant_level=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Int32(_IntBase):
    """
    A signed 32-bit integer between -0x8000 0000 and +0x7FFF FFFF, represented as
    a subtype of `int`.
    
    Constructor::
    
        dbus.Int32(value: int[, variant_level: int]) -> Int32
    
    ``value`` must be within the allowed range, or `OverflowError` will be
    raised.
    
    ``variant_level`` must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing an int32, this is represented in Python by an
        Int32 with variant_level==2.
    """
    def __init__(self, value, variant_level=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class _LongBase(long):
    """
    Base class for ``long`` subclasses with a ``variant_level`` attribute.
    Do not rely on the existence of this class outside dbus-python.
    """
    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


class Int64(_LongBase):
    """
    A signed 64-bit integer between -0x8000 0000 0000 0000 and
    +0x7FFF FFFF FFFF FFFF, represented as a subtype of `long`.
    
    Note that this may be changed in future to be a subtype of `int` on
    64-bit platforms; applications should not rely on either behaviour.
    
    This type only works on platforms where the C compiler has suitable
    64-bit types, such as C99 ``long long``.
    
    Constructor::
    
        dbus.Int64(value: long[, variant_level: int]) -> Int64
    
    ``value`` must be within the allowed range, or `OverflowError` will be
    raised.
    
    ``variant_level`` must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing an int64, this is represented in Python by an
        Int64 with variant_level==2.
    """
    def __init__(self, value, variant_level=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class MethodCallMessage(__dbus_lowlevel.Message):
    """
    A method-call message.
    
    Constructor::
    
        dbus.lowlevel.MethodCallMessage(destination: str or None, path: str,
                                        interface: str or None, method: str)
    
    ``destination`` is the destination bus name, or None to send the
    message directly to the peer (usually the bus daemon).
    
    ``path`` is the object-path of the object whose method is to be called.
    
    ``interface`` is the interface qualifying the method name, or None to omit
    the interface from the message header.
    
    ``method`` is the method name (member name).
    """
    def __init__(self, destination_or_None, path, interface_or_None, method): # real signature unknown; restored from __doc__
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass


class MethodReturnMessage(__dbus_lowlevel.Message):
    """
    A method-return message.
    
    Constructor::
    
        dbus.lowlevel.MethodReturnMessage(method_call: MethodCallMessage)
    """
    def __init__(self, method_call): # real signature unknown; restored from __doc__
        pass


class NativeMainLoop(object):
    """
    Object representing D-Bus main loop integration done in native code.
    Cannot be instantiated directly.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ObjectPath(_StrBase):
    """
    A D-Bus object path, such as '/com/centralfitestoque/MyApp/Documents/abc'.
    
    ObjectPath is a subtype of str, and object-paths behave like strings.
    
    Constructor::
    
        dbus.ObjectPath(path: str, variant_level: int) -> ObjectPath
    
    path must be an ASCII string following the syntax of object paths.
    variant_level must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing an object path, this is represented in Python by an
        ObjectPath with variant_level==2.
    """
    def __init__(self, path, variant_level): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class PendingCall(object):
    """
    Object representing a pending D-Bus call, returned by
    Connection.send_message_with_reply(). Cannot be instantiated directly.
    """
    def block(self): # real signature unknown; restored from __doc__
        """
        block()
        
        Block until this pending call has completed and the associated
        reply handler has been called.
        
        This can lead to a deadlock, if the called method tries to make a
        synchronous call to a method in this application.
        """
        pass

    def cancel(self): # real signature unknown; restored from __doc__
        """
        cancel()
        
        Cancel this pending call. Its reply will be ignored and the associated
        reply handler will never be called.
        """
        pass

    def get_completed(self): # real signature unknown; restored from __doc__
        """
        get_completed() -> bool
        
        Return true if this pending call has completed.
        
        If so, its associated reply handler has been called and it is no
        longer meaningful to cancel it.
        """
        return False

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class SignalMessage(__dbus_lowlevel.Message):
    """
    A signal message.
    
    Constructor::
    
       dbus.lowlevel.SignalMessage(path: str, interface: str, method: str)
    """
    def __init__(self, path, interface, method): # real signature unknown; restored from __doc__
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass


class Signature(_StrBase):
    """
    A string subclass whose values are restricted to valid D-Bus
    signatures. When iterated over, instead of individual characters it
    produces Signature instances representing single complete types.
    
    Constructor::
    
        ``Signature(value: str or unicode[, variant_level: int]) -> Signature``
    
    ``value`` must be a valid D-Bus signature (zero or more single complete
    types).
    
    ``variant_level`` must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing a signature, this is represented in Python by a
        Signature with variant_level==2.
    """
    def __init__(self, value_or_unicode, variant_level=None): # real signature unknown; restored from __doc__
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class String(unicode):
    """
    A string represented using Unicode - a subtype of `unicode`.
    
    All strings on D-Bus are required to be valid Unicode; in the "wire
    protocol" they're transported as UTF-8.
    
    By default, when strings are converted from D-Bus to Python, they
    come out as this class. If you prefer to get UTF-8 strings (as instances
    of a subtype of `str`) or you want to avoid the conversion overhead of
    going from UTF-8 to Python's internal Unicode representation, see the
    documentation for `dbus.UTF8String`.
    
    Constructor::
    
        String(value: str or unicode[, variant_level: int]) -> String
    
    variant_level must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing a string, this is represented in Python by a
        String or UTF8String with variant_level==2.
    """
    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, value_or_unicode, variant_level=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    variant_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of nested variants wrapping the real data. 0 if not in a variant"""



class Struct(tuple):
    """
    An structure containing items of possibly distinct types.
    
    Constructor::
    
        dbus.Struct(iterable, signature=None, variant_level=0) -> Struct
    
    D-Bus structs may not be empty, so the iterable argument is required and
    may not be an empty iterable.
    
    ``signature`` is either None, or a string representing the contents of the
    struct as one or more complete type signatures. The overall signature of
    the struct will be the given signature enclosed in parentheses, ``()``.
    
    If the signature is None (default) it will be guessed
    from the types of the items during construction.
    
    ``variant_level`` must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing a struct, this is represented in Python by a
        Struct with variant_level==2.
    """
    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, iterable, signature=None, variant_level=0): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


class UInt16(_IntBase):
    """
    An unsigned 16-bit integer between 0 and 0xFFFF, represented as
    a subtype of `int`.
    
    Constructor::
    
        dbus.UInt16(value: int[, variant_level: int]) -> UInt16
    
    ``value`` must be within the allowed range, or `OverflowError` will be
    raised.
    
    ``variant_level`` must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing a uint16, this is represented in Python by a
        UInt16 with variant_level==2.
    """
    def __init__(self, value, variant_level=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class UInt32(_LongBase):
    """
    An unsigned 32-bit integer between 0 and 0xFFFF FFFF, represented as a
    subtype of `long`.
    
    Note that this may be changed in future to be a subtype of `int` on
    64-bit platforms; applications should not rely on either behaviour.
    
    Constructor::
    
        dbus.UInt32(value: long[, variant_level: int]) -> UInt32
    
    ``value`` must be within the allowed range, or `OverflowError` will be
    raised.
    
    ``variant_level`` must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing a uint32, this is represented in Python by a
        UInt32 with variant_level==2.
    """
    def __init__(self, value, variant_level=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class UInt64(_LongBase):
    """
    An unsigned 64-bit integer between 0 and 0xFFFF FFFF FFFF FFFF,
    represented as a subtype of `long`.
    
    This type only exists on platforms where the C compiler has suitable
    64-bit types, such as C99 ``unsigned long long``.
    
    Constructor::
    
        dbus.UInt64(value: long[, variant_level: int]) -> UInt64
    
    ``value`` must be within the allowed range, or `OverflowError` will be
    raised.
    
    ``variant_level`` must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing a uint64, this is represented in Python by a
        UInt64 with variant_level==2.
    """
    def __init__(self, value, variant_level=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class UnixFd(object):
    """
    An Unix Fd.
    
    Constructor::
    
        dbus.UnixFd(value: int or file object[, variant_level: int]) -> UnixFd
    
    ``value`` must be the integer value of a file descriptor, or an object that
    implements the fileno() method. Otherwise, `ValueError` will be
    raised.
    
    UnixFd keeps a dup() (duplicate) of the supplied file descriptor. The
    caller remains responsible for closing the original fd.
    
    ``variant_level`` must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing an Unix Fd, this is represented in Python by an
        Unix Fd with variant_level==2.
    """
    def take(self): # real signature unknown; restored from __doc__
        """
        take() -> int
        
        This method returns the file descriptor owned by UnixFd object.
        Note that, once this method is called, closing the file descriptor is
        the caller's responsibility.
        
        This method may be called at most once; UnixFd 'forgets' the file
        descriptor after it is taken.
        
        :Raises ValueError: if this method has already been called
        """
        return 0

    def __init__(self, value_or_file_object, variant_level=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class UTF8String(_StrBase):
    """
    A string represented using UTF-8 - a subtype of `str`.
    
    All strings on D-Bus are required to be valid Unicode; in the "wire
    protocol" they're transported as UTF-8.
    
    By default, when byte arrays are converted from D-Bus to Python, they
    come out as a `dbus.String`, which is a subtype of `unicode`.
    If you prefer to get UTF-8 strings (as instances of this class) or you
    want to avoid the conversion overhead of going from UTF-8 to Python's
    internal Unicode representation, you can pass the ``utf8_strings=True``
    keyword argument to any of these methods:
    
    * any D-Bus method proxy, or ``connect_to_signal``, on the objects returned
      by `Bus.get_object`
    * any D-Bus method on a `dbus.Interface`
    * `dbus.Interface.connect_to_signal`
    * `Bus.add_signal_receiver`
    
    
    Constructor::
    
        dbus.UTF8String(value: str or unicode[, variant_level: int]) -> UTF8String
    
    If value is a str object it must be valid UTF-8.
    
    variant_level must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing a string, this is represented in Python by a
        String or UTF8String with variant_level==2.
    :Since: 0.80 (in older versions, use dbus.String)
    """
    def __init__(self, value_or_unicode, variant_level=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class _LibDBusConnection(object):
    """
    A reference to a ``DBusConnection`` from ``libdbus``, which might not
    have been attached to a `dbus.connection.Connection` yet.
    
    Cannot be instantiated from Python. The only use of this object is to
    pass it to the ``dbus.connection.Connection`` constructor instead of an
    address.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class _Server(object):
    """
    A D-Bus server.
    
    ::
    
       Server(address, connection_subtype, mainloop=None, auth_mechanisms=None)
         -> Server
    """
    def disconnect(self): # real signature unknown; restored from __doc__
        """
        disconnect()
        
        Releases the server's address and stops listening for new clients.
        
        If called more than once, only the first call has an effect.
        """
        pass

    def get_address(self): # real signature unknown; restored from __doc__
        """
        get_address() -> str
        
        Returns the address of the server.
        """
        return ""

    def get_id(self): # real signature unknown; restored from __doc__
        """
        get_id() -> str
        
        Returns the unique ID of the server.
        """
        return ""

    def get_is_connected(self): # real signature unknown; restored from __doc__
        """
        get_is_connected() -> bool
        
        Return true if this Server is still listening for new connections.
        """
        return False

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class _SignatureIter(object):
    # no doc
    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass


# variables with complex values

NULL_MAIN_LOOP = None # (!) real value is ''

_C_API = None # (!) real value is ''

