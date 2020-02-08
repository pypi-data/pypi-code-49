# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import atexit
import readline
import signal as sig
import sys
from argparse import ArgumentParser, Namespace
from collections import defaultdict
from getopt import gnu_getopt, GetoptError
from pathlib import Path
from queue import Queue
from shlex import split
from sys import stdout as STDOUT
from threading import Event
from typing import Callable, IO, List, Optional, Iterable, Iterator, TypeVar

from .colors import red, yellow
from .stack import stack
from . import repl_command
from .error import ReplError
from .handler import Handler
from .io import istream, str_to_istream, file_to_istream
from .task import _task, _task_thread

HISTORY_FILE_NAME = '.history'
HISTORY_FILE_LEN = 500
HELP = 'help'
EXIT = 'exit'

T = TypeVar('T')

class Repl:
  # pylint: disable=too-many-instance-attributes
  def __init__(self, ctx: str, seperator: str, banner: str = ''):
    self._seperator = seperator
    self._banner = banner
    self._history_directory = Path.home() / Path(f'.{ctx}')
    self._root_context = ctx
    self._setup_signal_handlers()
    self._setup_history()
    self._running = Event()
    self._args = _init_args()
    self._istream = istream(lambda: self._prompt(self._root_context))
    self._task_handler = _task_thread(Queue())
    self._handlers = defaultdict(dict)
    self._exit_hooks = stack()
    self._context = stack()

  def cmd(
      self,
      name: str,
      sub_cmd: Optional[str] = None,
      opts: List[str] = None,
      usage: List[str] = None
  ) -> Callable:
    def _call(call: Callable):
      handler = Handler(sub_cmd or name, opts, call, usage)
      self._handlers[name][handler.name] = handler
      return call
    return _call

  def print(self, *args, stream: IO = STDOUT):
    self._task_handler.put(_task(args, stream, False))

  def println(self, *args, stream: IO = STDOUT):
    self._task_handler.put(_task(args, stream, True))

  def warn(self, msg: str, stream: IO = STDOUT):
    self._task_handler.put(_task([yellow(msg)], stream, True))

  def error(self, msg: str, stream: IO = STDOUT):
    self._task_handler.put(_task([red(msg)], stream, True))

  def page(
      self,
      i: Iterable[T],
      page_size: int,
      formatter: Callable[[T], str],
      proceed: Callable[[IO], bool]):
    count = 1
    for item in i:
      self.println(formatter(item))
      if count < page_size:
        count += 1
      else:
        count = 1
        if not proceed(self.wait_for_io(':')):
          return

  def push_context(self, ctx: str):
    if self._context.head() != ctx:
      self._context.push(ctx)

  def run(self):
    self._setup()
    self._task_handler.start()
    self._running.set()

    while self._running.is_set():
      try:
        self._handle()
      except EOFError:
        sys.exit(0)
      finally:
        self._task_handler.wait()

  @staticmethod
  def history() -> Iterator[str]:
    l = readline.get_current_history_length()
    for i in range(0, l):
      yield readline.get_history_item(i)

  def add_exit_hook(self, exit_hook: Callable[..., None]):
    self._exit_hooks.push(exit_hook)

  def terminate(self, force: bool = False):
    if force or self._context.is_empty():
      readline.write_history_file(self._history_directory / HISTORY_FILE_NAME)
      while not self._exit_hooks.is_empty():
        try:
          self._exit_hooks.pop()()
        except Exception:
          pass
      self._task_handler.stop()
      self._running.clear()
      sys.exit(0)
    else:
      self._context.pop()

  def _handle(self):
    io = next(self._istream)()
    if not io:
      return
    for line in self._split_multiline(io):
      command, *argv = split(line)
      err = self._execute(command, *argv)
      if err:
        self.error(str(err))

  def wait_for_io(self, msg: str) -> str:
    io = None
    wait = True
    while not io:
      try:
        self._task_handler.wait()
        if wait:
          io = next(istream(lambda: msg))()
          wait = False
        else:
          return io
      except Exception:
        self._task_handler.wait()
    return io
  
  def _execute(self, command: str, *argv) -> Optional[ReplError]:
    try:
      if not self._check_context(command):
        return ReplError(f'Unknown command: {command}')
      cmds = self._parse_command(command, *argv)
      handler = self._handler_from(cmds.cmd, cmds.sub_cmd)
      res_opts = self._parse_opts(cmds, handler.opts)
    except KeyError as e:
      return ReplError(f'Unknown command: {cmds.cmd} {cmds.sub_cmd}')
    except GetoptError as e:
      return ReplError(f'{cmds.cmd} {cmds.sub_cmd}: {e.msg}')
    except Exception as e:
      return ReplError(None, e)
    return handler.handle(*res_opts)

  def _parse_command(self, command: str, *argv) -> repl_command:
    context = self._command_context(command)
    args = argv
    sub_command = ''
    if context != self._root_context:
      sub_command = self._infer_sub_command(command, args)
    else:
      sub_command = self._sub_command(command, args)
    if command != HELP and len(args) > 0 and self._context.is_empty():
      args = args[1:]
    return repl_command(context, sub_command, args)

  @staticmethod
  def _parse_opts(cmd: repl_command, opts: List[str] = None) -> List[str]:
    shortopts = ''.join([
      opt[1:] for opt in opts
      if len(opt) >= 2 and opt[0] == '-' and opt[1] != '-'
    ]) if opts else ''
    longopts = [
      opt[2:] for opt in opts
      if len(opt) >= 3 and opt[:2] == '--'
    ] if opts else [] # yapf: disable
    p = gnu_getopt(cmd.opts, shortopts, longopts)
    return p[1] + list(sum(p[0], ()))

  def _infer_sub_command(self, command: str, *args) -> str:
    sub_cmd = command
    if len(*args) > 0:
      sub_cmd = self._sub_command(command, args[0][0])
    return sub_cmd if self._check_handler(command, sub_cmd) else command

  @staticmethod
  def _sub_command(command: str, *args) -> str:
    parsed = [v for v in args if not v.startswith('-')]
    vlen = len(parsed)
    sub_cmd = command
    if vlen > 0:
      sub_cmd = parsed[0]
    return sub_cmd

  @staticmethod
  def _split_multiline(line: str) -> List[str]:
    parsed = split(line, posix=False)
    commands = []
    command = []
    for element in parsed:
      command.append(element)
    if command:
      commands.append(command)
    return [' '.join(command) for command in commands if command]

  def _prompt(self, p: str) -> str:
    if self._context.is_empty():
      return f'{p}{self._seperator} '
    return f'{p}:{self._context.head()}{self._seperator} '

  def _command_context(self, command: str) -> Optional[str]:
    if command in (EXIT, HELP):
      return command
    head = self._context.head()
    if head:
      return head
    return command

  def _check_context(self, command: str) -> bool:
    if command in (EXIT, HELP):
      return True
    context = self._command_context(command)
    return command in self._handlers[context]

  def _handler_from(self, command: str, sub_command: str) -> Handler:
    context = self._command_context(command)
    handler_dict = self._handlers[context]
    return handler_dict[sub_command]

  def _check_handler(self, command: str, sub_command: str) -> bool:
    return sub_command in self._handlers[command]

  def _setup(self):
    if self._args.command:
      self._istream = str_to_istream(self._args.cmd)
    elif self._args.file:
      self._istream = file_to_istream(Path(self._args.file))
    else:
      print(self._banner)

  def _setup_history(self):
    history_file = self._history_directory / HISTORY_FILE_NAME
    if not self._history_directory.exists():
      self._history_directory.mkdir(0o0770)
      with history_file.open('a+', encoding='utf-8') as f:
        f.flush()
        f.close()
    readline.read_history_file(history_file)
    readline.set_history_length(HISTORY_FILE_LEN)

  def _setup_signal_handlers(self):
    atexit.register(self._exit)
    for s in [
        sig.SIGABRT,
        sig.SIGILL,
        sig.SIGINT,
        sig.SIGSEGV,
        sig.SIGTERM,
        sig.SIGQUIT
    ]: # yapf: disable
      sig.signal(s, self._exit)

  # pylint: disable=unused-argument
  def _exit(self, *args):
    self.terminate(True)


def new_repl(prompt: str, sep: str = '$', banner: str = '') -> Repl:
  return Repl(prompt, sep, banner)


def _init_args() -> Namespace:
  parser = ArgumentParser()
  parser.add_argument('file', nargs='?', default=None)
  parser.add_argument('-command')
  return parser.parse_args()
