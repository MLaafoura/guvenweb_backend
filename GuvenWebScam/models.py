from django.db import models
from GuvenWebUser.models import GuvenUser


class ScamSource(models.Model):
    source = models.CharField(max_length=255)
    reported_by = models.ForeignKey(GuvenUser, on_delete=models.CASCADE)
    reported_at = models.DateTimeField(auto_now_add=True, blank=True)


class ScamReport(models.Model):
    scam_status_choices = [
                            ('Confirmed', 'Confirmed'),
                            ('Panding', 'Panding'),
                            ('Safe', 'Safe')  ]
    
    scam_type = models.CharField(max_length=100)
    scam_source = models.CharField(max_length=255)
    scam_date = models.DateTimeField(auto_now_add=True, blank=True)
    scam_description = models.CharField(max_length=2000)
    scam_picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    scam_status = models.CharField(choices=scam_status_choices, default='Pending', max_length=100)
    confirmed_by = models.ForeignKey(GuvenUser, default=None, on_delete=models.CASCADE)
    confirmed_at = models.DateTimeField(auto_now_add=True, blank=True)