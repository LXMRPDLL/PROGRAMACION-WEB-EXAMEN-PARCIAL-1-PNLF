# Generated by Django 4.1.1 on 2022-09-18 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.CharField(choices=[('Goalkeeper', 'GK'), ('Center Back', 'CB'), ('FullBack', 'LB/RB'), ('Wingback', 'LWB/RWB'), ('Sweeper', 'SW'), ('Defensive Midfielder', 'DM'), ('Central Midfielder', 'CM'), ('Attacking Midfielder', 'AM'), ('Left/Right Midfielder', 'LM/RM'), ('Center Forward', 'CF'), ('Striker', 'S'), ('Second Striker', 'SS')], default='CF', max_length=50),
        ),
    ]
