import aristotle_mdr.models as models
from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from aristotle_mdr.tests import utils
from aristotle_mdr.contrib.issues.models import Issue
from aristotle_mdr.contrib.reviews.models import ReviewRequest, REVIEW_STATES
from aristotle_bg_workers.tasks import send_notification_email

from django.core import mail
from django.conf import settings
from django.urls import reverse

import logging
import datetime
import reversion

logger = logging.getLogger(__name__)


class TestNotifications(utils.AristotleTestUtils, TestCase):
    defaults = {}

    def setUp(self):
        super().setUp()

        self.kenobi = get_user_model().objects.create_user('kenobi@jedi.order', 'password')

        with reversion.create_revision():
            self.item1 = models.ObjectClass.objects.create(
                name="Test Item 1 (visible to tested viewers)",
                definition="my definition",
                workgroup=self.wg1,
            )
            self.item2 = models.ObjectClass.objects.create(
                name="Test Item 2 (NOT visible to tested viewers)",
                definition="my definition",
                workgroup=self.wg2,
            )
            self.item3 = models.ObjectClass.objects.create(
                name="Test Item 3 (visible to tested viewers)",
                definition="my definition",
                workgroup=self.wg1,
            )

    def test_subscriber_is_notified_of_workgroup_item_edit(self):
        """Test that a user is notified when an item in their wg is edited"""
        self.assertEqual(self.viewer.notifications.count(), 0)

        with reversion.create_revision():
            reversion.set_user(self.editor)
            self.item1.name = 'changed'
            self.item1.save()

        self.assertEqual(self.viewer.notifications.count(), 1)

    def test_subscriber_is_not_notified_of_workgroup_item_edit_with_setting_off(self):
        """Test that a user is not notified when an item in their wg is edited without setting"""

        self.viewer.profile.notificationPermissions['metadata changes']['general changes'] = {
            "items in my workgroups": False,
            "items I have tagged / favourited": True,
            "any items I can edit": False
        }
        self.viewer.profile.save()
        self.assertEqual(self.viewer.notifications.count(), 0)

        with reversion.create_revision():
            reversion.set_user(self.editor)
            self.item1.name = 'changed'
            self.item1.save()

        self.assertEqual(self.viewer.notifications.count(), 0)

    def test_subscriber_is_notified_of_discussion(self):
        """Test that a user is notified of a discussion for an item they subscribe to"""
        self.assertEqual(self.wg1.discussions.all().count(), 0)

        self.assertEqual(self.viewer.notifications.count(), 0)
        # Create post in same workgroup
        models.DiscussionPost.objects.create(
            title="Hello",
            body="Sam",
            author=self.editor,
            workgroup=self.wg1
        )

        self.assertTrue('(discussion) has been created' in self.viewer.notifications.first().verb)
        self.assertEqual(self.viewer.notifications.count(), 1)

    def test_subscriber_not_notified_of_discussion_with_setting_off(self):
        """Test that a user who has turned off discussion notifications doesnt recieve them"""
        self.viewer.profile.notificationPermissions['discussions']['new posts'] = False
        self.viewer.profile.save()

        self.assertEqual(self.viewer.notifications.count(), 0)
        models.DiscussionPost.objects.create(
            title="Hello",
            body="Sam",
            author=self.editor,
            workgroup=self.wg1
        )
        self.assertEqual(self.viewer.notifications.count(), 0)

    def test_subscriber_is_notified_of_comment(self):
        """Test that a user is notified of a comment for an item they subscribe to"""
        self.assertEqual(self.wg1.discussions.all().count(), 0)
        self.wg1.giveRoleToUser('viewer', self.kenobi)

        surprise = models.DiscussionPost.objects.create(
            title="Hello",
            body="There",
            author=self.kenobi,
            workgroup=self.wg1
        )

        self.assertEqual(self.kenobi.notifications.count(), 0)
        models.DiscussionComment.objects.create(
            body="General kenobi!!",
            author=self.viewer,
            post=surprise,
        )

        self.assertEqual(self.kenobi.notifications.count(), 1)

    def test_subscriber_not_notified_of_comment_with_setting_off(self):
        """Test that a user who has turned off discussion notifications doesnt recieve them"""
        self.wg1.giveRoleToUser('viewer', self.kenobi)
        self.kenobi.profile.notificationPermissions['discussions']['new comments'] = False
        self.kenobi.profile.save()

        surprise = models.DiscussionPost.objects.create(
            title="Hello",
            body="There",
            author=self.kenobi,
            workgroup=self.wg1
        )

        self.assertEqual(self.kenobi.notifications.count(), 0)
        models.DiscussionComment.objects.create(
            body="General kenobi!!",
            author=self.viewer,
            post=surprise,
        )

        self.assertEqual(self.kenobi.notifications.count(), 0)

    def test_subscriber_is_not_notified_of_own_post(self):
        """Test that a user does not get a notification for their own post"""
        self.wg1.giveRoleToUser('viewer', self.kenobi)

        self.assertEqual(self.kenobi.notifications.count(), 0)
        surprise = models.DiscussionPost.objects.create(
            title="Hello",
            body="There",
            author=self.kenobi,
            workgroup=self.wg1
        )

        self.assertEqual(self.kenobi.notifications.count(), 0)

    def test_subscriber_is_not_notified_of_own_comment(self):
        """Test that a user does not get a notification for their own comment"""
        self.wg1.giveRoleToUser('viewer', self.kenobi)

        self.assertEqual(self.kenobi.notifications.count(), 0)
        surprise = models.DiscussionPost.objects.create(
            title="Hello",
            body="There",
            author=self.kenobi,
            workgroup=self.wg1
        )
        models.DiscussionComment.objects.create(
            body="General kenobi!!",
            author=self.kenobi,
            post=surprise,
        )

        self.assertEqual(self.kenobi.notifications.count(), 0)

    def test_subscriber_is_notified_of_supersede(self):
        """Test that a user is notified of a supersede for an item they subscribe to"""
        self.favourite_item(self.viewer, self.item1)
        self.assertTrue(self.viewer in self.item1.favourited_by.all())

        self.assertEqual(self.viewer.notifications.all().count(), 0)
        self.assertTrue(self.item1.can_view(self.viewer))
        self.assertTrue(self.item3.can_view(self.viewer))

        models.SupersedeRelationship.objects.create(
            older_item=self.item1,
            newer_item=self.item3,
            registration_authority=self.ra
        )
        self.assertTrue(self.item3 in self.item1.superseded_by_items.visible(self.viewer))

        self.assertEqual(self.viewer.notifications.all().count(), 2)
        self.assertTrue('has been superseded in the workgroup' in self.viewer.notifications.first().verb)
        self.assertTrue('(favourite item) has been superseded in the workgroup' in self.viewer.notifications.last().verb)

    def test_subscriber_is_not_notified_of_supersede_with_setting_off(self):
        """Test that a user who has turned off supersedes notifications doesnt recieve them"""
        self.viewer.profile.notificationPermissions['metadata changes']['superseded'] = {
            'items in my workgroups': False,
            'any items I can edit': False,
            'items I have tagged / favourited': True,
        }
        self.viewer.profile.save()

        self.assertEqual(self.viewer.notifications.all().count(), 0)
        models.SupersedeRelationship.objects.create(
            older_item=self.item1,
            newer_item=self.item3,
            registration_authority=self.ra
        )
        self.assertEqual(self.viewer.notifications.all().count(), 0)

    def test_subscriber_is_not_notified_of_supersedes_on_invisible_items(self):
        user1 = get_user_model().objects.create_user('subscriber@example.com', 'subscriber')
        self.wg1.giveRoleToUser('viewer', user1)
        self.favourite_item(user1, self.item1)
        self.assertTrue(user1 in self.item1.favourited_by.all())

        self.assertEqual(user1.notifications.all().count(), 0)
        self.assertTrue(self.item1.can_view(user1))
        self.assertFalse(self.item2.can_view(user1))

        models.SupersedeRelationship.objects.create(
            older_item=self.item1,
            newer_item=self.item2,
            registration_authority=self.ra
        )

        self.assertFalse(self.item2 in self.item1.superseded_by_items.visible(user1))

        user1 = get_user_model().objects.get(pk=user1.pk)
        self.assertEqual(user1.notifications.all().count(), 0)

    def test_registrar_is_notified_for_review_request(self):
        """Test that a registrar is notified of a new review request in their RA"""
        self.assertEqual(self.registrar.notifications.all().count(), 0)

        # Create review request in registrars ra
        rr = ReviewRequest.objects.create(
            registration_authority=self.ra,
            requester=self.viewer,
            workgroup=self.wg1,
        )

        self.assertEqual(self.registrar.notifications.all().count(), 1)
        notification = self.registrar.notifications.first()
        self.assertIn('created a review request', notification.verb)

    def test_registrar_is_notified_for_review_request_update(self):
        """Test that a registrar is notified of an updated review request in their RA"""
        # Create review request in registrars ra
        rr = ReviewRequest.objects.create(
            registration_authority=self.ra,
            requester=self.viewer,
            workgroup=self.wg1,
        )

        self.assertEqual(self.registrar.notifications.all().count(), 1)

        rr.staus = REVIEW_STATES.approved
        rr.save()

        self.assertEqual(self.registrar.notifications.all().count(), 2)
        notification = self.registrar.notifications.first()
        self.assertIn('Review request updated', notification.verb)

    def test_registrar_is_notified_of_supersede(self):
        """Test that a registrar is notified of a supersede for an item registered by their RA"""
        models.Status.objects.create(
            concept=self.item1,
            registrationAuthority=self.ra,
            registrationDate=datetime.date(2015, 4, 28),
            state=self.ra.locked_state
        )
        models.Status.objects.create(
            concept=self.item2,
            registrationAuthority=self.ra,
            registrationDate=datetime.date(2015, 4, 28),
            state=self.ra.locked_state
        )
        user1 = self.registrar
        user1.notifications.all().delete()

        self.assertEqual(user1.notifications.all().count(), 0)
        models.SupersedeRelationship.objects.create(
            older_item=self.item1,
            newer_item=self.item2,
            registration_authority=self.ra
        )

        self.assertTrue(self.item2 in self.item1.superseded_by_items.visible(user1))
        self.assertEqual(user1.notifications.all().count(), 1)
        self.assertTrue('(item registered by ' + self.ra.name + ') has been superseded.' in user1.notifications.first().verb)

    def test_registrar_is_notified_of_status_change(self):
        user1 = self.registrar
        user1.notifications.all().delete()

        self.assertEqual(user1.notifications.all().count(), 0)

        models.Status.objects.create(
            concept=self.item1,
            registrationAuthority=self.ra,
            registrationDate=timezone.now(),
            state=self.ra.locked_state
        )

        self.assertTrue(self.item1.statuses.count() == 1)
        self.assertEqual(user1.notifications.all().count(), 1)
        self.assertTrue("has been registered by Test RA with the status 'Candidate'." in user1.notifications.first().verb)

        models.Status.objects.create(
            concept=self.item1,
            registrationAuthority=self.ra,
            registrationDate=timezone.now(),
            state=self.ra.public_state
        )

        self.assertEqual(user1.notifications.all().count(), 2)
        self.assertTrue('(item registered by ' + self.ra.name + ") has changed its status to " in user1.notifications.first().verb)

    def test_subscriber_is_not_notified_when_issue_is_created_by_himself(self):

        user1 = get_user_model().objects.create_user('subscriber@example.com', 'subscriber')

        self.wg1.giveRoleToUser('viewer', user1)

        Issue.objects.create(
            name="My huge issue",
            description="This issue is very important!",
            item=self.item1,
            submitter=user1,
            isopen=True
        )

        self.assertEqual(user1.notifications.count(), 0)

    def test_subscriber_is_notified_when_issue_is_created(self):
        user1 = get_user_model().objects.create_user('subscriber@example.com', 'subscriber')
        user2 = get_user_model().objects.create_user('subscriber2@example.com', 'subscriber2')

        self.wg1.giveRoleToUser('viewer', user1)
        self.wg1.giveRoleToUser('viewer', user2)

        Issue.objects.create(
            name="My huge issue",
            description="This issue is very important!",
            item=self.item1,
            submitter=user1,
            isopen=True
        )

        self.assertEqual(user2.notifications.count(), 1)

    def test_subscriber_is_notified_when_favourited_item_edited(self):
        user = get_user_model().objects.create_user('subscriber@example.com', 'subscriber')

        self.favourite_item(user, self.item1)

        with reversion.create_revision():
            reversion.set_user(self.editor)
            self.item1.name = "This is a new name"
            self.item1.save()

        self.assertEqual(user.notifications.count(), 1)

    def test_subscriber_is_not_notified_when_favourited_item_edited_by_themselves(self):
        """Users should not receive notifications for actions they perform themselves"""
        self.favourite_item(self.editor, self.item1)

        with reversion.create_revision():
            reversion.set_user(self.editor)
            self.item1.name = "This is a new name"
            self.item1.save()

        self.assertEqual(self.editor.notifications.count(), 0)

    def test_subscriber_is_not_notified_when_within_aristotle_setting_off(self):
        """Test that a subscriber does not get notifications if the within aristotle method is off"""
        user1 = get_user_model().objects.create_user('subscriber@example.com', 'subscriber')
        user1.profile.notificationPermissions["notification methods"]["within aristotle"] = False
        user1.profile.save()
        self.favourite_item(user1, self.item1)

        self.item1.name = "This is a new name"
        self.item1.save()

        self.assertEqual(user1.notifications.count(), 0)

    def test_subscriber_is_notified_by_email(self):
        user1 = get_user_model().objects.create_user('subscriber@example.com', 'subscriber')
        user1.profile.notificationPermissions["notification methods"]["email"] = True
        user1.profile.save()

        send_notification_email(user1.email, "hello world")

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to[0], user1.email)
        self.assertEqual(mail.outbox[0].subject, 'Notification')
        self.assertEqual(mail.outbox[0].from_email, settings.DEFAULT_FROM_EMAIL)
        self.assertEqual(mail.outbox[0].body, 'hello world')

    def test_notification_visible_on_page(self):
        self.test_subscriber_is_notified_of_comment()
        notification_text = "(comment) has been created in the discussion"

        self.logout()
        response = self.client.post(
            reverse('friendly_login'),
            {'username': 'kenobi@jedi.order', 'password': 'password'}
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse("aristotle:userInbox"))
        self.assertContains(response, notification_text)

        # Mark all as read - none should exist any more.
        self.kenobi.notifications.mark_all_as_read()
        self.assertEqual(0, self.kenobi.notifications.unread().count())
        response = self.client.get(reverse("aristotle:userInbox"))
        self.assertNotContains(response, notification_text)

        # but notifications are still visible in the all messages page
        response = self.client.get(reverse("aristotle:userInboxAll"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, notification_text)
