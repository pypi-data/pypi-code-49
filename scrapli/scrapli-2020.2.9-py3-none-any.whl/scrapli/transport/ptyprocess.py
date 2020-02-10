"""
Ptyprocess is under the ISC license, as code derived from Pexpect.
    http://opensource.org/licenses/ISC

Copyright (c) 2013-2014, Pexpect development team
Copyright (c) 2012, Noah Spurrier <noah@noah.org>

PERMISSION TO USE, COPY, MODIFY, AND/OR DISTRIBUTE THIS SOFTWARE FOR ANY PURPOSE
WITH OR WITHOUT FEE IS HEREBY GRANTED, PROVIDED THAT THE ABOVE COPYRIGHT NOTICE
AND THIS PERMISSION NOTICE APPEAR IN ALL COPIES. THE SOFTWARE IS PROVIDED
"AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE
INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT
SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL
DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING
OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

Thank you to the folks who create and maintain pexpect, vendoring this here
has been ridiculously helpful! -CM
"""

import builtins
import errno
import fcntl
import io
import os
import pty
import resource
import signal
import struct
import sys
import termios
import time
from pty import CHILD, STDIN_FILENO
from shutil import which
from typing import Type, TypeVar


class PtyProcessError(Exception):
    """Generic error class for this package."""


PtyProcessType = TypeVar("PtyProcessType", bound="PtyProcess")


def _byte(i):
    return bytes([i])


_EOF, _INTR = None, None


def _make_eof_intr():
    """Set constants _EOF and _INTR.

    This avoids doing potentially costly operations on module load.
    """
    global _EOF, _INTR
    if (_EOF is not None) and (_INTR is not None):
        return

    # inherit EOF and INTR definitions from controlling process.
    try:
        from termios import VEOF, VINTR

        fd = None
        for name in "stdin", "stdout":
            stream = getattr(sys, "__%s__" % name, None)
            if stream is None or not hasattr(stream, "fileno"):
                continue
            try:
                fd = stream.fileno()
            except ValueError:
                continue
        if fd is None:
            # no fd, raise ValueError to fallback on CEOF, CINTR
            raise ValueError("No stream has a fileno")
        intr = ord(termios.tcgetattr(fd)[6][VINTR])
        eof = ord(termios.tcgetattr(fd)[6][VEOF])
    except (ImportError, OSError, IOError, ValueError, termios.error):
        # unless the controlling process is also not a terminal,
        # such as cron(1), or when stdin and stdout are both closed.
        # Fall-back to using CEOF and CINTR. There
        try:
            from termios import CEOF, CINTR

            (intr, eof) = (CINTR, CEOF)
        except ImportError:
            #                         ^C, ^D
            (intr, eof) = (3, 4)

    _INTR = _byte(intr)
    _EOF = _byte(eof)


def _setecho(fd, state):
    errmsg = "setecho() may not be called on this platform (it may still be possible to enable/disable echo when spawning the child process)"

    try:
        attr = termios.tcgetattr(fd)
    except termios.error as err:
        if err.args[0] == errno.EINVAL:
            raise IOError(err.args[0], "%s: %s." % (err.args[1], errmsg))
        raise

    if state:
        attr[3] = attr[3] | termios.ECHO
    else:
        attr[3] = attr[3] & ~termios.ECHO

    try:
        # I tried TCSADRAIN and TCSAFLUSH, but these were inconsistent and
        # blocked on some platforms. TCSADRAIN would probably be ideal.
        termios.tcsetattr(fd, termios.TCSANOW, attr)
    except IOError as err:
        if err.args[0] == errno.EINVAL:
            raise IOError(err.args[0], "%s: %s." % (err.args[1], errmsg))
        raise


def _setwinsize(fd, rows, cols):
    # Some very old platforms have a bug that causes the value for
    # termios.TIOCSWINSZ to be truncated. There was a hack here to work
    # around this, but it caused problems with newer platforms so has been
    # removed. For details see https://github.com/pexpect/pexpect/issues/39
    TIOCSWINSZ = getattr(termios, "TIOCSWINSZ", -2146929561)
    # Note, assume ws_xpixel and ws_ypixel are zero.
    s = struct.pack("HHHH", rows, cols, 0, 0)
    fcntl.ioctl(fd, TIOCSWINSZ, s)


class PtyProcess(object):
    """This class represents a process running in a pseudoterminal.

    The main constructor is the :meth:`spawn` classmethod.
    """

    string_type = bytes
    linesep = os.linesep.encode("ascii")
    crlf = "\r\n".encode("ascii")

    @staticmethod
    def write_to_stdout(b):
        try:
            return sys.stdout.buffer.write(b)
        except AttributeError:
            # If stdout has been replaced, it may not have .buffer
            return sys.stdout.write(b.decode("ascii", "replace"))

    encoding = None
    argv = None
    env = None
    launch_dir = None

    def __init__(self, pid, fd):
        _make_eof_intr()  # Ensure _EOF and _INTR are calculated
        self.pid = pid
        self.fd = fd
        readf = io.open(fd, "rb", buffering=0)
        writef = io.open(fd, "wb", buffering=0, closefd=False)
        self.fileobj = io.BufferedRWPair(readf, writef)

        self.terminated = False
        self.closed = False
        self.exitstatus = None
        self.signalstatus = None
        # status returned by os.waitpid
        self.status = None
        self.flag_eof = False
        # Used by close() to give kernel time to update process status.
        # Time in seconds.
        self.delayafterclose = 0.1
        # Used by terminate() to give kernel time to update process status.
        # Time in seconds.
        self.delayafterterminate = 0.1

    @classmethod
    def spawn(
        cls: Type[PtyProcessType],
        argv,
        cwd=None,
        env=None,
        echo=True,
        preexec_fn=None,
        dimensions=(24, 80),
        pass_fds=(),
    ) -> PtyProcessType:
        """Start the given command in a child process in a pseudo terminal.

        This does all the fork/exec type of stuff for a pty, and returns an
        instance of PtyProcess.

        If preexec_fn is supplied, it will be called with no arguments in the
        child process before exec-ing the specified command.
        It may, for instance, set signal handlers to SIG_DFL or SIG_IGN.

        Dimensions of the psuedoterminal used for the subprocess can be
        specified as a tuple (rows, cols), or the default (24, 80) will be used.

        By default, all file descriptors except 0, 1 and 2 are closed. This
        behavior can be overridden with pass_fds, a list of file descriptors to
        keep open between the parent and the child.
        """
        # Note that it is difficult for this method to fail.
        # You cannot detect if the child process cannot start.
        # So the only way you can tell if the child process started
        # or not is to try to read from the file descriptor. If you get
        # EOF immediately then it means that the child is already dead.
        # That may not necessarily be bad because you may have spawned a child
        # that performs some task; creates no stdout output; and then dies.

        if not isinstance(argv, (list, tuple)):
            raise TypeError("Expected a list or tuple for argv, got %r" % argv)

        # Shallow copy of argv so we can modify it
        argv = argv[:]
        command = argv[0]

        command_with_path = which(command)
        if command_with_path is None:
            raise FileNotFoundError(
                "The command was not found or was not " + "executable: %s." % command
            )
        command = command_with_path
        argv[0] = command

        # [issue #119] To prevent the case where exec fails and the user is
        # stuck interacting with a python child process instead of whatever
        # was expected, we implement the solution from
        # http://stackoverflow.com/a/3703179 to pass the exception to the
        # parent process

        # [issue #119] 1. Before forking, open a pipe in the parent process.
        exec_err_pipe_read, exec_err_pipe_write = os.pipe()

        pid, fd = pty.fork()

        # Some platforms must call setwinsize() and setecho() from the
        # child process, and others from the master process. We do both,
        # allowing IOError for either.

        if pid == CHILD:
            # set window size
            try:
                _setwinsize(STDIN_FILENO, *dimensions)
            except IOError as err:
                if err.args[0] not in (errno.EINVAL, errno.ENOTTY):
                    raise

            # disable echo if spawn argument echo was unset
            if not echo:
                try:
                    _setecho(STDIN_FILENO, False)
                except (IOError, termios.error) as err:
                    if err.args[0] not in (errno.EINVAL, errno.ENOTTY):
                        raise

            # [issue #119] 3. The child closes the reading end and sets the
            # close-on-exec flag for the writing end.
            os.close(exec_err_pipe_read)
            fcntl.fcntl(exec_err_pipe_write, fcntl.F_SETFD, fcntl.FD_CLOEXEC)

            # Do not allow child to inherit open file descriptors from parent,
            # with the exception of the exec_err_pipe_write of the pipe
            # and pass_fds.
            # Impose ceiling on max_fd: AIX bugfix for users with unlimited
            # nofiles where resource.RLIMIT_NOFILE is 2^63-1 and os.closerange()
            # occasionally raises out of range error
            max_fd = min(1048576, resource.getrlimit(resource.RLIMIT_NOFILE)[0])
            spass_fds = sorted(set(pass_fds) | {exec_err_pipe_write})
            for pair in zip([2] + spass_fds, spass_fds + [max_fd]):
                os.closerange(pair[0] + 1, pair[1])

            if cwd is not None:
                os.chdir(cwd)

            if preexec_fn is not None:
                try:
                    preexec_fn()
                except Exception as e:
                    ename = type(e).__name__
                    tosend = "{}:0:{}".format(ename, str(e))
                    tosend = tosend.encode("utf-8")

                    os.write(exec_err_pipe_write, tosend)
                    os.close(exec_err_pipe_write)
                    os._exit(1)

            try:
                if env is None:
                    os.execv(command, argv)
                else:
                    os.execvpe(command, argv, env)
            except OSError as err:
                # [issue #119] 5. If exec fails, the child writes the error
                # code back to the parent using the pipe, then exits.
                tosend = "OSError:{}:{}".format(err.errno, str(err))
                tosend = tosend.encode("utf-8")
                os.write(exec_err_pipe_write, tosend)
                os.close(exec_err_pipe_write)
                os._exit(os.EX_OSERR)

        # Parent
        inst = cls(pid, fd)

        # Set some informational attributes
        inst.argv = argv
        if env is not None:
            inst.env = env
        if cwd is not None:
            inst.launch_dir = cwd

        # [issue #119] 2. After forking, the parent closes the writing end
        # of the pipe and reads from the reading end.
        os.close(exec_err_pipe_write)
        exec_err_data = os.read(exec_err_pipe_read, 4096)
        os.close(exec_err_pipe_read)

        # [issue #119] 6. The parent reads eof (a zero-length read) if the
        # child successfully performed exec, since close-on-exec made
        # successful exec close the writing end of the pipe. Or, if exec
        # failed, the parent reads the error code and can proceed
        # accordingly. Either way, the parent blocks until the child calls
        # exec.
        if len(exec_err_data) != 0:
            try:
                errclass, errno_s, errmsg = exec_err_data.split(b":", 2)
                exctype = getattr(builtins, errclass.decode("ascii"), Exception)

                exception = exctype(errmsg.decode("utf-8", "replace"))
                if exctype is OSError:
                    exception.errno = int(errno_s)
            except:
                raise Exception("Subprocess failed, got bad error data: %r" % exec_err_data)
            else:
                raise exception

        try:
            inst.setwinsize(*dimensions)
        except IOError as err:
            if err.args[0] not in (errno.EINVAL, errno.ENOTTY, errno.ENXIO):
                raise

        return inst

    def __repr__(self):
        clsname = type(self).__name__
        if self.argv is not None:
            args = [repr(self.argv)]
            if self.env is not None:
                args.append("env=%r" % self.env)
            if self.launch_dir is not None:
                args.append("cwd=%r" % self.launch_dir)

            return "{}.spawn({})".format(clsname, ", ".join(args))

        else:
            return "{}(pid={}, fd={})".format(clsname, self.pid, self.fd)

    @staticmethod
    def _coerce_send_string(s):
        if not isinstance(s, bytes):
            return s.encode("utf-8")
        return s

    @staticmethod
    def _coerce_read_string(s):
        return s

    def __del__(self):
        """This makes sure that no system resources are left open. Python only
        garbage collects Python objects. OS file descriptors are not Python
        objects, so they must be handled explicitly. If the child file
        descriptor was opened outside of this class (passed to the constructor)
        then this does not close it. """

        if not self.closed:
            # It is possible for __del__ methods to execute during the
            # teardown of the Python VM itself. Thus self.close() may
            # trigger an exception because os.close may be None.
            try:
                self.close()
            # which exception, shouldn't we catch explicitly .. ?
            except:
                pass

    def fileno(self):
        """This returns the file descriptor of the pty for the child.
        """
        return self.fd

    def close(self, force=True):
        """This closes the connection with the child application. Note that
        calling close() more than once is valid. This emulates standard Python
        behavior with files. Set force to True if you want to make sure that
        the child is terminated (SIGKILL is sent if the child ignores SIGHUP
        and SIGINT). """
        if not self.closed:
            self.flush()
            self.fileobj.close()  # Closes the file descriptor
            # Give kernel time to update process status.
            time.sleep(self.delayafterclose)
            if self.isalive():
                if not self.terminate(force):
                    raise PtyProcessError("Could not terminate the child.")
            self.fd = -1
            self.closed = True
            # self.pid = None

    def flush(self) -> None:
        """This does nothing. It is here to support the interface for a
        File-like object. """

        pass

    def isatty(self):
        """This returns True if the file descriptor is open and connected to a
        tty(-like) device, else False.

        On SVR4-style platforms implementing streams, such as SunOS and HP-UX,
        the child pty may not appear as a terminal device.  This means
        methods such as setecho(), setwinsize(), getwinsize() may raise an
        IOError. """

        return os.isatty(self.fd)

    def waitnoecho(self, timeout=None):
        """This waits until the terminal ECHO flag is set False. This returns
        True if the echo mode is off. This returns False if the ECHO flag was
        not set False before the timeout. This can be used to detect when the
        child is waiting for a password. Usually a child application will turn
        off echo mode when it is waiting for the user to enter a password. For
        example, instead of expecting the "password:" prompt you can wait for
        the child to set ECHO off::

            p = pexpect.spawn('ssh user@example.com')
            p.waitnoecho()
            p.sendline(mypassword)

        If timeout==None then this method to block until ECHO flag is False.
        """

        if timeout is not None:
            end_time = time.time() + timeout
        while True:
            if not self.getecho():
                return True
            if timeout < 0 and timeout is not None:
                return False
            if timeout is not None:
                timeout = end_time - time.time()
            time.sleep(0.1)

    def getecho(self):
        """This returns the terminal echo mode. This returns True if echo is
        on or False if echo is off. Child applications that are expecting you
        to enter a password often set ECHO False. See waitnoecho().

        Not supported on platforms where ``isatty()`` returns False.  """

        try:
            attr = termios.tcgetattr(self.fd)
        except termios.error as err:
            errmsg = "getecho() may not be called on this platform"
            if err.args[0] == errno.EINVAL:
                raise IOError(err.args[0], "%s: %s." % (err.args[1], errmsg))
            raise

        self.echo = bool(attr[3] & termios.ECHO)
        return self.echo

    def setecho(self, state):
        """This sets the terminal echo mode on or off. Note that anything the
        child sent before the echo will be lost, so you should be sure that
        your input buffer is empty before you call setecho(). For example, the
        following will work as expected::

            p = pexpect.spawn('cat') # Echo is on by default.
            p.sendline('1234') # We expect see this twice from the child...
            p.expect(['1234']) # ... once from the tty echo...
            p.expect(['1234']) # ... and again from cat itself.
            p.setecho(False) # Turn off tty echo
            p.sendline('abcd') # We will set this only once (echoed by cat).
            p.sendline('wxyz') # We will set this only once (echoed by cat)
            p.expect(['abcd'])
            p.expect(['wxyz'])

        The following WILL NOT WORK because the lines sent before the setecho
        will be lost::

            p = pexpect.spawn('cat')
            p.sendline('1234')
            p.setecho(False) # Turn off tty echo
            p.sendline('abcd') # We will set this only once (echoed by cat).
            p.sendline('wxyz') # We will set this only once (echoed by cat)
            p.expect(['1234'])
            p.expect(['1234'])
            p.expect(['abcd'])
            p.expect(['wxyz'])


        Not supported on platforms where ``isatty()`` returns False.
        """
        _setecho(self.fd, state)

        self.echo = state

    def read(self, size=1024) -> bytes:
        """Read and return at most ``size`` bytes from the pty.

        Can block if there is nothing to read. Raises :exc:`EOFError` if the
        terminal was closed.

        Unlike Pexpect's ``read_nonblocking`` method, this doesn't try to deal
        with the vagaries of EOF on platforms that do strange things, like IRIX
        or older Solaris systems. It handles the errno=EIO pattern used on
        Linux, and the empty-string return used on BSD platforms and (seemingly)
        on recent Solaris.
        """
        try:
            s = self.fileobj.read1(size)
        except (OSError, IOError) as err:
            if err.args[0] == errno.EIO:
                # Linux-style EOF
                self.flag_eof = True
                raise EOFError("End Of File (EOF). Exception style platform.")
            raise
        if s == b"":
            # BSD-style EOF (also appears to work on recent Solaris (OpenIndiana))
            self.flag_eof = True
            raise EOFError("End Of File (EOF). Empty string style platform.")

        return s

    def readline(self):
        """Read one line from the pseudoterminal, and return it as unicode.

        Can block if there is nothing to read. Raises :exc:`EOFError` if the
        terminal was closed.
        """
        try:
            s = self.fileobj.readline()
        except (OSError, IOError) as err:
            if err.args[0] == errno.EIO:
                # Linux-style EOF
                self.flag_eof = True
                raise EOFError("End Of File (EOF). Exception style platform.")
            raise
        if s == b"":
            # BSD-style EOF (also appears to work on recent Solaris (OpenIndiana))
            self.flag_eof = True
            raise EOFError("End Of File (EOF). Empty string style platform.")

        return s

    def _writeb(self, b, flush=True):
        n = self.fileobj.write(b)
        if flush:
            self.fileobj.flush()
        return n

    def write(self, s, flush=True) -> int:
        """Write bytes to the pseudoterminal.

        Returns the number of bytes written.
        """
        return self._writeb(s, flush=flush)

    def sendcontrol(self, char):
        """Helper method that wraps send() with mnemonic access for sending control
        character to the child (such as Ctrl-C or Ctrl-D).  For example, to send
        Ctrl-G (ASCII 7, bell, '\a')::

            child.sendcontrol('g')

        See also, sendintr() and sendeof().
        """
        char = char.lower()
        a = ord(char)
        if 97 <= a <= 122:
            a = a - ord("a") + 1
            byte = _byte(a)
            return self._writeb(byte), byte
        d = {
            "@": 0,
            "`": 0,
            "[": 27,
            "{": 27,
            "\\": 28,
            "|": 28,
            "]": 29,
            "}": 29,
            "^": 30,
            "~": 30,
            "_": 31,
            "?": 127,
        }
        if char not in d:
            return 0, b""

        byte = _byte(d[char])
        return self._writeb(byte), byte

    def sendeof(self):
        """This sends an EOF to the child. This sends a character which causes
        the pending parent output buffer to be sent to the waiting child
        program without waiting for end-of-line. If it is the first character
        of the line, the read() in the user program returns 0, which signifies
        end-of-file. This means to work as expected a sendeof() has to be
        called at the beginning of a line. This method does not send a newline.
        It is the responsibility of the caller to ensure the eof is sent at the
        beginning of a line. """

        return self._writeb(_EOF), _EOF

    def sendintr(self):
        """This sends a SIGINT to the child. It does not require
        the SIGINT to be the first character on a line. """

        return self._writeb(_INTR), _INTR

    def eof(self) -> bool:
        """This returns True if the EOF exception was ever raised.
        """

        return self.flag_eof

    def terminate(self, force=False):
        """This forces a child process to terminate. It starts nicely with
        SIGHUP and SIGINT. If "force" is True then moves onto SIGKILL. This
        returns True if the child was terminated. This returns False if the
        child could not be terminated. """

        if not self.isalive():
            return True
        try:
            self.kill(signal.SIGHUP)
            time.sleep(self.delayafterterminate)
            if not self.isalive():
                return True
            self.kill(signal.SIGCONT)
            time.sleep(self.delayafterterminate)
            if not self.isalive():
                return True
            self.kill(signal.SIGINT)
            time.sleep(self.delayafterterminate)
            if not self.isalive():
                return True
            if force:
                self.kill(signal.SIGKILL)
                time.sleep(self.delayafterterminate)
                if not self.isalive():
                    return True
                else:
                    return False
            return False
        except OSError:
            # I think there are kernel timing issues that sometimes cause
            # this to happen. I think isalive() reports True, but the
            # process is dead to the kernel.
            # Make one last attempt to see if the kernel is up to date.
            time.sleep(self.delayafterterminate)
            if not self.isalive():
                return True
            else:
                return False

    def wait(self):
        """This waits until the child exits. This is a blocking call. This will
        not read any data from the child, so this will block forever if the
        child has unread output and has terminated. In other words, the child
        may have printed output then called exit(), but, the child is
        technically still alive until its output is read by the parent. """

        if self.isalive():
            pid, status = os.waitpid(self.pid, 0)
        else:
            return self.exitstatus
        self.exitstatus = os.WEXITSTATUS(status)
        if os.WIFEXITED(status):
            self.status = status
            self.exitstatus = os.WEXITSTATUS(status)
            self.signalstatus = None
            self.terminated = True
        elif os.WIFSIGNALED(status):
            self.status = status
            self.exitstatus = None
            self.signalstatus = os.WTERMSIG(status)
            self.terminated = True
        elif os.WIFSTOPPED(status):  # pragma: no cover
            # You can't call wait() on a child process in the stopped state.
            raise PtyProcessError(
                "Called wait() on a stopped child "
                + "process. This is not supported. Is some other "
                + "process attempting job control with our child pid?"
            )
        return self.exitstatus

    def isalive(self) -> bool:
        """This tests if the child process is running or not. This is
        non-blocking. If the child was terminated then this will read the
        exitstatus or signalstatus of the child. This returns True if the child
        process appears to be running or False if not. It can take literally
        SECONDS for Solaris to return the right status. """

        if self.terminated:
            return False

        if self.flag_eof:
            # This is for Linux, which requires the blocking form
            # of waitpid to get the status of a defunct process.
            # This is super-lame. The flag_eof would have been set
            # in read_nonblocking(), so this should be safe.
            waitpid_options = 0
        else:
            waitpid_options = os.WNOHANG

        try:
            pid, status = os.waitpid(self.pid, waitpid_options)
        except OSError as e:
            # No child processes
            if e.errno == errno.ECHILD:
                raise PtyProcessError(
                    "isalive() encountered condition "
                    + 'where "terminated" is 0, but there was no child '
                    + "process. Did someone else call waitpid() "
                    + "on our process?"
                )
            else:
                raise

        # I have to do this twice for Solaris.
        # I can't even believe that I figured this out...
        # If waitpid() returns 0 it means that no child process
        # wishes to report, and the value of status is undefined.
        if pid == 0:
            try:
                ### os.WNOHANG) # Solaris!
                pid, status = os.waitpid(self.pid, waitpid_options)
            except OSError as e:  # pragma: no cover
                # This should never happen...
                if e.errno == errno.ECHILD:
                    raise PtyProcessError(
                        "isalive() encountered condition "
                        + "that should never happen. There was no child "
                        + "process. Did someone else call waitpid() "
                        + "on our process?"
                    )
                else:
                    raise

            # If pid is still 0 after two calls to waitpid() then the process
            # really is alive. This seems to work on all platforms, except for
            # Irix which seems to require a blocking call on waitpid or select,
            # so I let read_nonblocking take care of this situation
            # (unfortunately, this requires waiting through the timeout).
            if pid == 0:
                return True

        if pid == 0:
            return True

        if os.WIFEXITED(status):
            self.status = status
            self.exitstatus = os.WEXITSTATUS(status)
            self.signalstatus = None
            self.terminated = True
        elif os.WIFSIGNALED(status):
            self.status = status
            self.exitstatus = None
            self.signalstatus = os.WTERMSIG(status)
            self.terminated = True
        elif os.WIFSTOPPED(status):
            raise PtyProcessError(
                "isalive() encountered condition "
                + "where child process is stopped. This is not "
                + "supported. Is some other process attempting "
                + "job control with our child pid?"
            )
        return False

    def kill(self, sig) -> None:
        """Send the given signal to the child application.

        In keeping with UNIX tradition it has a misleading name. It does not
        necessarily kill the child unless you send the right signal. See the
        :mod:`signal` module for constants representing signal numbers.
        """

        # Same as os.kill, but the pid is given for you.
        if self.isalive():
            os.kill(self.pid, sig)

    def setwinsize(self, rows, cols):
        """Set the terminal window size of the child tty.

        This will cause a SIGWINCH signal to be sent to the child. This does not
        change the physical window size. It changes the size reported to
        TTY-aware applications like vi or curses -- applications that respond to
        the SIGWINCH signal.
        """
        return _setwinsize(self.fd, rows, cols)
