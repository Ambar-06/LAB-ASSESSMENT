from django.urls import path

from .views import *

urlpatterns = [
    path('',Login),
    path('homepage/', homePage),
    path('chain_of_custody/', chain_of_custody,),
    path('chain_of_custody_form/', chain_of_custody_form, name ="Chain of Custody"),
    path('SampleIntakelog/', SampleIntakelog),
    path('SampleIntakeForm/', SampleIntakeForm, name='SampleIntakeForm'),
    path('SampleTrackingLog/', SampleTrackingLog),
    path('SampleTrackingForm/', SampleTrackingForm),
    path('SampleRetainLog/', SampleRetainLog),
    path('SampleRetainForm/', SampleRetainForm),
     path('Cannibanoidssamplepreplogsheet/', Cannibanoidssamplepreplogsheet),
    path('Cannibanoidsdatasheet100xdryweight/', Cannibanoidsdatasheet100xdryweight),
    path('Cannibanoidsdatasheet100xmgperg/', Cannibanoidsdatasheet100xmgperg),
    path('Cannibanoidsdatasheet100xwetweight/', Cannibanoidsdatasheet100xwetweight),
    path('Cannibanoidsdatasheet100x/', Cannibanoidsdatasheet100x),
    path('Cannibanoidsdatasheet2000xdryweight/', Cannibanoidsdatasheet2000xdryweight),
    path('Cannibanoidsdatasheet2000xmgperg/', Cannibanoidsdatasheet2000xmgperg),
    path('Cannibanoidsdatasheet2000xwetweight/', Cannibanoidsdatasheet2000xwetweight),
    path('Cannibanoidsdatasheet2000x/', Cannibanoidsdatasheet2000x),
    
]


app_name = 'labs'