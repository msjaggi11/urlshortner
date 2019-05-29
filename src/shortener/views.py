from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import MehnUrl
from .forms import SubmitUrlForm


# Create your views here.

# def homepage_view(request, *args,**kwargs):
#     results = MehnUrl.objects.filter(id__gte=1)
#     obj= '<br>'.join([q.url + "," + q.shortcode for q in results])
#     return HttpResponse(obj)

class HomepageView(View):
    def get(self,request,*args,**kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "Mehn.co",
            "form": the_form
        }
        return render(request,"home.html",context)

    def post(self,request,*args,**kwargs):
        #We should NOT use the RAW POST data. We should Validate it to prevent javascript or other malicious code.
        #print(request.POST.get('url'))
        form = SubmitUrlForm(request.POST)
        template = "home.html"
        context = {
            "title": "Mehn.co",
            "form": form
        }
        if form.is_valid():
            #print(form.cleaned_data)
            new_url = form.cleaned_data.get('url')
            obj,created = MehnUrl.objects.get_or_create(url=new_url)
            context = {
                'object': obj,
                'created': created,
            }
            if created:
                template = "success.html"
            else:
                template = "already-exists.html"
        return render(request,template,context)



class RedirectView(View):
    def get(self,request, shortcode=None, *args,**kwargs):
        #kwargs['shortcode'] will also have shortcode.
        #Note filter will return an Array, but "get" will return that ROW.
        #since all shortcodes are unique, it will return a array of only 1 row.
        #if we want users to go to 404, then use get_object_404 or use the code below to handle else part.
        print("Shortcode coming: ",shortcode)
        obj = get_object_or_404(MehnUrl,shortcode=shortcode) #this will call all() internally. So, override for only ACTIVE ones.
        #qs = MehnUrl.objects.filter(shortcode=shortcode) # 404 is a much better way. If not found, will result 404 not found.
        #qs = MehnUrl.objects.get(shortcode=shortcode) #this will raise exception if not found. Need try/catch
        #qs = MehnazUrl.objects.all().first()
        # if qs.exists():
        #     obj = qs.first() #if I don't do this then next line, I will need qs[0].url as QS is an array.
        #return HttpResponse(f"The URL : {obj.url}, Shortcode: {obj.shortcode}")
        return HttpResponseRedirect(obj.url)
        # else:
        #     return HttpResponse(f"The {shortcode} does not exist.")


