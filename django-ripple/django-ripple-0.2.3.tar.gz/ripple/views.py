
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.core.files.storage import default_storage
from .serializers import (
    ImageAssetSerializer, ArticleSerializer, ArticleCollectionSerializer,
    ArticleOrderSerializer, ArticleCollectionOrderSerializer,
    RichTextAssetSerializer, TextAssetSerializer, PasswordChangeSerializer,
    LoginSerializer, PasswordResetRequestSerializer,
    PasswordResetConfirmSerializer, ConfirmEmailSerializer, SignUpSerializer,
    UserSerializer
)
from .models import (
    ImageAsset, Article, ArticleCollection, ArticleOrder,
    ArticleCollectionOrder, RichTextAsset, TextAsset
)
from .assets import get_assets
from .auth import generate_verify_email_token
from . import errorcodes, get_signup_serializer, get_user_serializer
from ripple.MailFilter import filtered_send_mail
from rest_framework.exceptions import (
    ValidationError as RestValidationError, APIException,
    PermissionDenied, AuthenticationFailed
)
import coreapi
import functools
import json
import logging
import time
import traceback

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import (
    default_token_generator, PasswordResetTokenGenerator)
from django.contrib.auth import (
    authenticate, login as login_, logout as logout_)
from django.contrib.auth.password_validation import validate_password
from django.core import signing
from django.core.exceptions import ValidationError
from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters

from rest_framework import status, views, viewsets
from rest_framework.decorators import api_view, schema
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.generics import (
    ListAPIView, GenericAPIView, CreateAPIView,
    UpdateAPIView, RetrieveAPIView
)


logger = logging.getLogger(__name__)
User = get_user_model()
DAY = 60 * 60 * 24


def handle_errors(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)

        except Exception as e:
            logger.error(traceback.format_exc())

            # let rest_framework handle APIExceptions
            if(isinstance(e, APIException)):
                raise e

            return Response(traceback.format_exc(), status=500)
    return wrapper


unpack_token_schema = AutoSchema(manual_fields=[
    coreapi.Field("token", required=True, location="form",
                  type="string", description="token here"),
])


@api_view(['GET'])
@schema(unpack_token_schema)
@handle_errors
def unpack_token(request):
    """
    Unpack a signed token, return as JSON data.
    """
    token = request.GET.get('token')
    data = signing.loads(token)
    return Response(data)


def validate_expiry(timestamp, msg=''):
    if int(time.time()) > timestamp + 2 * DAY:
        raise ValueError(
            "Sorry, your session has expired, please try %s again.")


@api_view(['POST'])
@handle_errors
def logout(request):
    """
    Log the current user out.

    Returns no content
    """
    logout_(request)
    return Response(None, status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_session_data(request):
    ret = {}

    if 'API' in request.session.keys():
        ret = request.session['API']

    return Response(ret)


@api_view(['POST', 'PATCH'])
def update_session_data(request):
    if 'readonly' in request.data:
        del request.data['readonly']
    if request.method == 'POST':
        request.session['API'] = request.data
    elif request.method == 'PATCH':
        if 'API' not in request.session.keys():
            request.session['API'] = {}
        request.session['API'] = {**request.session['API'], **request.data}

    return Response(None, status=status.HTTP_204_NO_CONTENT)


def session(request):
    ret = {}

    if 'API' in request.session.keys():
        ret = request.session['API']

    return HttpResponse("Session = "+json.dumps(ret),
                        content_type="text/javascript")


def simple_upload(request):
    if request.method == 'POST' and request.FILES['upload'] and request.user.is_staff:
        myfile = request.FILES['upload']
        filename = default_storage.save(myfile.name, myfile)
        uploaded_file_url = default_storage.url(filename)
        return JsonResponse({
            'url': uploaded_file_url
        })
    return None


class TextAssetViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = TextAsset.objects.all()
    serializer_class = TextAssetSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'module': ['exact'], 'version': [
        'gt'], 'owner': ['exact'], 'published': ['exact'], 'assetid': ['exact']}


class RichTextAssetViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = RichTextAsset.objects.all()
    serializer_class = RichTextAssetSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'module': ['exact'], 'version': [
        'gt'], 'owner': ['exact'], 'published': ['exact'], 'assetid': ['exact']}


class ImageAssetViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = ImageAsset.objects.all()
    serializer_class = ImageAssetSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'module': ['exact'], 'version': [
        'gt'], 'owner': ['exact'], 'published': ['exact'], 'assetid': ['exact']}


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    filter_backends = (DjangoFilterBackend, )
    filter_fields = {'module': ['exact'], 'version': [
        'gt'], 'owner': ['exact'], 'published': ['exact'], 'assetid': ['exact']}


class ArticleCollectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = ArticleCollection.objects.all()
    serializer_class = ArticleCollectionSerializer

    filter_backends = (DjangoFilterBackend, )
    filter_fields = {'module': ['exact'], 'version': [
        'gt'], 'owner': ['exact'], 'published': ['exact'], 'assetid': ['exact']}


class ArticleOrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = ArticleOrder.objects.all()
    serializer_class = ArticleOrderSerializer


class ArticleCollectionOrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = ArticleCollectionOrder.objects.all()
    serializer_class = ArticleCollectionOrderSerializer


def assets(request):
    module = request.GET.get('module', 'main')
    return HttpResponse("GlobalAssets = "+json.dumps(get_assets(module=module, user=request.user)),
                        content_type="text/javascript")


def assets_admin(request):
    module = request.GET.get('module', 'main')
    return HttpResponse("GlobalAssets = "+json.dumps(get_assets(module=module, user=request.user)),
                        content_type="text/javascript")


class AccountStatusView(views.APIView):

    def get(self, request, *args, **kwargs):
     
        user = request.user

        if user and user.is_anonymous:
            user = None
        else:
            serialized_user = get_user_serializer()(user)

        response_data = {
            'is_authenticated': False,
            'is_admin': False,
            'is_staff': False,
            'is_email_verified': False
        } if user is None else serialized_user.data

        return Response(response_data)


class SignUpView(CreateAPIView):

    serializer_class = get_signup_serializer()

    def perform_create(self, serializer):
        # log in the user after sign up for simplicity
        super().perform_create(serializer)
        user = serializer.instance
        login_(self.request, user)

    def get_serializer_context(self):

        context = super().get_serializer_context()
        context['send_welcome_email'] = True
        return context


class LoginView(GenericAPIView):

    # @method_decorator(sensitive_post_parameters())
    def post(self, request):

        self.request = request

        serializer = LoginSerializer(
            data=request.data, context={'request': request})

        serializer.is_valid(raise_exception=True)

        login_(self.request, serializer.validated_data['user'])

        user_status = UserSerializer(request.user)

        return Response(user_status.data, status=status.HTTP_200_OK)


class LogoutView(views.APIView):

    permission_classes = (IsAuthenticated,)

    @handle_errors
    def post(self, request, *args, **kwargs):

        logout_(request)
        return Response({'detail': _('Successfully logged out.')},
                        status=status.HTTP_204_NO_CONTENT)


class PasswordChangeView(GenericAPIView):

    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    # prevents passwords being logged out
    @method_decorator(sensitive_post_parameters(
        'old_password', 'new_password1', 'new_password2'
    ))
    def dispatch(self, request, *args, **kwargs):

        return super(PasswordChangeView, self).dispatch(request, args, **kwargs)

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response({'detail': _("Password has been changed")})


class PasswordResetRequestView(GenericAPIView):

    serializer_class = PasswordResetRequestSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        # TODO red - wording correct?
        return Response({'detail': _((f"An email has been sent to {serializer.data['email']} with"
                                      " instructions to reset your password"))})
        # {"detail": _("Password reset request received.")})


class PasswordResetConfirmView(GenericAPIView):

    serializer_class = PasswordResetConfirmSerializer
    permission_classes = (AllowAny,)

    @method_decorator(sensitive_post_parameters(
        'new_password1', 'new_password2')
    )
    def dispatch(self, *args, **kwargs):
        return super(PasswordResetConfirmView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        # TODO red - log in after reset?

        login_(request, serializer.user)
        return Response({'detail': _('Password has been updated.')})


class SendEmailVerificationView(views.APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):

        request.user.send_verification_email()
        # TODO red - could save token in db and expire old tokens if multiple
        #  emails are requested

        return Response({'detail': 'Verification Email Sent.'})


class ConfirmEmailView(GenericAPIView):

    serializer_class = ConfirmEmailSerializer

    def post(self, request):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        login_(request, user)

        return Response({'detail': 'Email Verified Successfully'})

class UserUpdateView(UpdateAPIView, RetrieveAPIView):
    """
        get/put/patch end point for updating current
        user model data
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):

        queryset = get_user_model().objects.filter(
            id=self.request.user.id
        )
        return queryset
