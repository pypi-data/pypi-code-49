from django.shortcuts import get_object_or_404
from django.utils.text import Truncator
from rest_framework import serializers
from django.contrib.auth import get_user_model

from aparnik.contrib.users.api.serializers import UserSummaryListSerializer
from aparnik.contrib.filefields.api.serializers import FileFieldListSerailizer

from ..models import ChatSession, ChatSessionMessage, ChatSessionMember, ChatSessionTypeEnum

User = get_user_model()


# serializer
# Chat Session
class ChatSessionListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    url_members = serializers.SerializerMethodField()
    url_messages = serializers.SerializerMethodField()
    url_messages_create = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()
    title_session = serializers.SerializerMethodField()
    cover = serializers.SerializerMethodField()
    resourcetype = serializers.SerializerMethodField()

    class Meta:
        model = ChatSession
        fields = [
            'id',
            'url',
            'url_members',
            'url_messages',
            'url_messages_create',
            'owner',
            'title_session',
            'cover',
            'uri',
            'type',
            'created_at',
            'resourcetype',
        ]

        read_only_fields = [
            'id',
            'url',
            'url_members',
            'url_messages',
            'url_messages_create',
            'uri',
            'title_session',
            'cover',
            'created_at',
            'resourcetype',
        ]


    def get_owner(self, obj):
        return UserSummaryListSerializer(obj.owner, many=False, read_only=True, context=self.context).data

    def get_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.get_api_uri())

    def get_url_members(self, obj):
        return self.context['request'].build_absolute_uri(obj.get_member_api_uri())

    def get_url_messages(self, obj):
        return self.context['request'].build_absolute_uri(obj.get_messages_api_uri())

    def get_url_messages_create(self, obj):
        return self.context['request'].build_absolute_uri(obj.get_messages_create_api_uri())

    def get_title_session(self, obj):
        if obj.type == ChatSessionTypeEnum.PRIVATE:
            return obj.owner.get_full_name()
        return obj.title

    def get_cover(self, obj):
        cover_obj = None
        if obj.type == ChatSessionTypeEnum.PRIVATE:
            cover_obj = obj.owner.avatar
        else:
            cover_obj = obj.cover_obj
        if cover_obj:
            return FileFieldListSerailizer(cover_obj, many=False, read_only=True, context=self.context).data
        return None

    def get_resourcetype(self, obj):
        return obj.resourcetype


# Details Serializer
class ChatSessionDetailsSerializer(ChatSessionListSerializer):
    # members
    username = serializers.CharField(write_only=True, required=False)
    title = serializers.IntegerField(write_only=True, required=False)
    cover_obj_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = ChatSession
        fields = ChatSessionListSerializer.Meta.fields + [
            'username',
            'title',
            'cover_obj_id',
        ]

        read_only_fields = ChatSessionListSerializer.Meta.read_only_fields + [

        ]

    def update(self, instance, validated_data):
        self.handle_username(instance, validated_data)
        return super(ChatSessionDetailsSerializer, self).update(instance, validated_data)
    
    def create(self, validated_data):
        username = validated_data.get('username', None)
        if username:
            del validated_data['username']
        instance = super(ChatSessionDetailsSerializer, self).create(validated_data)
        validated_data['username'] = username
        self.handle_username(instance, validated_data)
        return instance

    def handle_username(self, instance, validated_data):
        username = validated_data.get('username', None)
        if username is not None:
            user = get_object_or_404(User.objects.all(), username=username)

            owner = instance.owner

            if owner != user:  # Only allow non owners join the room
                instance.members.get_or_create(
                    user=user, chat_session=instance
                )

    # def get_members(self, obj):
    #     members = [
    #         UserSummaryListSerializer(chat_session.user, many=False, read_only=True, context={'request': request})
    #         for chat_session in chat_session.members.all()
    #     ]
    #     members.insert(0, owner)  # Make the owner the first member

# Chat session member
class ChatSessionMemberListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    url_delete = serializers.SerializerMethodField()
    resourcetype = serializers.SerializerMethodField()

    class Meta:
        model = ChatSessionMember
        fields = [
            'user',
            'url_delete',
            'resourcetype',
        ]

        read_only_fields = [
            'user',
            'url_delete',
            'resourcetype',
        ]

    def get_user(self, obj):
        return UserSummaryListSerializer(obj.user, many=False, read_only=True, context=self.context).data

    def get_url_delete(self, obj):
        return self.context['request'].build_absolute_uri(obj.get_api_uri())

    def get_resourcetype(self, obj):
        return obj.resourcetype

class ChatSessionMemberDetailsSerializer(ChatSessionMemberListSerializer):

    class Meta:
        model = ChatSessionMember
        fields = ChatSessionMemberListSerializer.Meta.fields + [

        ]

        read_only_fields = ChatSessionMemberListSerializer.Meta.read_only_fields + [

        ]


# ChatSessionMessage
class ChatSessionMessageListSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    resourcetype = serializers.SerializerMethodField()
    
    class Meta:
        model = ChatSessionMessage
        fields = [
            'id',
            'user',
            'message',
            'file',
            'resourcetype',
        ]

        read_only_fields = [
            'file',
            'resourcetype',
        ]

    def get_file(self, obj):
        if obj.file_obj:
            return FileFieldListSerailizer(obj.file_obj, many=False, read_only=True, context=self.context).data
        return None

    def get_user(self, obj):
        return UserSummaryListSerializer(obj.user, many=False, read_only=True, context=self.context).data

    def get_resourcetype(self, obj):
        return obj.resourcetype

# Details Serializer
class ChatSessionMessageDetailsSerializer(ChatSessionMessageListSerializer):

    file_obj_id = serializers.IntegerField(required=False, write_only=True)

    class Meta:
        model = ChatSessionMessage
        fields = ChatSessionMessageListSerializer.Meta.fields + [
            'file_obj_id',
        ]

        read_only_fields = ChatSessionMessageListSerializer.Meta.read_only_fields + [

        ]
