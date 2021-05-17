from django.core.management import BaseCommand, call_command


class Command(BaseCommand):

    def handle(self, *args, **options):
        commands = [
            'load_countries',
            'load_cities',
            'load_airports'
        ]

        for c in commands:
            self.stdout.write(f'{c} command has started!')
            call_command(c)

        return 'Commands inserted'
