# Generated by Django 4.2.2 on 2023-07-21 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0007_alter_user_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='course',
            field=models.CharField(blank=True, choices=[('r', 'R科'), ('s', 'S科'), ('w', 'W科'), ('c', 'C科'), ('a', 'A科'), ('m', 'M科'), ('e', 'E科'), ('d', 'D科'), ('k', 'K科'), ('v', 'V科'), ('u', 'U科'), ('id', 'ID科'), ('ic', 'IC科'), ('is', 'IS科'), ('im', 'IM科'), ('in', 'IN科')], max_length=10),
        ),
    ]