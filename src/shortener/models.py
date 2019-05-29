from django.db import models
from .utils import create_shortcode
from django.conf import settings
from .validators import validate_url, validate_dot_com


SHORTCODE_MAX = getattr(settings,"SHORTCODE_MAX",15)
#SHORTCODE_MAX = settings.SHORTCODE_MAX #this also is correct.

#change the default behaviour of MehnUrl.objects.all()
#What if all should return only the active objects.
class MehnUrlManager(models.Manager):
    def all(self,*args,**kwargs):
        qs = super(MehnUrlManager,self).all(*args,**kwargs)
        qs = qs.filter(active=True)
        return qs

    #you can call it as MehnUrl.objects.refresh_shortcodes()
    def refresh_shortcodes(self,items=None):
        qs = MehnUrl.objects.filter(id__gte=1) #literally everything without all filtering Active stuff.
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items] #order by desc and only show upto n items.
        new_codes = 0
        for q in qs:
            #each query object in queryset is an instance of MehnUrl only.
            print(q.id)
            q.shortcode = create_shortcode(q)
            q.save()
            new_codes += 1
        return f"New codes made: {new_codes}"


# Create your models here.
class MehnUrl(models.Model):
    url         = models.CharField(max_length=200,validators=[validate_url,validate_dot_com])
    shortcode   = models.CharField(max_length=SHORTCODE_MAX,unique=True,blank=True)
    updated     = models.DateTimeField(auto_now=True) #only on save/update
    created     = models.DateTimeField(auto_now_add=True) #only on new entry created
    active      = models.BooleanField(default=True)

    def __str__(self):
        return self.url #could say self.id or self.pk on the listView in admin control panel

    objects = MehnUrlManager()

    def save(self,*args,**kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(MehnUrl,self).save(*args,**kwargs)

    def get_short_url(self):
        url_path = "/" + self.shortcode
        return url_path

    #class Meta:



