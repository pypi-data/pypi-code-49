import random
import string
from authing import Authing

test_name = ''
user_id = '5e355ac875bb6c50b05b31ae'
email = "fuergaosi@gmail.com"
username = "holegots"
password = "123456"
phone = "17624555576"
phoneCode = '1234'

clientId = '5e1bded76d0afd49b9792ea4'
secret = '6680cc1caff46b99c886a7ec4a48b8b2'
authing = Authing(clientId, secret, {
    "oauth": 'http://localhost:5510/graphql',
    "users": 'http://localhost:5510/graphql',
})


def random_email():
    return ''.join([random.choice(string.ascii_uppercase) for _ in range(random.randint(5, 12))]) + '@test.com'


def test_list():
    _list = authing.list()
    assert not _list.get('errors')


def test_loginResult_with_email():
    loginResult = authing.login(
        email=email,
        password=password
    )
    assert not loginResult.get('errors')
    global user_id
    user_id = loginResult['_id']


def test_LoginResult_with_username():
    loginResult = authing.login(
        username=username,
        password=password
    )
    assert user_id == loginResult['_id']


def test_getVerificationCode():
    verificationResult = authing.getVerificationCode(phone)
    if verificationResult[-1] == '请求过于频繁，请稍候再试':
        assert not verificationResult[0]
    else:
        assert verificationResult[0]


def test_readOauthList():
    oauthList = authing.readOAuthList()
    assert isinstance(oauthList, list)


def test_User():
    info = authing.user({
        "id": user_id
    })
    assert not info.get('errors')
    assert info['_id'] == user_id


def test_Error_User():
    info = authing.user({
        "id": '5aec1ea610ecb800018db176'
    })
    assert info is None


def test_sendEmailCode():
    code = authing.sendChangeEmailVerifyCode("fuergaosi@gmail.com")
    assert not code.get('errors')


def test_updateEmail():
    result = authing.updateEmail(
        {'email': 'fuergaosi@gmail.com', 'emailCode': '12345'}
    )
    assert result.get('errors')


def test_update():
    update = authing.update({
        "_id": '5aec1ea610ecb800018db176',
        "username": 'alter-by-py'
    })
    assert update.get('errors')


def test_checkLoginStatus():
    res = authing.checkLoginStatus()
    assert not res.get('errors')


def test_remove():
    pass


def test_sendRegisterPhoneCode():
    res = authing.sendRegisterPhoneCode(phone)
    assert not res[0]


def test_getUsersByRole():
    role = authing.createRole({'name': 'my role', 'descriptions': 'python test'})
    res = authing.getUsersByRole(role['_id'])
    assert not res.get('errors')


def test_bindOAuth():
    res = authing.bindOAuth({
        'user': user_id,
        'type': 'Github',
        'unionid': '1123123123',
        'userInfo': '{"uniondid":"1123123123","username":"demo"}'
    })
    assert not res.get('errors')


def test_cdnPreflightFun():
    assert authing.cdnPreflightFun()


def test_preflightFun():
    assert authing.preflightFun()[0]


def test_queryMFA():
    assert not authing.queryMFA().get('errors')
    # 需要当前用户带token访问


def test_loginByPhonePassword():
    authing.loginByPhonePassword(phone, password)


def test_changeMFA():
    assert not authing.changeMFA(user_id, True).get('errors')


def test_getUserPoolSettings():
    assert not authing.getUserPoolSettings().get('errors')


def test_getAuthedAppList():
    assert not authing.getAuthedAppList().get('errors')


def test_sendActivationEmail():
    assert not authing.sendActivationEmail().get('errors')


def test_updatePhone():
    assert authing.updatePhone({'phone': '13461115929', 'phoneCode': '1234'})


def test_unbindOAuth():
    assert authing.unbindOAuth(user_id, 'github').get('errors')


def test_sendOneTimePhoneCode():
    assert authing.sendOneTimePhoneCode(phone).get('errors')


def test_readUserOAuthList():
    assert not authing.readOAuthList().get('errors')


def test_decodeToken():
    assert not authing.decodeToken(authing.accessToken)


def test_loginByLDAP():
    assert not authing.loginByLDAP('tesla', 'password').get('errors')


def test_unbindEmail():
    assert authing.unbindEmail(user_id).get('errors')


def test_registerByPhone():
    authing.registerByPhone(phone, password, phoneCode)


def test_revokeAuthedApp():
    authing.revokeAuthedApp()
    pass
