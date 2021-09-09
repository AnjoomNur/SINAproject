from django.shortcuts import render
from ecommerceapp.models import Setting
from Product.models import Product,Images

# Create your views here.
def Home(request):
    setting=Setting.objects.get(id=1)
    sliding_images=Product.objects.all().order_by('id')[:2]
    latest_products=Product.objects.all().order_by('-id')
    products=Product.objects.all()
    context={'setting': setting,
            'sliding_images': sliding_images,
            'latest_products': latest_products,
            'products': products}
    return render(request,'home.html', context)

def product_single(request,id):
        
        setting=Setting.objects.get(id=1)
        single_product=Product.objects.get(id=id)
        images=Images.objects.filter(product_id=id)
        context={'setting': setting,
                 'single_product': single_product, 
                 'images':images,
        }
        return render(request,'product-single.html',context)