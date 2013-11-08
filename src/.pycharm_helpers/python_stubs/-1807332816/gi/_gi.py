# encoding: utf-8
# module gi._gi
# from /usr/lib/python2.7/dist-packages/gi/_gi.so
# by generator 1.130
# no doc

# imports
import gi as __gi
import gobject as __gobject


# functions

def enum_add(*args, **kwargs): # real signature unknown
    pass

def enum_register_new_gtype_and_add(*args, **kwargs): # real signature unknown
    pass

def flags_add(*args, **kwargs): # real signature unknown
    pass

def flags_register_new_gtype_and_add(*args, **kwargs): # real signature unknown
    pass

def hook_up_vfunc_implementation(*args, **kwargs): # real signature unknown
    pass

def register_interface_info(*args, **kwargs): # real signature unknown
    pass

def variant_new_tuple(*args, **kwargs): # real signature unknown
    pass

def variant_type_from_string(*args, **kwargs): # real signature unknown
    pass

# classes

class BaseInfo(object):
    # no doc
    def get_container(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_namespace(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass


class ArgInfo(__gi.BaseInfo):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Boxed(__gobject.GBoxed):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class BoxedInfo(__gi.BaseInfo):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class CallableInfo(__gi.BaseInfo):
    # no doc
    def get_arguments(self, *args, **kwargs): # real signature unknown
        pass

    def invoke(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class CallbackInfo(__gi.BaseInfo):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ConstantInfo(__gi.BaseInfo):
    # no doc
    def get_value(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class RegisteredTypeInfo(__gi.BaseInfo):
    # no doc
    def get_g_type(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class EnumInfo(__gi.RegisteredTypeInfo):
    # no doc
    def get_values(self, *args, **kwargs): # real signature unknown
        pass

    def is_flags(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ErrorDomainInfo(__gi.BaseInfo):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class FieldInfo(__gi.BaseInfo):
    # no doc
    def get_value(self, *args, **kwargs): # real signature unknown
        pass

    def set_value(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class FunctionInfo(__gi.CallableInfo):
    # no doc
    def is_constructor(self, *args, **kwargs): # real signature unknown
        pass

    def is_method(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class InterfaceInfo(__gi.RegisteredTypeInfo):
    # no doc
    def get_constants(self, *args, **kwargs): # real signature unknown
        pass

    def get_methods(self, *args, **kwargs): # real signature unknown
        pass

    def get_vfuncs(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ObjectInfo(__gi.RegisteredTypeInfo):
    # no doc
    def get_constants(self, *args, **kwargs): # real signature unknown
        pass

    def get_fields(self, *args, **kwargs): # real signature unknown
        pass

    def get_interfaces(self, *args, **kwargs): # real signature unknown
        pass

    def get_methods(self, *args, **kwargs): # real signature unknown
        pass

    def get_parent(self, *args, **kwargs): # real signature unknown
        pass

    def get_vfuncs(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class PropertyInfo(__gi.BaseInfo):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Repository(object):
    # no doc
    def enumerate_versions(self, *args, **kwargs): # real signature unknown
        pass

    def find_by_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_default(self, *args, **kwargs): # real signature unknown
        pass

    def get_infos(self, *args, **kwargs): # real signature unknown
        pass

    def get_loaded_namespaces(self, *args, **kwargs): # real signature unknown
        pass

    def get_typelib_path(self, *args, **kwargs): # real signature unknown
        pass

    def get_version(self, *args, **kwargs): # real signature unknown
        pass

    def require(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class RepositoryError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class SignalInfo(__gi.BaseInfo):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Struct(__gobject.GPointer):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class StructInfo(__gi.RegisteredTypeInfo):
    # no doc
    def get_fields(self, *args, **kwargs): # real signature unknown
        pass

    def get_methods(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class TypeInfo(__gi.BaseInfo):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class UnionInfo(__gi.RegisteredTypeInfo):
    # no doc
    def get_fields(self, *args, **kwargs): # real signature unknown
        pass

    def get_methods(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class UnresolvedInfo(__gi.BaseInfo):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ValueInfo(__gi.BaseInfo):
    # no doc
    def get_value(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class VFuncInfo(__gi.CallableInfo):
    # no doc
    def get_invoker(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

_API = None # (!) real value is ''

