import sys
sys.path.append("scoreserver/fixtures/")
script_dirs = ['AttackPointHistory', 'Category', 'Flag', 'Hint', 'Notice', 'Question', 'User']
for sd in script_dirs:
    sys.path.append("scoreserver/fixtures/{}".format(sd))
from scoreserver.fixtures import seed_generator
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_generator.main()
        print("[+] created initial_data.json at scoreserver/fixtures.")
        print("[!] If you want to load this data, please execute command below.")
        print(" - python manage.py loaddata initial_data")

