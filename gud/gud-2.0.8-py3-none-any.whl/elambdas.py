import shutil
import os
from time import sleep
import json
from botocore.exceptions import ClientError
import logging

from .entity import Entity
from .utils import pretty, rinse

MAGIC_DIR = '.gg'  # XXX: better way?

log = logging.getLogger(__name__)


class ELambdas(Entity):
    def __init__(self, group, state):
        super(ELambdas, self).__init__(group, state)
        self.type = 'ExistingLambdas'
        self.name = group['Group']['name'] + '_elambdas'

        self._requirements = ['Group']
        self._gg = Entity._session.client("greengrass")
        self._iam = Entity._session.client("iam")
        self._lambda = Entity._session.client("lambda")

    def _do_create(self):
        functions = []
        for l in self._group['ExistingLambdas']:
            functions.append({
                'Id': l['name'],
                'FunctionArn': l['aliasarn'],
                'FunctionConfiguration': l['greengrassConfig']
            })

        log.debug("Function definition list ready:\n{0}".format(pretty(functions)))

        log.info("Creating function definition: '{0}'".format(self.name + '_func_def_1'))
        fd = self._gg.create_function_definition(
            Name=self.name + '_func_def_1',
            InitialVersion={'Functions': functions}
        )
        self._state.update('Lambdas.FunctionDefinition', rinse(fd))

        fd_ver = self._gg.get_function_definition_version(
            FunctionDefinitionId=self._state.get('Lambdas.FunctionDefinition.Id'),
            FunctionDefinitionVersionId=self._state.get('Lambdas.FunctionDefinition.LatestVersion'))

        self._state.update('Lambdas.FunctionDefinition.LatestVersionDetails', rinse(fd_ver))

    def _do_remove(self):

        if not self._state.get('Lambdas.FunctionDefinition'):
            log.warning("Function definition was not created. Moving on...")
        else:
            fd_name = self._state.get('Lambdas.FunctionDefinition.Name')
            fd_id = self._state.get('Lambdas.FunctionDefinition.Id')
            log.info("Deleting function definition '{0}' Id='{1}".format(fd_name, fd_id))
            self._gg.delete_function_definition(FunctionDefinitionId=fd_id)
            self._state.remove('Lambdas.FunctionDefinition')

    def _default_lambda_role_arn(self):
        # TODO(XXX): Refactor, merge with _create_default_lambda_role;
        #            consider not messing with state here, move it up.
        if self._state.get('Lambdas.LambdaRole'):
            log.info("Default lambda role '{0}' already creted, RoleId={1} ".format(
                self._LAMBDA_ROLE_NAME, self._state.get('LambdaRole.Role.RoleId')))
        else:
            try:
                role = self._create_default_lambda_role()
            except ClientError as e:
                if e.response['Error']['Code'] == 'EntityAlreadyExists':
                    role = self._iam.get_role(RoleName=self._LAMBDA_ROLE_NAME)
                    log.warning("Role {0} already exists, reusing.".format(self._LAMBDA_ROLE_NAME))
                else:
                    raise e

            self._state.update('Lambdas.LambdaRole', rinse(role))
        return self._state.get('Lambdas.LambdaRole.Role.Arn')

    def _create_default_lambda_role(self):
        # TODO: redo as template and read from definition .yaml
        log.info("Creating default lambda role '{0}'".format(self._LAMBDA_ROLE_NAME))
        role_policy_document = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "lambda.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"

                }
            ]
        }

        role = self._iam.create_role(
            RoleName=self._LAMBDA_ROLE_NAME,
            AssumeRolePolicyDocument=json.dumps(role_policy_document)
        )

        log.info("Creating lambda role policy '{0}'".format(
            self._LAMBDA_ROLE_NAME + "_Policy"))
        inline_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": [
                        "logs:CreateLogGroup",
                        "logs:CreateLogStream",
                        "logs:PutLogEvents"
                    ],
                    "Resource": "arn:aws:logs:*:*:*"
                }
            ]
        }

        self._iam.put_role_policy(
            RoleName=self._LAMBDA_ROLE_NAME,
            PolicyName=self._LAMBDA_ROLE_NAME + "_Policy",
            PolicyDocument=json.dumps(inline_policy))

        return role

    def _remove_default_lambda_role(self):
        for p in self._iam.list_role_policies(RoleName=self._LAMBDA_ROLE_NAME)['PolicyNames']:
            log.info("Deleting lambda role policy '{0}'".format(p))
            self._iam.delete_role_policy(RoleName=self._LAMBDA_ROLE_NAME, PolicyName=p)

        log.info("Deleting default lambda role '{0}'".format(self._LAMBDA_ROLE_NAME))
        self._iam.delete_role(RoleName=self._LAMBDA_ROLE_NAME)
