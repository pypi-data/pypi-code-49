#!/usr/bin/python
"""\
@file   exc.py
@author Nat Goodspeed
@date   2011-01-04
@brief  Utilities for manipulating Python exceptions

Copyright (c) 2011, Nat Goodspeed
"""

from builtins import object
import sys
from contextlib import contextmanager
import functools
import itertools

# default parameter distinct from None so None can validly be passed
_OMITTED = object()

class reraise(object):
    """
    Consider this cleanup pattern:

    try:
        some_code()
    except Exception:
        essential_cleanup()
        raise

    You want to perform the cleanup on exception, but nonetheless you want to
    propagate the original exception out to the caller, original traceback and
    all.

    Sadly, because of Python's global current exception, that works only if
    essential_cleanup() does not itself handle any exceptions. For instance:

    try:
        x = some_dict[some_key]
    except KeyError:
        print "No key %r" % some_key

    This innocuous code is enough to foul up the no-args 'raise' statement in
    the 'except' clause that calls essential_cleanup().

    You can capture sys.exc_info() and re-raise specifically that exception:

    try:
        some_code()
    except Exception:
        type, value, tb = sys.exc_info()
        essential_cleanup()
        raise type, value, tb

    But now you've constructed the kind of reference loop against which
    http://docs.python.org/release/2.5.4/lib/module-sys.html#l2h-5141
    specifically warns, storing a traceback into a local variable.

    This is better:

    try:
        some_code()
    except Exception:
        type, value, tb = sys.exc_info()
        try:
            essential_cleanup()
            raise type, value, tb
        finally:
            del tb

    but you must admit it's pretty verbose -- it almost completely obscures
    the nature of the cleanup. Plus it's a PITB to remember.

    reraise encapsulates that last pattern, permitting you to write:

    try:
        some_code()
    except Exception:
        with reraise():
            essential_cleanup()

    This is as terse as the original, guarantees to preserve the original
    exception and avoids reference loops.

    As in the original construct, if essential_cleanup() itself raises an
    exception, that exception propagates out to the caller instead of the one
    raised by some_code().
    """
    def __enter__(self):
        self.type, self.value, self.tb = sys.exc_info()
        return self

    def __exit__(self, type, value, tb):
        try:
            if type or value or tb:
                # If code in the 'with' block raised an exception, just let that
                # exception propagate.
                return False

            if not (self.type or self.value or self.tb):
                # If there wasn't a current exception at __enter__() time,
                # don't raise one now.
                return False

            # This 'with' statement was entered with a current exception, and
            # code in the block did not override it with a newer exception.
            # Re-raise the one we captured in __enter__().
            _raise_with(self.type, self.value, self.tb)

        finally:
            # No matter how we leave this method, always delete the traceback
            # member.
            del self.tb

try:
    # We must import a separate module, instead of directly embedding the
    # Python 2 implementation of _raise_with() here, because we can't catch
    # SyntaxError in the module being scanned!
    from .raise_with2 import raise_with as _raise_with
except SyntaxError:
    # Python 3
    def _raise_with(type, value, traceback):
        # https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement
        # The _raise_from() call below is the closest Python 3 equivalent I
        # can find to the classic Python 2 'raise type, value, traceback'.
        # - If type and value are both from sys.exc_info(), then in effect
        #   value implies type, and the type parameter is unimportant.
        # - Traceback is attached by with_traceback() as shown.
        # - Passing cause=None cues the raise statement to NOT chain the
        #   current exception.
        _raise_from(value.with_traceback(traceback), cause=None)

def retry_func(func, *args, **kwds):
    """
    Call the passed callable 'func' with *args, **kwds. Return whatever it
    successfully returns. But on certain exceptions, retry the call.

    keyword-only args:
    exc=Exception
    times=3
    when=lambda e: True
    between=lambda tries: None

    If func(*args, **kwds) raises an exception of class 'exc', and if
    bool('when'(exception)) is True, retry the call up to 'times'. 'times' is
    the maximum number of times retry_func() will attempt to call 'func': a
    first "try" followed by up to ('times'-1) "retries".

    If a retry is necessary, retry_func() will call your 'between' callable,
    passing an int indicating how many tries it has attempted so far: 1, 2, ...
    This may be used to log the exception (via sys.exc_info()) and the fact
    that the operation is being retried. 'between' is not called after 'times'
    exceptions. That is, 'between' will be called at most ('times'-1) times.
    It is called when retry_func() is about to retry the original call, but
    not when retry_func() is giving up and letting the exception propagate.

    As in the case of try...except (exA, exB), 'exc' can be a tuple of
    exception classes.

    The filter callable 'when' can be used to select (e.g.) OSError
    exceptions with particular errno values.

    Example:

    retry_func(os.remove, somefilename,
               exc=OSError, when=lamba e: e.errno == errno.EACCES)

    If func(*args, **kwds) raises an exception that doesn't match 'exc', or if
    bool('when'(exception)) is False, or if retry_func() has already called
    'func' 'times' times, the exception will propagate to the caller.

    retry_func() does not examine the value returned by 'func'. If you want to
    retry somefunc(somearg) until you see a particular return value, define a
    distinctive Exception subclass. Then define a function that will call your
    target 'func' and raise your distinctive Exception subclass if the return
    value isn't what you want. Then pass that wrapper function and your
    distinctive Exception subclass to retry_func().

    Example:

    class NoneBad(Exception):
        pass

    def noNone(func, *args, **kwds):
        ret = func(*args, **kwds)
        if ret is None:
            raise NoneBad()
        return ret

    value = retry_func(noNone, somefunc, somearg, exc=NoneBad)
    # value will not be None. If calling somefunc(somearg) 'times' times
    # continues to produce None, this call will raise NoneBad instead.
    """
    exc     = kwds.pop("exc", Exception)
    times   = kwds.pop("times", 3)
    when    = kwds.pop("when", lambda e: True)
    between = kwds.pop("between", lambda tries: None)

    for tries in itertools.count(1):
        try:
            return func(*args, **kwds)
        except exc as e:
            # Here we know the exception matches 'exc'.
            if not when(e):
                # Doesn't match caller's 'when' condition
                raise
            if tries >= times:
                # func() failed too many times, give up
                raise
            # We're about to retry. Call 'between'.
            between(tries)

class retry(object):
    """
    decorator version of retry_func()

    Example:

    @retry(exc=OSError, when=lamba e: e.errno == errno.EACCES,
           between=lambda tries: time.sleep(1))
    def my_remove(path):
        os.remove(path)
    """
    def __init__(self, exc=Exception, times=3, when=lambda e: True, between=lambda tries: None):
        self.exc     = exc
        self.times   = times
        self.when    = when
        self.between = between

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwds):
            return retry_func(func,
                              exc=self.exc, times=self.times,
                              when=self.when, between=self.between,
                              *args, **kwds)
        return wrapper

def describe(exc):
    """
    Return a string 'ClassName: string message', given an 'exc' of type
    ClassName whose str(exc) returns 'string message'.

    'exc' can be any type, it's just really useful for exceptions.

    If exc2 of type Class2 was caused by exc1 of type Class 1, which was in
    turn caused by exc0 of type Class0, the returned string has the form:

    'Class0->Class1->Class2: string message'
    """
    return "%s: %s" % ('->'.join(x.__class__.__name__ for x in rexchain(exc)), exc)

def exchain(exc):
    """
    Given an exception instance, iterate through all the __context__ exceptions,
    from most recent to the original failure. That is, yield 'exc' first, then
    'exc.__context__', then 'exc.__context__.__context__', etc.
    """
    try:
        while exc is not None:
            yield exc
            exc = exc.__context__
    except AttributeError:
        pass

def rexchain(exc):
    """
    Given an exception instance, iterate through all the __context__ exceptions
    in reverse order, from the original failure to most recent. That is, yield
    'exc.__context__.__context__' first, then 'exc.__context__', then 'exc'.
    """
    # It's tempting to just return reversed(list(exchain(exc))), and maybe
    # that's the most efficient way. We never expect a huge long exception
    # chain. But we also try to avoid algorithms that require traversing all
    # of an iterable before retrieving any of it. Let's try it this way.
    try:
        # 'yield from' doesn't arrive until Python 3, and even now we're still
        # trying to maintain compatibility with Python 2...
        for x in rexchain(exc.__context__):
            yield x
    except AttributeError:
        pass

    if exc is not None:
        yield exc

def caused_by(exc, classes):
    """
    Given an exception instance 'exc', return which of the underlying causes
    of 'exc' is an instance of any of the tuple 'classes' (which may be passed
    as a scalar class), else None. That is:

    caused_by(exc, OSError)

    returns exc if exc is itself an instance of OSError, or exc.__context__ if
    that is an instance of OSError, or exc.__context__.__context__ if that is an
    instance of OSError...

    Python 3's OSError subclasses FileNotFoundError, FileExistsError et al.
    are particularly useful here.
    """
    try:
        # Loop over exchain(exc), checking each underlying exception in turn
        # to see if it's an instance of any of the passed classes. Stop and
        # return the first one we find.
        return next(x for x in exchain(exc) if isinstance(x, classes))
    except StopIteration:
        # No exception in exchain(exc) is an instance of any of 'classes'.
        return None

def caused_by_errno(exc, errnos):
    """
    Given an exception instance 'exc', return which of the underlying causes
    of 'exc' is an instance of OSError whose errno attribute matches any of
    the values in the tuple 'errnos' (which may be passed as a scalar int),
    else None. That is:

    caused_by_errno(exc, errno.EEXIST)

    returns exc if exc is an instance of OSError whose errno == errno.EEXIST,
    or if exc.__context__ if that matches, or exc.__context__.__context__ if that
    matches...

    If one OSError that does not match turns out to have been caused, directly
    or indirectly, by another OSError that does match, the latter will be
    returned. That is, caused_by_errno() doesn't stop at the first OSError and
    then test; it continues digging until it finds a match or runs out of
    underlying exceptions.

    This function is primarily useful for Python 2 compatibility. In a pure
    Python 3 script, write caused_by(exc, FileNotFoundError) instead of
    caused_by_errno(exc, errno.ENOENT).
    """
    # Unless 'errnos' was passed as a tuple, make a tuple containing it.
    if not isinstance(errnos, tuple):
        errnos = (errnos,)
    # Our promise to search for a matching OSError despite finding
    # non-matching OSError instances prohibits us from simply calling
    # caused_by(exc, OSError) and then testing.
    try:
        return next(x for x in exchain(exc)
                    if isinstance(x, OSError) and x.errno in errnos)
    except StopIteration:
        return None

@contextmanager
def translate_to(throw, catch=Exception):
    """
    Re-raise any 'catch' exception raised within the 'with' block as
    exception 'throw' instead.

    Usage:

    # Error is just an example of a module-local exception class
    class Error(Exception):
        pass

    with translate_to(Error):
        # Any Exception raised inside this 'with' block will be re-raised as
        # module-local exception class Error, whose message is
        # 'OriginalExceptionTypeName: original exception message'
        os.remove(nonexistent)

    or more specifically:

    with translate_to(Error, catch=(IOError, OSError)):
        with open('nonexistent.txt') as infile:
            content = infile.read()

    'throw' is the exception to raise when anything within the 'with' block
    raises any exception matching 'catch'. 'throw' can be the Exception
    subclass instance you want to raise, or the Exception subclass you want to
    raise -- more generally, a callable accepting (message string) that
    returns the Exception subclass instance you want to raise.

    'catch' is either an exception class, or a tuple of exception classes --
    as supported by the try statement's except clause. If omitted, it defaults
    to Exception. Any exception matching 'catch' will be re-raised as 'throw'.

    Cached 'throw' usage:

    translate = functools.partial(translate_to, Error)

    # Don't forget to pass multiple exceptions as a tuple!
    with translate((IOError, OSError)):
        os.remove(nonexistent)
    """
    try:
        yield
    except catch as err:
        raise_from(throw, cause=err)

def raise_from(throw, cause=_OMITTED):
    """
    Raise 'throw' (an Exception subclass instance), chaining 'cause' (an
    originating exception instance). If 'cause' is omitted, it's the
    current exception object from sys.exc_info().

    Passing cause=None is explicitly supported (Python 3.3+):
    https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement
    It suppresses exception chaining, in a context in which 'raise' would
    otherwise implicitly chain.

    If you pass 'throw' as an Exception subclass instead -- or more
    generally, a callable returning an Exception subclass instance -- it
    should accept (message string) as its argument. It will be called with
    describe(cause).

    This function blurs the distinction between Python 2 and 3. In both
    environments, code that catches the exception indicated by 'throw' can
    retrieve attribute '__context__' (or '__cause__'). That's the native idiom
    for Python 3, which raise_from() also supports in Python 2.

    When called from an 'except' block in Python 3, raise_from() isn't
    strictly necessary: the interpreter will automatically chain the original
    exception to whatever you 'raise' as '__context__'. ('__cause__' is only
    set by 'raise from'.) raise_from() is still helpful to a human reader,
    though, in that implicit '__context__' chaining is reported as:

    During handling of the above exception, another exception occurred:

    which sounds like a bug in your exception handler, rather than the message
    for explicit 'raise from' chaining ('__cause__' chaining):

    The above exception was the direct cause of the following exception:

    which more accurately describes the intentional translation to another
    Exception subclass.
    """
    if cause is _OMITTED:
        cause = sys.exc_info()[1]

    if not isinstance(throw, Exception):
        if cause is None:
            throw = throw()
        else:
            throw = throw(describe(cause))

    # by this time 'throw' is definitely an instance, not a class
    _raise_from(throw, cause)

try:
    # We must import a separate module, instead of directly embedding the
    # Python 3 implementation of _raise_from() here, because we can't catch
    # SyntaxError in the module being scanned!
    from .raise_from3 import raise_from as _raise_from

except SyntaxError:
    def _raise_from(throw, cause):
        """
        Python 2 implementation of raise_from(), which explicitly stores
        'cause' as both 'throw.__context__' and 'throw.__cause__'.
        """
        throw.__context__ = cause
        throw.__cause__ = cause
        # It would also be possible to use the traceback module to append the
        # original exception's traceback to the new exception's message, or
        # some such.
        raise throw

@contextmanager
def suppress(*exceptions):
    """
    Just like Python 3 contextlib.suppress(), which isn't available in Python 2:

    with suppress(IOError, OSError):
        print(open('nonexistent.txt').read())
    """
    try:
        yield
    except exceptions:
        pass

@contextmanager
def suppress_errno(*errnos):
    """
    Whereas suppress() unconditionally suppresses every exception of a
    specific exception class, suppress_errno() suppresses only OSError
    exceptions, and only those whose errno attribute matches any of the passed
    errnos values.

    with suppress_errno(errno.EEXIST):
        os.mkdir(subdir)
    """
    try:
        yield
    except OSError as err:
        if err.errno not in errnos:
            raise

def capture(func, *args, **kwds):
    """
    Sometimes we need to multiplex an exception through normal channels:
    return it from a function rather than raising it, collect it in a list,
    push it through a queue...

    capture() calls 'func(*args, **kwds)', captures any Exception subclass
    instance it might raise and returns it as the return value. If func()
    returns normally, capture() returns its return value.

    If you pass keyword-only argument _exc=ExceptionSubclass or
    _exc=(TupleOfExceptionSubclasses), only exceptions of those subclasses are
    captured; any others propagate to the caller. The name _exc minimizes the
    chance of collision with any keyword arguments you may want to pass to
    func().

    See also uncapture().
    """
    exc = kwds.pop('_exc', Exception)
    try:
        return func(*args, **kwds)
    except exc as err:
        return err

def uncapture(value):
    """
    uncapture() demultiplexes a value-or-Exception instance. If value isn't an
    Exception subclass instance, it returns it. If it's an Exception subclass
    instance, it raises it.

    This is a bit like C++ std::expected::value().

    See also capture().
    """
    if isinstance(value, Exception):
        raise value

    return value
