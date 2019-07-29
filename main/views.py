from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import *
from services.models import Service as ServiceItem
from portfolios.models import Portfolio as PortfolioItem
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home(request):
    header = Header.objects.first()
    home = Home.objects.first()
    about = About.objects.first()
    service = Service.objects.first()
    portfolio = Portfolio.objects.first()
    contact = Contact.objects.first()
    footer = Footer.objects.first()
    socials = SocialMedia.objects.all()
    freelance_accounts = FreelanceAccount.objects.all()

    services_items = ServiceItem.objects.all()
    portfolio_items = PortfolioItem.objects.all()
    print(services_items.first().icon.icon)
    context = {'header':header , 'home':home , 'about':about , 'service':service , 'services_items':services_items , 'portfolio':portfolio , 'pis':portfolio_items , 'contact':contact , 'footer':footer , 'socials':socials , 'freelance_accounts':freelance_accounts}
    return render(request, 'home.html', context)

@csrf_exempt
def send_mail(request):
    # settings.ADMINS = (('Admins', test_admin_email),)

    if request.is_ajax():
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        email = request.POST['email']
        body = request.POST['message']
        msg = Message(firstname=fn,lastname=ln, email=email, body=body)
        msg.save()
        # send_mail("subject", "message",'akram@mail.com', email)
        message = "thank you {} {}".format(fn,ln)
    else:
        message = "did not send"


    return HttpResponse(message)
