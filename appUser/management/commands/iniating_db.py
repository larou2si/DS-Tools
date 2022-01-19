from django.core.management.base import BaseCommand
# from webDataScience.settings import BASE_DIR
import time, datetime


class Command(BaseCommand):
    # def add_arguments(self, parser):
    # pass

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Start Command'))
        started_time = time.perf_counter()
        

        self.stdout.write(self.style.SUCCESS(f'End Command in {datetime.timedelta(seconds=time.perf_counter() - started_time)}'))