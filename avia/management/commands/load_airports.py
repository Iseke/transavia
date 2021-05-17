import urllib3, xmltodict, json

from django.core.management.base import BaseCommand, CommandError
from avia.models import City, Country, Airport


class Command(BaseCommand):

    def handle(self, *args, **options):
        url = 'https://staging-ws.epower.amadeus.com/wstrans/MasterData/Airports.xml'
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
            res = res['Airports']['Airport']
        except Exception as e:
            print(e)
            res = ''
        if res != '':
            for row in res:
                try:
                    cur_country = Country.objects.get(country_code=row['CountryCode'])
                    cur_city = City.objects.get(city_code=row['CityCode'])
                    result = Airport.objects.get_or_create(country_code=cur_country, city_code=cur_city,
                                                           airport_code=row['AirportCode'],
                                                           airport_name=row['AirportName'])
                    cnt += 1
                except Exception as e:
                    print(e)
                    print(row)
        print(cnt)

        return str(cnt)+' airports inserted'
