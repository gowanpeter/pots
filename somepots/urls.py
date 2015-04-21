from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    #url(r'^index/(?P<piece_id>\w{0,50})/$', 'somepots.views.PieceView', name='piece'),
    url(r'^glaze$', 'somepots.views.GlazeView', name='glaze'),
    url(r'^documentation$', 'somepots.views.DocumentationView', name='documentation',),
    url(r'^condition$', 'somepots.views.ConditionView', name='condition',),
    url(r'^exhibition$', 'somepots.views.ExhibitionLookupView', name='exhibition',),
    url(r'^hline$', 'somepots.views.HeathLineLookupView', name='hline',),
    url(r'^logo$', 'somepots.views.LogoView', name='logo',),
    url(r'^maker$', 'somepots.views.MakerLookupView', name='maker',),
    url(r'^material$', 'somepots.views.MaterialLookupView', name='material',),
    url(r'^method$', 'somepots.views.MethodLookupView', name='method',),
    url(r'^pub$', 'somepots.views.PublicationView', name='pub',),
    url(r'^setc$', 'somepots.views.SetCollectionView', name='set',),
)




    #src/kk
 #   url(r'^somepots/', include('somepots.urls', namespace='somepots', app_name='kk')),
 #   url(r'^$',somepots.views.kk_directory, name='kk')


#if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL,
                          #document_root=settings.STATIC_ROOT)
    #urlpatterns += static(settings.MEDIA_URL,
                          #document_root=settings.MEDIA_ROOT)                    
