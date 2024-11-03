from django.contrib import messages
from django.shortcuts import render, redirect
from .models import (
    Counter,
    WhyChooseUs,
    Service,
    Testimonial,
    FAQ,
    Partner,
    Team,
    Subscribe,
    ContactUs,
)
from .forms import ContactUsForm, SubscribeForm


def index(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()

    testimonials = Testimonial.objects.all()
    faqs = FAQ.objects.all()
    counters = Counter.objects.all()
    services = Service.objects.all()
    partners = Partner.objects.all()
    context = {
        'banner': True,
        'testimonials': testimonials,
        'faqs': faqs,
        'counters': counters,
        'services': services,
        'partners': partners,
        'form': form,
    }
    return render(request, 'app/index.html', context)


def about(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'app/about.html', context)


def why(request):
    why_chooses = WhyChooseUs.objects.all()
    context = {
        'why_chooses': why_chooses
    }
    return render(request, 'app/why-us.html', context)


def service(request):
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'app/services.html', context)


def contact(request):
    form = ContactUsForm()
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success! Your action was completed successfully.')
            return redirect('.')
    context = {
        'form': form
    }
    return render(request, 'app/contact.html', context)
