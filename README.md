django-fiber-modeltranslation
=============================

App that enables i18n (translations) for django-fiber using django-modeltranslation. 


Installation
============

Assuming you have correctly installed django-plans in your app you only need to add following apps to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        
        ...
        
        'fiber',  
    
        # add also
    
        'modeltranslation', 
        'fiber_modeltranslation',
    )

and you should also define your languages in django ``LANG`` variable, eg.::

    LANGUAGES = (
        ('pl', 'Polski'),
        ('en', 'English'),
        )

Please note that adding those to ``INSTALLED_APPS`` **changes** django models. Concretely it adds for every registered ``field`` that should translated, additional fields with name ``field_<lang_code>``, e.g. for given model::

    class MyModel(models.Model):
        name = models.CharField(max_length=10)

There will be generated fields: ``name`` , ``name_en``, ``name_pl``.

You should probably migrate your database, using South is recommended. Migrations should be kept in your local project.

How to migrate fiber with South
===============================

Here is some step-by-step example how to turn your legacy django-fiber installation synced using syncdb into translated fiber with South migrations.

1. Inform South that you want to store migrations in custom place::

    # Add to INSTALLED_APS
    SOUTH_MIGRATION_MODULES = {
        'fiber': 'YOUR_APP.migrations.fiber',
    }

2. Add required directory (django package)::

    mkdir -p YOUR_APP/migrations/fiber
    touch YOUR_APP/migrations/fiber/__init__.py

3. Create initial migration (referring to the database state as it is now)::

    python manage.py schemamigration --initial fiber

4. Fake migration (because the changes are already in the database)::

    python manage.py migrate fiber --fake

5. Install fiber_i18n to INSTALLED_APPS::

    INSTALLED_APS += ('fiber_modeltranslation', )

6. Migrate what changed::

    $ python manage.py schemamigration --auto fiber
    $ python migrate fiber


That's it. You are now running fiber in i18n mode with languages you declared in LANGUAGES setting.

This app will also make all required adjustments in django admin.

For more info on how translation works in details please refer to `django-modeltranslation docs<https://django-modeltranslation.readthedocs.org/en/latest/>`_.



