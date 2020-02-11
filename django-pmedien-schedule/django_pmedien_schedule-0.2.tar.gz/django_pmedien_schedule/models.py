# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import socket
import threading
import time

from django.db import models

from django.utils.timezone import now

WEEKDAYS = (
    ('mo', 'Montag', 'mon'),
    ('di', 'Dienstag', 'tue'),
    ('mi', 'Mittwoch', 'wed'),
    ('do', 'Donnerstag', 'thu'),
    ('fr', 'Freitag', 'fri'),
    ('sa', 'Samstag', 'sat'),
    ('so', 'Sonntag', 'sun'),
)


class ScheduleGroup(models.Model):
    name = models.CharField('Name', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gruppe'
        verbose_name_plural = 'Gruppen'


class Schedule(models.Model):
    active = models.BooleanField('Aktiv?', default=True)
    override_day = models.BooleanField(u'Tag überschreiben?', default=False)
    name = models.CharField('Aufgabe', max_length=100)

    ref_schedule_group = models.ForeignKey(
        ScheduleGroup, verbose_name='Aufgabengruppe', blank=True, null=True, on_delete=models.SET_NULL
    )

    start_date = models.DateField('Erstes Ausführungsdatum', default=now, help_text='(inklusive)')
    last_date = models.DateField('Letztes Ausführungsdatum', blank=True, null=True, help_text='(inklusive)')

    start_time = models.TimeField('Erste Ausführung:', default='00:00:00', help_text='(inklusive)')
    last_time = models.TimeField('Letzte Ausführung Urzeit:', default='00:00:00', help_text='(inclusive)')
    repeat_duration = models.DurationField('Wiederholung nach Dauer', default='00:00:00',
                                           help_text='(00:00:00 = keine Wiederholung)')

    for i in range(7):
        locals()['d_{}'.format(i)] = models.BooleanField(WEEKDAYS[i][1], default=False)

    def announce(self):
        time.sleep(.5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 40000))
        s.sendall(b'reload_jobs')
        s.close()

    def save(self, *args, **kwargs):
        super(Schedule, self).save(*args, **kwargs)
        threading.Thread(target=self.announce).start()

    def delete(self, *args, **kwargs):
        super(Schedule, self).delete(*args, **kwargs)
        threading.Thread(target=self.announce).start()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-active', '-override_day', 'start_date', 'start_time')
        verbose_name = 'Aufgabe'
        verbose_name_plural = 'Aufgaben'
