#!/usr/bin/python3

import os
import sys

########################################################################################################################
#                                                 Main function                                                        #
########################################################################################################################


def main():
    sys.path.append('../')
    sys.path.append('/app')
    import git
    import github
    from bitbucket.client import Client
    from bitbucket.exceptions import NotAuthenticatedError
    import random
    from git.exc import GitCommandError
    from ghcopy.utils import error_handler
    from ghcopy.config import translate as _, logger, cmd_args, config_args

    def repo_work(clone_url, language):
        """

        :param clone_url:
        :param language:
        :type language: str
        :return:
        """
        try:
            out_dir = '%s/%s/%s' % (cmd_args.output, hub[:1].upper() + hub[1:].lower(),
                                    language[:1].upper() + language[1:].lower())
            os.makedirs(out_dir, 0o755, True)
            repo_dir = '%s/%s' % (out_dir, clone_url.split('/')[-1].split('.')[0])
            if not os.path.isdir(repo_dir):
                logger.info('%s \'%s\'' % (_('cloning into'), repo_dir))
                git.Repo.clone_from(clone_url, repo_dir,
                                    multi_options=['--config credential.%s.username=%s' % (clone_url, user),
                                                   '--config core.askPass=%s' % pass_file_name])
            else:
                rp = git.Repo(repo_dir)
                config = rp.config_writer()
                config.set_value('credential "%s"' % clone_url, 'username', user)
                config.set_value('core', 'askpass', pass_file_name)
                for remote in rp.remotes:
                    logger.info('%s \'%s\'' % (_('fetching'), repo_dir))
                    remote.fetch()
                    logger.info('%s \'%s\'' % (_('pulling current branch'), repo_dir))
                    remote.pull()
        except GitCommandError as e:
            errors = e.stderr[3:-2].split('\n')
            for error in errors:
                logger.error(error)
            return
        except Exception as e:
            error_handler(logger, e, _('unexpected exception'), debug_info=True)
            return

    user = cmd_args.user if cmd_args.user else config_args.get('user', None)
    password = cmd_args.password if cmd_args.password else config_args.get('password', None)
    token = cmd_args.token if cmd_args.token else config_args.get('token', None)
    hub = cmd_args.hub if cmd_args.hub else config_args.get('type', 'github')
    if (not user or not password) and not token:
        logger.error('%s' % _('parameters \'user\' and \'password\' or \'token\' are required'))
        exit(1)
    pass_file_name = '/tmp/%s' % (''.join([str(random.randint(0, 9)) for _ in range(16)]))
    pass_file = open(pass_file_name, 'w')
    if hub == 'github':
        password = '' if token else password
    pass_file.write('#!/bin/bash\n\necho "%s"' % password)
    pass_file.close()
    os.chmod(pass_file_name, 0o755)
    try:
        os.makedirs(cmd_args.output, 0o755, True)
        if hub == 'github':
            logger.info('github %s, %s: %s' % (_('copying started'), _('logging level'), cmd_args.log_level))
            user = token if token else user
            g = github.Github(user, password)
            for repo in g.get_user().get_repos():
                repo_work(repo.clone_url, repo.language)
        elif hub == 'bitbucket':
            page = 1
            repos = 0
            size = 1
            logger.info('bitbucket %s, %s: %s' % (_('copying started'), _('logging level'), cmd_args.log_level))
            client = Client(user, password)
            while repos < size:
                response = client.get_repositories(params={'page': page})
                size = response['size']
                for repo in response['values']:
                    repos += 1
                    repo_work(repo['links']['clone'][0]['href'], repo.get('language', 'Undefined'))
                page += 1
        else:
            logger.error('%s' % _('incorrect repository type'))
            exit(1)
        logger.info('%s %s' % (hub, _('copying ended')))
    except NotAuthenticatedError:
        logger.error('%s' % _('incorrect user name, password or token'))
        exit(1)
    except github.BadCredentialsException:
        logger.error('%s' % _('incorrect user name, password or token'))
        exit(1)
    finally:
        os.unlink(pass_file_name)
    exit(0)


########################################################################################################################
#                                                  Entry point                                                         #
########################################################################################################################


if __name__ == '__main__':
    main()
