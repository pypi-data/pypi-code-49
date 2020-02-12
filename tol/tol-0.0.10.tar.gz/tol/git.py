def get_short_hash(repo_path):
    """
    Get git short hash
    """
    return "git -C {repo_path} log --pretty=format:'%h' -n 1".format(repo_path=repo_path)


def get_branch(repo_path):
    """
    Get git branch
    """
    return "git -C {repo_path} rev-parse --abbrev-ref HEAD".format(repo_path=repo_path)
