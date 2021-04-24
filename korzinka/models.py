from django.db import models

def get_upload_path(instance, filename):
	return f'products/{instance.name}/{filename}'


class Product(models.Model):
	CATEGORY = [
		(0, 'Все товары'),
		(1,'Мука и продукты для выпечки'),
		(2,'Крупы'),
		(3,'Макаронные изделия'),
		(4,'Растительные масла'),
		(5,'Консервация'),
		(6,'Соусы,приправы,маринады'),
		(7,'Десертные продукты'),
		(8,'Хлеб,батон,лепешки,лаваш'),
		(9,'Сдобные изделия,выпечка'),
		(10,'Хлебцы,сухари,сушки'),
		(11,'Напитки'),
		(12,'Рыба,морепродукты'),
		(13,'Колбасные изделия'),
		(14,'Молочные изделия'),
		(15,'Сыры'),
		(16,'Масло сливочное'),
		(17,'Замороженные пельмены'),
		(18,'Тесто,выпечка замороженная'),
		(19,'Замороженные морепродукты'),	
	]

	category = models.SmallIntegerField(choices=CATEGORY, verbose_name='Категория товаров', default=0)
	name = models.CharField(max_length=200, verbose_name='Наименование товара')
	description = models.TextField(blank=True)
	price = models.PositiveIntegerField(help_text='в сомах', null=True)
	weight = models.PositiveSmallIntegerField(blank=True,help_text='в граммах', null=True)
	volume = models.PositiveSmallIntegerField(blank=True,help_text='в миллилитрах', null=True)
	image = models.ImageField(upload_to=get_upload_path)


	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	def __str__(self):
		return self.name