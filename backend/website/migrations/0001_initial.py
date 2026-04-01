from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('sort_order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={'ordering': ['sort_order', 'id']},
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_type', models.CharField(choices=[('privacy', 'Privacy Policy'), ('terms', 'Terms of Service'), ('refund', 'Refund Policy'), ('cookie', 'Cookie Policy'), ('disclaimer', 'Disclaimer')], max_length=20)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('sort_order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={'ordering': ['sort_order', 'id']},
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(default='Yash Gupta', max_length=120)),
                ('support_email', models.EmailField(default='yash@theyashgupta.com', max_length=254)),
                ('support_phone', models.CharField(default='+91 96963 45822', max_length=30)),
                ('whatsapp_number', models.CharField(default='919696345822', max_length=20)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
