import uuid

from core import fields
from django.db import models
from policy.models import Policy


class Premium(models.Model):
    id = models.AutoField(db_column='PremiumId', primary_key=True)
    uuid = models.CharField(db_column='PremiumUUID', max_length=36, default=uuid.uuid4, unique=True)
    legacy_id = models.IntegerField(
        db_column='LegacyID', blank=True, null=True)
    policy = models.ForeignKey(
        Policy, models.DO_NOTHING, db_column='PolicyID')
    payer = models.ForeignKey(
        "contribution.Payer", models.DO_NOTHING, db_column='PayerID', blank=True, null=True)
    amount = models.DecimalField(
        db_column='Amount', max_digits=18, decimal_places=2)
    receipt = models.CharField(db_column='Receipt', max_length=50)
    pay_date = fields.DateField(db_column='PayDate')
    pay_type = models.CharField(db_column='PayType', max_length=1)
    is_photo_fee = models.BooleanField(
        db_column='isPhotoFee', blank=True, null=True)
    is_offline = models.BooleanField(
        db_column='isOffline', blank=True, null=True)
    reporting_id = models.IntegerField(
        db_column='ReportingId', blank=True, null=True)
    validity_from = fields.DateTimeField(db_column='ValidityFrom')
    validity_to = fields.DateTimeField(
        db_column='ValidityTo', blank=True, null=True)
    audit_user_id = models.IntegerField(db_column='AuditUserID')
    # rowid = models.TextField(db_column='RowID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblPremium'


class Payer(models.Model):
    PAYER_TYPE_COOP = 'C'
    PAYER_TYPE_DONOR = 'D'
    PAYER_TYPE_GOV = 'G'
    PAYER_TYPE_LOCAL_AUTH = 'L'
    PAYER_TYPE_OTHER = 'O'
    PAYER_TYPE_PRIVATE_ORG = 'P'
    PAYER_TYPE_CHOICES = (
        (PAYER_TYPE_COOP, 'Co-operative'),
        (PAYER_TYPE_DONOR, 'Donor'),
        (PAYER_TYPE_GOV, 'Government'),
        (PAYER_TYPE_LOCAL_AUTH, 'Local Authority'),
        (PAYER_TYPE_OTHER, 'Other'),
        (PAYER_TYPE_PRIVATE_ORG, 'Private Organization'),
    )

    id = models.AutoField(db_column='PayerID', primary_key=True)
    uuid = models.CharField(db_column='PayerUUID', max_length=36, default=uuid.uuid4, unique=True)
    legacy_id = models.IntegerField(db_column='LegacyID', blank=True, null=True)
    payer_type = models.CharField(db_column='PayerType', max_length=1, choices=PAYER_TYPE_CHOICES)
    # payer_type = models.ForeignKey(
    #     "contribution.PayerType", models.DO_NOTHING, db_column='PayerType', blank=True, null=True)
    payer_name = models.CharField(db_column='PayerName', max_length=100, null=False)
    payer_address = models.CharField(db_column='PayerAddress', max_length=100, null=True, blank=True)
    location = models.ForeignKey("location.Location", db_column="LocationId", blank=True, null=True,
                                 on_delete=models.DO_NOTHING, related_name='+')
    phone = models.CharField(db_column='Phone', max_length=50, null=True, blank=True)
    fax = models.CharField(db_column='Fax', max_length=50, null=True, blank=True)
    eMail = models.CharField(db_column='eMail', max_length=50, null=True, blank=True)

    validity_from = fields.DateTimeField(db_column='ValidityFrom')
    validity_to = fields.DateTimeField(
        db_column='ValidityTo', blank=True, null=True)
    audit_user_id = models.IntegerField(db_column='AuditUserID')
    # rowid = models.TextField(db_column='RowID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblPayer'
