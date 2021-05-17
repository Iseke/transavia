import urllib3, xmltodict, json

from django.core.management.base import BaseCommand, CommandError
from avia.models import Country


class Command(BaseCommand):

    def handle(self, *args, **options):
        url = 'https://staging-ws.epower.amadeus.com/wstrans/MasterData/Countries.xml'
        http = urllib3.PoolManager()
        resp = http.request('GET', url)
        try:
            data = xmltodict.parse(resp.data)
        except Exception as e:
            print(e)
            data = ''
        res = json.dumps(data)
        cnt = 0
        try:
            res = json.loads(res)
            res = res['Countries']['Country']
        except Exception as e:
            print(e)
            res = ''
        if res != '':
            for row in res:
                try:
                    result = Country.objects.get_or_create(country_code=row['CountryCode'],
                                                           country_name=row['CountryName'], continent=row['Continent'])
                    cnt += 1
                except Exception as e:
                    print(e)
        print(cnt)
        return str(cnt) + ' countries inserted'
