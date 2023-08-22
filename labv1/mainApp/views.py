from django.shortcuts import render,HttpResponseRedirect, HttpResponse
import datetime
from django.utils import timezone
from django.contrib import messages
from datetime import timedelta

from .models import *
from .serializers import *
from .forms import *



def Login(Request):
    return render(Request,"Login.html")

def homePage(Request):
    return render(Request,"home.html")

def chain_of_custody(Request):
   
    return render(Request,"Chain of Custody.html")
 

def chain_of_custody_form(Request):
    return render(Request,"Chain of Custody.html")

def SampleIntakelog(Request):
    if Request.method == 'GET':
        sample_list = SampleIntake.objects.all().order_by('-Default_Id')

    return render(Request,"Sample Intake log.html",  {"sample_list" :sample_list})

def SampleIntakeForm(request):
    print(request)
    print(request.method)
    if request.method == 'POST':
        try:
            date = request.POST.get('Date')
            sample_id = request.POST.get('SampleId')
            sample_name = request.POST.get('SampleName')
            matrix = request.POST.get('Matrix')
            batch_number = request.POST.get('BatchNumber')
            sample_size = request.POST.get('SampleSize')
            batch_size = request.POST.get('BatchSize')
            distributor_name = request.POST.get('DistributorName')
            distributor_license = request.POST.get('DistributorLicence')
            custody_number = request.POST.get('CustodyNumber')
            
            # Perform validation here if needed
            
            # Save data to the model
            sample = SampleIntake(
                Date=date,
                SampleId=sample_id,
                SampleName=sample_name,
                Matrix=matrix,
                BatchNumber=batch_number,
                SampleSize=sample_size,
                BatchSize=batch_size,
                DistributorName=distributor_name,
                DistributorLicence=distributor_license,
                CustodyNumber=custody_number
            )
            sample.save()
            messages.success(request, 'Sample Added Successfully.')
            today = datetime.datetime.now()
            today_onlyDate = today.strftime('%m-%d-%Y')
            month, day, year_ = today_onlyDate.split('-')
            year = year_[-2:]
            initialsOfId = f'{month}{day}{year}'
            current_datetime = datetime.datetime.now()

            start_of_day = current_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
            end_of_day = start_of_day + timedelta(days=1)

            instances_on_current_date = SampleIntake.objects.filter(CurrentDate__gte=start_of_day, CurrentDate__lt=end_of_day)
            lastDigitsOfId = len(instances_on_current_date)+1
            print(len(instances_on_current_date))
            print(initialsOfId)
            print(lastDigitsOfId)
            if len(str(lastDigitsOfId)) == 1:
                finalId = f'{initialsOfId}-0{lastDigitsOfId}'
            else:
                finalId = f'{initialsOfId}-{lastDigitsOfId}'
            print(finalId)
            return render(request,"Sample Intake Form.html", {"sample_id" :finalId})
        except Exception as e:
            print(e)
            return HttpResponse(f'<h1>{e}</h1>')
    elif request.method == 'GET':
        today = datetime.datetime.now()
        today_onlyDate = today.strftime('%m-%d-%Y')
        month, day, year_ = today_onlyDate.split('-')
        year = year_[-2:]
        initialsOfId = f'{month}{day}{year}'
        current_datetime = datetime.datetime.now()

        start_of_day = current_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_day = start_of_day + timedelta(days=1)

        instances_on_current_date = SampleIntake.objects.filter(CurrentDate__gte=start_of_day, CurrentDate__lt=end_of_day)
        lastDigitsOfId = len(instances_on_current_date)+1
        print(len(instances_on_current_date))
        print(initialsOfId)
        print(lastDigitsOfId)
        if len(str(lastDigitsOfId)) == 1:
            finalId = f'{initialsOfId}-0{lastDigitsOfId}'
        else:
            finalId = f'{initialsOfId}-{lastDigitsOfId}'
        print(finalId)
        return render(request,"Sample Intake Form.html", {"sample_id" :finalId})

def SampleTrackingLog(Request):
    return render(Request,"Sample Tracking Log.html")

def SampleTrackingForm(Request):
    return render(Request,"Sample Tracking Form.html")

def SampleRetainLog(Request):
    return render(Request,"Sample Retention Log.html")

def SampleRetainForm(Request):
    return render(Request,"Sample Retention Form.html")

def Cannibanoidssamplepreplogsheet(Request):
    return render(Request,"FO-121 Cannabinoids Sample Prep Log Sheet.html")

def Cannibanoidsdatasheet100xdryweight(Request):
    return render(Request,"FO-080 Cannibanoids Data Sheet 100x dry weight .html")

def Cannibanoidsdatasheet100xmgperg(Request):
    return render(Request,"FO-080 Cannibanoids Data Sheet 100x mg per g.html")

def Cannibanoidsdatasheet100xwetweight(Request):
    return render(Request,"FO-080 Cannibanoids Data Sheet 100x wet weight .html")

def Cannibanoidsdatasheet100x(Request):
    return render(Request,"FO-080 Cannibanoids Data Sheet 100x.html")

def Cannibanoidsdatasheet2000xdryweight(Request):
    return render(Request,"FO-080 Cannibanoids Data Sheet 2000x dry weight .html")

def Cannibanoidsdatasheet2000xmgperg(Request):
    return render(Request,"FO-080 Cannibanoids Data Sheet 2000x mg per g.html")

def Cannibanoidsdatasheet2000xwetweight(Request):
    return render(Request,"FO-080 Cannibanoids Data Sheet 2000x wet weight .html")

def Cannibanoidsdatasheet2000x(Request):
    return render(Request,"FO-080 Cannibanoids Data Sheet 2000x.html")