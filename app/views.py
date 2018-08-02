"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.contrib import messages

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/indexBS.cshtml',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def blog(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blogBS.cshtml',
        {
            'title':'Blog',
            'year':datetime.now().year,
        }
    )

def resources(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/resources.cshtml',
        {
            'title':'Resources',
            'year':datetime.now().year,
        }
    )

def products(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/products.cshtml',
        {
            'title':'Products',
            'year':datetime.now().year,
        }
    )

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            contact_phone = request.POST.get('contact_phone', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information

            template = get_template('app/contact_template.txt')
            context = {'contact_name': contact_name,
                       'contact_email': contact_email,
                       'contact_phone': contact_phone,
                       'form_content': form_content,}
            content = template.render(context)

            email = EmailMessage("New contact form submission", content, "GreatAmericanNaturalPetFood.com" + '', ['info@greatamericannaturalpetfood.com'], headers={'Reply to': contact_email})
            email.send()
            messages.success(request, 'You have successfully submitted your information.  We will contact you as soon as possible.  Thank you.')
            return redirect('contact')

    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contactBS.cshtml',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
            'form': form_class,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/aboutBS.cshtml',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
