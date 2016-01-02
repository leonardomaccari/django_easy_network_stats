=====
easy_network_stats
=====

This app takes the data from django_netjsongraph and makes
simple statistics on link and path quality

Quick start
-----------

1. Add "easy_network_stats" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_netjson',
        'easy_network_stats',
    ]

2. Include the polls URLconf in your project urls.py like this::

    FIXME FIXME

3. Run `python manage.py migrate` to create the models.

4. Start the development server and visit http://127.0.0.1:8000/admin/

    FIXME FIXME

5. Dependencies
   kronos
   django_netjsongraph (my version grom github)

6. Configuration

+--------------------------------------+---------------------------+---------------------------------------------------------------------------------------------------------+
| Setting                              | Default value             | Description                                                                                             |
+======================================+===========================+=========================================================================================================+
| ``CRON_STRING``                      | ``""``                    | A crontab-style string to determine when the topology database is updated, like "1 * * * *" (every hour)|
+--------------------------------------+---------------------------+---------------------------------------------------------------------------------------------------------+
