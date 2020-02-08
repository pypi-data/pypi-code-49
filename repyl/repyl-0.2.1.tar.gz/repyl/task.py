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

from threading import Thread, Event
from queue import Queue
from collections import namedtuple

_task = namedtuple('_task', ['text', 'stream', 'new_line'])

class _task_thread(Thread):
  def __init__(self, Q: Queue):
    super(_task_thread, self).__init__()
    self.setDaemon(True)
    self._running = Event()
    self._running.set()
    self._Q = Q

  def wait(self):
    self._Q.join()

  def stop(self):
    self._running.clear()

  def put(self, task: _task):
    self._Q.put(task)

  def run(self):
    while self._running.is_set():
      task = _task(*self._Q.get())
      new_line = task.new_line
      if task.text:
        task.stream.write(*task.text)
      else:
        new_line = True

      if new_line:
        task.stream.write('\n')

      task.stream.flush()
      self._Q.task_done()
