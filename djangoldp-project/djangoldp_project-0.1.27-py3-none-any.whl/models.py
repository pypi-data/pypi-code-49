import random
import string
from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from djangoldp.models import Model
from .permissions import CustomerPermissions, ProjectPermissions, ProjectMemberPermissions


class Customer(Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    logo = models.URLField(blank=True, null=True)
    companyRegister = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="owned_customers", on_delete=models.DO_NOTHING,
                              null=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        auto_author = 'owner'
        permission_classes=[CustomerPermissions]

    def __str__(self):
        return self.name


class BusinessProvider(Model):
    name = models.CharField(max_length=255)
    fee = models.PositiveIntegerField(default='0')

    def __str__(self):
        return self.name


def auto_increment_project_number():
  last_inc = Project.objects.all().order_by('id').last()
  if not last_inc:
    return 1
  return last_inc.number + 1


class Project(Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    number = models.PositiveIntegerField(default=auto_increment_project_number, editable=False)
    creationDate = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)  # WARN add import
    team = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Member', blank=True)
    captain = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, blank=True, null=True,
                                related_name='+')
    driveID = models.TextField(null=True, blank=True)
    businessProvider = models.ForeignKey(BusinessProvider, blank=True, null=True, on_delete=models.DO_NOTHING)
    jabberID = models.CharField(max_length=255, blank=True, null=True)
    jabberRoom = models.BooleanField(default=True)

    class Meta:
        nested_fields = ['team', 'customer', 'members']
        permission_classes = [ProjectPermissions]
        rdf_type = 'hd:project'

    def __str__(self):
        return self.name

    def get_admins(self):
        return self.members.filter(is_admin=True)


class Member(Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=255, null=True, blank=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        container_path = "project-members/"
        permission_classes = [ProjectMemberPermissions]
        unique_together = ['user', 'project']

    def __str__(self):
        if self.name is None:
            return ""
        return self.name

    def save(self, *args, **kwargs):
        # cannot be duplicated Members
        if not self.pk and Member.objects.filter(project=self.project, user=self.user).exists():
            # override existing member
            existing = Member.objects.get(project=self.project, user=self.user)
            existing.delete()

        super(Member, self).save(*args, **kwargs)


@receiver(pre_save, sender=Project)
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


@receiver(post_save, sender=Project)
def set_captain_as_member(instance, created, **kwargs):
    # add captain as an admin member, if they've not already been added
    if created and instance.captain is not None and\
            not instance.members.filter(user=instance.captain).exists():
        captain = Member(user=instance.captain, project=instance, is_admin=True)
        captain.save()
