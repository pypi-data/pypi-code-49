# vim: set fileencoding=utf-8 :

###################################################################################
#                                                                                 #
# Copyright (c) 2019 Idiap Research Institute, http://www.idiap.ch/               #
# Contact: beat.support@idiap.ch                                                  #
#                                                                                 #
# Redistribution and use in source and binary forms, with or without              #
# modification, are permitted provided that the following conditions are met:     #
#                                                                                 #
# 1. Redistributions of source code must retain the above copyright notice, this  #
# list of conditions and the following disclaimer.                                #
#                                                                                 #
# 2. Redistributions in binary form must reproduce the above copyright notice,    #
# this list of conditions and the following disclaimer in the documentation       #
# and/or other materials provided with the distribution.                          #
#                                                                                 #
# 3. Neither the name of the copyright holder nor the names of its contributors   #
# may be used to endorse or promote products derived from this software without   #
# specific prior written permission.                                              #
#                                                                                 #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND #
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED   #
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE          #
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE    #
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL      #
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR      #
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER      #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,   #
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE   #
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.            #
#                                                                                 #
###################################################################################


"""BEAT Computation Protocol definitions"""

#  This is the version of BCP/Client we implement
BCPC_CLIENT = b"BCPC01"

#  BCP/Client commands, as strings
BCPC_REQUEST = b"\001"

bcpc_commands = [None, b"REQUEST"]

#  This is the version of BCP/Worker we implement
BCPW_WORKER = b"BCPW01"

#  BCP/Server commands, as strings
BCPW_READY = b"\001"
BCPW_REQUEST = b"\002"
BCPW_REPLY = b"\003"
BCPW_HEARTBEAT = b"\004"
BCPW_DISCONNECT = b"\005"

bcpw_commands = [None, b"READY", b"REQUEST", b"REPLY", b"HEARTBEAT", b"DISCONNECT"]

# BCP/Processing commands, as strings
BCPP_JOB_RECEIVED = b"\001"
BCPP_JOB_STARTED = b"\002"
BCPP_JOB_DONE = b"\003"
BCPP_JOB_ERROR = b"\004"
BCPP_JOB_CANCELLED = b"\005"
BCPP_ERROR = b"\006"

bcpp_commands = [
    None,
    b"JOB_RECEIVED",
    b"JOB_STARTED",
    b"JOB_DONE",
    b"JOB_ERROR",
    b"JOB_CANCELLED",
    b"ERROR",
]

# BCP/Execution commands
BCPE_EXECUTE = b"\001"  #: Execute the given job
BCPE_CANCEL = b"\002"  #: Cancel the given job
BCPE_SCHEDULER_SHUTDOWN = b"\003"  #: Shutdown the scheduler

bcpe_commands = [None, "EXECUTE", "CANCEL", "BCPE_SCHEDULER_SHUTDOWN"]
