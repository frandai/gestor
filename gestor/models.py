from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Attribute(models.Model):
    ATTRIBUTE_TYPE = (
        ('T','text'),
        ('D','date'),
        ('N','number'),
        ('C','choice'),
        ('E','Email'),
        ('P','Phone'),
        ('I', 'ID national number'),
        ('B', 'Bank Account'),
    )
    name = models.CharField(max_length=30)
    internal_name = models.CharField(max_length=30, null=False, blank=False)
    attribute_type = models.CharField(max_length=1, choices=ATTRIBUTE_TYPE)
    mandatory = models.BooleanField()
    def __str__(self):
        return '%s (%s)' % (self.name, self.internal_name)

class Choice(models.Model):
    name = models.CharField(max_length=1000)
    attribute = models.ForeignKey(
        Attribute,
        blank = True,
        null = True,
        on_delete = models.CASCADE,
    )

class Event(models.Model):
    pass
    
class Group(models.Model):
    event = models.ManyToManyField(
        Event,
        blank = True,
    )
    parent = models.ForeignKey(
        'self',
        blank = True,
        null = True,
        on_delete = models.CASCADE,
    )

class Organization(models.Model):
    event = models.ManyToManyField(
        Event,
        blank = True,
    )

class MainOrganization(Organization):
    def save(self, *args, **kwargs):
        self.id = 1
        return super().save(*args, **kwargs)

class Member(User):
    event = models.ManyToManyField(
        Event,
        blank = True,
    )
    organization = models.ManyToManyField(
        Organization,
        blank = True,
    )
    group = models.ManyToManyField(
        Group,
        blank = True,
    )
    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')


class AttributeValue(models.Model):
    value = models.CharField(max_length=1000)
    attribute = models.ForeignKey(
        Attribute,
        blank = False,
        null = False,
        on_delete = models.CASCADE,
    )
    event = models.ForeignKey(
        Event,
        blank = True,
        null = True,
        on_delete = models.CASCADE,
    )
    group = models.ForeignKey(
        Group,
        blank = True,
        null = True,
        on_delete = models.CASCADE,
    )
    organization = models.ForeignKey(
        Organization,
        blank = True,
        null = True,
        on_delete = models.CASCADE,
    )
    member = models.ForeignKey(
        Member,
        blank = True,
        null = True,
        on_delete = models.CASCADE,
    )
    def __str__(self):
        return '%s (%s)' % (self.value, self.attribute)