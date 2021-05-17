from django.core.management import BaseCommand

from avia.models import Country


class Command(BaseCommand):

    def handle(self, *args, **options):
        all_country = Country.objects.all()
        cnt = 0
        for country in all_country:
            country.delete()
            cnt += 1
        print(cnt)
        return str(cnt) + ' countries deleted!!!'
