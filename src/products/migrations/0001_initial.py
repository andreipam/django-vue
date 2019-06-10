# Generated by Django 2.2.1 on 2019-06-10 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='images/categorys')),
                ('tags', models.CharField(blank=True, help_text='SEO keywords', max_length=100, null=True)),
                ('display_order', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_expended', models.BooleanField(default=False, help_text='Catergory will always shown expended')),
                ('updated_by', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='products.Category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('display_order', 'id'),
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_order', models.IntegerField(default=0)),
                ('image_url', models.ImageField(upload_to='images/products')),
                ('updated_by', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, max_length=800, null=True)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('quantity', models.IntegerField()),
                ('tags', models.CharField(blank=True, help_text='keywords to help with searching and SEO', max_length=250, null=True)),
                ('weight', models.FloatField(default=0)),
                ('length', models.FloatField(default=0)),
                ('width', models.FloatField(default=0)),
                ('height', models.FloatField(default=0)),
                ('updated_by', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Category')),
                ('pictuer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ProductImages')),
            ],
        ),
    ]
