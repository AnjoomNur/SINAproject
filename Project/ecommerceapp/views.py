from django.shortcuts import render
from ecommerceapp.models import Setting

# Create your views here.
def Home(request):
    setting=Setting.objects.get(id=1)
    context={'setting': setting}
    return render(request,'home.html', context)
