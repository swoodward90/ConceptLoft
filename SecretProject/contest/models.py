from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
	company_name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.company_name

class UserProfile(models.Model):
	name = models.CharField(max_length=100)
	school = models.CharField(max_length=100)
	year = models.IntegerField(max_length=2)
	email = models.EmailField()
	
	def __unicode__(self):
		return self.name

class Distribution(models.Model):
	STANDARD = 'SD'
	EQUAL = 'EQ'
	CUSTOM = 'CM'
	distribution_choices = ((STANDARD, 'Standard'), (EQUAL, 'Equal'), (CUSTOM, 'Custom'),)
	distribution_type = models.CharField(max_length=2, choices=distribution_choices, default=STANDARD)
	""" Three winners """
	winner_one_three = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)
	winner_two_three = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)
	winner_three_three = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)
	"""Two winners"""
	winner_one_two = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)
	winner_two_two = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)

	def __unicode__(self):
		return self.distribution_type

	def choices(self):
		choices = {'w13':winner_one_three, 'w23':winner_two_three, 'w33':winner_three_three, 'w12':winner_one_two, 'w22':winner_two_two}
 		return choices

class Contest(models.Model):
	""" Stores the specifics about a contest submitted by a company """ 
	company = models.ForeignKey(Company)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	number_winning = models.IntegerField()
	prize_money = models.IntegerField()
	distribution = models.ForeignKey(Distribution)
	contest_length = models.IntegerField()
	start_date = models.DateField()
	entrant = models.ManyToManyField(UserProfile, null=True, blank=True)

	def __unicode__(self):
		return self.title

class Entry(models.Model):
	user_profile = models.ForeignKey(UserProfile)
	contest = models.ForeignKey(Contest)
	uploaded_design = models.FileField(upload_to='uploads/')

	def __unicode__(self):
		return self.user_profile.name

