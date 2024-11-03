from django.db import models


class BaseModel(models.Model):
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ('id', )


class Counter(BaseModel):
    title = models.CharField(max_length=255)
    count = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class WhyChooseUs(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Why choose us'


class Service(BaseModel):
    image = models.ImageField(upload_to='services')
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class Testimonial(BaseModel):
    image = models.ImageField(upload_to='testimonial')
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class FAQ(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class Partner(BaseModel):
    image = models.ImageField(upload_to='partners')
    link = models.URLField(null=True, blank=True)


class Subscribe(BaseModel):
    mail = models.EmailField()

    def __str__(self):
        return self.mail


class ContactUs(BaseModel):
    full_name = models.CharField(max_length=255)
    mail = models.EmailField()
    phone = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Contact us'


class Team(BaseModel):
    image = models.ImageField(upload_to='testimonial')
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name



