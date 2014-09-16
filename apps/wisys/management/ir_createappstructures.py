from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = ''
    help = 'Creates app structures'

    def handle(self, *args, **options):
        self.stdout.write('Creating application structures.')



        self.stdout.write('Successfully created application structure')