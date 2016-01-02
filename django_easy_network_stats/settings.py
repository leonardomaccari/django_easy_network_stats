from django.conf import settings

CRON_STRING = getattr(settings, "EASY_STATS_CRON_STRING", "")
