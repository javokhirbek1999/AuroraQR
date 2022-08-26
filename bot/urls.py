from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('generateQr/', views.GenerateQrView.as_view(), name='generateQr' ),
    path('qrCode/', views.QrCodeView.as_view(), name='qrCode' ),
    path('qrColor/', views.QrColorView.as_view(), name='qrColor' ),
    path('about/', views.AboutView.as_view(), name='about' ),
    path('help/', views.HelpView.as_view(), name='help' ),
]