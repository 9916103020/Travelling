from django.shortcuts import render, HttpResponse
from travel.models import Heading, navbar, footer, package, service, specialoffer, clientreview, destination, place, \
    offer
import smtplib
from django.views.decorators.csrf import csrf_protect
from io import StringIO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email import charset as Charset
from email.generator import Generator
import smtplib


# Create your views here.

def home(request):
    title = Heading.objects.get(pk=1)
    nav = navbar.objects.get(pk=1)
    foot = footer.objects.get(pk=1)
    pack = package.objects.get(pk=1)
    serv = service.objects.get(pk=1)
    spec = specialoffer.objects.get(pk=1)
    client = clientreview.objects.get(pk=1)
    dest = destination.objects.get(pk=1)
    trp = place.objects.all()
    # for i in trp:
    #     print(i)
    args = {'title': title, 'nav': nav, 'foot': foot, 'pack': pack, 'serv': serv, 'spec': spec, 'client': client,
            'dest': dest, 'trp': trp}
    return render(request, 'index.html', args)


@csrf_protect
def inquiry(request):
    title = Heading.objects.get(pk=1)
    nav = navbar.objects.get(pk=1)
    foot = footer.objects.get(pk=1)
    pack = package.objects.get(pk=1)
    serv = service.objects.get(pk=1)
    spec = specialoffer.objects.get(pk=1)
    client = clientreview.objects.get(pk=1)
    dest = destination.objects.get(pk=1)
    args = {'title': title, 'nav': nav, 'foot': foot, 'pack': pack, 'serv': serv, 'spec': spec, 'client': client,
            'dest': dest}
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        phone = request.POST['phone']
        subject = request.POST['subject']
        sender = "Kaushlendra@youngskytravels.com"
        msg = request.POST['msg']
        # Example address data
        from_address = [name, email]
        recipient = [u'ABC Srivastava', sender]
        subject = subject

        # Example body
        html = u'Unicode⏎\nTest⏎'
        text = msg + "\n\n" + "Name: " + name + "\n\n" + "Email Address: " + email + "\n\n" + "Phone Number: " + phone

        # Default encoding mode set to Quoted Printable. Acts globally!
        Charset.add_charset('utf-8', Charset.QP, Charset.QP, 'utf-8')

        # 'alternative’ MIME type – HTML and plain text bundled in one e-mail message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "%s" % Header(subject, 'utf-8')
        # Only descriptive part of recipient and sender shall be encoded, not the email address
        msg['From'] = "\"%s\" <%s>" % (Header(from_address[0], 'utf-8'), from_address[1])
        msg['To'] = "\"%s\" <%s>" % (Header(recipient[0], 'utf-8'), recipient[1])

        # Attach both parts
        htmlpart = MIMEText(html, 'html', 'UTF-8')
        textpart = MIMEText(text, 'plain', 'UTF-8')
        msg.attach(htmlpart)
        msg.attach(textpart)

        # Create a generator and flatten message object to 'file’
        str_io = StringIO()
        g = Generator(str_io, False)
        g.flatten(msg)
        # str_io.getvalue() contains ready to sent message

        # Optionally - send it – using python's smtplib
        # or just use Django's
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login("youngskytravels@gmail.com", "tatpwgeicdqttlma")
        s.sendmail("Kaushlendra@youngskytravels.com", recipient[1], str_io.getvalue())
        return render(request, 'index.html')
    return render(request, 'inquiry_form.html', args)
# Kaushlendra@youngskytravels.com

def personal(request):
    title = Heading.objects.get(pk=1)
    nav = navbar.objects.get(pk=1)
    foot = footer.objects.get(pk=1)
    off = offer.objects.all()
    name = request.GET['trip']
    args = {'nav': nav, 'foot': foot, 'off': off, 'name': name, 'title': title}
    return render(request, 'all_days_nights.html', args)


def day_nights(request):
    id = request.GET['it']
    off = offer.objects.get(pk=id)
    foot = footer.objects.get(pk=1)
    args = {'off':off, 'foot': foot}
    return render(request, 'cust_pers.html', args)
