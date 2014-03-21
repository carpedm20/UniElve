from django.db import models

import random

# Create your models here.
class Elevator(models.Model):
  group = models.IntegerField(default = 1)
  dong = models.IntegerField(default = 301)
  min_floor = models.IntegerField(default = 1)
  max_floor = models.IntegerField(default = 20)

  def __unicode__(self):
    return unicode(self.dong)

  #def get_random_floor(self):
    #return random.randint(self.min_foor, self.max_floor)
