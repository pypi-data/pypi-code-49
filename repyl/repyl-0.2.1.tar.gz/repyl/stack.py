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

from typing import Optional, TypeVar

A = TypeVar('A')

class Stack:
  def __init__(self):
    self._stack = []

  def push(self, a: A):
    self._stack.append(a)

  def pop(self) -> Optional[A]:
    if not self._stack:
      return None
    return self._stack.pop()

  def head(self) -> Optional[A]:
    if not self._stack:
      return None
    return self._stack[0]

  def tail(self) -> Optional[A]:
    if not self._stack:
      return None
    return self._stack[-1]

  def size(self) -> int:
    return len(self._stack)

  def is_empty(self) -> bool:
    return not self._stack

def stack() -> Stack:
  return Stack()
