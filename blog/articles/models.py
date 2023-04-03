from django.db import models
    

class Article(models.Model):
    """A model of a article."""
    name = models.CharField("Article name", max_length=200)
    image = models.URLField(default='https://s3.amazonaws.com/libapps/accounts/37359/images/Titanic_front_page.jpg')
    text = models.CharField(max_length=5000, default='')
    section_name = models.CharField(choices=(
            ('dn', "Daily News"),
            ('sp', "Sport"),
            ('cu', "Culture"),
            ('mu', "Music"),
            ('bu', "Business"),
        ),
        max_length=2,
        default='',
    )

    def __str__(self):
        # translator = {
        #     'dn': "Daily News",
        #     'sp': "Sport",
        #     'cu': "Culture",
        #     'mu': "Music",
        #     'bu': "Business",
        # }
        # + "," + {translator[self.section_name]}
        return f'{self.name}'
