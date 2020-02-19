import base64
import json
import os
import urllib
import ssl
import rsa
from sgqlc.endpoint.http import HTTPEndpoint

LOGIN_METHOD_USING_EMAIL = "EMAIL"
LOGIN_METHOD_USING_PHONE = "PHONE"
LOGIN_METHOD_USING_USERNAME = "USERNAME"


class AuthingEndPoint(HTTPEndpoint):

    def __init__(self, url, base_headers=None, timeout=None, urlopen=None):
        HTTPEndpoint.__init__(
            self, url=url, base_headers=base_headers, timeout=timeout, urlopen=urlopen)

    def __call__(self, query, variables=None, operation_name=None,
                 extra_headers=None, timeout=None):
        '''Calls the GraphQL endpoint.
        :param query: the GraphQL query or mutation to execute. Note
          that self is converted using ``bytes()``, thus one may pass
          an object implementing ``__bytes__()`` method to return the
          query, eventually in more compact form (no indentation, etc).
        :type query: :class:`str` or :class:`bytes`.
        :param variables: variables (dict) to use with
          ``query``. self is only useful if the query or
          mutation contains ``$variableName``.
        :type variables: dict
        :param operation_name: if more than one operation is listed in
          ``query``, then it should specify the one to be executed.
        :type operation_name: str
        :param extra_headers: dict with extra HTTP headers to use.
        :type extra_headers: dict
        :param timeout: overrides the default timeout.
        :type timeout: float
        :return: dict with optional fields ``data`` containing the GraphQL
          returned data as nested dict and ``errors`` with an array of
          errors. Note that both ``data`` and ``errors`` may be returned!
        :rtype: dict
        '''
        if isinstance(query, bytes):
            query = query.decode('utf-8')
        elif not isinstance(query, str):
            # allows sgqlc.operation.Operation to be passed
            # and generate compact representation of the queries
            query = bytes(query).decode('utf-8')

        post_data = json.dumps({
            'query': query,
            'variables': variables,
            'operationName': operation_name,
        }).encode('utf-8')
        headers = self.base_headers.copy()
        if extra_headers:
            headers.update(extra_headers)
        headers.update({
            'Accept': 'application/json; charset=utf-8',
            'Content-Type': 'application/json; charset=utf-8',
            'Content-Length': len(post_data),
        })

        self.logger.debug('Query:\n%s', query)

        req = urllib.request.Request(
            url=self.url, data=post_data, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ssl._create_unverified_context()) as f:
                body = f.read().decode('utf-8')
                try:
                    data = json.loads(body)
                    if data and data.get('errors'):
                        data['errors'][0]['message']['errors'] = True
                        return data['errors'][0]['message']
                    return data
                except json.JSONDecodeError as exc:
                    return {'data': None, 'errors': [{
                        'message': exc,
                        'exception': exc,
                        'body': body,
                    }]}
        except urllib.error.HTTPError as exc:
            return self._log_http_error(query, req, exc)

    def _log_http_error(self, query, req, exc):
        '''Log :exc:`urllib.error.HTTPError`, converting to
        GraphQL's ``{"data": null, "errors": [{"message": str(exc)...}]}``

        :param query: the GraphQL query that triggered the result.
        :type query: str

        :param req: :class:`urllib.request.Request` instance that was opened.
        :type req: :class:`urllib.request.Request`

        :param exc: :exc:`urllib.error.HTTPError` instance
        :type exc: :exc:`urllib.error.HTTPError`

        :return: GraphQL-compliant dict with keys ``data`` and ``errors``.
        :rtype: dict
        '''
        body = exc.read().decode('utf-8')
        content_type = exc.headers.get('Content-Type', '')
        if not content_type.startswith('application/json'):
            return {'data': None, 'errors': [{
                'message': exc,
                'exception': exc,
                'status': exc.code,
                'headers': exc.headers,
                'body': body,
            }]}
        else:
            # GraphQL servers return 400 and {'errors': [...]}
            # if only errors was returned, no {'data': ...}
            data = json.loads(body)
            if data and data.get('errors'):
                data.get('errors')[0]['message']['errors'] = True
                return data.get('errors')[0]['message']
            return {'data': None, 'errors': [{
                'message': exc,
                'exception': exc,
                'status': exc.code,
                'headers': exc.headers,
                'body': body,
            }]}


class Authing():
    """docstring for Authing"""

    def __init__(self, clientId, secret, options=None):
        self.clientId = clientId
        self.secret = secret
        self.cdnPreflightUrl = "https://usercontents.authing.cn"
        self.preflightUrl = {
            'users': "https://users.authing.cn/system/status",
            'oauth': "https://oauth.authing.cn/system/status"
        }
        self.base_path = os.path.abspath(os.path.dirname(__file__))
        if options is None:
            options = {"oauth": 'https://oauth.authing.cn/graphql', "users": 'https://users.authing.cn/graphql',
                       "userToken": None}
        if "userToken" not in options:
            options["userToken"] = None

        self.userToken = options["userToken"]

        self.services = {
            "oauth": options["oauth"],
            "users": options["users"]
        }

        with open('./pub.pem', mode='rb') as pubFile:
            keyData = pubFile.read()
            self.pubKey = rsa.PublicKey.load_pkcs1_openssl_pem(keyData)

        self.auth()

    def GqlRequest(self, query, variables, operations_name):
        result = self.authService(query, variables)
        if not result.get('errors'):
            return result['data'][operations_name]
        else:
            return result

    @staticmethod
    def requiredCheck(options: dict, names):
        for name in names:
            if name not in options.keys():
                raise BaseException(f'{name} is required')

    def auth(self):
        if 'authService' not in self.__dict__:
            self.authService = self._initService(self.services['users'])

            authQuery = '''
                query getAccessTokenByAppSecret($secret: String!, $clientId: String!){
                    getAccessTokenByAppSecret(secret: $secret, clientId: $clientId)
                }
            '''
            variables = {'clientId': self.clientId, 'secret': self.secret}

            authResult = ''

            authResult = self.authService(authQuery, variables)

            print(authResult)

            if authResult.get('errors'):
                raise Exception(authResult)
            else:
                self.accessToken = authResult['data']['getAccessTokenByAppSecret']

                self.oauth = self._initOAuth(headers={
                    'Authorization': 'Bearer {}'.format(self.accessToken)
                })

                self.users = self._initUsers({
                    "Authorization": 'Bearer {}'.format(self.userToken or self.accessToken)
                })

                self.authService = self._initService(self.services['users'], headers={
                    "Authorization": 'Bearer {}'.format(self.userToken or self.accessToken)
                })

                if self.userToken:
                    self.users = self._initUsers({
                        "Authorization": 'Bearer {}'.format(self.userToken)
                    })

    def _initService(self, url, headers={}):
        return AuthingEndPoint(url, headers)

    def _initOAuth(self, headers={}):
        self.oauth = self._initService(self.services['oauth'], headers=headers)
        return self.oauth

    def _initUsers(self, headers={}):
        self.users = self._initService(self.services['users'], headers=headers)
        return self.users

    def login(self, email=None, username: str = None, password=None, verifyCode=None):

        if not email and not username:
            raise Exception('请提供邮箱 email 或用户名 username')

        if not password:
            raise Exception('请提供密码：password')

        loginQuery = """
            mutation login($unionid: String, $email: String, $password: String, $lastIP: String, $registerInClient: String!, $verifyCode: String) {
                login(unionid: $unionid, email: $email, password: $password, lastIP: $lastIP, registerInClient: $registerInClient, verifyCode: $verifyCode) {
                    _id
                    email
                    emailVerified
                    username
                    nickname
                    company
                    photo
                    browser
                    token
                    tokenExpiredAt
                    loginsCount
                    lastLogin
                    lastIP
                    signedUp
                    blocked
                    isDeleted
                }
            }
        """

        _password = self.encrypt(password)

        variables = {
            "password": _password,
            "registerInClient": self.clientId,
            "verifyCode": verifyCode
        }
        if email:
            variables['email'] = email
        elif username:
            variables['username'] = username

        loginResult = self.users(loginQuery, variables)

        if not loginResult.get('errors'):
            self.users = self._initUsers({
                "Authorization": 'Bearer {}'.format(loginResult['data']['login']['token'])
            })
            return loginResult['data']['login']
        else:
            return loginResult

    def loginByPhoneCode(self, phone: str, phoneCode: int):

        if not isinstance(phoneCode, int):
            raise Exception("phoneCode 必须为 int 类型")

        loginQuery = """
            mutation login($phone: String, $phoneCode: Int, $registerInClient: String!, $browser: String) {
                login(phone: $phone, phoneCode: $phoneCode, registerInClient: $registerInClient, browser: $browser) {
                    _id
                    email
                    unionid
                    openid
                    emailVerified
                    username
                    nickname
                    phone
                    company
                    photo
                    browser
                    token
                    tokenExpiredAt
                    loginsCount
                    lastLogin
                    lastIP
                    signedUp
                    blocked
                    isDeleted
                }
            }
        """
        variables = {
            "registerInClient": self.clientId,
            'phone': phone,
            'phoneCode': phoneCode
        }

        loginResult = self.users(loginQuery, variables)
        if not loginResult.get('errors'):
            self.users = self._initUsers({
                "Authorization": 'Bearer {}'.format(loginResult['data']['login']['token'])
            })
            return loginResult['data']['login']
        else:
            return loginResult

    def getVerificationCode(self, phone: str) -> (bool, str):
        """

        :param phone: 手机号
        :return: 返回一个二元组，第一个表示是否成功，第二个为文字提示
        """
        send_sms_spi = "{}/send_smscode/{}/{}".format(
            self.services['users'].replace("/graphql", ''),
            phone,
            self.clientId
        )
        req = urllib.request.Request(send_sms_spi)
        resp = urllib.request.urlopen(req)
        data = json.loads(resp.read())
        code, msg = data['code'], data['message']
        success = code == 200
        return success, msg

    def register(self, email=None, password=None):

        if not email:
            raise Exception('请提供邮箱：email')

        if not password:
            raise Exception('请提供密码：password')

        registerQuery = """
            mutation register(
                $unionid: String,
                $email: String, 
                $password: String, 
                $lastIP: String, 
                $forceLogin: Boolean,
                $registerInClient: String!,
                $oauth: String,
                $username: String,
                $nickname: String,
                $registerMethod: String,
                $photo: String
            ) {
                register(userInfo: {
                    unionid: $unionid,
                    email: $email,
                    password: $password,
                    lastIP: $lastIP,
                    forceLogin: $forceLogin,
                    registerInClient: $registerInClient,
                    oauth: $oauth,
                    registerMethod: $registerMethod,
                    photo: $photo,
                    username: $username,
                    nickname: $nickname
                }) {
                    _id,
                    email,
                    emailVerified,
                    username,
                    nickname,
                    company,
                    photo,
                    browser,
                    password,
                    token,
                    group {
                        name
                    },
                    blocked
                }
            }
        """

        _password = self.encrypt(password)

        variables = {
            'email': email,
            'password': _password,
            'registerInClient': self.clientId
        }

        result = self.users(registerQuery, variables)

        if not result.get('errors'):
            return result['data']['register']
        else:
            return result

    def registerByPhone(self, phone: str, password: str, phoneCode: str, Client: str = None):
        _password = self.encrypt(password)
        variables = {
            'phone': phone,
            'password': _password,
            'phoneCode': phoneCode,
            'registerInClient': self.clientId if not Client else Client,
        }
        registerQuery = """
            mutation register(
                $unionid: String,
                $phone: String, 
                $phoneCode: String,
                $password: String, 
                $lastIP: String, 
                $forceLogin: Boolean,
                $registerInClient: String!,
                $oauth: String,
                $username: String,
                $nickname: String,
                $registerMethod: String,
                $photo: String
            ) {
                register(userInfo: {
                    unionid: $unionid,
                    phone: $phone,
                    phoneCode: $phoneCode,
                    password: $password,
                    lastIP: $lastIP,
                    forceLogin: $forceLogin,
                    registerInClient: $registerInClient,
                    oauth: $oauth,
                    registerMethod: $registerMethod,
                    photo: $photo,
                    username: $username,
                    nickname: $nickname
                }) {
                    _id,
                    email,
                    emailVerified,
                    username,
                    nickname,
                    company,
                    photo,
                    browser,
                    password,
                    token,
                    group {
                        name
                    },
                    blocked
                }
            }
        """
        return self.GqlRequest(registerQuery, variables, 'register')

    def encrypt(self, data):
        _data = rsa.encrypt(data.encode('utf8'), self.pubKey)
        return base64.b64encode(_data).decode()

    def user(self, options):

        if not options.get('id'):
            raise Exception('请提供用户id: { "id": "xxxxxxxx" }')

        query = '''
            query user($id: String!, $registerInClient: String!){
                user(id: $id, registerInClient: $registerInClient) {
                    _id
                    email
                    emailVerified
                    username
                    nickname
                    company
                    photo
                    browser
                    registerInClient
                    registerMethod
                    oauth
                    token
                    tokenExpiredAt
                    loginsCount
                    lastLogin
                    lastIP
                    signedUp
                    blocked
                    isDeleted
                }
            }
        '''
        variables = {
            "id": options['id'],
            "registerInClient": self.clientId
        }

        result = self.users(query, variables)

        if not result.get('errors'):
            return result['data']['user']
        else:
            return result

    def list(self, page=1, count=10):

        query = '''
            query users($registerInClient: String, $page: Int, $count: Int){
              users(registerInClient: $registerInClient, page: $page, count: $count) {
                totalCount
                list {
                  _id
                  email
                  emailVerified
                  username
                  nickname
                  company
                  photo
                  browser
                  password
                  registerInClient
                  token
                  tokenExpiredAt
                  loginsCount
                  lastLogin
                  lastIP
                  signedUp
                  blocked
                  isDeleted
                  group {
                    _id
                    name
                    descriptions
                    createdAt
                  }
                  clientType {
                    _id
                    name
                    description
                    image
                    example
                  }
                  userLocation {
                    _id
                    when
                    where
                  }
                  userLoginHistory {
                    totalCount
                    list{
                      _id
                      when
                      success
                      ip
                      result
                    }
                  }
                  systemApplicationType {
                    _id
                    name
                    descriptions
                    price
                  }
                }
              }
            }
        '''
        variables = {
            "page": page,
            "count": count,
            "registerInClient": self.clientId
        }

        result = self.users(query, variables)

        if not result.get('errors'):
            return result['data']['users']
        else:
            return result

    def checkLoginStatus(self, token=None):
        query = """
            query checkLoginStatus($token: String) {
                checkLoginStatus(token: $token) {
                    status
                    code
                        message
                }
            }        
        """

        result = None

        if not token:
            result = self.users(query)
        else:
            result = self.users(query, {
                token: token
            })

        if not result.get('errors'):
            return result['data']['checkLoginStatus']
        else:
            return result

    def logout(self, uid):

        if not uid:
            raise Exception('请提供用户id：uid')

        return self.update({
            "_id": uid,
            "tokenExpiredAt": 0
        })

    def remove(self, uid):

        if not uid:
            raise Exception('请提供用户id：uid')

        query = """
            mutation removeUsers($ids: [String], $registerInClient: String, $operator: String){
              removeUsers(ids: $ids, registerInClient: $registerInClient, operator: $operator) {
                _id
              }
            }        
        """
        variables = {
            "ids": [uid],
            "registerInClient": self.clientId
        }

        result = self.authService(query, variables)

        if not result.get('errors'):
            return result['data']['removeUsers']
        else:
            return result

    def update(self, options):
        '''
        options = {
            _id: String MUST
            email: String
            emailVerified: Boolean
            username: String
            nickname: String
            company: String
            photo: {String || file object}
            browser: String
            password: String
            oldPassword: String(当有password时, 此参数必需)
            token: String
            tokenExpiredAt: String
            loginsCount: Number
            lastLogin: String
            lastIP: String
            signedUp: String
            blocked: Boolean
            isDeleted: Boolean        
        }
        '''

        if not options.get('_id'):
            raise Exception('请提供用户id: { "_id": "xxxxxxxx" }')

        typeList = {
            '_id': 'String!',
            'email': 'String',
            'emailVerified': 'Boolean',
            'username': 'String',
            'nickname': 'String',
            'company': 'String',
            'photo': 'String',
            'browser': 'String',
            'password': 'String',
            'oldPassword': 'String',
            'registerInClient': 'String!',
            'token': 'String',
            'tokenExpiredAt': 'String',
            'loginsCount': 'Int',
            'lastLogin': 'String',
            'lastIP': 'String',
            'signedUp': 'String',
            'blocked': 'Boolean',
            'isDeleted': 'Boolean'
        }

        query = """
            mutation UpdateUser(
                {0}
            ){
              updateUser(options: {
                {1}
              }) {
                _id
                email
                emailVerified
                username
                nickname
                company
                photo
                browser
                registerInClient
                registerMethod
                oauth
                token
                tokenExpiredAt
                loginsCount
                lastLogin
                lastIP
                signedUp
                blocked
                isDeleted
              }
            }
        """

        variables = options
        variables['registerInClient'] = self.clientId

        def genParams(variables):

            resultTpl = []
            tpl = "${}: {}"

            for key in variables:
                if typeList.get(key):
                    _type = typeList.get(key)
                    resultTpl.append(tpl.format(key, _type))

            return ',\r\n                '.join(resultTpl)

        def genSecondParams(variables):

            resultTpl = []
            tpl = "{}: ${}"

            for key in variables:
                if typeList.get(key):
                    resultTpl.append(tpl.format(key, key))

            return ',\r\n                '.join(resultTpl)

        _query = query.replace('{0}', genParams(variables))
        _query = _query.replace('{1}', genSecondParams(variables))

        print(_query)

        if 'password' in variables:
            variables['password'] = self.encrypt(variables['password'])

        if 'oldPassword' in variables:
            variables['oldPassword'] = self.encrypt(variables['oldPassword'])

        result = self.authService(_query, variables)

        print(_query)

        if not result.get('errors'):
            return result['data']['updateUser']
        else:
            return result

    def sendResetPasswordEmail(self, options={"email": ''}):
        '''
            options = {
                "email": 'xxxxx'
            }
        '''

        if options.get('email'):
            raise Exception('请提供用户邮箱：{"email": "xxxx@xxx.com"}')

        query = """
            mutation sendResetPasswordEmail(
                $email: String!,
                $client: String!
            ){
                sendResetPasswordEmail(
                    email: $email,
                    client: $client
                ) {
                      message
                      code
                }
            }
        """

        variables = {
            "email": options['email'],
            "client": self.clientId
        }

        result = self.authService(query, variables)

        if not result.get('errors'):
            return result['data']['sendResetPasswordEmail']
        else:
            return result

    def verifyResetPasswordVerifyCode(self, options={'email': '', 'verifyCode': ''}):
        '''
            options = {
                email: email,
                verifyCode: verifyCode
            }
        '''

        if options.get('email'):
            raise Exception(
                '请提供用户邮箱：{"email": "xxxx@xxx.com", "verifyCode": "xxxx"}')

        if options.get('verifyCode'):
            raise Exception(
                '请提供验证码：{"email": "xxxx@xxx.com", "verifyCode": "xxxx"}')

        query = """
            mutation verifyResetPasswordVerifyCode(
                $email: String!,
                $client: String!,
                $verifyCode: String!
            ) {
                verifyResetPasswordVerifyCode(
                    email: $email,
                    client: $client,
                    verifyCode: $verifyCode
                ) {
                      message
                      code
                }
            }
        """

        variables = {
            "email": options['email'],
            "verifyCode": options['verifyCode'],
            "client": self.clientId
        }

        result = self.authService(query, variables)

        if not result.get('errors'):
            return result['data']['verifyResetPasswordVerifyCode']
        else:
            return result

    def changePassword(self, options={'email': '', 'verifyCode': '', 'password': ''}):
        '''
            options = {
                email: email,
                password: password,
                verifyCode: verifyCode
            }
        '''

        if options.get('email'):
            raise Exception(
                """请提供用户邮箱：{"email": "xxxx@xxx.com", "verifyCode": "xxxx", "password": "xxxx"'}""")

        if options.get('verifyCode'):
            raise Exception(
                '请提供验证码：{"email": "xxxx@xxx.com", "verifyCode": "xxxx", "password": "xxxx"}')

        query = """
            mutation changePassword(
                $email: String!,
                $client: String!,
                $password: String!,
                $verifyCode: String!
            ){
                changePassword(
                    email: $email,
                    client: $client,
                    password: $password,
                    verifyCode: $verifyCode
                ) {
                    _id
                    email
                    emailVerified
                    username
                    nickname
                    company
                    photo
                    browser
                    registerInClient
                    registerMethod
                    oauth
                    token
                    tokenExpiredAt
                    loginsCount
                    lastLogin
                    lastIP
                    signedUp
                    blocked
                    isDeleted
                }
            }
        """

        variables = {
            "email": options['email'],
            "verifyCode": options['verifyCode'],
            "password": self.encrypt(options['password']),
            "client": self.clientId
        }

        result = self.authService(query, variables)

        if not result.get('errors'):
            return result['data']['changePassword']
        else:
            return result

    def sendVerifyEmail(self, options={"email": ''}):
        '''
            options = {
                client: clientId,
                email: email
            }
        '''

        if options.get('email'):
            raise Exception('请提供用户邮箱：{"email": "xxxx@xxx.com"}')

        query = """
            mutation sendVerifyEmail(
                $email: String!,
                $client: String!
            ){
                sendVerifyEmail(
                    email: $email,
                    client: $client
                ) {
                    message,
                    code,
                    status
                }
            }
        """

        variables = {
            "email": options['email'],
            "client": self.clientId
        }

        result = self.authService(query, variables)

        if not result.get('errors'):
            return result['data']['sendVerifyEmail']
        else:
            return result

    def readOAuthList(self):

        query = '''
            query getOAuthList($clientId: String!) {
                ReadOauthList(clientId: $clientId) {
                    _id
                    name
                    image
                    description
                    type
                    enabled
                    client
                    user
                    oAuthUrl
                }
            }
        '''
        variables = {'clientId': self.clientId}

        result = self.oauth(query, variables)

        if not result.get('errors'):
            return result['data']['ReadOauthList']
        else:
            return result

    def queryPermissions(self, userId):

        query = '''
            query QueryRoleByUserId($user: String!, $client: String!){
                queryRoleByUserId(user: $user, client: $client) {
                totalCount
                list {
                    group {
                    name
                    permissions
                    }
                }
                }
            }
        '''
        variables = {
            'clientId': self.clientId,
            'user': userId
        }

        result = self.authService(query, variables)

        if not result.get('errors'):
            return result['data']['queryRoleByUserId']
        else:
            return result

    def queryRoles(self, options):

        query = '''
            query ClientRoles(
            $clientId: String!
            $page: Int
            $count: Int
            ) {
            clientRoles(
                client: $clientId
                page: $page
                count: $count
            ) {
                totalCount
                list {
                _id
                name
                descriptions
                client
                createdAt
                permissions
                }
            }
            }
        '''
        variables = {
            'clientId': self.clientId,
            'page': options.page,
            'count': options.count
        }

        result = self.authService(query, variables)

        if not result.get('errors'):
            return result['data']['clientRoles']
        else:
            return result

    def updateEmail(self, options):
        '''
        options = {
                email: email,
                emailCode: emailCode,
            }
        '''
        if not options.get('email', None):
            raise Exception('email 不能为空')
        if not options.get('emailCode', None):
            raise Exception('emailCode 不能为空')
        query = '''    
            mutation updateEmail(
                $userPoolId: String!
                $email: String!
                $emailCode: String!
                $oldEmail: String
                $oldEmailCode: String
            ) {
                updateEmail(
                    userPoolId: $userPoolId
                    email: $email
                    emailCode: $emailCode
                    oldEmail: $oldEmail
                    oldEmailCode: $oldEmailCode
                ) {
                    _id
                    email
                    phone
                    emailVerified
                    username
                    nickname
                    company
                    photo
                    browser
                    registerInClient
                    registerMethod
                    oauth
                    token
                    tokenExpiredAt
                    loginsCount
                    lastLogin
                    lastIP
                    signedUp
                    blocked
                    isDeleted
                }
            }
        '''
        variables = {
            'email': options['email'],
            'emailCode': options['emailCode'],
            'oldEmail': options.get('oldEmail'),
            'oldEmailCode': options.get('oldEmailCode'),
            'userPoolId': self.clientId
        }
        result = self.authService(query, variables)
        if not result.get('errors'):
            return result['data']['updateEmail']
        else:
            return result

    def sendChangeEmailVerifyCode(self, email: str):
        if not email:
            raise Exception('错误的邮箱')
        query = """
            mutation sendChangeEmailVerifyCode(
                $email: String!,
                $userPoolId: String!
            ){
                sendChangeEmailVerifyCode(
                email: $email,
                userPoolId: $userPoolId
                ) {
                    message
                    code
                    status
                }
            }
        """
        variables = {
            'email': email,
            'userPoolId': self.clientId,
        }
        result = self.authService(query, variables)
        if not result.get('errors'):
            return result['data']['sendChangeEmailVerifyCode']
        else:
            return result

    def createRole(self, options):

        query = '''
            mutation CreateRole(
                $name: String!
                $client: String!
                $descriptions: String
            ) {
                createRole(
                    name: $name
                    client: $client
                    descriptions: $descriptions
                ) {
                    _id,
                    name,
                    client,
                    descriptions
                }
            }
        '''
        variables = {
            'client': self.clientId,
            'name': options['name'],
            'descriptions': options['descriptions']
        }

        result = self.authService(query, variables)

        if not result.get('errors'):
            return result['data']['createRole']
        else:
            return result

    def updateRolePermissions(self, options):

        query = '''
            mutation UpdateRole(
            $_id: String!
            $name: String!
            $client: String!
            $descriptions: String
            $permissions: String
            ) {
            updateRole(
                _id: $_id
                name: $name
                client: $client
                descriptions: $descriptions
                permissions: $permissions
            ) {
                _id,
                name,
                client,
                descriptions,
                permissions
            }
            }
        '''
        variables = {
            'clientId': self.clientId,
            'name': options.name,
            'permissions': options.permissions,
            '_id': options.roleId
        }

        result = self.authService(query, variables)

        if not result.get('errors'):
            return result['data']['updateRole']
        else:
            return result

    def assignUserToRole(self, options):

        query = '''
            mutation AssignUserToRole(
            $group: String!
            $client: String!
            $user: String!
            ) {
            assignUserToRole(
                group: $group
                client: $client
                user: $user
            ) {
                totalCount,
                list {
                _id,
                client {
                    _id
                },
                user {
                    _id
                },
                createdAt
                }
            }
            }
        '''
        variables = {
            'clientId': self.clientId,
            'group': options.roleId,
            'user': options.user
        }

        result = self.authService(query, variables)

        if not result.get('errors'):
            return result['data']['assignUserToRole']
        else:
            return result

    def removeUserFromRole(self, options):

        query = '''
            mutation RemoveUserFromGroup(
                $group: String!
                $client: String!
                $user: String!
            ) {
            removeUserFromGroup(
                group: $group
                client: $client
                user: $user
            ) {
                _id,
                group {
                    _id
                },
                client {
                    _id
                },
                user {
                    _id
                }
            }
            }
        '''
        variables = {
            'clientId': self.clientId,
            'group': options.roleId,
            'user': options.user
        }

        result = self.authService(query, variables)

        if not result.get('errors'):
            return result['data']['removeUserFromGroup']
        else:
            return result

    def sendRegisterPhoneCode(self, phone: str) -> (bool, str):
        """
        :param phone: 手机号
        :return: 返回一个二元组，第一个表示是否成功，第二个为文字提示
        """
        send_sms_spi = "{}/notification/send_register_smscode/{}/{}".format(
            self.services['users'].replace("/graphql", ''),
            phone,
            self.clientId
        )
        req = urllib.request.Request(send_sms_spi)
        resp = urllib.request.urlopen(req)
        data = json.loads(resp.read())
        code, msg = data['code'], data['message']
        success = code == 200
        return success, msg

    def getUsersByRole(self, roleId: str, page: int = 1, count: int = 10):
        query = """
        query UserGroup($group: String!, $client: String!, $page: Int, $count: Int) {
          userGroup(client: $client, group: $group, page: $page, count: $count) {
            totalCount
            list {
              _id
              group {
                _id
              }
              client {
                _id
              }
              user {
                _id
                photo
                username
                email
              }
              createdAt
            }
          }
        }
        """
        variables = {
            'client': self.clientId,
            'group': roleId,
            'page': page,
            'count': count,
        }
        result = self.authService(query, variables)
        if not result.get('errors'):
            return result['data']['userGroup']
        else:
            return result

    def bindOAuth(self, options):
        query = '''
        mutation bindOtherOAuth(
          $user: String,
          $client: String,
          $type: String!,
          $unionid: String!,
          $userInfo: String!
        ) {
          bindOtherOAuth (
            user: $user,
            client: $client,
            type: $type,
            unionid: $unionid,
            userInfo: $userInfo
          ) {
            _id
            user
            client
            type
            userInfo
            unionid
            createdAt
          }
        }
        '''
        variables = options
        return self.GqlRequest(query, variables, 'bindOtherOAuth')

    def cdnPreflightFun(self) -> bool:
        # 返回对于cdnPreflightUrl的访问是否为 200 如果不为 200 证明 CDN 服务预检失败
        return urllib.request.urlopen(self.cdnPreflightUrl).getcode() == 200

    def preflightFun(self) -> (bool, str):
        # 返回一个 tuple 对于 oauth 和 user 进行检测 如果两者都为 200 则返回true 否则 返回 (False,错误字符串)
        user_status = urllib.request.urlopen(self.preflightUrl['users']).getcode() == 200
        oauth_status = urllib.request.urlopen(self.preflightUrl['oauth']).getcode() == 200
        return user_status and oauth_status, ['用户服务网络预检失败 ', ''][user_status] + ['认证服务网络预检失败', ''][oauth_status]

    def queryMFA(self, userPoolId: str, userId: str) -> dict:
        query = '''
          query queryMFA($_id: String,$userId: String,$userPoolId: String) {
            queryMFA(_id: $_id, userId: $userId, userPoolId: $userPoolId) {
              _id
              userId
              userPoolId
              enable
              shareKey
            }
          }
        '''
        variables = {
            'userPoolId': userPoolId,
            'userId': userId,
        }
        return self.GqlRequest(query, variables, 'queryMFA')

    def loginByPhonePassword(self, phone: str, password: str, registerInClient: str = None,
                             browser: str = 'python_sdk'):
        query = '''
        mutation login($phone: String, $password: String, $registerInClient: String!, $browser: String) {
            login(phone: $phone, password: $password, registerInClient: $registerInClient, browser: $browser) {
              _id
              email
              unionid
              openid
              emailVerified
              username
              nickname
              phone
              company
              photo
              browser
              token
              tokenExpiredAt
              loginsCount
              lastLogin
              lastIP
              signedUp
              blocked
              isDeleted
            }
        }'''
        variables = {
            'phone': phone,
            'password': self.encrypt(password),
            'registerInClient': self.clientId if not registerInClient else registerInClient,
            'browser': browser
        }
        return self.GqlRequest(query, variables, 'login')

    def changeMFA(self, userId: str, enable: bool, userPoolId: str = None):
        query = '''
        mutation changeMFA($_id: String,$userId: String,$userPoolId: String,$enable: Boolean!, $refreshKey: Boolean) {
            changeMFA(_id: $_id, userId: $userId, userPoolId: $userPoolId, enable: $enable, refreshKey: $refreshKey) {
                _id
                userId
                userPoolId
                shareKey
                enable
            }
        }
        '''
        variables = {
            'userId': userId,
            'enable': enable,
            'userPoolId': self.clientId if not userPoolId else userPoolId
        }
        return self.GqlRequest(query, variables, 'changeMFA')

    def getUserPoolSettings(self, userPoolId: str = None) -> dict:
        query = '''
        query getUserPoolSettings($userPoolId: String!) {
        getUserPoolSettings(userPoolId: $userPoolId) {
            name
            logo
            descriptions
            allowedOrigins
            emailVerifiedDefault
            useMiniLogin
            useSelfWxapp
            registerDisabled
            showWXMPQRCode
            enableEmail
            jwtExpired
            }
        }
        '''
        variables = {
            'userPoolId': self.clientId if not userPoolId else userPoolId
        }
        return self.GqlRequest(query, variables, 'getUserPoolSettings')

    def getAuthedAppList(self, userId: str, page: int, count: int, clientId: str = None):
        query = '''
        query GetUserAuthorizedApps($clientId: String, $userId: String, $page: Int, $count: Int) {
            GetUserAuthorizedApps(clientId: $clientId, userId: $userId, page: $page, count: $count) {
              OAuthApps {
                  _id
                  name
                  domain
                  clientId
                  description
                  isDeleted
                  grants
                  redirectUris
                  when
              }
              OIDCApps {
                  _id
                  name
                  client_id
                  domain
                  description
                  authorization_code_expire
                  when
                  isDeleted
                  id_token_signed_response_alg
                  response_types
                  grant_types
                  token_endpoint_auth_method
                  redirect_uris
                  image
                  access_token_expire
                  id_token_expire
                  cas_expire
            
              }
              totalCount
            }
        }
        '''
        variables = {
            'clientId': self.clientId if not clientId else clientId,
            'userId': userId,
            'page': page,
            'count': count
        }

    def sendActivationEmail(self, email: str, client: str = None) -> dict:
        query = '''
        mutation SendVerifyEmail($email: String!, $client: String!) {
            sendVerifyEmail(email: $email, client: $client) {
              message
            }
        }
        '''
        variables = {
            'email': email,
            'client': self.clientId if not client else client,
        }
        return self.GqlRequest(query, variables, 'sendVerifyEmail')

    def updatePhone(self, options):
        '''

        :param options={ userPoolId, phone, phonecode}:
        :return:
        '''
        if not options.get('userPoolId', None):
            options['userPoolId'] = self.clientId
        self.requiredCheck(options, ['phone', 'phoneCode'])
        query = '''
        mutation updatePhone(
            $userPoolId: String!
            $phone: String!
            $phoneCode: String!
            $oldPhone: String
            $oldPhoneCode: String
        ) {
            updatePhone(
                userPoolId: $userPoolId
                phone: $phone
                phoneCode: $phoneCode
                oldPhone: $oldPhone
                oldPhoneCode: $oldPhoneCode
            ) {
                _id
                email
                phone
                emailVerified
                username
                nickname
                company
                photo
                browser
                registerInClient
                registerMethod
                oauth
                token
                tokenExpiredAt
                loginsCount
                lastLogin
                lastIP
                signedUp
                blocked
                isDeleted
            }
        }        
        '''
        return self.GqlRequest(query, options, 'updatePhone')

    def unbindOAuth(self, user, oauth_type: str, client: str = None):
        query = '''
        mutation unbindOtherOAuth(
            $user: String,
            $client: String,
            $type: String!
        ){
            unbindOtherOAuth(
            user: $user,
            client: $client,
            type: $type
            ) {
            _id
            user
            client
            type
            userInfo
            unionid
            createdAt
            }
        }
        '''
        variables = {
            'user': user,
            'client': self.clientId if not client else client,
            'type': oauth_type,
        }
        return self.GqlRequest(query, variables, 'unbindOtherOAuth')

    def sendOneTimePhoneCode(self, phone: str) -> (bool, str):
        """

        :param phone: 手机号
        :return: 返回一个二元组，第一个表示是否成功，第二个为文字提示
        """
        send_sms_spi = "{}/send_smscode/{}/{}".format(
            self.services['users'].replace("/graphql", ''),
            phone,
            self.clientId
        )
        req = urllib.request.Request(send_sms_spi)
        resp = urllib.request.urlopen(req)
        data = json.loads(resp.read())
        code, msg = data['code'], data['message']
        success = code == 200
        return success, msg

    def readUserOAuthList(self, user: str, client: str = None):
        query = '''
        query notBindOAuthList($user: String, $client: String) {
          notBindOAuthList(user: $user, client: $client) {
            type
            oAuthUrl
            image
            name
            binded
          }
        }
        '''
        return self.GqlRequest(query, {
            'user': user,
            'client': self.clientId if not client else client,
        }, 'notBindOAuthList')

    def decodeToken(self, token):
        query = '''
        query decodeJwtToken($token: String) {
          decodeJwtToken(token: $token) {
              data {
                email
                id
                clientId
              }
              status {
                code
                message
              }
              iat
              exp
            }
          }
        '''
        return self.GqlRequest(query, {'token': token}, 'decodeJwtToken')

    def loginByLDAP(self, username, password, client: str = None, browser: str = 'python_sdk'):
        query = '''
        mutation LoginByLDAP($username: String!, $password: String!, $clientId: String!, $browser: String) {
            LoginByLDAP(username: $username, clientId: $clientId, password: $password, browser: $browser) {
                _id
                email
                emailVerified
                unionid
                openid
                oauth
                registerMethod
                username
                nickname
                company
                photo
                browser
                token
                tokenExpiredAt
                loginsCount
                lastLogin
                lastIP
                signedUp
                blocked
            }
        }
        '''
        return self.GqlRequest(query, {
            'username': username,
            'password': password,
            'clientId': self.clientId if not client else client,
            'browser': browser,
        }, 'LoginByLDAP')

    def RefreshToken(self, user: str, client: str = None):
        query = '''
            mutation RefreshToken(
                    $client: String!
                    $user: String!
                ) {
                refreshToken(
                    client: $client
                    user: $user
                ) {
                    token
                    iat
                    exp
                }
            }
        '''
        return self.GqlRequest(query, {
            'user': user,
            'client': self.clientId if not client else client,
        }, 'refreshToken')

    def unbindEmail(self, user: str, client: str = None):
        query = '''
        mutation unbindEmail(
          $user: String,
          $client: String,
        ){
          unbindEmail(
            user: $user,
            client: $client,
          ) {
            _id
            email
            emailVerified
            username
            nickname
            company
            photo
            browser
            registerInClient
            registerMethod
            oauth
            token
            tokenExpiredAt
            loginsCount
            lastLogin
            lastIP
            signedUp
            blocked
            isDeleted
          }
        }
        '''
        return self.GqlRequest(query, {
            'user': user,
            'client': self.clientId if not client else client
        }, 'unbindEmail')

    def revokeAuthedApp(self, user: str, app: str, client: str = None):
        query = '''
        mutation RevokeUserAuthorizedApp($userPoolId: String, $userId: String, $appId: String) {
          RevokeUserAuthorizedApp(userPoolId: $userPoolId, userId: $userId, appId: $appId) {
              isRevoked
              _id
              scope
              appId
              userId
              type
              when
          }
        }
        '''
        return self.GqlRequest(query, {
            'userPoolId': self.clientId if not client else client,
            'userId': user,
            'appId': app,
        }, 'RevokeUserAuthorizedApp')

    def userPatch(self, ids):
        query = '''
        query userPatch($ids: String!){
          userPatch(ids: $ids) {
            list {
              _id
              unionid
              email
              emailVerified
              username
              nickname
              company
              photo
              browser
              registerInClient
              registerMethod
              oauth
              token
              tokenExpiredAt
              loginsCount
              lastLogin
              lastIP
              signedUp
              blocked
              isDeleted
              userLocation {
                _id
                when
                where
              }
              userLoginHistory {
                totalCount
                list {
                  _id
                  when
                  success
                  ip
                  result
                }
              }
            }
            totalCount
          }
        }
        '''
        return self.GqlRequest(query, {'ids': ids}, 'userPatch')
