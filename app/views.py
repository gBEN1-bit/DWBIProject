"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Contact
from .models import LimitDefinition, CustomerSectorDetails
from openpyxl import load_workbook
import pandas as pd
from django.db import connection
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django import forms
from datetime import datetime
from app import forms
from django.shortcuts import reverse


from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse



from django.shortcuts import render
from django.db import connection
from django.template import RequestContext

from django.views.decorators.csrf import csrf_protect



#def newdata(request):
#    showdata = LimitDefinition.objects.all()  # Retrieve data from the database
#    context = {
#        'showdata': showdata,  # Pass the data to the template
#    }
#    return render(request, 'home/index.html', context)

import matplotlib.pyplot as plt
import numpy as np

@csrf_protect
def index(request):
    # Retrieve data from the database using your SQL queries
    # Example SQL query:
    with connection.cursor() as cursor:
        cursor.execute("SELECT FORMAT(GETDATE(), 'dddd, MMMM d, yyyy') AS today;")
        today = cursor.fetchone()[0]
        cursor.execute("SELECT [ProcessingDate] AS maxdate FROM [FintrakDWDev].[EDW].[ExposureSummary] WHERE [ExposureType] = 'Total Exposure';")
        maxdate = cursor.fetchone()[0]
        cursor.execute("SELECT [ExposureAmount] AS directexposure FROM [FintrakDWDev].[EDW].[ExposureSummary] WHERE [ExposureType] = 'Digital Loans';")
        digitalloans = cursor.fetchone()[0]
        cursor.execute("SELECT [ExposureAmount] AS directexposure FROM [FintrakDWDev].[EDW].[ExposureSummary] WHERE [ExposureType] = 'Direct Exposure';")
        directexposure = cursor.fetchone()[0]
        cursor.execute("SELECT [ExposureAmount] AS contingentexposure FROM [FintrakDWDev].[EDW].[ExposureSummary] WHERE [ExposureType] = 'Contingent Exposure';")
        contingentexposure = cursor.fetchone()[0]
        cursor.execute("SELECT [ExposureAmount] AS totalexposurelcy FROM [FintrakDWDev].[EDW].[ExposureSummary] WHERE [ExposureType] = 'Total Exposure';")
        totalexposurelcy = cursor.fetchone()[0]
        username = request.user.get_short_name() or request.user.get_username()
        query = "SELECT DATEADD(hour, 1, CAST(last_login AS datetime)) AS UpdatedLastLogin FROM [FintrakApp].[dbo].[auth_user] WHERE username = %s;"
        cursor.execute(query, [username])
        lastlogin = cursor.fetchone()[0]
        cursor.execute("""
            SELECT 
                [ExposureAmount] AS [Direct Exposure],
                [Month]
            FROM [FintrakDWDev].[dbo].[ExposureSummaryMoM]
            WHERE [ExposureType] = 'Direct Exposure'
        """)
        directexposuremom = cursor.fetchall()

    context = {
        'directexposuremom': directexposuremom,
        'maxdate': maxdate,
        'today': today,
        'digitalloans': digitalloans,
        'contingentexposure': contingentexposure,
        'directexposure': directexposure,
        'totalexposurelcy': totalexposurelcy,
        'lastlogin': lastlogin,
        'title': 'Dashboard',
        'year': datetime.now().year,
        # Add other data variables as needed
    }

    return render(request, 'home/index.html', context)

#def index(request):
#        return render(request, 'home/index.html')

#def index(request):
#    context = {'segment': 'index'}

#    html_template = loader.get_template('home/index.html')
#    return HttpResponse(html_template.render(context, request))
#@login_required(login_url="/login/")
#def index(request):
#    context = {'segment': 'index'}
#    return render(request, 'home/index.html', context)

def timeout(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/timeout.html',
        {
            'title':'TimeOut',
            'year':datetime.now().year,
        }
    )


class CustomLoginView(LoginView):
    template_name = 'app/login.html'
    authentication_form = forms.BootstrapAuthenticationForm


    def get_success_url(self):
        return reverse('reports')

def home(request):
      # Retrieve data from the database using your SQL queries
    # Example SQL query:
    with connection.cursor() as cursor:
         #cursor.execute(" select max(ProcessingDate) as maxdate FROM [FintrakDWDev].[EDW].[FacilityDetails];")
        #maxdate = cursor.fetchone()[0]
        #cursor.execute("SELECT FORMAT(SUM([TotalExposureLCY]), 'N2') AS totalexposurelcy FROM  [FintrakDWDev].[EDW].[FacilityDetails];")
        #totalexposurelcy = cursor.fetchone()[0]
        username = request.user.get_short_name() or request.user.get_username()
        query = "SELECT DATEADD(hour, 1, CAST(last_login AS datetime)) AS UpdatedLastLogin FROM [FintrakApp].[dbo].[auth_user] WHERE username = %s;"
        cursor.execute(query, [username])
        lastlogin = cursor.fetchone()[0]

    context = {
        #'maxdate': maxdate,
        #'totalexposurelcy': totalexposurelcy,
        'lastlogin': lastlogin,
        'title': 'Dashboard',
        'year':datetime.now().year,
        # Add other data variables as needed
    }
    return render(
        request,
        'home/index.html',context
        
    )


#def profile(request):
#    """Renders the home page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'home/page-user.html',
#        {
#            'title':'Profile',
#            'year':datetime.now().year,
#        }
#    )


@csrf_protect
def reports(request):
     # Retrieve data from the database using your SQL queries
    # Example SQL query:
    with connection.cursor() as cursor:
        cursor.execute(" SELECT FORMAT(GETDATE(), 'dddd, MMMM d, yyyy') AS today;")
        today = cursor.fetchone()[0]        
        cursor.execute("SELECT [ProcessingDate] AS maxdate FROM  [FintrakDWDev].[EDW].[ExposureSummary] where [ExposureType] = 'Total Exposure';")
        maxdate = cursor.fetchone()[0]
        cursor.execute("SELECT [ExposureAmount] AS directexposure FROM  [FintrakDWDev].[EDW].[ExposureSummary] where [ExposureType] = 'Digital Loans';")
        digitalloans = cursor.fetchone()[0]
        cursor.execute("SELECT [ExposureAmount] AS directexposure FROM  [FintrakDWDev].[EDW].[ExposureSummary] where [ExposureType] = 'Direct Exposure';")
        directexposure = cursor.fetchone()[0]
        cursor.execute("SELECT [ExposureAmount] AS contingentexposure FROM  [FintrakDWDev].[EDW].[ExposureSummary] where [ExposureType] = 'Contingent Exposure';")
        contingentexposure = cursor.fetchone()[0]
        cursor.execute("SELECT [ExposureAmount] AS totalexposurelcy FROM  [FintrakDWDev].[EDW].[ExposureSummary] where [ExposureType] = 'Total Exposure';")
        totalexposurelcy = cursor.fetchone()[0]
        username = request.user.get_short_name() or request.user.get_username()
        query = "SELECT DATEADD(hour, 1, CAST(last_login AS datetime)) AS UpdatedLastLogin FROM [FintrakApp].[dbo].[auth_user] WHERE username = %s;"
        cursor.execute(query, [username])
        lastlogin = cursor.fetchone()[0]

    context = {
        'maxdate': maxdate,
        'today': today,
        'digitalloans': digitalloans,
        'contingentexposure': contingentexposure,
        'directexposure': directexposure,
        'totalexposurelcy': totalexposurelcy,
        'lastlogin': lastlogin,
        'title': 'Home',
        'year':datetime.now().year,
        # Add other data variables as needed
    }

    #template_names = ['home/index.html', 'app/test.html']
    return render(request, 'app/test.html', context)


#def reports(request):
#    """Renders the home page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/test.html',
#        {
#            'title':'Home',
#            'year':datetime.now().year,
#        }
#    )

def allreport(request):
     # Retrieve data from the database using your SQL queries
    # Example SQL query:
    with connection.cursor() as cursor:
         #cursor.execute(" select max(ProcessingDate) as maxdate FROM [FintrakDWDev].[EDW].[FacilityDetails];")
        #maxdate = cursor.fetchone()[0]
        #cursor.execute("SELECT FORMAT(SUM([TotalExposureLCY]), 'N2') AS totalexposurelcy FROM  [FintrakDWDev].[EDW].[FacilityDetails];")
        #totalexposurelcy = cursor.fetchone()[0]
        cursor.execute(" SELECT FORMAT(GETDATE(), 'dddd, MMMM d, yyyy') AS today;")
        today = cursor.fetchone()[0]
        username = request.user.get_short_name() or request.user.get_username()
        query = "SELECT DATEADD(hour, 1, CAST(last_login AS datetime)) AS UpdatedLastLogin FROM [FintrakApp].[dbo].[auth_user] WHERE username = %s;"
        cursor.execute(query, [username])
        lastlogin = cursor.fetchone()[0]

    context = {
        #'maxdate': maxdate,
        #'totalexposurelcy': totalexposurelcy,
        'today' : today,
        'lastlogin': lastlogin,
        'title': 'Reports',
        'year':datetime.now().year,
        # Add other data variables as needed
    }
    return render(
        request,
        'app/reports.html',context
       
    )


def crm(request):
     # Retrieve data from the database using your SQL queries
    # Example SQL query:
    with connection.cursor() as cursor:
         #cursor.execute(" select max(ProcessingDate) as maxdate FROM [FintrakDWDev].[EDW].[FacilityDetails];")
        #maxdate = cursor.fetchone()[0]
        #cursor.execute("SELECT FORMAT(SUM([TotalExposureLCY]), 'N2') AS totalexposurelcy FROM  [FintrakDWDev].[EDW].[FacilityDetails];")
        #totalexposurelcy = cursor.fetchone()[0]
        cursor.execute(" SELECT FORMAT(GETDATE(), 'dddd, MMMM d, yyyy') AS today;")
        today = cursor.fetchone()[0]
        username = request.user.get_short_name() or request.user.get_username()
        query = "SELECT DATEADD(hour, 1, CAST(last_login AS datetime)) AS UpdatedLastLogin FROM [FintrakApp].[dbo].[auth_user] WHERE username = %s;"
        cursor.execute(query, [username])
        lastlogin = cursor.fetchone()[0]

    context = {
        #'maxdate': maxdate,
        #'totalexposurelcy': totalexposurelcy,
        'today' : today,
        'lastlogin': lastlogin,
        'title': 'Reports',
        'year':datetime.now().year,
        # Add other data variables as needed
    }
    return render(
        request,
        'app/crm.html',context
       
    )




def contact(request):
     # Retrieve data from the database using your SQL queries
    # Example SQL query:
    with connection.cursor() as cursor:
         #cursor.execute(" select max(ProcessingDate) as maxdate FROM [FintrakDWDev].[EDW].[FacilityDetails];")
        #maxdate = cursor.fetchone()[0]
        #cursor.execute("SELECT FORMAT(SUM([TotalExposureLCY]), 'N2') AS totalexposurelcy FROM  [FintrakDWDev].[EDW].[FacilityDetails];")
        #totalexposurelcy = cursor.fetchone()[0]
        username = request.user.get_short_name() or request.user.get_username()
        query = "SELECT DATEADD(hour, 1, CAST(last_login AS datetime)) AS UpdatedLastLogin FROM [FintrakApp].[dbo].[auth_user] WHERE username = %s;"
        cursor.execute(query, [username])
        lastlogin = cursor.fetchone()[0]

    context = {
        #'maxdate': maxdate,
        #'totalexposurelcy': totalexposurelcy,
        'lastlogin': lastlogin,
        'title': 'Contact',
         'message':'Your contact page.',
        'year':datetime.now().year,
        # Add other data variables as needed
    }
    return render(
        request,
        'app/contact.html', context
       
    )

def about(request):
    with connection.cursor() as cursor:
         #cursor.execute(" select max(ProcessingDate) as maxdate FROM [FintrakDWDev].[EDW].[FacilityDetails];")
        #maxdate = cursor.fetchone()[0]
        #cursor.execute("SELECT FORMAT(SUM([TotalExposureLCY]), 'N2') AS totalexposurelcy FROM  [FintrakDWDev].[EDW].[FacilityDetails];")
        #totalexposurelcy = cursor.fetchone()[0]
        username = request.user.get_short_name() or request.user.get_username()
        query = "SELECT DATEADD(hour, 1, CAST(last_login AS datetime)) AS UpdatedLastLogin FROM [FintrakApp].[dbo].[auth_user] WHERE username = %s;"
        cursor.execute(query, [username])
        lastlogin = cursor.fetchone()[0]

    context = {
        #'maxdate': maxdate,
        #'totalexposurelcy': totalexposurelcy,
        'lastlogin': lastlogin,
        'title': 'About',
         'message':'Your application description page.',
        'year':datetime.now().year,
        # Add other data variables as needed
    }
    return render(
        request,
        'app/about.html', Context
       
    )





def allcontactus(request):
    if request.method == "POST":
        allcontactus = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        allcontactus.name = name
        allcontactus.email = email
        allcontactus.message = message
        allcontactus.save()
        
    return render(request, 'app/contactus.html')

from django.shortcuts import render
from django.db import connection
from datetime import datetime
from .models import LimitDefinition
import pandas as pd

def excelupload(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT FORMAT(GETDATE(), 'dddd, MMMM d, yyyy') AS today;")
        today = cursor.fetchone()[0]
        username = request.user.get_short_name() or request.user.get_username()
        query = "SELECT DATEADD(hour, 1, CAST(last_login AS datetime)) AS UpdatedLastLogin FROM [FintrakApp].[dbo].[auth_user] WHERE username = %s;"
        cursor.execute(query, [username])
        lastlogin = cursor.fetchone()[0]

    context = {
        'today': today,
        'lastlogin': lastlogin,
        'title': 'Limit Definition Upload',
        'year': datetime.now().year,
    }

    if request.method == 'POST':
        if 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            if excel_file.name == 'LIMIT_DEFINITION.xlsx':
                try:
                    df = pd.read_excel(excel_file, keep_default_na=False)  # Add keep_default_na=False
                    required_columns = ['Name', 'Year', 'Category', 'Limit', 'ThresholdTarget', 'ordernumber', 'subCategory', 'ID', 'CategoryCode']
                    if set(required_columns) == set(df.columns):
                        with connection.cursor() as cursor:
                            cursor.execute("TRUNCATE TABLE Limit_Definition_;")
                        LimitDefinition.objects.bulk_create([LimitDefinition(**row) for row in df.to_dict('records')])
                        success_message = 'LIMIT_DEFINITION.xlsx uploaded successfully.'
                        uploaded_records = df.to_dict('records')  # Get the uploaded records as a list of dictionaries
                        return render(request, 'app/excelupload.html', {'success_message': success_message, 'uploaded_records': uploaded_records, **context})
                    else:
                        failure_message = 'Column names in the Excel file do not match the expected structure for LIMIT_DEFINITION.xlsx.'
                        return render(request, 'app/excelupload.html', {'failure_message': failure_message, **context})
                except Exception as e:
                    failure_message = f'Failed to process LIMIT_DEFINITION.xlsx: {str(e)}'
                    return render(request, 'app/excelupload.html', {'failure_message': failure_message, **context})
            else:
                failure_message = 'Invalid Excel file. Only LIMIT_DEFINITION.xlsx files are allowed.'
                return render(request, 'app/excelupload.html', {'failure_message': failure_message, **context})
        else:
            warning_message = 'Choose a LIMIT_DEFINITION.XSLX file.'
            return render(request, 'app/excelupload.html', {'warning_message': warning_message, **context})
    else:
        return render(request, 'app/excelupload.html', context)

import pandas as pd
from django.db import connection
from django.shortcuts import render
from datetime import datetime

from .models import CustomerSectorDetails

def sectorupload(request):
    # Retrieve data from the database using your SQL queries
    # Example SQL query:
    with connection.cursor() as cursor:
        cursor.execute("SELECT FORMAT(GETDATE(), 'dddd, MMMM d, yyyy') AS today;")
        today = cursor.fetchone()[0]
        username = request.user.get_short_name() or request.user.get_username()
        query = "SELECT DATEADD(hour, 1, CAST(last_login AS datetime)) AS UpdatedLastLogin FROM [FintrakApp].[dbo].[auth_user] WHERE username = %s;"
        cursor.execute(query, [username])
        lastlogin = cursor.fetchone()[0]

    context = {
        'today': today,
        'lastlogin': lastlogin,
        'title': 'Sector Limit Upload',
        'year': datetime.now().year,
        # Add other data variables as needed
    }

    if request.method == 'POST':
        if 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            if excel_file.name.lower() == 'sector_details.xlsx':
                if excel_file.name.lower().endswith('.xlsx'):
                    try:
                        df = pd.read_excel(excel_file, keep_default_na=False)  # Add keep_default_na=False

                        # Check column names
                        required_columns = ['CUST_ID', 'LOCATION', 'SECTOR_DESC','SECTOR_CODE', 'OBLIGOR_RISK_RATING', 'IFRS_ CLASSIFICATION', 'SBU_DIVISION', 'CBK GRADE']
                        if set(required_columns) == set(df.columns):
                            # Truncate the table before uploading records
                            with connection.cursor() as cursor:
                                cursor.execute("TRUNCATE TABLE stg_customer_sector_details;")
                            # Process and save data to the CustomerSectorDetails model
                            records = []
                            for index, row in df.iterrows():
                                cust_id = row['CUST_ID']
                                location = row['LOCATION']
                                sector_desc = row['SECTOR_DESC']
                                sector_code = row['SECTOR_CODE']
                                obligor_risk_rating = row['OBLIGOR_RISK_RATING']
                                ifrs_classification = row['IFRS_ CLASSIFICATION']
                                sbu_division = row['SBU_DIVISION']
                                cbk_grade = row['CBK GRADE']

                                CustomerSectorDetails.objects.create(
                                    CUST_ID=cust_id,
                                    LOCATION=location,
                                    SECTOR_DESC=sector_desc,
                                    SECTOR_CODE=sector_code,
                                    OBLIGOR_RISK_RATING=obligor_risk_rating,
                                    IFRS_CLASSIFICATION=ifrs_classification,
                                    SBU_DIVISION=sbu_division,
                                    CBK_GRADE=cbk_grade,
                                )

                                record = {
                                    'CUST_ID': cust_id,
                                    'LOCATION': location,
                                    'SECTOR_DESC': sector_desc,
                                    'SECTOR_CODE': sector_code,
                                    'OBLIGOR_RISK_RATING': obligor_risk_rating,
                                    'IFRS_CLASSIFICATION': ifrs_classification,
                                    'SBU_DIVISION': sbu_division,
                                    'CBK_GRADE': cbk_grade,
                                }
                                records.append(record)

                            success_message = 'SECTOR_DETAILS.XLSX uploaded successfully.'
                            return render(request, 'app/sectorupload.html', {'success_message': success_message, 'records': records, **context})
                        else:
                            failure_message = 'Column names in the Excel file do not match the expected structure for SECTOR_DETAILS.XLSX.'
                            return render(request, 'app/sectorupload.html', {'failure_message': failure_message, **context})
                    except Exception as e:
                        failure_message = f'Failed to process SECTOR_DETAILS.XLSX: {str(e)}'
                        return render(request, 'app/sectorupload.html', {'failure_message': failure_message, **context})
                else:
                    failure_message = 'Invalid Excel file format. Only SECTOR_DETAILS.XLSX files are allowed.'
                    return render(request, 'app/sectorupload.html', {'failure_message': failure_message, **context})
            else:
                failure_message = 'Invalid Excel file name. Only SECTOR_DETAILS.XLSX files are allowed.'
                return render(request, 'app/sectorupload.html', {'failure_message': failure_message, **context})
        else:
            warning_message = 'Choose a SECTOR_DETAILS.XLSX file.'
            return render(request, 'app/sectorupload.html', {'warning_message': warning_message, **context})
    else:
        return render(request, 'app/sectorupload.html', context)





   


   
