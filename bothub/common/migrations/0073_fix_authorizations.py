# Generated by Django 2.2.12 on 2020-07-31 11:35

from django.db import migrations


def noop(apps, schema_editor):  # pragma: no cover
    pass


def update_authorization(apps, schema_editor):  # pragma: no cover
    RepositoryAuthorization = apps.get_model("common", "RepositoryAuthorization")
    User = apps.get_model("authentication", "User")
    ROLE_ADMIN = 3

    def is_owner(auth):
        try:
            user = auth.user
        except User.DoesNotExist:  # pragma: no cover
            return False  # pragma: no cover
        return auth.repository.owner == user

    for auth in RepositoryAuthorization.objects.all():
        if is_owner(auth):
            auth.role = ROLE_ADMIN
            auth.save(update_fields=["role"])


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0006_auto_20200729_1220"),
        ("common", "0072_auto_20200729_1704"),
    ]

    operations = [migrations.RunPython(update_authorization, noop)]