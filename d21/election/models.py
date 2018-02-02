from django.db import models


class Election(models.Model):
    title = models.CharField(max_length=255)
    max_positive_votes = models.PositiveIntegerField(default=1)
    max_negative_votes = models.PositiveIntegerField(default=2)

    # TODO: validate ratio up/down votes count
    # TODO: create classmethod for voting
    # TODO: create method for retrieve election result

    class Meta:
        # TODO
        pass


class Choice(models.Model):
    title = models.CharField(max_length=255)
    election = models.ForeignKey(Election, related_name='choices', on_delete=models.CASCADE)

    class Meta:
        # TODO
        pass


class Vote(models.Model):
    choice = models.ForeignKey(Choice, related_name='choices', on_delete=models.CASCADE)
    # TODO: field for vote up/down
    # TODO: field for person, must be anonym, some personal (gender, age, ...) info is allowed

    class Meta:
        # TODO: unique together for vote/person
        pass
