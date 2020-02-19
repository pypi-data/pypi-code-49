import os

from ..tracer import tags


def get_repository_information():
    if os.getenv('TRAVIS'):
        return {
            'repository': os.getenv('TRAVIS_REPO_SLUG'),
            'commit': os.getenv('TRAVIS_COMMIT'),
            'branch': os.getenv('TRAVIS_BRANCH'),
            'source_root': os.getenv('TRAVIS_BUILD_DIR'),
        }
    elif os.getenv('CIRCLECI'):
        return {
            'repository': os.getenv('CIRCLE_REPOSITORY_URL'),
            'commit': os.getenv('CIRCLE_SHA1'),
            'branch': os.getenv('CIRCLE_BRANCH'),
            'source_root': os.getenv('CIRCLE_WORKING_DIRECTORY'),
        }
    elif os.getenv('JENKINS_URL'):
        return {
            'repository': os.getenv('GIT_URL'),
            'commit': os.getenv('GIT_COMMIT'),
            'branch': os.getenv('GIT_BRANCH'),
            'source_root': os.getenv('WORKSPACE'),
        }
    elif os.getenv('GITLAB_CI'):
        return {
            'repository': os.getenv('CI_REPOSITORY_URL'),
            'commit': os.getenv('CI_COMMIT_SHA'),
            'branch': os.getenv('CI_COMMIT_BRANCH'),
            'source_root': os.getenv('CI_BUILDS_DIR'),
        }
    elif os.getenv('APPVEYOR'):
        return {
            'commit': os.getenv('APPVEYOR_REPO_COMMIT'),
            'branch': os.getenv('APPVEYOR_REPO_BRANCH'),
            'source_root': os.getenv('APPVEYOR_BUILD_FOLDER'),
        }
    elif os.getenv('TF_BUILD'):
        return {
            'repository': os.getenv('BUILD_REPOSITORY_URI'),
            'commit': os.getenv('BUILD_SOURCEVERSION'),
            'branch': os.getenv('BUILD_SOURCEBRANCH'),
            'source_root': os.getenv('AGENT_BUILDDIRECTORY'),
        }
    elif os.getenv('BITBUCKET_COMMIT'):
        return {
            'repository': os.getenv('BITBUCKET_REPO_SLUG'),
            'commit': os.getenv('BITBUCKET_COMMIT'),
            'branch': os.getenv('BITBUCKET_BRANCH'),
            'source_root': os.getenv('BITBUCKET_CLONE_DIR'),
        }
    elif os.getenv('GITHUB_SHA'):
        return {
            'repository': 'https://github.com/{repository}'.format(repository=os.getenv('GITHUB_REPOSITORY')),
            'commit': os.getenv('GITHUB_SHA'),
            'branch': os.getenv('GITHUB_REF'),
            'source_root': os.getenv('GITHUB_WORKSPACE'),
        }
    elif os.getenv('TEAMCITY_VERSION'):
        # ** TODO ** how to get branch?
        return {
            'repository': os.getenv('BUILD_VCS_URL'),
            'commit': os.getenv('BUILD_VCS_NUMBER'),
            'source_root': os.getenv('BUILD_CHECKOUTDIR'),
        }
    elif os.getenv('BUILDKITE'):
        return {
            'repository': os.getenv('BUILDKITE_REPO'),
            'commit': os.getenv('BUILDKITE_COMMIT'),
            'source_root': os.getenv('BUILDKITE_BUILD_CHECKOUT_PATH'),
        }
    else:
        return {}


def get_ci_tags():
    if os.getenv('TRAVIS'):
        return {
            tags.CI: True,
            tags.CI_PROVIDER: 'Travis',
            tags.CI_BUILD_ID: os.getenv('TRAVIS_BUILD_ID'),
            tags.CI_BUILD_NUMBER: os.getenv('TRAVIS_BUILD_NUMBER'),
            tags.CI_BUILD_URL: 'https://travis-ci.com/%s/builds/%s'
            % (os.getenv('TRAVIS_REPO_SLUG'), os.getenv('TRAVIS_BUILD_ID')),
        }
    elif os.getenv('CIRCLECI'):
        return {
            tags.CI: True,
            tags.CI_PROVIDER: 'CircleCI',
            tags.CI_BUILD_NUMBER: os.getenv('CIRCLE_BUILD_NUM'),
            tags.CI_BUILD_URL: os.getenv('CIRCLE_BUILD_URL'),
        }
    elif os.getenv('JENKINS_URL'):
        return {
            tags.CI: True,
            tags.CI_PROVIDER: 'Jenkins',
            tags.CI_BUILD_ID: os.getenv('BUILD_ID'),
            tags.CI_BUILD_NUMBER: os.getenv('BUILD_NUMBER'),
            tags.CI_BUILD_URL: os.getenv('BUILD_URL'),
        }
    elif os.getenv('GITLAB_CI'):
        return {
            tags.CI: True,
            tags.CI_PROVIDER: 'GitLab',
            tags.CI_BUILD_ID: os.getenv('CI_JOB_ID'),
            tags.CI_BUILD_URL: os.getenv('CI_JOB_URL'),
        }
    elif os.getenv('APPVEYOR'):
        return {
            tags.CI: True,
            tags.CI_PROVIDER: 'AppVeyor',
            tags.CI_BUILD_NUMBER: os.getenv('APPVEYOR_BUILD_NUMBER'),
            tags.CI_BUILD_ID: os.getenv('APPVEYOR_BUILD_ID'),
            tags.CI_BUILD_URL: 'https://ci.appveyor.com/project/{slug}/builds/{build_id}'.format(
                slug=os.getenv('APPVEYOR_PROJECT_SLUG'), build_id=os.getenv('APPVEYOR_BUILD_ID'),
            ),
        }
    elif os.getenv('TF_BUILD'):
        return {
            tags.CI: True,
            tags.CI_PROVIDER: 'Azure Pipelines',
            tags.CI_BUILD_NUMBER: os.getenv('BUILD_BUILDNUMBER'),
            tags.CI_BUILD_ID: os.getenv('BUILD_BUILDID'),
            tags.CI_BUILD_URL: '{uri}/{project}/_build/results?buildId={build_id}&_a=summary'.format(
                uri=os.getenv('SYSTEM_TEAMFOUNDATIONCOLLECTIONURI'),
                project=os.getenv('SYSTEM_TEAMPROJECT'),
                build_id=os.getenv('BUILD_BUILDID'),
            ),
        }
    elif os.getenv('BITBUCKET_COMMIT'):
        return {
            tags.CI: True,
            tags.CI_PROVIDER: 'Bitbucket Pipelines',
            tags.CI_BUILD_NUMBER: os.getenv('BITBUCKET_BUILD_NUMBER'),
        }
    elif os.getenv('GITHUB_SHA'):
        return {
            tags.CI: True,
            tags.CI_PROVIDER: 'GitHub',
            tags.CI_BUILD_URL: 'https://github.com/{repository}/commit/{sha}/checks'.format(
                repository=os.getenv('GITHUB_REPOSITORY'), sha=os.getenv('GITHUB_SHA')
            ),
        }
    elif os.getenv('TEAMCITY_VERSION'):
        return {
            tags.CI: True,
            tags.CI_PROVIDER: 'TeamCity',
            tags.CI_BUILD_NUMBER: os.getenv('BUILD_NUMBER'),
            tags.CI_BUILD_ID: os.getenv('BUILD_ID'),
            tags.CI_BUILD_URL: '{url}/viewLog.html?buildId={build_id}'.format(
                url=os.getenv('SERVER_URL'), build_id=os.getenv('BUILD_ID')
            ),
        }
    elif os.getenv('BUILDKITE'):
        return {
            tags.CI: True,
            tags.CI_PROVIDER: 'Buildkite',
            tags.CI_BUILD_NUMBER: os.getenv('BUILDKITE_BUILD_NUMBER'),
            tags.CI_BUILD_ID: os.getenv('BUILDKITE_BUILD_ID'),
            tags.CI_BUILD_URL: os.getenv('BUILDKITE_BUILD_URL'),
        }
    elif os.getenv('CI'):
        return {tags.CI: True}
    else:
        return {tags.CI: False}
