Directorio media
------------------------------------
- debe configurarse en el archivo :
a. settings.py 
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

b. urls.py:
  if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

** Crear super usuario
python manage.py createsuperuser


** para hacer que un modelo se pueda acceder desde el panel de administrador debe de agregarse en el archivo admin.py
from .models import Service
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

** Extender nombre de la aplicación
- Ir al archivo services\apps.py y configurar el atributo verbose_name   :

  class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'
    verbose_name = 'Gestor de servicios'

- Luego ir a webempresa\settings.py y extender el nombre del archivo en INSTALLED_APPS
  cambiar de 'service' a ''services.apps.ServicesConfig','
  
** Extender contexto
- crer archivo processors.py
  from .models import Link

  def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx
- Ir a settings.py del proyecto y en Templates agregars
TEMPLATES = [
    { ....
        
        'OPTIONS': {
            'context_processors': [
               ...
                'social.processors.ctx_dict'
            ],
        },
    },
]




admin.site.register(Service, ServiceAdmin)
