from django.db import models
from django.utils.translation import gettext_lazy as _

class Contact(models.Model):
    name = models.CharField(_("Name"), max_length=250, blank=False)
    email = models.EmailField(_("Email"), max_length=250, blank=False)
    subject = models.CharField(_("Subject"), max_length=250, blank=False)
    note = models.TextField(_("Note"))
    date = models.DateTimeField(_("Date"), auto_now=True)

    def __str__(self):
        return f'{self.name} : {self.subject}'
