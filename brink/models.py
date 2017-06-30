from django.db import models


class HelpRequest(models.Model):
    TYPE_ROUGH_SLEEPING = 'slp'
    TYPE_BEGGING = 'beg'
    TYPE_ANTISOCIAL_BEHAVIOR = 'asb'
    TYPE_HEALTH = 'hlt'
    TYPE_SAFETY = 'saf'

    TYPE_CHOICES = (
        (TYPE_ROUGH_SLEEPING, 'Rough Sleeping'),
        (TYPE_BEGGING, 'Begging'),
        (TYPE_ANTISOCIAL_BEHAVIOR, 'Anti-Social Behaviour'),
        (TYPE_HEALTH, 'Health'),
        (TYPE_SAFETY, 'Safety')
    )

    time = models.DateTimeField()
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    latitude = models.FloatField()
    longitude = models.FloatField()
    resolved = models.BooleanField(default=False)

    def __unicode__(self):
        return "{} at {}".format(self.get_type_display(),
                                 self.time.isoformat())

    class Meta:
        # Query history for a certain type
        index_together = ('time', 'type')
