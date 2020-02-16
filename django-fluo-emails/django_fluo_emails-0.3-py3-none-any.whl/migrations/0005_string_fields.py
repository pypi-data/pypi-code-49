# Copyright (C) 2007-2020, Raffaele Salmaso <raffaele@salmaso.org>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from django.db import migrations, models
import emails.models
import fluo.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0004_base_manager_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailtemplate',
            options={'ordering': ['name'], 'verbose_name': 'email template', 'verbose_name_plural': 'email templates'},
        ),
        migrations.AlterField(
            model_name='attachment',
            name='filename',
            field=fluo.db.models.fields.StringField(blank=True, default='', max_length=None, verbose_name='filename'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attachment',
            name='mimetype',
            field=fluo.db.models.fields.StringField(blank=True, default='', max_length=None, verbose_name='mimetype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='email',
            name='all_recipients',
            field=models.TextField(blank=True, verbose_name='recipients'),
        ),
        migrations.AlterField(
            model_name='email',
            name='bcc_emails',
            field=fluo.db.models.fields.StringField(blank=True, max_length=None, verbose_name='bcc emails'),
        ),
        migrations.AlterField(
            model_name='email',
            name='cc_emails',
            field=fluo.db.models.fields.StringField(blank=True, max_length=None, verbose_name='cc emails'),
        ),
        migrations.AlterField(
            model_name='email',
            name='from_email',
            field=fluo.db.models.fields.StringField(default=emails.models._get_default_from_email, max_length=None, verbose_name='from email'),
        ),
        migrations.AlterField(
            model_name='email',
            name='headers',
            field=models.TextField(blank=True, verbose_name='headers'),
        ),
        migrations.AlterField(
            model_name='email',
            name='raw',
            field=models.TextField(blank=True, verbose_name='raw message'),
        ),
        migrations.AlterField(
            model_name='email',
            name='subject',
            field=fluo.db.models.fields.StringField(max_length=None, verbose_name='subject'),
        ),
        migrations.AlterField(
            model_name='email',
            name='to_emails',
            field=fluo.db.models.fields.StringField(blank=True, max_length=None, verbose_name='to emails'),
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='body_html',
            field=models.TextField(blank=True, verbose_name='html body'),
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='default_bcc',
            field=fluo.db.models.fields.StringField(blank=True, default='', help_text='comma separated value', max_length=None, verbose_name='default bcc'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='default_cc',
            field=fluo.db.models.fields.StringField(blank=True, default='', help_text='comma separated value', max_length=None, verbose_name='default cc'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='default_reply_to',
            field=fluo.db.models.fields.StringField(blank=True, default='', help_text='comma separated value', max_length=None, verbose_name='default reply_to'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='default_to',
            field=fluo.db.models.fields.StringField(blank=True, default='', help_text='comma separated value', max_length=None, verbose_name='default to'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='from_email',
            field=fluo.db.models.fields.StringField(default=emails.models._get_default_from_email, max_length=None, verbose_name='from email'),
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='name',
            field=fluo.db.models.fields.StringField(db_index=True, max_length=None, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='notes',
            field=models.TextField(blank=True, default='', verbose_name='notes'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='subject',
            field=fluo.db.models.fields.StringField(max_length=None, verbose_name='subject'),
        ),
        migrations.AlterField(
            model_name='emailtemplatetranslation',
            name='body_html',
            field=models.TextField(blank=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='emailtemplatetranslation',
            name='subject',
            field=fluo.db.models.fields.StringField(max_length=None, verbose_name='subject'),
        ),
    ]
