from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = ''
    help = 'Creates app'

    def handle(self, *args, **options):
        self.stdout.write('Creating New Application.')



        self.stdout.write('Successfully created new application.')