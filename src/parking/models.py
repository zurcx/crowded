from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models

# Create your models here.


class employees(models.Model):
	id = models.AutoField(primary_key=True, db_column='id')
	full_name = models.CharField(_('Nome Completo'), max_length=70, db_column='full_name')
	first_name = models.CharField(_('Primeiro Nome'), max_length=25, db_column='first_name')
	last_name = models.CharField(_('Sobrenome'), max_length=35, db_column='last_name')
	adhesive = models.IntegerField(_('Adesivo'), db_column='adhesive')
