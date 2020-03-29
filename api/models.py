from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from fcm_django.fcm import fcm_send_topic_message

class Report(models.Model):
    signature = models.CharField(max_length=50)
    severity = models.IntegerField()

@receiver(post_save, sender=Report)
def report_only_after_deal_created(sender, instance, created, **kwargs):
    if created:
        fcm_send_topic_message(topic_name='new_infections', data_message={"signature": instance.signature})
