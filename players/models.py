from django.db import models
from django.contrib.auth.models import User

from teams.models import Team

# Create your models here.
CHOICES = (
    ('Goalkeeper', 'GK'),
    ('Center Back', 'CB'),
    ('FullBack', 'LB/RB'),
    ('Wingback', 'LWB/RWB'),
    ('Sweeper', 'SW'),
    ('Defensive Midfielder', 'DM'),
    ('Central Midfielder', 'CM'),
    ('Attacking Midfielder', 'AM'),
    ('Left/Right Midfielder', 'LM/RM'),
    ('Center Forward', 'CF'),
    ('Striker', 'S'),
    ('Second Striker', 'SS'),
)

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.CharField(max_length=50, default='CF', choices=CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, max_length=50, default='slug')

    def __str__(self):
        return self.first_name + ' ' + self.last_name