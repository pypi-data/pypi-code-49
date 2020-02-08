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

from typing import Callable, List, Optional
from inspect import BoundArguments, signature, Parameter
from .error import ReplError


class Handler:
  def __init__(
      self,
      name: str,
      opts: List[str],
      call: Callable,
      usage: List[str]):
    self.name = name
    self.opts = opts
    self.call = call
    self.usage = usage

  def handle(self, *args) -> Optional[ReplError]:
    try:
      self.call(*self._bound_args(self._bind(*args)))
    except Exception as e:
      return ReplError(None, e)
    return None

  def _bind(self, *args) -> BoundArguments:
    return signature(self.call).bind(*args)

  @staticmethod
  def _bound_args(args: BoundArguments) -> List:
    pos = Parameter.POSITIONAL_ONLY
    return [
      v if args.signature.parameters[k].kind is not pos else list(*v)
      for k, v in args.arguments.items()
    ]

  def __str__(self):
    return self.name
