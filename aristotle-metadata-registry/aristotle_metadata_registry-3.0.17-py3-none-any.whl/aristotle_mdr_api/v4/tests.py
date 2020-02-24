from rest_framework.test import APIClient
from django.test import TestCase, tag
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

from aristotle_mdr import models as mdr_models
from aristotle_mdr.contrib.issues import models
from aristotle_mdr.contrib.custom_fields import models as cf_models
from aristotle_mdr.contrib.favourites.models import Tag
from aristotle_mdr_api.token_auth.models import AristotleToken

import logging
import json

logger = logging.getLogger(__name__)


class BaseAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.um = get_user_model()
        self.user = self.um.objects.create_user(
            email='testuser@example.com',
            password='testing123'
        )
        self.other_user = self.um.objects.create_user(
            email='anothertestuser@example.com',
            password='1234'
        )
        self.so = mdr_models.StewardOrganisation.objects.create(
            name='Best Stewardship Organisation',
        )
        self.wg = mdr_models.Workgroup.objects.create(
            name='Best Working Group',
            stewardship_organisation=self.so
        )
        self.su = self.um.objects.create_user(
            email='super@example.com',
            password='1234',
            is_superuser=True
        )

    def login_user(self):
        self.client.login(
            email='testuser@example.com',
            password='testing123'
        )

    def login_superuser(self):
        self.client.login(
            email='super@example.com',
            password='1234'
        )

    def login_other_user(self):
        self.client.login(
            email=self.other_user.email,
            password='1234'
        )

    def create_test_issue(self, user=None):
        submitter = user or self.user
        return models.Issue.objects.create(
            name='Many problem',
            description='many',
            item=self.item,
            submitter=submitter,
        )


def get_simple_issue_data(item):
    return {
        'name': 'Test issue',
        'description': 'Just a test one',
        'labels': [],
        'item': item.pk,
    }


def get_issue_data_with_suggested_changes(item):
    data = get_simple_issue_data(item)
    data.update(
        {'proposal_field': 'name',
         'proposal_value': 'My suggested new name is so much better'}
    )
    return data


class IssueEndpointsTestCase(BaseAPITestCase):
    def setUp(self):
        super().setUp()
        self.item = mdr_models.ObjectClass.objects.create(
            name='API Request',
            definition='A request to an api',
            submitter=self.user
        )

    def post_issue(self, data):
        response = self.client.post(
            reverse('api_v4:issues:create'),
            data,
            format='json'
        )
        return response

    def test_create_issue_own_item(self):
        self.login_user()
        response = self.post_issue(get_simple_issue_data(self.item))

        self.assertEqual(response.status_code, 201)

    def test_create_issue_non_owned_item(self):
        self.login_user()
        item = mdr_models.ObjectClass.objects.create(
            name='New API Request',
            definition='Very new'
        )

        response = self.post_issue(get_simple_issue_data(item))
        self.assertEqual(response.status_code, 400)
        # Make sure error returned for item
        self.assertTrue('item' in response.data)

    def test_submitter_can_propose_changes_on_an_item_they_can_see(self):
        """Tests that a submitter can propose changes on an item they can see"""
        self.wg.giveRoleToUser('submitter', self.user)
        self.login_user()

        item = mdr_models.ObjectClass.objects.create(
            name="An object class with a lot of issues",
            definition="So many issues you would not believe",
            workgroup=self.wg
        )
        data = get_issue_data_with_suggested_changes(item)
        response = self.post_issue(data)

        self.assertEqual(response.status_code, 201)  # Assert that the issue was created

    def test_submitter_cant_propose_changes_on_an_item_they_cant_see(self):
        """Test that a submitter can't propose changes on an item they cannot see"""
        self.wg.giveRoleToUser('submitter', self.user)
        self.login_user()

        other_workgroup = mdr_models.Workgroup.objects.create(name="Another workgroup",
                                                              definition="That the user is not part of",
                                                              stewardship_organisation=self.so)
        item = mdr_models.ObjectClass.objects.create(
            name="An object class with a lot of issues",
            definition="That is invisible to the submitter",
            workgroup=other_workgroup
        )
        data = get_issue_data_with_suggested_changes(item)
        response = self.post_issue(data)

        self.assertEqual(response.status_code, 400)

    def test_submitter_can_create_issue_with_label(self):
        """Test that a submitter can create an issue with a label for the item's stewardship organisation"""
        self.wg.giveRoleToUser('submitter', self.user)
        self.login_user()

        issue_label = models.IssueLabel.objects.create(label="Very important label",
                                                       stewardship_organisation=self.so,
                                                       description="This label is extremely important")
        self.assertTrue(models.IssueLabel.objects.all().count() == 1)

        item = mdr_models.ObjectClass.objects.create(
            name="An object class with a lot of issues",
            definition="That the submitter can see",
            workgroup=self.wg
        )

        data = get_simple_issue_data(item)
        data.update({'labels': [issue_label.pk]})

        response = self.post_issue(data)
        self.assertEqual(response.status_code, 201)

        # Check that the correct label is returned in the response
        self.assertTrue([1] == json.loads(response.content.decode('utf-8'))['labels'])

    @tag('issue_comment')
    def test_create_issue_comment(self):
        self.login_user()
        issue = self.create_test_issue()

        response = self.client.post(
            reverse('api_v4:issues:comment'),
            {
                'body': 'Test comment',
                'issue': issue.id
            },
            format='json'
        )

        self.assertEqual(response.status_code, 201)

        comments = issue.comments.all()
        self.assertEqual(len(comments), 1)

    @tag('issue_comments')
    def test_cant_comment_non_viewable_issue(self):
        issue = self.create_test_issue()

        self.login_other_user()
        response = self.client.post(
            reverse('api_v4:issues:comment'),
            {
                'body': 'Test comment',
                'issue': issue.id
            },
            format='json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertTrue('issue' in response.data)

    @tag('update_and_comment')
    def test_close_with_comment(self):
        issue = self.create_test_issue()

        self.login_user()
        response = self.client.post(
            reverse('api_v4:issues:update_and_comment', args=[issue.pk]),
            {
                'isopen': False,
                'comment': {
                    'body': 'Not an issue'
                }
            },
            format='json'
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue('issue' in response.data)
        self.assertTrue('comment' in response.data)
        self.assertFalse(response.data['issue']['isopen'])

        issue = models.Issue.objects.get(pk=issue.pk)
        self.assertFalse(issue.isopen)
        self.assertEqual(issue.comments.count(), 1)

        issuecomment = issue.comments.first()
        self.assertEqual(issuecomment.body, 'Not an issue')
        self.assertEqual(issuecomment.author, self.user)

    @tag('update_and_comment')
    def test_close_without_comment(self):
        issue = self.create_test_issue()

        self.login_user()
        response = self.client.post(
            reverse('api_v4:issues:update_and_comment', args=[issue.pk]),
            {
                'isopen': False,
            },
            format='json'
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue('issue' in response.data)
        self.assertFalse('comment' in response.data)
        self.assertFalse(response.data['issue']['isopen'])

        issue.refresh_from_db()
        self.assertFalse(issue.isopen)
        self.assertEqual(issue.comments.count(), 0)

    @tag('issue_apply')
    def test_close_with_changes(self):
        updated_definition = 'Fixed definition'

        issue = models.Issue.objects.create(
            name='Fix definition',
            description='It needs fixing',
            item=self.item,
            submitter=self.user,
            proposal_field='definition',
            proposal_value=updated_definition
        )

        self.login_user()
        response = self.client.post(
            reverse('api_v4:issues:approve', args=[issue.pk]),
            {'isopen': False},
            format='json'
        )

        # Check response
        self.assertEqual(response.status_code, 200)

        # Make sure issue is closed
        issue.refresh_from_db()
        self.assertFalse(issue.isopen)

        # Check item was updated
        self.item.refresh_from_db()
        self.assertEqual(self.item.definition, updated_definition)


class CustomFieldsTestCase(BaseAPITestCase):
    def create_test_fields(self):
        cf1 = cf_models.CustomField.objects.create(
            order=1,
            name='Spiciness',
            type='int',
            system_name='spiciness',
            help_text='The Spiciness'
        )
        cf2 = cf_models.CustomField.objects.create(
            order=2,
            name='Blandness',
            type='int',
            system_name='blandness',
            help_text='The Blandness'
        )
        return [cf1.id, cf2.id]

    def test_list_custom_fields(self):
        self.create_test_fields()
        self.login_superuser()

        response = self.client.get(
            reverse('api_v4:custom_field_list'),
        )
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.data), 2)

    def test_creation_of_multiple_custom_fields(self):
        self.login_superuser()
        postdata = [
            {'order': 1, 'name': 'Spiciness', 'system_name': 'spiciness', 'type': 'int', 'help_text': 'The Spiciness'},
            {'order': 2, 'name': 'Blandness', 'system_name': 'blandness', 'type': 'int', 'help_text': 'The Blandness'}
        ]

        response = self.client.post(
            reverse('api_v4:custom_field_list'),
            postdata,
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(cf_models.CustomField.objects.count(), 2)
        self.assertEqual(cf_models.CustomField.objects.filter(name='Spiciness').count(), 1)
        self.assertEqual(cf_models.CustomField.objects.filter(name='Blandness').count(), 1)

    def test_multiple_create_as_standard_user(self):
        self.login_user()
        postdata = [
            {'order': 1, 'name': 'Spiciness', 'system_name': 'spiciness', 'type': 'int', 'help_text': 'The Spiciness'},
            {'order': 2, 'name': 'Blandness', 'system_name': 'blandness', 'type': 'int', 'help_text': 'The Blandness'}
        ]

        response = self.client.post(
            reverse('api_v4:custom_field_list'),
            postdata,
            format='json'
        )
        self.assertEqual(response.status_code, 403)

    def test_multiple_update(self):
        ids = self.create_test_fields()
        self.login_superuser()

        postdata = [
            {'id': ids[0], 'order': 1, 'name': 'Spic', 'system_name': 'spicy', 'type': 'int',
             'help_text': 'The Spiciness'},
            {'id': ids[1], 'order': 2, 'name': 'Bland', 'type': 'int', 'system_name': 'bland',
             'help_text': 'The Blandness'}
        ]

        response = self.client.post(
            reverse('api_v4:custom_field_list'),
            postdata,
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(cf_models.CustomField.objects.count(), 2)
        self.assertEqual(cf_models.CustomField.objects.filter(name='Spic').count(), 1)
        self.assertEqual(cf_models.CustomField.objects.filter(name='Bland').count(), 1)

    def test_reorder_fields(self):
        ids = self.create_test_fields()
        self.login_superuser()

        postdata = [
            {'id': ids[0], 'order': 2, 'name': 'Spiciness', 'system_name': 'spiciness', 'type': 'int',
             'help_text': 'The Spiciness'},
            {'id': ids[1], 'order': 1, 'name': 'Blandness', 'type': 'int', 'system_name': 'blandness',
             'help_text': 'The Blandness'}
        ]
        response = self.client.post(
            reverse('api_v4:custom_field_list'),
            postdata,
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(cf_models.CustomField.objects.count(), 2)
        self.assertEqual(cf_models.CustomField.objects.get(order=1).name, 'Blandness')
        self.assertEqual(cf_models.CustomField.objects.get(order=2).name, 'Spiciness')

    def test_add_field_with_same_name(self):
        ids = self.create_test_fields()
        self.login_superuser()

        postdata = [
            {'id': ids[0], 'order': 1, 'name': 'Blandness', 'system_name': 'spiciness', 'type': 'int',
             'help_text': 'The Spiciness'},
            {'id': ids[1], 'order': 2, 'name': 'Blandness_old', 'system_name': 'blandness', 'type': 'int',
             'help_text': 'The Blandness'}
        ]
        response = self.client.post(
            reverse('api_v4:custom_field_list'),
            postdata,
            format='json'
        )
        self.assertEqual(response.status_code, 200)

    def test_multiple_delete_does_not_work(self):
        ids = self.create_test_fields()
        self.login_superuser()

        postdata = [
            {'id': ids[0], 'order': 1, 'name': 'Spiciness', 'system_name': 'spiciness', 'type': 'int',
             'help_text': 'The Spiciness'},
        ]

        response = self.client.post(
            reverse('api_v4:custom_field_list'),
            postdata,
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(cf_models.CustomField.objects.count(), 2)

    def test_creating_two_fields_with_no_allowed_model_and_same_unique_name_fails(self):
        """Test that the creation of two custom fields with the same allowed model and the same
           unique name is blocked"""
        ids = self.create_test_fields()
        self.login_superuser()

        postdata = [
            {'id': ids[0], 'order': 1, 'name': 'Spiciness', 'unique_name': 'spiciness', 'type': 'int'},
            {'id': ids[1], 'order': 2, 'name': 'Blandness', 'unique_name': 'spiciness', 'type': 'int'}
        ]

        response = self.client.post(
            reverse('api_v4:custom_field_list'),
            postdata,
            format='json'
        )
        self.assertEqual(response.status_code, 400)

    def test_creating_custom_fields_with_same_system_name_but_different_allowed_models_succeeds(self):
        """Test that creating custom fields with the same system_name
        but different allowed models is successfully namespaced"""
        self.login_superuser()

        object_class_ct = ContentType.objects.get_for_model(mdr_models.ObjectClass).pk
        data_element_ct = ContentType.objects.get_for_model(mdr_models.DataElement).pk

        postdata = [
            {'order': 1, 'name': 'Spiciness', 'system_name': 'mildness', 'allowed_model': object_class_ct,
             'type': 'int', 'help_text': 'The Spiciness'},
            {'order': 2, 'name': 'Spiciness', 'system_name': 'mildness', 'allowed_model': data_element_ct,
             'type': 'int', 'help_text': 'The Spiciness'}
        ]

        response = self.client.post(
            reverse('api_v4:custom_field_list'),
            postdata,
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(cf_models.CustomField.objects.all().count(), 2)

        # Check that the system names are set correctly in the database
        custom_field_1 = cf_models.CustomField.objects.get(name='Spiciness', allowed_model=object_class_ct)
        self.assertEqual(custom_field_1.system_name, 'objectclass:mildness')

        custom_field_2 = cf_models.CustomField.objects.get(name='Spiciness', allowed_model=data_element_ct)
        self.assertEqual(custom_field_2.system_name, 'dataelement:mildness')

    def test_creating_custom_fields_with_same_system_name_and_allowed_model_fails(self):
        """Test that creating custom fields with same name and allowed_model fails"""
        self.login_superuser()

        object_class_ct = ContentType.objects.get_for_model(mdr_models.ObjectClass).pk

        postdata = [
            {'order': 1, 'name': 'Spiciness', 'system_name': 'spiciness', 'allowed_model': object_class_ct,
             'type': 'int', 'help_text': 'The Spiciness'},
            {'order': 2, 'name': 'Spiciness', 'system_name': 'spiciness', 'allowed_model': object_class_ct,
             'type': 'int', 'help_text': 'The Spiciness'}
        ]

        response = self.client.post(
            reverse('api_v4:custom_field_list'),
            postdata,
            format='json'
        )

        self.assertEqual(response.status_code, 400)

    def test_creating_custom_field_with_no_system_name_correctly_set_to_all(self):
        self.login_superuser()

        postdata = [{'order': 1, 'name': 'Spiciness', 'system_name': 'spiciness',
                     'type': 'int', 'help_text': 'The Spiciness'}]

        response = self.client.post(
            reverse('api_v4:custom_field_list'),
            postdata,
            format='json'
        )

        self.assertEqual(response.status_code, 200)

        custom_field_1 = cf_models.CustomField.objects.get(name='Spiciness', allowed_model=None)
        self.assertEqual(custom_field_1.system_name, 'all:spiciness')


@tag('perms')
class PermsTestCase(BaseAPITestCase):

    def setUp(self):
        super().setUp()
        self.item = mdr_models.ObjectClass.objects.create(
            name='Brand new item',
            definition='Great'
        )
        self.issue = models.Issue.objects.create(
            name='Many problem',
            description='many',
            item=self.item,
            submitter=self.user
        )

    def post_issue_close(self, issue):
        return self.client.post(
            reverse('api_v4:issues:update_and_comment', args=[issue.pk]),
            {
                'isopen': False,
            },
            format='json'
        )

    def test_get_issue_allowed(self):
        self.item.submitter = self.user
        self.item.save()

        self.login_user()
        response = self.client.get(
            reverse('api_v4:issues:issue', args=[self.issue.pk]),
        )
        self.assertEqual(response.status_code, 200)

    def test_get_issue_not_allowed(self):
        self.login_other_user()
        response = self.client.get(
            reverse('api_v4:issues:issue', args=[self.issue.pk]),
        )
        self.assertEqual(response.status_code, 403)

    def test_close_issue_as_item_viewer(self):
        self.wg.grant_role(user=self.other_user, role=self.wg.roles.viewer)
        self.item.workgroup = self.wg
        self.item.save()

        issue = self.create_test_issue()

        self.login_other_user()
        response = self.post_issue_close(issue)
        self.assertEqual(response.status_code, 403)

    def test_close_issue_as_item_editor(self):
        self.wg.grant_role(user=self.other_user, role=self.wg.roles.submitter)
        self.item.workgroup = self.wg
        self.item.save()

        issue = self.create_test_issue()

        self.login_other_user()
        response = self.post_issue_close(issue)
        self.assertEqual(response.status_code, 200)

    def test_can_always_close_own_issue(self):
        issue = self.create_test_issue(self.other_user)

        self.login_other_user()
        response = self.post_issue_close(issue)
        self.assertEqual(response.status_code, 200)

    def test_item_tag_edit_perms(self):
        oc = mdr_models.ObjectClass.objects.create(
            name='Wow',
            definition='wow',
            submitter=self.other_user
        )

        self.login_user()
        response = self.client.put(
            reverse('api_v4:item_tags', args=[oc.id]),
            {'tags': [{'name': 'wowee'}]},
            format='json'
        )
        self.assertEqual(response.status_code, 403)

    def test_tag_view_perms(self):
        tag = Tag.objects.create(
            name='mytag',
            description='Yeet',
            profile=self.other_user.profile
        )

        self.login_user()
        response = self.client.patch(
            reverse('api_v4:tags', args=[tag.id]),
            {'description': 'no'},
            format='json'
        )
        self.assertEqual(response.status_code, 403)

    def test_tag_delete_perms(self):
        tag = Tag.objects.create(
            name='mytag',
            description='Yeet',
            profile=self.other_user.profile
        )

        self.login_user()
        response = self.client.delete(
            reverse('api_v4:tags', args=[tag.id]),
            {'description': 'no'},
            format='json'
        )
        self.assertEqual(response.status_code, 403)

        self.assertTrue(Tag.objects.filter(id=tag.id).exists())

    def create_token(self, permissions):
        token = AristotleToken.objects.create(
            name='MyToken',
            key='abc',
            user=self.user,
            permissions=permissions
        )

    def query_item_with_token(self, permissions, status_code):
        """Used in the following 2 tests"""
        self.item.submitter = self.user
        self.item.save()
        self.create_token(permissions)
        self.client.credentials(HTTP_AUTHORIZATION='Token abc')
        response = self.client.get(reverse('api_v4:item:item', args=[self.item.id]))
        self.assertEqual(response.status_code, status_code)

    def test_query_item_with_token_correct_perms(self):
        # Query with meteadata read, expect 200
        self.query_item_with_token({'metadata': {'read': True}}, 200)

    def test_query_item_with_token_incorrect_perms(self):
        # Query without metadata read, expect 403
        self.query_item_with_token({'metadata': {'read': False}}, 403)

    def test_query_unviewable_item_with_token(self):
        # Query on item not visible to user, expect 403
        self.create_token({'metadata': {'read': True}})
        self.client.credentials(HTTP_AUTHORIZATION='Token abc')
        response = self.client.get(reverse('api_v4:item:item', args=[self.item.id]))
        self.assertEqual(response.status_code, 403)
