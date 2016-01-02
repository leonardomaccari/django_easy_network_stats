import kronos
from django.core.management import call_command
from .settings import CRON_STRING


@kronos.register(CRON_STRING)
def update_db():
    print "updated!"
    call_command('update_topology')
