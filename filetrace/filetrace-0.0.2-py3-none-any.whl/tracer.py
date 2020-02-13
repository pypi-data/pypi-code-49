import sys
from ptrace.debugger import (
    PtraceDebugger,
    ProcessExit,
    ProcessSignal,
    NewProcessEvent,
    ProcessExecution,
)
from os.path import realpath
from logging import getLogger, error
from ptrace import PtraceError
from ptrace.error import PTRACE_ERRORS, writeError
from ptrace.func_call import FunctionCallOptions
from ptrace.debugger.child import createChild
from ptrace.tools import locateProgram
from errno import EPERM
from ptrace.syscall import SYSCALL_PROTOTYPES, FILENAME_ARGUMENTS


class FileRunTracer:
    def __init__(self, run_argumetns, options={}):
        self.run_argumetns = run_argumetns
        self.options = options
        self.debugger = PtraceDebugger()
        self._setup_file_filter()

    def pid_binary(self, pid):
        """ Return the binary path for a given pid """
        return realpath(f"/proc/{pid}/exe")

    def _setup_file_filter(self):
        """ Create fitler for syscals containg filename/path arguments"""
        self.filename_syscalls = set()  # Syscalls that we want to track
        for syscall, format in SYSCALL_PROTOTYPES.items():
            restype, arguments = format
            if any(argname in FILENAME_ARGUMENTS for argtype, argname in arguments):
                self.filename_syscalls.add(syscall)

    def run(self):
        self.debugger.traceFork()
        self.debugger.traceExec()
        self.syscall_options = FunctionCallOptions()
        process = self.createProcess()
        if not process:
            return
        try:
            self.syscallTraceLoop(process)
        except ProcessExit as event:
            self.processExited(event)
        except PtraceError as err:
            error("ptrace() error: %s" % err)
        except KeyboardInterrupt:
            error("Interrupted.")
        except PTRACE_ERRORS as err:
            writeError(getLogger(), err, "Debugger error")
        self.debugger.quit()

    def createProcess(self):
        self.trackExec(locateProgram(self.run_argumetns[0]))
        self.pid = pid = createChild(self.run_argumetns, False)
        try:
            return self.debugger.addProcess(pid, is_attached=True)
        except (ProcessExit, PtraceError) as err:
            if isinstance(err, PtraceError) and err.errno == EPERM:
                error(
                    "ERROR: You are not allowed to trace process %s"
                    " (permission denied or process already traced)" % pid
                )
            else:
                error("ERROR: Process can no be attached! %s" % err)
        return None

    def syscallTraceLoop(self, process):

        # First query to break at next syscall
        self.prepareProcess(process)

        while True:
            # No more process? Exit
            if not self.debugger:
                break

            # Wait until next syscall enter
            try:
                event = self.debugger.waitSyscall()
            except ProcessExit as event:
                self.processExited(event)
                continue
            except ProcessSignal as event:
                event.process.syscall(event.signum)
                continue
            except NewProcessEvent as event:
                self.newProcess(event)
                continue
            except ProcessExecution as event:
                self.processExecution(event)
                continue

            # Process syscall enter or exit
            self.syscall(event.process)

    def processExecution(self, event):
        """ new process being executed as a result of an exec/fork """
        process = event.process
        binary = realpath(f"/proc/{process.pid}/exe")
        self.trackExec(binary)
        process.syscall()

    def ignoreSyscall(self, syscall):
        """
        the ignoreSyscall callback is invoked by the debugger to assert
        if a debugged syscall should be ignored

        We only care about syscalls containg a filename argument
        """
        return syscall.name not in self.filename_syscalls

    def syscall(self, process):
        state = process.syscall_state
        syscall = state.event(self.syscall_options)
        # Only care about tracked syscals, during the exit
        if syscall and syscall.result is not None:
            self.trackSyscall(syscall)

        # Break at next syscall
        process.syscall()

    def trackSyscall(self, syscall):
        if syscall.result > 0:  # We don't care about failed calls
            filename = [arg for arg in syscall.arguments if arg.name == "filename"]
            filename = filename[0]
            print("Open ----", filename.getText()[1:-1], file=sys.stderr)

    def trackExec(self, program):
        print("Execute -", program, file=sys.stderr)

    def processExited(self, event):
        pass
        # Display exit message
        # if event.process.pid == self.pid:
        #    error("*** %s ***" % event)

    def prepareProcess(self, process):
        process.syscall()
        process.syscall_state.ignore_callback = self.ignoreSyscall

    def newProcess(self, event):
        process = event.process
        self.prepareProcess(process)
        process.parent.syscall()
