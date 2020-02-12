import sys
from ptrace.debugger import (
    PtraceDebugger,
    ProcessExit,
    ProcessSignal,
    NewProcessEvent,
    ProcessExecution,
)
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

        # Setup ignore callback
        process.syscall_state.ignore_callback = self.ignoreSyscall

        while True:

            # No more process? Exit
            if not self.debugger:
                break

            # Wait for the next syscall event
            process.syscall()
            state = process.syscall_state

            # Wait until next syscall enter
            try:
                self.debugger.waitSyscall()
                syscall = state.event(self.syscall_options)
                if not syscall:  # Ignored syscall
                    continue
                if syscall.result is not None:  # Existing syscall
                    self.trackSyscall(syscall)
            except ProcessExit as event:
                self.processExited(event)
                continue
            except ProcessSignal as event:
                event.display()
                event.process.syscall(event.signum)
                continue
            except NewProcessEvent as event:
                self.newProcess(event)
                continue
            except ProcessExecution as event:
                self.processExecution(event)
                continue

    def ignoreSyscall(self, syscall):
        """
        the ignoreSyscall callback is invoked by the debugger to assert
        if a debugged syscall should be ignored

        We only care about syscalls containg a filename argument
        """
        return syscall.name not in self.filename_syscalls

    def trackSyscall(self, syscall):
        if syscall.result > 0:  # We don't care about failed calls
            filename = [arg for arg in syscall.arguments if arg.name == "filename"]
            filename = filename[0]
            print("Opening", filename.getText()[1:-1], file=sys.stderr)

    def trackExec(self, program):
        print("Execute", program, file=sys.stderr)

    def processExited(self, event):
        pass
        # Display exit message
        # if event.process.pid == self.pid:
        #    error("*** %s ***" % event)
