from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from shortner.forms import ShortUrlForm

from shortner.models import ShortUrl
from shortner.utils import unique_key_generator
# Create your views here.
from django.shortcuts import get_object_or_404
import qrcode
import qrcode.image.svg

from django.core.files import File


class ShorturlMixin(View):
    model = ShortUrl
    form_class = ShortUrlForm
    paginate_by = 10
    queryset = ShortUrl.objects.all()
    success_url = reverse_lazy("index")

class UrlListCreateView(ShorturlMixin):
    def get(self,request,*args,**kwargs):
        # to list all the created urls
        if request.user.is_authenticated:
            objects = ShortUrl.objects.filter(creator=request.user).order_by('-id')
            return render(request,'index.html',{'objects':objects})
        
        return redirect(reverse_lazy("login"))
    
    
    def post(self,request,*args,**kwargs):
        # to create short urls
        original_url = self.request.POST.get('input-url')
        custom_key = self.request.POST.get('custom-key')
        objects = ShortUrl.objects.filter(creator=request.user).order_by('-id')
        short_key = None
        if custom_key:
            if ShortUrl.objects.filter(custom_key=custom_key).exists():
                errors = {'custom_key': "This key is already reserved.Try another one"}
                return render(request,'index.html',{'objects':objects,'errors':errors})
            short_key = custom_key[:20]
            
        
        if not short_key: 
            short_key = unique_key_generator()
        object = ShortUrl.objects.create(
            original_url = original_url,
            creator = request.user,
            short_key = short_key,
            custom_key = custom_key

        )
        url =reverse('url_redirect', kwargs={'slug': object.short_key})
        # make sure to run the server on port 8000
        full_url =  "http://127.0.0.1:8000" + url
        img  = qrcode.make(full_url, image_factory=qrcode.image.svg.SvgImage)
        with open('qr.svg', 'wb') as qr:
            img.save(qr)

        # Saving the QR code file in the model field
        object.qr_code.save('qr.svg', File(open('qr.svg', 'rb')))
        object.save()

      
        return render(request,'index.html',{'objects':objects})
    
    


class UrlRedirectView(View):
    def get(self,request,*args,**kwargs):
        slug= self.kwargs.get("slug")
        obj = get_object_or_404(ShortUrl, short_key=slug)
        obj.hit_count += 1
        obj.save()
        return redirect(obj.original_url)

    

