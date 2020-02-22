#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: zhangkai
Email: kai.zhang1@nio.com
Last modified: 2018-06-03 00:38:17
'''
import datetime
import hashlib
import random
import uuid

import tornado.web
from bson import ObjectId
from utils import awaitable
from utils import Dict

from .application import Blueprint
from .basehandler import BaseHandler

bp = Blueprint(__name__)


class BaseHandler(BaseHandler):

    def encrypt(self, password):
        return hashlib.md5(f'digua_{password}'.encode()).hexdigest()

    async def gen_code(self, email):
        code = ''.join(random.sample('0123456789', 4))
        key = f'{self.prefix}_code_{email}'
        await awaitable(self.rd.setex(key, 600, code))
        return code

    async def get_user(self, email):
        if email.find('@') >= 0:
            return await awaitable(self.db.users.find_one({'email': email}))
        else:
            return await awaitable(self.db.users.find_one({'username': email}))

    async def check_code(self):
        email = self.get_argument('email', None)
        code = self.get_argument('code', None)
        if email and code:
            key = f'{self.prefix}_code_{email}'
            if code == await awaitable(self.rd.get(key)):
                return Dict({'err': 0})
        return Dict({'err': 1, 'msg': '验证码无效'})

    async def check_username(self):
        username = self.get_argument('username', None)
        if not username:
            return Dict({'err': 1, 'msg': '请输入用户名'})
        if len(username) < 6:
            return Dict({'err': 1, 'msg': '用户名至少6个字符'})
        if len(username) > 20:
            return Dict({'err': 1, 'msg': '用户名至多20个字符'})
        if await awaitable(self.db.users.find_one({'username': username})):
            return Dict({'err': 1, 'msg': '用户名重复'})
        return Dict({'err': 0})

    async def check_email(self):
        email = self.get_argument('email', None)
        if not email:
            return Dict({'err': 1, 'msg': '请输入Email'})
        if len(email) > 64:
            return Dict({'err': 1, 'msg': 'Email地址太长'})
        if not email.find('@') >= 0:
            return Dict({'err': 1, 'msg': '请填写正确的Email格式'})
        if await awaitable(self.db.users.find_one({'email': email})):
            return Dict({'err': 1, 'msg': 'Email地址重复'})
        return Dict({'err': 0})

    async def check_scene(self):
        scene = self.get_argument('scene', None)
        if not scene:
            return Dict({'err': 1, 'msg': f'scene is not defined: {scene}'})

        resp = await self.http.get(scene)
        if not resp.code == 200:
            return Dict({'err': 1, 'msg': f'get scene failed: {scene}'})

        ret = resp.json()
        if not ret.err:
            user = await awaitable(self.db.users.find_one({'openId': ret.openId}))
            ret.token = self.current_user.token
            ret.err = 0
            if not user:
                user = ret
                if self.current_user:
                    ret.active = True
                    await awaitable(self.db.users.update_one({'_id': self.current_user._id}, {'$set': ret}))
                else:
                    user.id = await awaitable(self.db.users.seq_id)
                    user.token = uuid.uuid4().hex
                    user.active = True
                    user.created_at = datetime.datetime.now().replace(microsecond=0)
                    await awaitable(self.db.users.insert_one(user))
            elif self.current_user and self.current_user._id != user._id:
                return {'err': 2, 'msg': f'该微信号已绑定用户{user.id}'}
            expires = datetime.datetime.now() + datetime.timedelta(days=30)
            self.set_cookie('user_token', user.token, expires=expires)
        return ret


@bp.route("/check")
class CheckHandler(BaseHandler):

    async def get(self):
        for key, value in self.args.items():
            if hasattr(self, f'check_{key}'):
                ret = await getattr(self, f'check_{key}')()
                break
        else:
            ret = Dict({'err': 1, 'msg': 'not authorized'})
        self.finish(ret)


@bp.route("/logout")
class LogoutHandler(BaseHandler):

    def get(self):
        self.clear_cookie('user_token')
        self.clear_cookie('user_info')
        self.redirect('/')


@bp.route("/signup")
class SignupHandler(BaseHandler):

    def get(self):
        self.next = self.get_argument('next', '/')
        self.render('signup.html')

    async def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)
        email = self.get_argument('email', None)

        ret = await self.check_username()
        if ret.err:
            return self.finish(ret)

        ret = await self.check_email()
        if ret.err:
            return self.finish(ret)

        if username and password and email:
            token = uuid.uuid4().hex
            seq_id = await awaitable(self.db.users.seq_id)
            doc = self.args.copy()
            doc.update({
                'id': seq_id,
                'username': username,
                'password': self.encrypt(password),
                'email': email,
                'token': token,
                'created_at': datetime.datetime.now().replace(microsecond=0)
            })
            await awaitable(self.db.users.insert_one(doc))
            self.set_cookie('user_token', token, expires_days=30)
            self.finish({'err': 0})
            # await self.app.http.get(f'https://{self.request.host}/email/active', params={'email': email})
        else:
            self.finish({'err': 1, 'msg': '信息未填写完整'})


@bp.route("/signin")
class SigninHandler(BaseHandler):

    def get(self):
        self.next = self.get_argument('next', '/')
        self.render('signin.html')

    async def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)
        remember = self.get_argument('remember', None)
        if username and password:
            if username.find('@') >= 0:
                doc = {'email': username, 'password': self.encrypt(password)}
            else:
                doc = {'username': username, 'password': self.encrypt(password)}
            user = await awaitable(self.db.users.find_one(doc))
            if user:
                ret = {'err': 0, 'msg': '登录成功'}
                if remember == 'on':
                    self.set_cookie('user_token', user.token, expires_days=30)
                else:
                    self.set_cookie('user_token', user.token)
            else:
                ret = {'err': 1, 'msg': '用户名或密码错误'}
        else:
            ret = {'err': 1, 'msg': '请输入用户名和密码'}
        self.finish(ret)


@bp.route("/user")
class UserHandler(BaseHandler):

    async def get(self):
        user = await awaitable(self.current_user)
        if user:
            user = dict([(k, v) for k, v in user.items() if k not in ['token', 'password', '_id']])
            self.finish(user)
        else:
            self.finish({'err': 1, 'msg': '用户未登录'})

    @tornado.web.authenticated
    async def post(self):
        user = await awaitable(self.current_user)
        old_password = self.get_argument('old_password', None)
        password = self.get_argument('password', None)
        if not (old_password and self.encrypt(old_password) == user.password):
            return self.finish({'err': 1, 'msg': '原密码错误'})
        if not password:
            return self.finish({'err': 1, 'msg': '请输入新密码'})
        await awaitable(self.db.users.update_one({'_id': user._id},
                                                 {'$set': {'password': self.encrypt(password)}}))
        self.finish({'err': 0})


@bp.route("/reset")
class ResetHandler(BaseHandler):

    def get(self):
        self.render('reset.html')

    async def post(self):
        ret = await self.check_code()
        if ret.err:
            return self.finish(ret)

        email = self.get_argument('email', None)
        password = self.get_argument('password', None)
        if email and password:
            user = await self.get_user(email)
            if user:
                await awaitable(self.db.users.update_one({'_id': user._id},
                                                         {'$set': {'password': self.encrypt(password)}}))
                self.finish({'err': 0})
            else:
                self.finish({'err': 1, 'msg': '用户不存在'})
        else:
            self.finish({'err': 1, 'msg': '缺少关键信息'})


@bp.route(r'/active/(\w+)')
class ActiveHandler(BaseHandler):

    async def get(self, code):
        email = await awaitable(self.rd.get(f'active_{code}'))
        if email:
            await awaitable(self.db.users.update_one({'email': email}, {'$set': {'active': True}}))
        self.redirect('/admin')

    async def post(self, _id):
        await awaitable(self.db.users.update_one({'_id': ObjectId(_id)}, {'$set': {'active': True}}))
        self.finish({'err': 0})


@bp.route(r'/email/(\w+)')
class EmailHandler(BaseHandler):

    async def get(self, action):
        email = self.get_argument('email', None)
        if not email:
            return self.finish({'err': 1, 'msg': '请输入邮箱'})

        if action == 'reset':
            user = await self.get_user(email)
            if user:
                email = user.email
                title = f'{self.request.host} 重设密码邮件'
                code = await self.gen_code(email)
                content = f'您本次操作的验证码为: {code}'
            else:
                return self.finish({'err': 1, 'msg': '用户不存在'})
        elif action == 'active':
            title = f'{self.request.host} 激活邮件'
            code = uuid.uuid4().hex
            await awaitable(self.rd.setex(f'active_{code}', 600, email))
            url = f'https://{self.request.host}/active/{code}'
            content = f'请点击链接或将其复制到地址栏打开: <br><a href="{url}">{url}</a>'
        else:
            return self.finish({'err': 1, 'msg': 'action is not defined'})

        await self.app.email.send(email, title, content)
        self.finish({'err': 0})

    post = get
