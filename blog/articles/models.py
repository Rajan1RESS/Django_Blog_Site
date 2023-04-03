from django.db import models

# Create your models here.
class Section(models.Model):
    """A model of a sections"""
    section_name = models.CharField(choices=(
            ('dn', "Daily News"),
            ('sp', "Sport"),
            ('cu', "Culture"),
            ('mu', "Music"),
            ('bu', "Business"),
        ),
        max_length=2
    )

    def __str__(self):
        translator = {
            'dn': "Daily News",
            'sp': "Sport",
            'cu': "Culture",
            'mu': "Music",
            'bu': "Business",
        }
        return f'{translator[self.instrument]}'  
    

class Article(models.Model):
    """A model of a article."""
    name = models.CharField("Article name", max_length=200)
    image = models.URLField(default='https://cdn.pixabay.com/photo/2018/02/12/16/35/phonograph-record-3148686__340.jpg')
    text = models.CharField(max_length=5000, default='')
    section = models.ForeignKey("Section",on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name}'  
