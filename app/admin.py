from django.contrib import admin
from .models import (
    Counter,
    WhyChooseUs,
    Service,
    Testimonial,
    FAQ,
    Partner,
    Subscribe,
    ContactUs,
    Team,
)

admin.site.register([Counter,
                     WhyChooseUs,
                     Service,
                     Testimonial,
                     FAQ,
                     Partner,
                     Subscribe,
                     ContactUs,
                     Team,
                     ])
