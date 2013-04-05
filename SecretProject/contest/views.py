# Create your views here.
import os
import urllib
import json

from django.http import HttpResponse
from django.shortcuts import render
from contest.models import *

def home(request):
    return render(request, "home.html")

def business(request):
	companies = Company.objects.all()
	company_names = []
	for company in companies:
		name = company.company_name
		name = str(name)
		company_names.append(name)
	company_names = json.dumps(company_names)
	return render(request, "business.html", {'companies':companies, "company_names":company_names})

def designers(request):
	contests = Contest.objects.all()
	return render(request, "designers.html", {'contests':contests})

def detail(request, contest_id=0):
    contest = Contest.objects.get(id=contest_id)
    return render(request, "detail.html", {'contest': contest})

def entry(request, contest_id=0):
	contest = Contest.objects.get(id=contest_id)
	return render(request, "entry.html", {'contest': contest})

def success(request):
	if request.method=="POST":
		title = request.POST['title_box']
		company_name = request.POST['company_name_box']
		number_winning = request.POST['num_winning']
		number_winning = int(float(number_winning))
		prize_money = request.POST['prize_money_box']
		distr = request.POST['distrRadios']
		total_days = request.POST['total_days_box']
		start_date = request.POST['start_date_box']
		description = request.POST['description_box']
		winner_one_three = 0.4
		winner_two_three = 0.25
		winner_three_three = 0.1
		winner_one_two = 0.5
		winner_two_two = 0.25
		if distr == 'EQ':
			winner_one_three = 0.25
			winner_two_three = 0.25
			winner_three_three = 0.25
			winner_one_two = 0.375
			winner_two_two = 0.375
		elif distr == 'CM':
			winner_one_three = request.POST['prize_percent_13']
			winner_two_three = request.POST['prize_percent_23']
			winner_three_three = request.POST['prize_percent_33']
			winner_one_two = request.POST['prize_percent_12']
			winner_two_two = request.POST['prize_percent_22']
		distribution = Distribution(distribution_type=distr, winner_one_three=winner_one_three, 
			winner_two_three=winner_two_three, winner_three_three=winner_three_three, 
			winner_one_two=winner_one_two, winner_two_two=winner_two_two)
		distribution.save()
		try: 
			company = Company.objects.get(company_name=company_name)
		except Company.DoesNotExist:
			company = Company(company_name=company_name)
			company.save()
	contest = Contest(company=company, title=title, description=description, number_winning=number_winning, 
		prize_money=prize_money, distribution=distribution, contest_length=total_days, start_date=start_date)
	contest.save()
	return render(request, "success.html")

def entrysuccess(request, contest_id=0):
	contest = Contest.objects.get(id=contest_id)
	if request.method=="POST":
		name = request.POST['name_box']
		school = request.POST['school_box']
		school_year = request.POST['school_year']
		school_year = int(float(school_year))
		email = request.POST['email_box']
		if request.FILES.get('file_upload'):
			uploaded_design = request.FILES['file_upload']
		else:
			uploaded_design = None
		try: 
			user_profile = UserProfile.objects.get(email=email)
		except UserProfile.DoesNotExist:
			user_profile = UserProfile(name=name, school=school, year=school_year, email=email)
			user_profile.save()
		entry = Entry(user_profile=user_profile, contest=contest, uploaded_design=uploaded_design)
		entry.save()
	return render(request, "success.html")