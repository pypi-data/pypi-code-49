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

from itertools import repeat as read
from pathlib import Path
from typing import Callable, Iterator


def istream(call: Callable) -> Iterator[Callable]:
  yield from read(lambda: input(call()))


def str_to_istream(cmd: str) -> Iterator[Callable]:
  yield lambda: cmd


def file_to_istream(path: Path) -> Iterator[Callable]:
  def closure(line: str) -> Callable[..., str]:
    l = line
    return lambda: l

  try:
    with open(path, "r") as f:
      for line in f:
        yield closure(line)
  except Exception:
    raise IOError(path)
