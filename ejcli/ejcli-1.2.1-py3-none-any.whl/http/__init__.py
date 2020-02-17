import ejcli._http.ejudge, ejcli._http.ejudge.ejfuse, ejcli._http.pcms, ejcli._http.jjs, ejcli._http.informatics, ejcli._http.informatics_new, ejcli._http.codeforces, ejcli._http.gcj, urllib.request
from ejcli._http.ejudge import contest_name
from ejcli.error import EJError

backend_path = [ejcli._http.ejudge.ejfuse.EJFuse, ejcli._http.jjs.JJS, ejcli._http.informatics.Informatics, ejcli._http.informatics_new.Informatics, ejcli._http.codeforces.CodeForces, ejcli._http.gcj.GCJ, ejcli._http.pcms.PCMS, ejcli._http.ejudge.Ejudge]

def login(url, login, password, **kwds):
    for i in backend_path:
        try: f = i.detect(url)
        except Exception: f = False
        if f:
            return (i(url, login, password, **kwds), True)
    raise EJError("Unknown CMS")

def login_type(url):
    for i in backend_path:
        try: f = i.detect(url)
        except Exception: pass
        if f: return i.login_type(url)
    return []

def _create_wrapper(name):
    def func(*args, **kwds):
        return getattr(args[0], name)(*args[2:], **kwds)
    globals()[name] = func

for _w in ['task_list', 'submission_list', 'submission_results', 'task_ids', 'submit', 'status', 'scores', 'compile_error', 'submission_status', 'submission_source', 'do_action', 'compiler_list', 'submission_stats', 'problem_info', 'download_file', 'submission_score', 'clars', 'submit_clar', 'read_clar', 'get_samples', 'may_cache', 'scoreboard']:
    _create_wrapper(_w)

del _create_wrapper, _w

def has_feature(url, cookie, methodname, argname):
    if not hasattr(url, methodname): return False
    m = getattr(url, methodname).__func__.__code__
    return argname in m.co_varnames[:m.co_argcount+m.co_kwonlyargcount]
