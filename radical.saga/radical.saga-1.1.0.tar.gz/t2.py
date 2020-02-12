import sys
import radical.saga as rs

js = rs.job.Service(rm='slurm+ssh://mnmda047@lxlogin5.lrz.de')
j  = js.get_job(sys.argv[1])

print(j.id, j.state, j.stdout)

