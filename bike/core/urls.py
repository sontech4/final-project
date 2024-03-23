# We are in urls.py file of core app

from django.urls import path
from . import views
#------ To incude Media file ---------------
from django.conf import settings
from django.conf.urls.static import static
#-----------------------------------------------
urlpatterns = [
    # path('',views.home,name='home'),
    path('',views.HomeView.as_view(),name='home'),

    path('about/',views.about,name='about'),

    path('contact/',views.contact,name='contact'),

    #------- Hero View Functions ------------
    # path('hero_categories',views.hero_categories,name='herocategories'),
    path('hero_categories/',views.HeroCategoriesView.as_view(),name='herocategories'),

    #------- Cat View Functions ------------
    # path('suzuki_categories',views.suzuki_categories,name='catcategories'),
    path('suzuki_categories/',views.SuzukiCategoriesView.as_view(),name='suzukicategories'),

    
    # path('bike_details',views.bike_details,name='bikedetails'),
    path('bike_details/<int:id>/',views.BikeDetailView.as_view(),name='bikedetails'),

    path('registration/',views.registration,name='registration'),

    path('login/',views.log_in,name='login'),

    path('profile/',views.profile,name='profile'),

    path('address/',views.address,name='address'),

    path('delete_address/<int:id>',views.delete_address,name='deleteaddress'),

    path('logout/',views.log_out, name="logout"),

    path('changepassword/',views.changepassword, name="changepassword"),

    path('add_to_cart/<int:id>/',views.add_to_cart, name="addtocart"),

    path('view_cart/',views.view_cart, name="viewcart"),

    path('add_quantity/<int:id>/', views.add_quantity, name='add_quantity'),

    path('delete_quantity/<int:id>/', views.delete_quantity, name='delete_quantity'),

    path('delete_cart/<int:id>',views.delete_cart, name="deletecart"),
    
    path('checkout/',views.checkout,name='checkout'),

    path('payment/',views.payment,name='payment'),
    
    path('payment_success/<int:selected_address_id>/',views.payment_success,name='paymentsuccess'),

    path('payment_failed/',views.payment_failed,name='paymentfailed'),

    path('order/',views.order,name='order'),

    path('buynow/<int:id>',views.buynow,name='buynow'),

    path('buynow_payment/<int:id>',views.buynow_payment,name='buynowpayment'),

    path('buynow_payment_success/<int:selected_address_id>/<int:id>',views.buynow_payment_success,name='buynowpaymentsuccess'),
]
#--------- THis is will add file to media folder -----------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
