# encoding: utf-8
# module apt_pkg
# from /usr/lib/python2.7/dist-packages/apt_pkg.so
# by generator 1.130
"""
Classes and functions wrapping the apt-pkg library.

The apt_pkg module provides several classes and functions for accessing
the functionality provided by the apt-pkg library. Typical uses might
include reading APT index files and configuration files and installing
or removing packages.
"""
# no imports

# Variables with simple values

CurStateConfigFiles = 5
CurStateHalfConfigured = 2
CurStateHalfInstalled = 4
CurStateInstalled = 6
CurStateNotInstalled = 0
CurStateUnPacked = 1

CURSTATE_CONFIG_FILES = 5

CURSTATE_HALF_CONFIGURED = 2
CURSTATE_HALF_INSTALLED = 4

CURSTATE_INSTALLED = 6

CURSTATE_NOT_INSTALLED = 0

CURSTATE_UNPACKED = 1

DATE = 'Apr 18 2012'

Date = 'Apr 18 2012'

InstStateHold = 2
InstStateHoldReInstReq = 3
InstStateOk = 0
InstStateReInstReq = 1

INSTSTATE_HOLD = 2

INSTSTATE_HOLD_REINSTREQ = 3

INSTSTATE_OK = 0
INSTSTATE_REINSTREQ = 1

LibVersion = '4.12.0'

LIB_VERSION = '4.12.0'

PriExtra = 5
PriImportant = 1
PriOptional = 4
PriRequired = 2
PriStandard = 3

PRI_EXTRA = 5
PRI_IMPORTANT = 1
PRI_OPTIONAL = 4
PRI_REQUIRED = 2
PRI_STANDARD = 3

SelStateDeInstall = 3
SelStateHold = 2
SelStateInstall = 1
SelStatePurge = 4
SelStateUnknown = 0

SELSTATE_DEINSTALL = 3
SELSTATE_HOLD = 2
SELSTATE_INSTALL = 1
SELSTATE_PURGE = 4
SELSTATE_UNKNOWN = 0

Time = '08:46:13'

TIME = '08:46:13'

VERSION = '0.8.16~exp12ubuntu10'

_COMPAT_0_7 = 1

# functions

def Base64Encode(String): # real signature unknown; restored from __doc__
    """ Base64Encode(String) -> String """
    return ""

def base64_encode(value): # real signature unknown; restored from __doc__
    """
    base64_encode(value: bytes) -> str
    
    Encode the given bytestring into Base64. The input may not
    contain a null byte character (use the base64 module for this).
    """
    return ""

def CheckDep(PkgVer, DepOp, DepVer): # real signature unknown; restored from __doc__
    """ CheckDep(PkgVer,DepOp,DepVer) -> bool """
    return False

def CheckDomainList(String, String_1): # real signature unknown; restored from __doc__
    """ CheckDomainList(String,String) -> Bool """
    return False

def check_dep(pkg_ver, dep_op, dep_ver): # real signature unknown; restored from __doc__
    """
    check_dep(pkg_ver: str, dep_op: str, dep_ver: str) -> bool
    
    Check that the given requirement is fulfilled; i.e. that the version
    string given by 'pkg_ver' matches the version string 'dep_ver' under
    the condition specified by the operator 'dep_op' (<,<=,=,>=,>).
    
    Return True if 'pkg_ver' matches 'dep_ver' under the
    condition 'dep_op'; for centralfitestoque, this returns True:
    
        apt_pkg.check_dep('1', '<=', '2')
    """
    return False

def check_domain_list(host, domains): # real signature unknown; restored from __doc__
    """
    check_domain_list(host: str, domains: str) -> bool
    
    Check if the host given by 'host' belongs to one of the domains
    specified in the comma separated string 'domains'. An centralfitestoque
    would be:
    
        check_domain_list('alioth.debian.org','debian.net,debian.org')
    
    which would return True because alioth belongs to debian.org.
    """
    return False

def DeQuoteString(String): # real signature unknown; restored from __doc__
    """ DeQuoteString(String) -> String """
    return ""

def dequote_string(string): # real signature unknown; restored from __doc__
    """
    dequote_string(string: str) -> str
    
    Dequote the given string by replacing all HTTP encoded values such
    as '%20' with their decoded value (in this case, ' ').
    """
    return ""

def GetAcquire(): # real signature unknown; restored from __doc__
    """ GetAcquire() -> Acquire """
    return Acquire

def GetCache(): # real signature unknown; restored from __doc__
    """ GetCache() -> PkgCache """
    pass

def GetCdrom(): # real signature unknown; restored from __doc__
    """ GetCdrom() -> Cdrom """
    return Cdrom

def GetDepCache(Cache): # real signature unknown; restored from __doc__
    """ GetDepCache(Cache) -> DepCache """
    return DepCache

def GetLock(*args, **kwargs): # real signature unknown
    """
    get_lock(file: str, errors: bool) -> int
    
    Create an empty file of the given name and lock it. If the locking
    succeeds, return the file descriptor of the lock file. Afterwards,
    locking the file from another process will fail and thus cause
    get_lock() to return -1 or raise an Error (if 'errors' is True).
    
    From Python 2.6 on, it is recommended to use the context manager
    provided by apt_pkg.FileLock instead using the with-statement.
    """
    pass

def GetPackageManager(DepCache): # real signature unknown; restored from __doc__
    """ GetPackageManager(DepCache) -> PackageManager """
    return PackageManager

def GetPkgAcqFile(pkgAquire, uri, md5=None, size=None, descr=None, shortDescr=None, destDir=None, destFile=None): # real signature unknown; restored from __doc__
    """ GetPkgAcqFile(pkgAquire, uri[, md5, size, descr, shortDescr, destDir, destFile]) -> PkgAcqFile """
    pass

def GetPkgActionGroup(DepCache): # real signature unknown; restored from __doc__
    """ GetPkgActionGroup(DepCache) -> PkgActionGroup """
    pass

def GetPkgProblemResolver(*args, **kwargs): # real signature unknown
    """ GetDepProblemResolver(DepCache) -> PkgProblemResolver """
    pass

def GetPkgRecords(Cache): # real signature unknown; restored from __doc__
    """ GetPkgRecords(Cache) -> PkgRecords """
    pass

def GetPkgSourceList(): # real signature unknown; restored from __doc__
    """ GetPkgSourceList() -> PkgSourceList """
    pass

def GetPkgSrcRecords(): # real signature unknown; restored from __doc__
    """ GetPkgSrcRecords() -> PkgSrcRecords """
    pass

def gettext(msg, domain='python-apt'): # real signature unknown; restored from __doc__
    """
    gettext(msg: str[, domain: str = 'python-apt']) -> str
    
    Translate the given string. This is much faster than Python's version
    and only does translations after setlocale() has been called.
    """
    return ""

def get_architectures(): # real signature unknown; restored from __doc__
    """
    get_architectures() -> list
    
    Return the list of supported architectures on this system. On a 
    multiarch system this can be more than one. The main architectures
    is the first item in the list.
    """
    return []

def get_lock(file, errors): # real signature unknown; restored from __doc__
    """
    get_lock(file: str, errors: bool) -> int
    
    Create an empty file of the given name and lock it. If the locking
    succeeds, return the file descriptor of the lock file. Afterwards,
    locking the file from another process will fail and thus cause
    get_lock() to return -1 or raise an Error (if 'errors' is True).
    
    From Python 2.6 on, it is recommended to use the context manager
    provided by apt_pkg.FileLock instead using the with-statement.
    """
    return 0

def init(): # real signature unknown; restored from __doc__
    """
    init()
    
    Shorthand for doing init_config() and init_system(). When working
    with command line arguments, first call init_config() then parse
    the command line and finally call init_system().
    """
    pass

def InitConfig(*args, **kwargs): # real signature unknown
    """
    init_config()
    
    Load the default configuration and the config file.
    """
    pass

def InitSystem(*args, **kwargs): # real signature unknown
    """
    init_system()
    
    Construct the apt_pkg system.
    """
    pass

def init_config(): # real signature unknown; restored from __doc__
    """
    init_config()
    
    Load the default configuration and the config file.
    """
    pass

def init_system(): # real signature unknown; restored from __doc__
    """
    init_system()
    
    Construct the apt_pkg system.
    """
    pass

def md5sum(p_object): # real signature unknown; restored from __doc__
    """
    md5sum(object) -> str
    
    Return the md5sum of the object. 'object' may either be a string, in
    which case the md5sum of the string is returned, or a file() object
    (or file descriptor), in which case the md5sum of its contents is
    returned.
    """
    return ""

def newConfiguration(*args, **kwargs): # real signature unknown
    """ Construct a configuration instance """
    pass

def ParseCommandLine(*args, **kwargs): # real signature unknown
    """
    parse_commandLine(config: Configuration, options: list, argv: list) -> list
    
    Parse the command line in 'argv' into the configuration space. The
    list 'options' contains a list of 3-tuples or 4-tuples in the form:
    
       (short_option: str, long_option: str, variable: str[, type: str])
    
    The element 'short_option' is one character, the 'long_option' element
    is the name of the long option, the element 'variable' the name of the
    configuration option the result will be stored in and type is one of
    'HasArg', 'IntLevel', 'Boolean', 'InvBoolean', 'ConfigFile',
    'ArbItem'. The default type is 'Boolean'. Read the online documentation
    in python-apt-doc and its tutorial on writing an apt-cdrom clone for more
    details.
    """
    pass

def ParseDepends(*args, **kwargs): # real signature unknown
    """
    parse_depends(s: str) -> list
    
    Parse the dependencies given by 's' and return a list of lists. Each of
    these lists represents one or more options for an 'or' dependency in
    the form of '(pkg, ver, comptype)' tuples. The tuple element 'pkg'
    is the name of the package; the element 'ver' is the version, or ''
    if no version was requested. The element 'ver' is a comparison
    operator ('<', '<=', '=', '>=', or '>').
    """
    pass

def ParseSection(Text): # real signature unknown; restored from __doc__
    """
    ParseSection(Text) -> TagSection()
    
    Deprecated.
    """
    return TagSection

def ParseSrcDepends(*args, **kwargs): # real signature unknown
    """
    parse_depends(s: str) -> list
    
    Parse the dependencies given by 's' and return a list of lists. Each of
    these lists represents one or more options for an 'or' dependency in
    the form of '(pkg, ver, comptype)' tuples. The tuple element 'pkg'
    is the name of the package; the element 'ver' is the version, or ''
    if no version was requested. The element 'ver' is a comparison
    operator ('<', '<=', '=', '>=', or '>').
    """
    pass

def ParseTagFile(file): # real signature unknown; restored from __doc__
    """
    ParseTagFile(file) -> TagFile()
    
    Deprecated.
    """
    return TagFile

def parse_commandline(*args, **kwargs): # real signature unknown
    """
    parse_commandLine(config: Configuration, options: list, argv: list) -> list
    
    Parse the command line in 'argv' into the configuration space. The
    list 'options' contains a list of 3-tuples or 4-tuples in the form:
    
       (short_option: str, long_option: str, variable: str[, type: str])
    
    The element 'short_option' is one character, the 'long_option' element
    is the name of the long option, the element 'variable' the name of the
    configuration option the result will be stored in and type is one of
    'HasArg', 'IntLevel', 'Boolean', 'InvBoolean', 'ConfigFile',
    'ArbItem'. The default type is 'Boolean'. Read the online documentation
    in python-apt-doc and its tutorial on writing an apt-cdrom clone for more
    details.
    """
    pass

def parse_depends(s): # real signature unknown; restored from __doc__
    """
    parse_depends(s: str) -> list
    
    Parse the dependencies given by 's' and return a list of lists. Each of
    these lists represents one or more options for an 'or' dependency in
    the form of '(pkg, ver, comptype)' tuples. The tuple element 'pkg'
    is the name of the package; the element 'ver' is the version, or ''
    if no version was requested. The element 'ver' is a comparison
    operator ('<', '<=', '=', '>=', or '>').
    """
    return []

def parse_src_depends(s): # real signature unknown; restored from __doc__
    """
    parse_src_depends(s: str) -> list
    
    Parse the dependencies given by 's' and return a list of lists. Each of
    these lists represents one or more options for an 'or' dependency in
    the form of '(pkg, ver, comptype)' tuples. The tuple element 'pkg'
    is the name of the package; the element 'ver' is the version, or ''
    if no version was requested. The element 'ver' is a comparison
    operator ('<', '<=', '=', '>=', or '>').
    
    Dependencies may be restricted to certain architectures and the result
    only contains those dependencies for the architecture set in the
    configuration variable APT::Architecture
    """
    return []

def PkgSystemLock(*args, **kwargs): # real signature unknown
    """
    pkgsystem_lock() -> bool
    
    Acquire the global lock for the package system by using /var/lib/dpkg/lock
    to do the locking. From Python 2.6 on, the apt_pkg.SystemLock context
    manager is available and should be used instead.
    """
    pass

def PkgSystemUnLock(*args, **kwargs): # real signature unknown
    """
    pkgsystem_unlock() -> bool
    
    Release the global lock for the package system.
    """
    pass

def pkgsystem_lock(): # real signature unknown; restored from __doc__
    """
    pkgsystem_lock() -> bool
    
    Acquire the global lock for the package system by using /var/lib/dpkg/lock
    to do the locking. From Python 2.6 on, the apt_pkg.SystemLock context
    manager is available and should be used instead.
    """
    return False

def pkgsystem_unlock(): # real signature unknown; restored from __doc__
    """
    pkgsystem_unlock() -> bool
    
    Release the global lock for the package system.
    """
    return False

def QuoteString(String, String_1): # real signature unknown; restored from __doc__
    """ QuoteString(String,String) -> String """
    return ""

def quote_string(string, repl): # real signature unknown; restored from __doc__
    """
    quote_string(string: str, repl: str) -> str
    
    Escape the string 'string', replacing any character not allowed in a URLor specified by 'repl' with its ASCII value preceded by a percent sign(so for centralfitestoque ' ' becomes '%20').
    """
    return ""

def ReadConfigDir(*args, **kwargs): # real signature unknown
    """
    read_config_dir(configuration: apt_pkg.Configuration, dirname: str)
    
    Read all configuration files in the dir given by 'dirname' in the
    correct order.
    """
    pass

def ReadConfigFile(*args, **kwargs): # real signature unknown
    """
    read_config_file(configuration: apt_pkg.Configuration, filename: str)
    
    Read the configuration file 'filename' and set the appropriate
    options in the configuration object.
    """
    pass

def ReadConfigFileISC(*args, **kwargs): # real signature unknown
    """
    read_config_file(configuration: apt_pkg.Configuration, filename: str)
    
    Read the configuration file 'filename' and set the appropriate
    options in the configuration object.
    """
    pass

def read_config_dir(configuration, dirname): # real signature unknown; restored from __doc__
    """
    read_config_dir(configuration: apt_pkg.Configuration, dirname: str)
    
    Read all configuration files in the dir given by 'dirname' in the
    correct order.
    """
    pass

def read_config_file(configuration, filename): # real signature unknown; restored from __doc__
    """
    read_config_file(configuration: apt_pkg.Configuration, filename: str)
    
    Read the configuration file 'filename' and set the appropriate
    options in the configuration object.
    """
    pass

def read_config_file_isc(*args, **kwargs): # real signature unknown
    """
    read_config_file(configuration: apt_pkg.Configuration, filename: str)
    
    Read the configuration file 'filename' and set the appropriate
    options in the configuration object.
    """
    pass

def RewriteSection(*args, **kwargs): # real signature unknown
    """
    rewrite_section(section: TagSection, order: list, rewrite_list: list) -> str
    
    Rewrite the section given by 'section' using 'rewrite_list', and order the
    fields according to 'order'.
    
    The parameter 'order' is a list object containing the names of the fields
    in the order they should appear in the rewritten section.
    apt_pkg.REWRITE_PACKAGE_ORDER and apt_pkg.REWRITE_SOURCE_ORDER are two
    predefined lists for rewriting package and source sections, respectively
    
    The parameter 'rewrite_list' is a list of tuples of the form
    '(tag, newvalue[, renamed_to])', where 'tag' describes the field which
    should be changed, 'newvalue' the value which should be inserted or None
    to delete the field, and the optional renamed_to can be used to rename the
    field.
    """
    pass

def rewrite_section(section, order, rewrite_list): # real signature unknown; restored from __doc__
    """
    rewrite_section(section: TagSection, order: list, rewrite_list: list) -> str
    
    Rewrite the section given by 'section' using 'rewrite_list', and order the
    fields according to 'order'.
    
    The parameter 'order' is a list object containing the names of the fields
    in the order they should appear in the rewritten section.
    apt_pkg.REWRITE_PACKAGE_ORDER and apt_pkg.REWRITE_SOURCE_ORDER are two
    predefined lists for rewriting package and source sections, respectively
    
    The parameter 'rewrite_list' is a list of tuples of the form
    '(tag, newvalue[, renamed_to])', where 'tag' describes the field which
    should be changed, 'newvalue' the value which should be inserted or None
    to delete the field, and the optional renamed_to can be used to rename the
    field.
    """
    return ""

def sha1sum(p_object): # real signature unknown; restored from __doc__
    """
    sha1sum(object) -> str
    
    Return the sha1sum of the object. 'object' may either be a string, in
    which case the sha1sum of the string is returned, or a file() object
    (or file descriptor), in which case the sha1sum of its contents is
    returned.
    """
    return ""

def sha256sum(p_object): # real signature unknown; restored from __doc__
    """
    sha256sum(object) -> str
    
    Return the sha256sum of the object. 'object' may either be a string, in
    which case the sha256sum of the string is returned, or a file() object
    (or file descriptor), in which case the sha256sum of its contents is
    returned.
    """
    return ""

def SizeToStr(p_int): # real signature unknown; restored from __doc__
    """ SizeToStr(int) -> String """
    return ""

def size_to_str(bytes): # real signature unknown; restored from __doc__
    """
    size_to_str(bytes: int) -> str
    
    Return a string describing the size in a human-readable manner using
    SI prefix and base-10 units, e.g. '1k' for 1000, '1M' for 1000000, etc.
    """
    return ""

def StringToBool(String): # real signature unknown; restored from __doc__
    """ StringToBool(String) -> int """
    return 0

def string_to_bool(string): # real signature unknown; restored from __doc__
    """
    string_to_bool(string: str) -> int
    
    Return 1 if the string is a value such as 'yes', 'true', '1';
    0 if the string is a value such as 'no', 'false', '0'; -1 if
    the string is not recognized.
    """
    return 0

def StrToTime(String): # real signature unknown; restored from __doc__
    """ StrToTime(String) -> Int """
    return 0

def str_to_time(rfc_time): # real signature unknown; restored from __doc__
    """
    str_to_time(rfc_time: str) -> int
    
    Convert the given RFC 1123 formatted string to a Unix timestamp.
    """
    return 0

def TimeRFC1123(p_int): # real signature unknown; restored from __doc__
    """ TimeRFC1123(int) -> String """
    return ""

def TimeToStr(p_int): # real signature unknown; restored from __doc__
    """ TimeToStr(int) -> String """
    return ""

def time_rfc1123(unixtime): # real signature unknown; restored from __doc__
    """
    time_rfc1123(unixtime: int) -> str
    
    Format the given Unix time according to the requirements of
    RFC 1123.
    """
    return ""

def time_to_str(seconds): # real signature unknown; restored from __doc__
    """
    time_to_str(seconds: int) -> str
    
    Return a string describing the number of seconds in a human
    readable manner using days, hours, minutes and seconds.
    """
    return ""

def UpstreamVersion(*args, **kwargs): # real signature unknown
    """
    upstream_version(ver: str) -> str
    
    Return the upstream version for the package version given by 'ver'.
    """
    pass

def upstream_version(ver): # real signature unknown; restored from __doc__
    """
    upstream_version(ver: str) -> str
    
    Return the upstream version for the package version given by 'ver'.
    """
    return ""

def URItoFileName(String): # real signature unknown; restored from __doc__
    """ URItoFileName(String) -> String """
    return ""

def uri_to_filename(uri): # real signature unknown; restored from __doc__
    """
    uri_to_filename(uri: str) -> str
    
    Return a filename based on the given URI after replacing some
    parts not suited for filenames (e.g. '/').
    """
    return ""

def VersionCompare(*args, **kwargs): # real signature unknown
    """
    version_compare(a: str, b: str) -> int
    
    Compare the given versions; return -1 if 'a' is smaller than 'b',
    0 if they are equal, and 2 if 'a' is larger than 'b'.
    """
    pass

def version_compare(a, b): # real signature unknown; restored from __doc__
    """
    version_compare(a: str, b: str) -> int
    
    Compare the given versions; return -1 if 'a' is smaller than 'b',
    0 if they are equal, and 2 if 'a' is larger than 'b'.
    """
    return 0

# classes

class Acquire(object):
    """
    Acquire([progress: apt.progress.base.AcquireProgress])
    
    Coordinate the retrieval of files via network or local file system
    (using 'copy:/path/to/file' style URIs). The optional argument
    'progress' takes an apt.progress.base.AcquireProgress object
    which may report progress information.
    """
    def run(self): # real signature unknown; restored from __doc__
        """
        run() -> int
        
        Run the fetcher and return one of RESULT_CANCELLED,
        RESULT_CONTINUE, RESULT_FAILED. RESULT_CONTINUE means that all items
        which where queued prior to calling run() have been fetched
        successfully. RESULT_CANCELLED means that the process was canceled
        by the progress class. And RESULT_FAILED means a generic failure.
        """
        return 0

    def shutdown(self): # real signature unknown; restored from __doc__
        """
        shutdown()
        
        Shut the fetcher down, removing all items from it. Future access to
        queued AcquireItem objects will cause a segfault. The partial result
        is kept on the disk and not removed and APT might reuse it.
        """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, progress=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    fetch_needed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total amount of data to be fetched (number of bytes)."""

    items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of all items as apt_pkg.AcquireItem objects, including already
fetched ones and to be fetched ones."""

    partial_present = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The amount of data which is already available (number of bytes)."""

    total_needed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The amount of data that needs to fetched plus the amount of data
which has already been fetched (number of bytes)."""

    workers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of all active workers as apt_pkg.AcquireWorker objects."""


    ResultCancelled = 2
    ResultContinue = 0
    ResultFailed = 1
    RESULT_CANCELLED = 2
    RESULT_CONTINUE = 0
    RESULT_FAILED = 1


class AcquireItem(object):
    """
    Represent a single item to be fetched by an Acquire object.
    
    It is not possible to construct instances of this class directly.
    Prospective users should construct instances of a subclass such as
    AcquireFile instead. It is not possible to create subclasses on the
    Python level, only on the C++ level.
    """
    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    complete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A boolean value determining whether the item has been fetched
completely"""

    desc_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A string describing the URI from which the item is acquired."""

    destfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The path to the file where the item will be stored."""

    error_text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If an error occured, a string describing the error; empty string
otherwise."""

    filesize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of the file (number of bytes). If unknown, it is set to 0."""

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ID of the item. An integer which can be set by progress classes."""

    is_trusted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the item is trusted or not. Only True for packages
which come from a repository signed with one of the keys in
APT's keyring."""

    local = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether we are fetching a local item (copy:/) or not."""

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A localized string such as 'Fetching' which indicates the current
mode."""

    partialsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The amount of data which has already been fetched (number of bytes)."""

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An integer representing the item's status which can be compared
against one of the STAT_* constants defined in this class."""


    StatAuthError = 4
    StatDone = 2
    StatError = 3
    StatFetching = 1
    StatIdle = 0
    STAT_AUTH_ERROR = 4
    STAT_DONE = 2
    STAT_ERROR = 3
    STAT_FETCHING = 1
    STAT_IDLE = 0
    STAT_TRANSIENT_NETWORK_ERROR = 5


class AcquireFile(AcquireItem):
    """
    AcquireFile(owner, uri[, md5, size, descr, short_descr, destdir,destfile])
    
    Represent a file to be fetched. The parameter 'owner' points to
    an apt_pkg.Acquire object and the parameter 'uri' to the source
    location. Normally, the file will be stored in the current directory
    using the file name given in the URI. This directory can be changed
    by passing the name of a directory to the 'destdir' parameter. It is
    also possible to set a path to a file using the 'destfile' parameter,
    but both cannot be specified together.
    
    The parameters 'short_descr' and 'descr' can be used to specify
    a short description and a longer description for the item. This
    information is used by progress classes to refer to the item and
    should be short, for centralfitestoque, package name as 'short_descr' and
    and something like 'http://localhost sid/main python-apt 0.7.94.2'
    as 'descr'.
    The parameters 'md5' and 'size' are used to verify the resulting
    file. The parameter 'size' is also to calculate the total amount
    of data to be fetched and is useful for resuming a interrupted
    download.
    
    All parameters can be given by name (i.e. as keyword arguments).
    """
    def __init__(self, owner, uri, md5=None, size=None, descr=None, short_descr=None, destdir=None, destfile=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class AcquireItemDesc(object):
    """
    Provide the description of an item and the URI the item is
    fetched from. Progress classes make use of such objects to
    retrieve description and other information about an item.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A string describing the item."""

    owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The owner of the item, an apt_pkg.AcquireItem object."""

    shortdesc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A short string describing the item (e.g. package name)."""

    uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The URI from which this item would be downloaded."""



class AcquireWorker(object):
    """
    Represent a sub-process responsible for fetching files from
    remote locations. This sub-process uses 'methods' located in
    the directory specified by the configuration option
    Dir::Bin::Methods.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    current_item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The item currently being fetched, as an apt_pkg.AcquireItemDesc object."""

    current_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The amount of data fetched so far for the current item."""

    resumepoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The amount of data which was already available when the download was
started."""

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The status of the worker, as a string."""

    total_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total size of the item."""



class ActionGroup(object):
    """
    ActionGroup(depcache)
    
    Create a new ActionGroup() object. The parameter *depcache* refers to an
    apt_pkg.DepCache() object.
    
    ActionGroups disable certain cleanup actions, so modifying many packages
    is much faster.
    
    ActionGroup() can also be used with the 'with' statement, but be aware
    that the ActionGroup() is active as soon as it is created, and not just
    when entering the context. This means you can write::
    
        with apt_pkg.ActionGroup(depcache):
            depcache.markInstall(pkg)
    
    Once the block of the with statement is left, the action group is 
    automatically released from the cache.
    """
    def release(self): # real signature unknown; restored from __doc__
        """
        release()
        
        End the scope of this action group.  If this is the only action
        group bound to the cache, this will cause any deferred cleanup
        actions to be performed.
        """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """
        __enter__() -> ActionGroup
        
        A dummy action which just returns the object itself, so it can
        be used as a context manager.
        """
        return ActionGroup

    def __exit__(self, *excinfo): # real signature unknown; restored from __doc__
        """
        __exit__(*excinfo) -> bool
        
        Same as release(), but for use as a context manager.
        """
        return False

    def __init__(self, depcache): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Cache(object):
    """
    Cache([progress]) -> Cache() object.
    
    The APT cache file contains a hash table mapping names of binary
    packages to their metadata. A Cache object is the in-core
    representation of the same. It provides access to APT’s idea of the
    list of available packages.
    The optional parameter *progress* can be used to specify an 
    apt.progress.base.OpProgress() object (or similar) which reports
    progress information while the cache is being opened.  If this
    parameter is not supplied, the progress will be reported in simple,
    human-readable text to standard output. If it is None, no output
    will be made.
    
    The cache can be used like a mapping from package names to Package
    objects (although only getting items is supported). Instead of a name,
    a tuple of a name and an architecture may be used.
    """
    def Close(self, *args, **kwargs): # real signature unknown
        """ Close the cache """
        pass

    def Open(self, *args, **kwargs): # real signature unknown
        """ Open the cache; deprecated and unsafe """
        pass

    def update(self, progress, sources, pulse_interval): # real signature unknown; restored from __doc__
        """
        update(progress, sources: SourceList, pulse_interval: int) -> bool
        
        Update the index files used by the cache. A call to this method
        does not affect the current Cache object; instead, a new one
        should be created in order to use the changed index files.
        
        The parameter 'progress' can be used to specify an
        apt.progress.base.AcquireProgress() object , which will report
        progress information while the index files are being fetched.
        The parameter 'sources', if provided, is an apt_pkg.SourcesList
        object listing the remote repositories to be used.
        The 'pulse_interval' parameter indicates how long (in microseconds)
        to wait between calls to the pulse() method of the 'progress' object.
        The default is 500000 microseconds.
        """
        return False

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, progress=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    depends_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of apt_pkg.Dependency objects stored in the cache."""

    file_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of apt_pkg.PackageFile objects stored in the cache."""

    groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of Group objects in the cache"""

    group_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of apt_pkg.Group objects stored in the cache."""

    is_multi_arch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the cache supports multi-arch."""

    packages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of apt_pkg.Package objects stored in the cache."""

    package_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of apt_pkg.Package objects stored in the cache."""

    package_file_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of apt_pkg.PackageFile objects stored in the cache."""

    policy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The PkgPolicy for the cache"""

    provides_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of Provides relations described in the cache."""

    version_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of apt_pkg.Version objects stored in the cache."""

    ver_file_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of (Version, PackageFile) relations."""



class Cdrom(object):
    """
    Cdrom()
    
    Cdrom objects can be used to identify Debian installation media and to
    add them to /etc/apt/sources.list.
    """
    def add(self, progress): # real signature unknown; restored from __doc__
        """
        add(progress: apt_pkg.CdromProgress) -> bool
        
        Add the given CD-ROM to the sources.list. Return True on success;
        raise an error on failure or return False.
        """
        return False

    def ident(self, progress): # real signature unknown; restored from __doc__
        """
        ident(progress: apt_pkg.CdromProgress) -> str
        
        Try to identify the CD-ROM and if successful return the hexadecimal
        CDROM-ID (and a integer version suffix separated by -) as a
        string. Otherwise, return None or raise an error.
        
        The ID is created by hashing all file and directory names on the
        CD-ROM and appending the version.
        """
        return ""

    def Ident(self, *args, **kwargs): # real signature unknown
        """ DEPRECATED. DO NOT USE """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Configuration(object):
    """
    Configuration()
    
    Represent the configuration of APT by mapping option keys to
    values and storing configuration parsed from files like
    /etc/apt/apt.conf. The most important Configuration object
    is apt_pkg.config which points to the global configuration
    object. Other top-level Configuration objects can be created
    by calling the constructor, but there is usually no reason to.
    """
    def clear(self, key): # real signature unknown; restored from __doc__
        """
        clear(key: str)
        
        Remove the specified option and all sub-options.
        """
        pass

    def dump(self): # real signature unknown; restored from __doc__
        """
        dump() -> str
        
        Return a string dump this Configuration object.
        """
        return ""

    def exists(self, key): # real signature unknown; restored from __doc__
        """
        exists(key: str) -> bool
        
        Check whether the given key exists.
        """
        return False

    def find(self, key, default=''): # real signature unknown; restored from __doc__
        """
        find(key: str[, default: str = '']) -> str
        
        Find the value for the given key and return it. If the
        given key does not exist, return default instead.
        """
        return ""

    def find_b(self, *args, **kwargs): # real signature unknown
        """
        find_i(key: str[, default: bool = False]) -> bool
        
        Same as find, but for boolean values; returns False on unknown values.
        """
        pass

    def find_dir(self, key, default=''): # real signature unknown; restored from __doc__
        """
        find_dir(key: str[, default: str = '']) -> str
        
        Same as find_file(), but for directories. The difference is
        that this function adds a trailing slash to the result.
        """
        return ""

    def find_file(self, key, default=''): # real signature unknown; restored from __doc__
        """
        find_file(key: str[, default: str = '']) -> str
        
        Same as find(), but for filenames. In the APT configuration, there
        is a special section Dir:: for storing filenames. find_file() locates
        the given key and then goes up and prepends the directory names to the
        return value. For centralfitestoque, for:
        
            apt_pkg.config['Dir'] = 'a'
            apt_pkg.config['Dir::D'] = 'b'
            apt_pkg.config['Dir::D::F'] = 'c'
        
        find_file('Dir::D::F') returns 'a/b/c'. There is also a special
        configuration setting RootDir which will always be prepended to the
        result (the default being ''). Thus, if RootDir is 'x', the centralfitestoque
        would return 'x/a/b/c'.
        """
        return ""

    def find_i(self, key, default=0): # real signature unknown; restored from __doc__
        """
        find_i(key: str[, default: int = 0]) -> int
        
        Same as find, but for integer values.
        """
        return 0

    def get(self, *args, **kwargs): # real signature unknown
        """
        find(key: str[, default: str = '']) -> str
        
        Find the value for the given key and return it. If the
        given key does not exist, return default instead.
        """
        pass

    def has_key(self, *args, **kwargs): # real signature unknown
        """
        exists(key: str) -> bool
        
        Check whether the given key exists.
        """
        pass

    def keys(self, root=None): # real signature unknown; restored from __doc__
        """
        keys([root: str]) -> list
        
        Return a list of all keys in the configuration object. If 'root'
        is given, limit the list to those below the root.
        """
        return []

    def list(self, root=None): # real signature unknown; restored from __doc__
        """
        list([root: str]) -> list
        
        Return a list of all items at the given root, using their full
        name. For centralfitestoque, in a configuration object where the options A,
        B, and B::C are set, the following expressions evaluate to True:
        
           conf.list() == ['A', 'B']
           conf.list('A') == ['']
           conf.list('B') == ['B::C']
        """
        return []

    def my_tag(self): # real signature unknown; restored from __doc__
        """
        my_tag() -> str
        
        Return the tag of the root of this Configuration object. For the
        default object, this is an empty string. For a subtree('APT') of
        such an object, it would be 'APT' (given as an centralfitestoque).
        """
        return ""

    def set(self, key, value): # real signature unknown; restored from __doc__
        """
        set(key: str, value: str)
        
        Set the given key to the given value. To set int or bool values,
        encode them using str(value) and then use find_i()/find_b()
        to retrieve their value again.
        """
        pass

    def subtree(self, key): # real signature unknown; restored from __doc__
        """
        subtree(key: str) -> apt_pkg.Configuration
        
        Return a new apt_pkg.Configuration object with the given option
        as its root. Example:
        
            apttree = config.subtree('APT')
            apttree['Install-Suggests'] = config['APT::Install-Suggests']
        """
        pass

    def value_list(self, root=None): # real signature unknown; restored from __doc__
        """
        value_list([root: str]) -> list
        
        Same as list(), but instead of returning the keys, return the values.
        """
        return []

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass


class DepCache(object):
    """
    DepCache(cache: apt_pkg.Cache)
    
    A DepCache() holds extra information on the state of the packages.
    
    The parameter 'cache' refers to an apt_pkg.Cache() object.
    """
    def commit(self, acquire_progress, install_progress): # real signature unknown; restored from __doc__
        """
        commit(acquire_progress, install_progress)
        
        Commit all the marked changes. This method takes two arguments,
        'acquire_progress' takes an apt.progress.base.AcquireProgress
        object and 'install_progress' an apt.progress.base.InstallProgress
        object.
        """
        pass

    def fix_broken(self): # real signature unknown; restored from __doc__
        """
        fix_broken() -> bool
        
        Fix broken packages.
        """
        return False

    def get_candidate_ver(self, pkg): # real signature unknown; restored from __doc__
        """
        get_candidate_ver(pkg: apt_pkg.Package) -> apt_pkg.Version
        
        Return the candidate version for the package, normally the version
        with the highest pin (changeable using set_candidate_ver).
        """
        pass

    def init(self, progress): # real signature unknown; restored from __doc__
        """
        init(progress: apt.progress.base.OpProgress)
        
        Initialize the depcache (done automatically when constructing
        the object).
        """
        pass

    def is_auto_installed(self, pkg): # real signature unknown; restored from __doc__
        """
        is_auto_installed(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is marked as automatically installed.
        """
        return False

    def is_garbage(self, pkg): # real signature unknown; restored from __doc__
        """
        is_garbage(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is garbage, i.e. whether it is automatically
        installed and the reverse dependencies are not installed anymore.
        """
        return False

    def is_inst_broken(self, pkg): # real signature unknown; restored from __doc__
        """
        is_inst_broken(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is broken, ignoring marked changes.
        """
        return False

    def is_now_broken(self, pkg): # real signature unknown; restored from __doc__
        """
        is_now_broken(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is broken, taking marked changes into account.
        """
        return False

    def is_upgradable(self, pkg): # real signature unknown; restored from __doc__
        """
        is_upgradable(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is upgradable.
        """
        return False

    def marked_delete(self, pkg): # real signature unknown; restored from __doc__
        """
        marked_delete(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is marked for removal.
        """
        return False

    def marked_downgrade(self, pkg): # real signature unknown; restored from __doc__
        """
        marked_downgrade(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is marked for downgrade.
        """
        return False

    def marked_install(self, pkg): # real signature unknown; restored from __doc__
        """
        marked_install(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is marked for installation.
        """
        return False

    def marked_keep(self, pkg): # real signature unknown; restored from __doc__
        """
        marked_keep(pkg: apt_pkg.Package) -> bool
        
        Check whether the package should be kept.
        """
        return False

    def marked_reinstall(self, pkg): # real signature unknown; restored from __doc__
        """
        marked_reinstall(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is marked for re-installation.
        """
        return False

    def marked_upgrade(self, pkg): # real signature unknown; restored from __doc__
        """
        marked_upgrade(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is marked for upgrade.
        """
        return False

    def mark_auto(self, pkg, auto): # real signature unknown; restored from __doc__
        """
        mark_auto(pkg: apt_pkg.Package, auto: bool)
        
        Mark package as automatically installed (if auto=True),
        or as not automatically installed (if auto=False).
        """
        pass

    def mark_delete(self, pkg, purge=False): # real signature unknown; restored from __doc__
        """
        mark_delete(pkg: apt_pkg.Package[, purge: bool = False])
        
        Mark package for deletion, and if 'purge' is True also for purging.
        """
        pass

    def mark_install(self, pkg, auto_inst=True, from_user=True): # real signature unknown; restored from __doc__
        """
        mark_install(pkg: apt_pkg.Package[, auto_inst=True, from_user=True])
        
        Mark the package for installation. The parameter 'auto_inst' controls
        whether the dependencies of the package are marked for installation
        as well. The parameter 'from_user' controls whether the package is
        registered as NOT automatically installed.
        """
        pass

    def mark_keep(self, pkg): # real signature unknown; restored from __doc__
        """
        mark_keep(pkg: apt_pkg.Package)
        
        Mark package to be kept.
        """
        pass

    def minimize_upgrade(self): # real signature unknown; restored from __doc__
        """
        minimize_upgrade() -> bool
        
        Go over the entire set of packages and try to keep each package
        marked for upgrade. If a conflict is generated then the package
        is restored.
        """
        return False

    def read_pinfile(self, file=None): # real signature unknown; restored from __doc__
        """
        read_pinfile([file: str])
        
        Read the pin policy
        """
        pass

    def set_candidate_release(self, pkg, ver, rel): # real signature unknown; restored from __doc__
        """
        set_candidate_release(pkg: apt_pkg.Package, ver: apt_pkg.Version, rel: string) -> bool
        
        Sets not only the candidate version 'ver' for package 'pkg', but walks also down the dependency tree and checks if it is required to set the candidate of the dependency to a version from the given release string 'rel', too.
        """
        return False

    def set_candidate_ver(self, pkg, ver): # real signature unknown; restored from __doc__
        """
        set_candidate_ver(pkg: apt_pkg.Package, ver: apt_pkg.Version) -> bool
        
        Set the candidate version of 'pkg' to 'ver'.
        """
        return False

    def set_reinstall(self, pkg, reinstall): # real signature unknown; restored from __doc__
        """
        set_reinstall(pkg: apt_pkg.Package, reinstall: bool)
        
        Set whether the package should be reinstalled (reinstall = True or False).
        """
        pass

    def upgrade(self, dist_upgrade=True): # real signature unknown; restored from __doc__
        """
        upgrade([dist_upgrade: bool = True]) -> bool
        
        Mark the packages for upgrade under the same conditions apt-get
        upgrade does. If 'dist_upgrade' is True, also allow packages to
        be upgraded if they require installation/removal of other packages;
        just like apt-get dist-upgrade.
        """
        return False

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, cache): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    broken_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of packages with broken dependencies in the cache."""

    deb_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of the packages which are needed for the changes to be
applied."""

    del_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of packages marked for removal."""

    inst_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of packages marked for installation."""

    keep_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of packages marked for keep."""

    policy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The apt_pkg.Policy object used by this cache."""

    usr_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The amount of space required for installing/removing the packages,
i.e. the Installed-Size of all packages marked for installation
minus the Installed-Size of all packages for removal."""



class Dependency(object):
    """
    Represent a dependency from one package version to a package,
    and (optionally) a version relation (e.g. >= 1). Dependency
    objects also provide useful functions like all_targets() or
    smart_target_pkg() for selecting packages to satisfy the
    dependency.
    """
    def all_targets(self): # real signature unknown; restored from __doc__
        """
        all_targets() -> list
        
        A list of all apt_pkg.Version objects satisfying the dependency.
        """
        return []

    def smart_target_pkg(self): # real signature unknown; restored from __doc__
        """
        smart_target_pkg() -> apt_pkg.Package
        
        Return the first package which provides a package with the name
        of the target package.
        """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    comp_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of comparison, as a string (one of '<', '<=', '=', '>=', '>')."""

    dep_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of the dependency; may be translated"""

    dep_type_enum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Same as dep_type, but with a numeric value instead of a string. Can
be compared against the TYPE_ constants defined in this class."""

    dep_type_untranslated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Same as dep_type, but guaranteed to be untranslated."""

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The numeric ID of this dependency object."""

    parent_pkg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The apt_pkg.Package object of the package which depends."""

    parent_ver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The apt_pkg.Version object of the package which depends."""

    target_pkg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The apt_pkg.Package object of the package depended upon"""

    target_ver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The version of the package depended upon as a string"""


    TYPE_CONFLICTS = 5
    TYPE_DEPENDS = 1
    TYPE_DPKG_BREAKS = 8
    TYPE_ENHANCES = 9
    TYPE_OBSOLETES = 7
    TYPE_PREDEPENDS = 2
    TYPE_RECOMMENDS = 4
    TYPE_REPLACES = 6
    TYPE_SUGGESTS = 3


class DependencyList(object):
    """
    A simple list-like type for representing multiple dependency
    objects in an efficient manner; without having to generate
    all Dependency objects in advance.
    """
    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass


class Description(object):
    """
    Represent a package description and some attributes. Needed for
    things like translated descriptions.
    """
    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    file_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of all apt_pkg.PackageFile objects related to this description."""

    language_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The language code of the description. Empty string for untranslated
descriptions."""

    md5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The MD5 hash of the description."""



class FileLock(object):
    """
    SystemLock(filename: str)
    
    Context manager for locking using a file. The lock is established
    as soon as the method __enter__() is called. It is released when
    __exit__() is called.
    
    This should be used via the 'with' statement, for centralfitestoque:
    
       with apt_pkg.FileLock(filename):
           ...
    
    Once the block is left, the lock is released automatically. The object
    can be used multiple times:
    
       lock = apt_pkg.FileLock(filename)
       with lock:
           ...
       with lock:
           ...
    """
    def __enter__(self, *args, **kwargs): # real signature unknown
        """ Lock the system. """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """ Unlock the system. """
        pass

    def __init__(self, filename): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Group(object):
    """
    Group(cache, name)
    
    Group of packages with the same name.
    
    Provides access to all packages sharing a name. Can be used this
    like a list, or by using the special find_*() methods. If you use
    it as a sequence, make sure to access it linearly, as this uses a
    linked list internally.
    """
    def find_package(self, architecture): # real signature unknown; restored from __doc__
        """
        find_package(architecture: str) -> Package
        
        Return a package for the given architecture, or None if none exists
        """
        return Package

    def find_preferred_package(self, prefer_non_virtual=True): # real signature unknown; restored from __doc__
        """
        find_preferred_package(prefer_non_virtual: bool = True) -> Package
        
        Return a package for the best architecture, either the native one
        or the first found one. If none exists, return None. If non_virtual
        is True, prefer non-virtual packages over virtual ones.
        """
        return Package

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, cache, name): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class GroupList(object):
    """
    A GroupList is an internally used structure to represent
    the 'groups' attribute of apt_pkg.Cache objects in a more
    efficient manner by creating Group objects only when they
    are accessed.
    """
    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass


class Hashes(object):
    """
    Hashes([object: (bytes, file)])
    
    Calculate hashes for the given object. It can be used to create all
    supported hashes for a file.
    
    The parameter 'object' can be a bytestring, an object providing the
    fileno() method, or an integer describing a file descriptor.
    """
    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    md5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The MD5Sum of the file as a string."""

    sha1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The SHA1Sum of the file as a string."""

    sha256 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The SHA256Sum of the file as a string."""



class HashString(object):
    """
    HashString(type, hash) OR HashString('type:hash')
    
    Create a new HashString object. The first form allows you to specify
    a type and a hash, and the second form a single string where type and
    hash are separated by a colon, e.g.::
    
       HashString('MD5Sum', '6cc1b6e6655e3555ac47e5b5fe26d04e')
    
    Valid options for 'type' are: MD5Sum, SHA1, SHA256.
    """
    def verify_file(self, filename): # real signature unknown; restored from __doc__
        """
        verify_file(filename: str) -> bool
        
        Verify that the file indicated by filename matches the hash.
        """
        return False

    def __init__(self, type, hash): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    hashtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of the hash, as a string (possible: MD5Sum,SHA1,SHA256)."""



class IndexFile(object):
    """
    Represent an index file, i.e. package indexes, translation indexes,
    and source indexes.
    """
    def archive_uri(self, path): # real signature unknown; restored from __doc__
        """
        archive_uri(path: str) -> str
        
        Return the URI to the given path in the archive.
        """
        return ""

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    describe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A string describing the index file."""

    exists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A boolean value determining whether the index file exists."""

    has_packages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A boolean value determining whether the index file has packages."""

    is_trusted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A boolean value determining whether the file can be trusted; e.g.
because it is from a source with a GPG signed Release file."""

    label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The label of the index file."""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of the files, measured in bytes."""



class IndexRecords(object):
    """
    IndexRecords()
    
    Representation of a Release file.
    """
    def get_dist(self): # real signature unknown; restored from __doc__
        """
        get_dist() -> str
        
        Return a distribution set in the release file.
        """
        return ""

    def load(self, filename): # real signature unknown; restored from __doc__
        """
        load(filename: str)
        
        Load the file given by filename.
        """
        pass

    def lookup(self, key): # real signature unknown; restored from __doc__
        """
        lookup(key: str) -> (HashString, int)
        
        Look up the filename given by 'key' and return a tuple (hash, size),
        where the first element 'hash' is an apt_pkg.HashString object
        and the second element 'size' is an int object.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class MetaIndex(object):
    """
    Provide information on meta-indexes (i.e. Release files), such as
    whether they are trusted or their URI.
    """
    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    dist = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The distribution, as a string."""

    index_files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of all IndexFile objects associated with this meta index."""

    is_trusted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A boolean value determining whether the file can be trusted."""

    uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The uri the meta index is located at."""



class OrderList(object):
    """
    OrderList(depcache: DepCache)
    
    Sequence type for packages with special ordering methods.
    """
    def append(self, pkg): # real signature unknown; restored from __doc__
        """
        append(pkg: Package)
        
        Append a package to the end of the list.
        """
        pass

    def flag(self, pkg, flag, unset_flags=None): # real signature unknown; restored from __doc__
        """
        flag(pkg: Package, flag: int[, unset_flags: int])
        
        Flag the package, set flags in 'flag' and remove flags in
        'unset_flags'.
        """
        pass

    def is_flag(self, pkg, flag): # real signature unknown; restored from __doc__
        """
        is_flag(pkg: Package, flag: int)
        
        Check if the flag(s) are set.
        """
        pass

    def is_missing(self, *args, **kwargs): # real signature unknown
        """
        is_now(pkg: Package)
        
        Check if the package is marked for install.
        """
        pass

    def is_now(self, pkg): # real signature unknown; restored from __doc__
        """
        is_now(pkg: Package)
        
        Check if the package is flagged for any state but removal.
        """
        pass

    def order_configure(self): # real signature unknown; restored from __doc__
        """
        order_configure()
        
        Order the packages for configuration (see Debian Policy).
        """
        pass

    def order_critical(self): # real signature unknown; restored from __doc__
        """
        order_critical()
        
        Order by PreDepends only (critical unpack order).
        """
        pass

    def order_unpack(self): # real signature unknown; restored from __doc__
        """
        order_unpack()
        
        Order the packages for unpacking (see Debian Policy).
        """
        pass

    def score(self, pkg): # real signature unknown; restored from __doc__
        """
        score(pkg: Package) -> int
        
        Return the score of the package.
        """
        return 0

    def wipe_flags(self, flags): # real signature unknown; restored from __doc__
        """
        wipe_flags(flags: int)
        
        Remove the flags in 'flags' from all packages in this list
        """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, depcache): # real signature unknown; restored from __doc__
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    FLAG_ADDED = 1
    FLAG_ADD_PENDIG = 2
    FLAG_AFTER = 256
    FLAG_CONFIGURED = 32
    FLAG_IMMEDIATE = 4
    FLAG_IN_LIST = 128
    FLAG_LOOP = 8
    FLAG_REMOVED = 64
    FLAG_STATES_MASK = 112
    FLAG_UNPACKED = 16


class Package(object):
    """
    Represent a package. A package is uniquely identified by its name
    and each package can have zero or more versions which can be
    accessed via the version_list property. Packages can be installed
    and removed by apt_pkg.DepCache.
    """
    def get_fullname(self, pretty=False): # real signature unknown; restored from __doc__
        """
        get_fullname([pretty: bool = False]) -> str
        
        Get the full name of the package, including the architecture. If
        'pretty' is True, the architecture is omitted for native packages,
        that is, and amd64 apt package on an amd64 system would give 'apt'.
        """
        return ""

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    architecture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The architecture of the package."""

    auto = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ignore it, it does nothing. You want to use
DepCache.is_auto_installed instead."""

    current_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current state, which can be compared against the constants
CURSTATE_CONFIG_FILES, CURSTATE_HALF_CONFIGURED,
CURSTATE_HALF_INSTALLED, CURSTATE_INSTALLED, CURSTATE_NOT_INSTALLED,
CURSTATE_UNPACKED of the apt_pkg module."""

    current_ver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The version of the package currently installed or None."""

    essential = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Boolean value determining whether the package is essential."""

    has_provides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the package is provided by at least one other package."""

    has_versions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the package has at least one version in the cache."""

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The numeric ID of the package"""

    important = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Boolean value determining whether the package has the 'important'
flag set ('Important: yes' in the Packages file). No longer used."""

    inst_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The state of the install, which be compared against the constants
INSTSTATE_HOLD, INSTSTATE_HOLD_REINSTREQ, INSTSTATE_OK,
INSTSTATE_REINSTREQ of the apt_pkg module."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the package."""

    provides_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of all packages providing this package. The list contains
tuples in the format (providesname, providesver, version)
where 'version' is an apt_pkg.Version object."""

    rev_depends_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An apt_pkg.DependencyList object of all reverse dependencies."""

    section = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The section of the package."""

    selected_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The state of the selection, which can be compared against the constants
SELSTATE_DEINSTALL, SELSTATE_HOLD, SELSTATE_INSTALL, SELSTATE_PURGE,
SELSTATE_UNKNOWN of the apt_pkg module."""

    version_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of all apt_pkg.Version objects for this package."""



class PackageFile(object):
    """
    A package file is an index file stored in the cache with some
    additional pieces of information.
    """
    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    architecture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The architecture of the package file. Unused, empty string nowadays."""

    archive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The archive of the package file (i.e. 'Suite' in the Release file)."""

    component = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The component of this package file (e.g. 'main')."""

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The path to the file."""

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The numeric ID of this PackageFile object."""

    index_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A string describing the type of index. Known values are
'Debian Package Index', 'Debian Translation Index', and
'Debian dpkg status file'."""

    label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The label set in the release file (e.g. 'Debian')."""

    not_automatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the NotAutomatic flag is set in the Release file."""

    not_source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether this package file lacks an active (sources.list) source;packages listed in such a file cannot be downloaded."""

    origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The origin set in the release file."""

    site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The hostname of the location this file comes from."""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of the file."""

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The version set in the release file (e.g. '5.0.X' for lenny, where X
is a point release)."""



class PackageList(object):
    """
    A PackageList is an internally used structure to represent
    the 'packages' attribute of apt_pkg.Cache objects in a more
    efficient manner by creating Package objects only when they
    are accessed.
    """
    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass


class _PackageManager(object):
    """
    _PackageManager objects allow the fetching of packages marked for
    installation and the installation of those packages.
    This is an abstract base class that cannot be subclassed
    in Python. The only subclass is apt_pkg.PackageManager. This
    class is an implementation-detail and not part of the API.
    """
    def do_install(self, status_fd): # real signature unknown; restored from __doc__
        """
        do_install(status_fd: int) -> int
        
        Install the packages and return one of the class constants
        RESULT_COMPLETED, RESULT_FAILED, RESULT_INCOMPLETE. The argument
        status_fd can be used to specify a file descriptor that APT will
        write status information on (see README.progress-reporting in the
        apt source code for information on what will be written there).
        """
        return 0

    def fix_missing(self): # real signature unknown; restored from __doc__
        """
        fix_missing() -> bool
        
        Fix the installation if a package could not be downloaded.
        """
        return False

    def get_archives(self, fetcher, p_list, recs): # real signature unknown; restored from __doc__
        """
        get_archives(fetcher: Acquire, list: SourceList, recs: PackageRecords) -> bool
        
        Download the packages marked for installation via the Acquire object
        'fetcher', using the information found in 'list' and 'recs'.
        """
        return False

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    ResultCompleted = 0
    ResultFailed = 1
    ResultIncomplete = 2
    RESULT_COMPLETED = 0
    RESULT_FAILED = 1
    RESULT_INCOMPLETE = 2


class PackageManager(_PackageManager):
    """
    PackageManager(depcache: apt_pkg.DepCache)
    
    PackageManager objects allow the fetching of packages marked for
    installation and the installation of those packages. The parameter
    'depcache' specifies an apt_pkg.DepCache object where information
    about the package selections is retrieved from.
    
    Methods in this class can be overridden in sub classes
    to implement behavior different from APT's dpkg implementation.
    """
    def configure(self, pkg): # real signature unknown; restored from __doc__
        """
        configure(pkg: Package) -> bool 
        
        Add a configure action. Can be overridden in subclasses.
        
        New in version 0.8.0.
        """
        return False

    def go(self, status_fd): # real signature unknown; restored from __doc__
        """
        go(status_fd: int) -> bool 
        
        Start dpkg. Can be overridden in subclasses.
        
        New in version 0.8.0.
        """
        return False

    def install(self, pkg, filename): # real signature unknown; restored from __doc__
        """
        install(pkg: Package, filename: str) -> bool 
        
        Add a install action. Can be overridden in subclasses.
        
        New in version 0.8.0.
        """
        return False

    def remove(self, pkg, purge): # real signature unknown; restored from __doc__
        """
        remove(pkg: Package, purge: bool) -> bool 
        
        Add a removal action. Can be overridden in subclasses.
        
        New in version 0.8.0.
        """
        return False

    def reset(self): # real signature unknown; restored from __doc__
        """
        reset()
        
        Reset the package manager for a new round.
        Can be overridden in subclasses.
        
        New in version 0.8.0.
        """
        pass

    def __init__(self, depcache): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class PackageRecords(object):
    """
    PackageRecords(cache: apt_pkg.Cache)
    
    Package Records contain information about packages. Those objects
    can be used to retrieve information such as maintainer or filename
    of a package. They can also be used to retrieve the raw records
    of the packages (i.e. those stanzas stored in Packages files).
    """
    def lookup(self, (packagefile, index)): # real signature unknown; restored from __doc__
        """
        lookup((packagefile: apt_pkg.PackageFile, index: int)) -> bool
        
        Changes to a new package
        """
        return False

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, cache): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The filename of the package, as stored in the 'Filename' field."""

    homepage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The homepage of the package, as stored in the 'Homepage' field."""

    long_desc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The long description of the packages; i.e. all lines in the
'Description' field except for the first one."""

    maintainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maintainer of the package, as stored in the 'Maintainer' field."""

    md5_hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The MD5 hash value of the package, as stored in the 'MD5Sum' field."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the package, as stored in the 'Package' field."""

    record = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The raw record, suitable for parsing by apt_pkg.TagSection."""

    sha1_hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The SHA1 hash value, as stored in the 'SHA1' field."""

    sha256_hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The SHA256 hash value, as stored in the 'SHA256' field."""

    short_desc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The short description of the package, i.e. the first line of the
'Description' field."""

    source_pkg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the source package, if different from the name of the
binary package. This information is retrieved from the 'Source' field."""

    source_ver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The version of the source package, if it differs from the version
of the binary package. Just like 'source_pkg', this information
is retrieved from the 'Source' field."""



class Policy(object):
    """
    Policy(cache)
    
    Representation of the policy of the Cache object given by cache. This
    provides a superset of policy-related functionality compared to the
    DepCache class. The DepCache can be used for most purposes, but there
    may be some cases where a special policy class is needed.
    """
    def create_pin(self, type, pkg, data, priority): # real signature unknown; restored from __doc__
        """
        create_pin(type: str, pkg: str, data: str, priority: int)
        
        Create a pin for the policy. The parameter 'type' refers to one of the
        strings 'Version', 'Release', or 'Origin'. The argument 'pkg' is the
        name of the package. The parameter 'data' refers to the value
        (e.g. 'unstable' for type='Release') and the other possible options.
        The parameter 'priority' gives the priority of the pin.
        """
        pass

    def get_candidate_ver(self, *args, **kwargs): # real signature unknown
        """
        get_match(package: apt_pkg.Package) -> apt_pkg.Version
        
        Get the best package for the job.
        """
        pass

    def get_match(self, package): # real signature unknown; restored from __doc__
        """
        get_match(package: apt_pkg.Package) -> apt_pkg.Version
        
        Return a matching version for the given package.
        """
        pass

    def get_priority(self, package): # real signature unknown; restored from __doc__
        """
        get_priority(package: apt_pkg.Package) -> int
        
        Return the priority of the package.
        """
        return 0

    def read_pindir(self, dirname): # real signature unknown; restored from __doc__
        """
        read_pindir(dirname: str) -> bool
        
        Read the pin files in the given dir (e.g. '/etc/apt/preferences.d')
        and add them to the policy.
        """
        return False

    def read_pinfile(self, filename): # real signature unknown; restored from __doc__
        """
        read_pinfile(filename: str) -> bool
        
        Read the pin file given by filename (e.g. '/etc/apt/preferences')
        and add it to the policy.
        """
        return False

    def __init__(self, cache): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class ProblemResolver(object):
    """
    ProblemResolver(depcache: apt_pkg.DepCache)
    
    ProblemResolver objects take care of resolving problems
    with dependencies. They mark packages for installation/
    removal and try to satisfy all dependencies.
    """
    def clear(self, pkg): # real signature unknown; restored from __doc__
        """
        clear(pkg: apt_pkg.Package)
        
        Revert the actions done by protect()/remove() on the package.
        """
        pass

    def install_protect(self): # real signature unknown; restored from __doc__
        """
        install_protect()
        
        Install all protected packages.
        """
        pass

    def protect(self, pkg): # real signature unknown; restored from __doc__
        """
        protect(pkg: apt_pkg.Package)
        
        Mark the package as protected in the resolver, meaning that its
        state will not be changed.
        """
        pass

    def remove(self, pkg): # real signature unknown; restored from __doc__
        """
        remove(pkg: apt_pkg.Package)
        
        Mark the package for removal in the resolver.
        """
        pass

    def resolve(self, fix_broken=True): # real signature unknown; restored from __doc__
        """
        resolve([fix_broken: bool = True]) -> bool
        
        Try to intelligently resolve problems by installing and removing
        packages. If 'fix_broken' is True, apt will try to repair broken
        dependencies of installed packages.
        """
        return False

    def resolve_by_keep(self): # real signature unknown; restored from __doc__
        """
        resolve_by_keep() -> bool
        
        Try to resolve problems only by using keep.
        """
        return False

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, depcache): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class SourceList(object):
    """
    SourceList()
    
    Represent the list of sources stored in /etc/apt/sources.list and
    similar files.
    """
    def find_index(self, pkgfile): # real signature unknown; restored from __doc__
        """
        find_index(pkgfile: apt_pkg.PackageFile) -> apt_pkg.IndexFile
        
        Return the index file for the given package file, or None if none
        could be found.
        """
        pass

    def get_indexes(self, acquire, all=False): # real signature unknown; restored from __doc__
        """
        get_indexes(acquire: apt_pkg.Acquire[, all: bool=False]) -> bool
        
        Add all indexes (i.e. stuff like Release files, Packages files)
        to the Acquire object 'acquire'. If 'all' is True, all indexes
        will be added, otherwise only changed indexes will be added.
        """
        return False

    def read_main_list(self): # real signature unknown; restored from __doc__
        """
        read_main_list() -> bool
        
        Read /etc/apt/sources.list and similar files to populate the list
        of indexes.
        """
        return False

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of MetaIndex() objects."""



class SourceRecords(object):
    """
    SourceRecords()
    
    Provide an easy way to look up the records of source packages and
    provide easy attributes for some widely used fields of the record.
    """
    def lookup(self, name): # real signature unknown; restored from __doc__
        """
        lookup(name: str) -> bool
        
        Look up the source package with the given name. Each call moves
        the position of the records parser forward. If there are no
        more records, return None. If the lookup failed this way,
        access to any of the attributes will result in an AttributeError.
        """
        return False

    def restart(self): # real signature unknown; restored from __doc__
        """
        restart()
        
        Restart the lookup process. This moves the parser to the first
        package and lookups can now be made just like on a new object.
        """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    binaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of the names of the binaries produced by this source package."""

    BuildDepends = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Deprecated function and deprecated output format."""

    build_depends = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A dictionary describing the build-time dependencies of the package;
the format is the same as used for apt_pkg.Version.depends_list_str."""

    files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of tuples (md5: str, size: int, path: str, type: str), whereas
'type' can be 'diff' (includes .debian.tar.gz), 'dsc', 'tar'."""

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index file associated with this record as a list of
apt_pkg.IndexFile objects."""

    maintainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maintainer of the package."""

    package = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the source package."""

    record = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The raw record, suitable for parsing using apt_pkg.TagSection."""

    section = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The section of the source package."""

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The version of the source package."""



class SystemLock(object):
    """
    SystemLock()
    
    Context manager for locking the package system. The lock is established
    as soon as the method __enter__() is called. It is released when
    __exit__() is called.
    
    This should be used via the 'with' statement, for centralfitestoque:
    
       with apt_pkg.SystemLock():
           ...
    
    Once the block is left, the lock is released automatically. The object
    can be used multiple times:
    
       lock = apt_pkg.SystemLock()
       with lock:
           ...
       with lock:
           ...
    """
    def __enter__(self, *args, **kwargs): # real signature unknown
        """ Lock the system. """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """ Unlock the system. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class TagFile(object):
    """
    TagFile(file)
    
    TagFile() objects provide access to debian control files, which consist
    of multiple RFC822-style sections.
    
    To provide access to those sections, TagFile objects provide an iterator
    which yields TagSection objects for each section.
    
    TagFile objects also provide another API which uses a shared TagSection
    object in the 'section' member. The functions step() and jump() can be
    used to navigate within the file; offset() returns the current
    position.
    
    It is important to not mix the use of both APIs, because this can have
    unwanted effects.
    
    The parameter 'file' refers to an object providing a fileno() method or
    a file descriptor (an integer)
    """
    def jump(self, offset): # real signature unknown; restored from __doc__
        """
        jump(offset: int) -> bool
        
        Jump to the given offset; return True on success. Note that jumping to
        an offset is not very reliable, and the 'section' attribute may point
        to an unexpected section.
        """
        return False

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def offset(self): # real signature unknown; restored from __doc__
        """
        offset() -> int
        
        Return the current offset.
        """
        return 0

    def step(self): # real signature unknown; restored from __doc__
        """
        step() -> bool
        
        Step forward in the file
        """
        return False

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, file): # real signature unknown; restored from __doc__
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    section = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current section, as a TagSection object."""



class TagSection(object):
    """
    TagSection(text: str)
    
    Provide methods to access RFC822-style header sections, like those
    found in debian/control or Packages files.
    
    TagSection() behave like read-only dictionaries and also provide access
    to the functions provided by the C++ class (e.g. find)
    """
    def bytes(self): # real signature unknown; restored from __doc__
        """
        bytes() -> int
        
        Return the number of bytes this section is large.
        """
        return 0

    def find(self, name, default=None): # real signature unknown; restored from __doc__
        """
        find(name: str[, default = None]) -> str
        
        Find the key given by 'name' and return the value. If the key can
        not be found, return 'default'.
        """
        return ""

    def find_flag(self, name): # real signature unknown; restored from __doc__
        """
        find_flag(name: str) -> int
        
        Return 1 if the key's value is 'yes' or a similar value describing
        a boolean true. If the field does not exist, or does not have such a
        value, return 0.
        """
        return 0

    def find_raw(self, name, default=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        find_raw(name: str[, default = None] -> str
        
        Same as find(), but returns the complete 'key: value' field; instead of
        just the value.
        """
        pass

    def get(self, *args, **kwargs): # real signature unknown
        """
        find(name: str[, default = None]) -> str
        
        Find the key given by 'name' and return the value. If the key can
        not be found, return 'default'.
        """
        pass

    def has_key(self, name): # real signature unknown; restored from __doc__
        """
        has_key(name: str) -> bool
        
        Return True if the key given by 'name' exists, False otherwise.
        """
        return False

    def keys(self): # real signature unknown; restored from __doc__
        """
        keys() -> list
        
        Return a list of all keys.
        """
        return []

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, text): # real signature unknown; restored from __doc__
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass


class Version(object):
    """ Version Object """
    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
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

    arch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The architecture of this specific version of the package."""

    depends_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A dictionary mapping dependency types to lists (A) of lists (B) of
apt_pkg.Dependency objects. The lists (B) represent or dependencies
like 'a || b'."""

    depends_list_str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Same as depends_list, except that the apt_pkg.Dependency objects
are 3-tuples of the form (name, version, operator); where operator
is one of '<', '<=', '=', '>=', '>'."""

    downloadable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the version can be downloaded."""

    file_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of tuples (packagefile: apt_pkg.PackageFile, index: int) for the
PackageFile objects related to this package. The index can be used
to retrieve the record of this package version."""

    hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The numeric hash of the version used in the internal storage."""

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The numeric ID of the package."""

    installed_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The installed size of this package version."""

    multi_arch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Multi-arch state of this package, as an integer. See
the various MULTI_ARCH_* members."""

    parent_pkg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The parent package of this version."""

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The priority of the package as an integer, which can be compared to
the constants PRI_EXTRA, PRI_IMPORTANT, PRI_OPTIONAL, PRI_REQUIRED,
PRI_STANDARD of the apt_pkg module."""

    priority_str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The priority of the package, as a string."""

    provides_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of all packages provided by this version. The list contains
tuples in the format (providesname, providesver, version)
where 'version' is an apt_pkg.Version object."""

    section = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The section of this package version."""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of the package file."""

    translated_description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An apt_pkg.Description object for the translated description if
available or the untranslated fallback."""

    ver_str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The version string."""


    MULTI_ARCH_ALL = 1
    MULTI_ARCH_ALLOWED = 8
    MULTI_ARCH_ALL_ALLOWED = 9
    MULTI_ARCH_ALL_FOREIGN = 3
    MULTI_ARCH_FOREIGN = 2
    MULTI_ARCH_NONE = 0
    MULTI_ARCH_SAME = 4


# variables with complex values

Config = None # (!) real value is ''

config = Config

RewritePackageOrder = [
    'Package',
    'Essential',
    'Status',
    'Priority',
    'Section',
    'Installed-Size',
    'Maintainer',
    'Original-Maintainer',
    'Architecture',
    'Source',
    'Version',
    'Revision',
    'Config-Version',
    'Replaces',
    'Provides',
    'Depends',
    'Pre-Depends',
    'Recommends',
    'Suggests',
    'Conflicts',
    'Breaks',
    'Conffiles',
    'Filename',
    'Size',
    'MD5Sum',
    'SHA1',
    'SHA256',
    'SHA512',
    'MSDOS-Filename',
    'Description',
]

RewriteSourceOrder = [
    'Package',
    'Source',
    'Binary',
    'Version',
    'Priority',
    'Section',
    'Maintainer',
    'Original-Maintainer',
    'Build-Depends',
    'Build-Depends-Indep',
    'Build-Conflicts',
    'Build-Conflicts-Indep',
    'Architecture',
    'Standards-Version',
    'Format',
    'Directory',
    'Files',
]

REWRITE_PACKAGE_ORDER = [
    'Package',
    'Essential',
    'Status',
    'Priority',
    'Section',
    'Installed-Size',
    'Maintainer',
    'Original-Maintainer',
    'Architecture',
    'Source',
    'Version',
    'Revision',
    'Config-Version',
    'Replaces',
    'Provides',
    'Depends',
    'Pre-Depends',
    'Recommends',
    'Suggests',
    'Conflicts',
    'Breaks',
    'Conffiles',
    'Filename',
    'Size',
    'MD5Sum',
    'SHA1',
    'SHA256',
    'SHA512',
    'MSDOS-Filename',
    'Description',
]

REWRITE_SOURCE_ORDER = [
    'Package',
    'Source',
    'Binary',
    'Version',
    'Priority',
    'Section',
    'Maintainer',
    'Original-Maintainer',
    'Build-Depends',
    'Build-Depends-Indep',
    'Build-Conflicts',
    'Build-Conflicts-Indep',
    'Architecture',
    'Standards-Version',
    'Format',
    'Directory',
    'Files',
]

_C_API = None # (!) real value is ''

