from django.db import models

# Create your models here.
class GlasnostDaily(models.Model):
    # Django can not handle multiple column primary keys, see https://code.djangoproject.com/wiki/MultipleColumnPrimaryKeys
    # Instead we lie to django
    counter = models.IntegerField(primary_key=True)
    rangedate = models.DateTimeField()
    destination = models.CharField(max_length=128)
    source = models.CharField(max_length=128)

    class Meta:
      db_table = 'glasnost_daily' 

    def __unicode__(self):
        return self.destination + ' => ' + self.source + ' (' + unicode(self.counter) + ')'

# Create your models here.
class GlasnostMonthly(models.Model):
    # Django can not handle multiple column primary keys, see https://code.djangoproject.com/wiki/MultipleColumnPrimaryKeys
    # Instead we lie to django
    counter = models.IntegerField(primary_key=True)
    rangedate = models.DateTimeField()
    destination = models.CharField(max_length=128)
    source = models.CharField(max_length=128)

    class Meta:
      db_table = 'glasnost_monthly' 

    def __unicode__(self):
        return self.destination + ' => ' + self.source + ' (' + unicode(self.counter) + ')'

# Create your models here.
class GlasnostYearly(models.Model):
    # Django can not handle multiple column primary keys, see https://code.djangoproject.com/wiki/MultipleColumnPrimaryKeys
    # Instead we lie to django
    counter = models.IntegerField(primary_key=True)
    rangedate = models.DateTimeField()
    destination = models.CharField(max_length=128)
    source = models.CharField(max_length=128)

    class Meta:
      db_table = 'glasnost_yearly' 

    def __unicode__(self):
        return self.destination + ' => ' + self.source + ' (' + unicode(self.counter) + ')'
