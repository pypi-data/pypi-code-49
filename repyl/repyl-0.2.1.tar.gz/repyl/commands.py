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

from .registry import Registry_
from .repl import Repl, EXIT, HELP
from .handler import Handler


class Commands(Registry_):
  def _register(self, shell: Repl):
    @shell.cmd(EXIT, usage=['exits the repl'])
    def __exit_shell():
      shell.terminate()

    @shell.cmd('history', usage=['shows command history'])
    def __history():
      for l in shell.history():
        if l:
          shell.println(l)

    @shell.cmd(HELP, usage=['prints this message'])
    def __usage(*args):
      shell.println(_context_usage(args).expandtabs(10))

    # helpers
    def _root_usage() -> str:
      text = ''
      # pylint: disable=protected-access
      for k, v in shell._handlers.items():
        h = v[k] if k in v else None
        if h:
          text += _format_usage(k, k, h)
      return text

    def _context_usage(*args) -> str:
      # pylint: disable=protected-access
      head_ctx = shell._context.head()
      if (not args) or (not args[0]):
        if not head_ctx:
          return _root_usage()
        return _format_usages(head_ctx, shell._handlers)
      cmds = args[0][0]
      has_sub_cmd = len(cmds) > 1
      cmd, sub_cmd = (cmds[0], cmds[1]) if has_sub_cmd else (cmds[0], cmds[0])

      if head_ctx:
        cmd = head_ctx
      if cmd == sub_cmd:
        return _format_usages(cmd, shell._handlers)
      try:
        return _format_usage(cmd, sub_cmd, shell._handler_from(cmd, sub_cmd))
      except Exception:
        return f'Unknown command: {cmd} {sub_cmd}'

    def _format_usages(cmd: str, d: dict) -> str:
      text = ''
      h_dict = d[cmd]
      if not h_dict:
        return f'Unknown command: {cmd}'
      for k, h in h_dict.items():
        text += _format_usage(cmd, k, h)
      return text

    def _format_usage(cmd: str, sub_cmd: str, h: Handler) -> str:
      use = '\n\t\t'.join(h.usage) if h.usage else ''
      c = f'{cmd}\t{sub_cmd}' if sub_cmd != cmd else sub_cmd
      return f'{c}\t{use}\n'
