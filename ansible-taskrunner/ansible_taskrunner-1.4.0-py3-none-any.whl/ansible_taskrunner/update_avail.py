try:
    from pygit2 import Repository, RemoteCallbacks, GIT_MERGE_ANALYSIS_UP_TO_DATE, GIT_CHECKOUT_FORCE, credentials
except:
    pass

class GitUpdater(object):
    def __init__(self, local_path, username, password):
        self.local_path = local_path
        self.callbacks = RemoteCallbacks(credentials=credentials.UserPass(username, password))

    def update(self, check_only=True):
        repo = Repository(self.local_path)
        # reset local change
        repo.checkout('HEAD', strategy=GIT_CHECKOUT_FORCE)
        remote = repo.remotes[0]
        # fetch from remote
        remote.fetch(callbacks=self.callbacks)
        remote_master_id = repo.lookup_reference('refs/remotes/origin/master').target
        merge_result, _ = repo.merge_analysis(remote_master_id)

        if merge_result & GIT_MERGE_ANALYSIS_UP_TO_DATE:
            # no update available
            return False
        else:
            # always fast-forward ... destroy local changes
            if not check_only:
                repo.checkout_tree(repo.get(remote_master_id), strategy=GIT_CHECKOUT_FORCE)
                master_ref = repo.lookup_reference('refs/heads/master')
                master_ref.set_target(remote_master_id)
                repo.head.set_target(remote_master_id)

            return True

updater = GitUpdater('.', 'berttejeda', 's3442Dd72')
print(updater.update(check_only=True))