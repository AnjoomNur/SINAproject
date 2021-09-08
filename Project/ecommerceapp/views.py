from django.shortcuts import render
from ecommerceapp.models import Setting
from Product.models import Product

# Create your views here.
def Home(request):
    setting=Setting.objects.get(id=1)
    sliding_images=Product.objects.all()
    context={'setting': setting,
            'sliding_images': sliding_images}
    return render(request,'home.html', context)
