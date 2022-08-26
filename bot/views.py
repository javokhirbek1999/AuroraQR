import threading
from django.views.generic import TemplateView, View


from .telegramBot import *

def setupBotThread():
    """
    Setup the thread for running the bot in background 
    """

    botThread = threading.Thread(target=main)
    
    botThread.start()
    

class HomeView(TemplateView):
    setupBotThread()
    template_name = 'main.html'

class GenerateQrView(TemplateView):
    setupBotThread()
    template_name = 'generateQr.html'

class QrCodeView(TemplateView):
    setupBotThread()
    template_name = 'QRcode.html'

class QrColorView(TemplateView):
    setupBotThread()
    template_name = 'QRcolor.html'

class AboutView(TemplateView):
    setupBotThread()
    template_name = 'about.html'

    def get_template_names(self):
        return super().get_template_names()

class HelpView(TemplateView):
    setupBotThread()
    template_name = 'help.html'



