#!/usr/bin/env python2
#   IRPF90 is a Fortran90 preprocessor written in Python for programming using
#   the Implicit Reference to Parameters (IRP) method.
#   Copyright (C) 2009 Anthony SCEMAMA 
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program; if not, write to the Free Software Foundation, Inc.,
#   51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#   Anthony Scemama
#   LCPQ - IRSAMC - CNRS
#   Universite Paul Sabatier
#   118, route de Narbonne      
#   31062 Toulouse Cedex 4      
#   scemama@irsamc.ups-tlse.fr


import util 
from command_line import command_line

do_debug = command_line.do_debug
do_openmp = command_line.do_openmp
do_memory = command_line.do_memory

import irpf90_t

FILENAME = irpf90_t.irpdir+"irp_stack.irp.F90"

def create():

  txt = """
module irp_stack_mod
  integer, parameter            :: STACKMAX=1000
  character*(128),allocatable   :: irp_stack(:)
  double precision,allocatable  :: irp_cpu(:)
  integer                       :: stack_index
  logical                       :: alloc = .False.
  character*(128)               :: white = ''
end module

subroutine irp_enter(irp_where)
 use irp_stack_mod
 character*(*) :: irp_where
"""

  txt += "$1"

  if do_memory:
     txt+="""
 if (.not.alloc) then
   print *, 'Allocating irp_stack(',STACKMAX+1,')'
   print *, 'Allocating irp_cpu(',STACKMAX+1,')'
 endif"""
  txt +="""
$2
end subroutine

subroutine irp_enter_f(irp_where)
 use irp_stack_mod
 character*(*) :: irp_where
$1
"""
  if do_memory:
    txt+="""
 if (.not.alloc) then
   print *, 'Allocating irp_stack(',STACKMAX+1,')'
   print *, 'Allocating irp_cpu(',STACKMAX+1,')'
 endif
"""
  txt += """
$2
end subroutine

subroutine irp_leave (irp_where)
 use irp_stack_mod
  character*(*) :: irp_where
  double precision :: cpu
$3
$4
end subroutine
"""

  # $1
  if do_debug:
    s = """
 if (.not.alloc) then
   allocate(irp_stack(0:STACKMAX))
   allocate(irp_cpu(0:STACKMAX))
   stack_index = 0
   alloc = .True.
 endif
 stack_index = min(stack_index+1,STACKMAX)
 irp_stack(stack_index) = irp_where"""
    if do_memory:
      txt+="""
  print *, 'Allocating irp_stack(',STACKMAX+1,')'
  print *, 'Allocating irp_cpu(',STACKMAX+1,')' """
  else:
    s = ""
  txt = txt.replace("$1",s)

  # $2
  if do_debug:
    txt = txt.replace("$2","""
  print *, white(1:stack_index)//'-> ', trim(irp_where)
  call cpu_time(irp_cpu(stack_index))""")
  else:
    txt = txt.replace("$2","")

  # $3
  if do_debug:
    txt = txt.replace("$3","""
  call cpu_time(cpu)
  print *, white(1:stack_index)//'<- ', &
    trim(irp_stack(stack_index)), &
    cpu-irp_cpu(stack_index)""")
  else:
    txt = txt.replace("$3","")

  # $4
  if do_debug:
    txt = txt.replace("$4","""
  stack_index = max(0,stack_index-1)""")
  else:
    txt = txt.replace("$4","")

  txt += """
subroutine irp_trace
 use irp_stack_mod
 integer :: i
 if (.not.alloc) return
 print *, 'Stack trace: '
 print *, '-------------------------'
 do i=1,stack_index
  print *, trim(irp_stack(i))
 enddo
 print *, '-------------------------'
end subroutine
"""

  txt = txt.split('\n')
  txt = map(lambda x: x+"\n",txt)
  if not util.same_file(FILENAME, txt):
    file = open(FILENAME,'w')
    file.writelines(txt)
    file.close()


