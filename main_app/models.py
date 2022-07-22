from django.db import models
from django.urls import reverse
from datetime import date

RATING = (
    ('A', 'Awesome'),
    ('B', 'Good'),
    ('C', 'Soso'),
    ('D', 'Bad'),
)

class Bar(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    address = models.CharField(max_length=100)
    menu = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bar_id': self.id})

class Rating(models.Model):
    date = models.DateField('rating date')
    rate = models.CharField(
        max_length=1,
        choices=RATING,
        default=RATING[0][0]
    )
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_rate_display()} on {self.date}"

  # change the default sort
    class Meta:
        ordering = ['-date']