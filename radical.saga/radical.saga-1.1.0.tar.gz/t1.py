import radical.saga as rs

js = rs.job.Service(rm='slurm+ssh://mnmda047@lxlogin5.lrz.de')
j  = js.run_job('sleep 30 && echo hello_world')

print(j.id, j.state)

