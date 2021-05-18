from django.db import models


class Country(models.Model):
    country_code = models.CharField(primary_key=True, max_length=5)
    country_name = models.CharField(max_length=255)
    continent = models.CharField(max_length=124)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = "Countries"

    def __str__(self):
        return f'{self.country_code}, {self.country_name}, {self.continent}'

    def get_name(self):
        return self.country_name


class City(models.Model):
    city_code = models.CharField(primary_key=True, max_length=5)
    city_name = models.CharField(max_length=255)
    country_code = models.ForeignKey(to='Country', on_delete=models.CASCADE, related_name='%(class)s_country')

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = "Cities"

    def __str__(self):
        return f'{self.city_code}, {self.city_name}, {self.country_code.get_name()}'

    def get_name(self):
        return self.city_name

    def get_country(self):
        return self.country_code


class Airport(models.Model):
    airport_code = models.CharField(max_length=5, unique=True)
    airport_name = models.CharField(max_length=255)
    country_code = models.ForeignKey(to='Country', on_delete=models.CASCADE, related_name='%(class)s_country')
    city_code = models.ForeignKey(to='City', on_delete=models.CASCADE, related_name='%(class)s_city')
    type_code = models.CharField(max_length=2)

    class Meta:
        verbose_name = 'Airport'
        verbose_name_plural = "Airports"

    def __str__(self):
        return f'{self.airport_code}, {self.airport_name}, {self.city_code.get_name()}, {self.country_code.get_name()}'

    def get_name(self):
        return self.airport_name

    def get_country(self):
        return self.country_code

    def get_city(self):
        return self.city_code

    def get_type_code(self):
        return self.type_code

    def to_json(self):
        return {
            'city': {
                'city_code': self.city_code.city_code,
                'city_name': self.city_code.city_name
            },
            'airport': {
                'airport_code': self.airport_code,
                'airport_name': self.airport_name
            }
        }
