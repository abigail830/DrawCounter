from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import RegexValidator
from datetime import date


class Member(models.Model):
    member_name = models.CharField(max_length=20, unique=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$',
                                 message="Phone number must be entered start with'+' & Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=16, blank=True)

    join_date = models.DateField('The date joined as member', default=date.today)

    remark = models.CharField(max_length=100,blank=True,default='')

    def __str__(self):
        return self.member_name + '/' + self.phone_number + ':' + self.remark


class Counter(models.Model):
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name="counts",
        related_query_name="count",
    )
    available_count = models.DecimalField('Avaiable Counts', max_digits=2, decimal_places=0)
    last_update_date = models.DateField('Last Update Date', default=date.today)
    remark = models.CharField(max_length=100,blank=True,default='')

    def __str__(self):
        return self.member.member_name + ': remain ' + str(self.available_count) + ' times @' + str(self.last_update_date)
