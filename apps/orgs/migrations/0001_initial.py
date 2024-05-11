# Generated by Django 4.1.13 on 2024-05-09 03:16

from django.db import migrations, models
import orgs.models
import uuid

default_id = '00000000-0000-0000-0000-000000000002'


def add_default_org(apps, schema_editor):
    org_cls = apps.get_model('orgs', 'Organization')
    defaults = {'name': 'Default', 'id': default_id}
    org_cls.objects.get_or_create(defaults=defaults, id=default_id)


def update_builtin_org(apps, schema_editor):
    org_model = apps.get_model('orgs', 'Organization')
    org_model.objects.create(
        id='00000000-0000-0000-0000-000000000004',
        name='SYSTEM', builtin=True
    )

    # 更新 Default
    org_model.objects.filter(name='DEFAULT').update(builtin=True)



class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('builtin', models.BooleanField(default=False, verbose_name='Builtin')),
            ],
            options={
                'verbose_name': 'Organization',
                'permissions': (('view_rootorg', 'Can view root org'), ('view_alljoinedorg', 'Can view all joined org')),
            },
            bases=(orgs.models.OrgRoleMixin, models.Model),
        ),
        migrations.RunPython(add_default_org),
        migrations.RunPython(update_builtin_org),
    ]
