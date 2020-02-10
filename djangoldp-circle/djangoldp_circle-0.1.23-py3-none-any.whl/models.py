import random
import string
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from djangoldp.models import Model
from .permissions import CirclePermissions, CircleMemberPermissions

STATUS_CHOICES = [
    ('Public', 'Public'),
    ('Private', 'Private'),
    ('Archived', 'Archived'),
]


class Circle(Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    creationDate = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='Public')
    team = models.ManyToManyField(settings.AUTH_USER_MODEL, through="CircleMember", blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="owned_circles", on_delete=models.DO_NOTHING)
    jabberID = models.CharField(max_length=255, blank=True, null=True, unique=True)
    jabberRoom = models.BooleanField(default=True)

    class Meta:
        auto_author = 'owner'
        nested_fields = ["team", 'members']
        permission_classes = [CirclePermissions]
        rdf_type = 'hd:circle'

    def __str__(self):
        return self.name

    def get_admins(self):
        return self.members.filter(is_admin=True)


class CircleMember(Model):
    circle = models.ForeignKey(Circle, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="circles")
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return str(self.circle.name) + " - " + str(self.user.name())

    class Meta:
        container_path = "circle-members/"
        permission_classes = [CircleMemberPermissions]
        unique_together = ['user', 'circle']

    def save(self, *args, **kwargs):
        # cannot be duplicated CircleMembers
        if not self.pk and CircleMember.objects.filter(circle=self.circle, user=self.user).exists():
            return

        super(CircleMember, self).save(*args, **kwargs)

@receiver(pre_save, sender=Circle)
def set_jabberid(sender, instance, **kwargs):
    if settings.JABBER_DEFAULT_HOST and not instance.jabberID:
        instance.jabberID = '{}@conference.{}'.format(
            ''.join(
                [
                    random.choice(string.ascii_letters + string.digits)
                    for n in range(12)
                ]
            ).lower(),
            settings.JABBER_DEFAULT_HOST
        )
        instance.jabberRoom = True

@receiver(post_save, sender=Circle)
def set_owner_as_member(instance, created, **kwargs):
    # add owner as an admin member
    if created and not instance.members.filter(user=instance.owner).exists():
        CircleMember.objects.create(user=instance.owner, circle=instance, is_admin=True)
