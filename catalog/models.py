from django.db import models

NULLABLE = {"blank": True, "null": True}

class Category(models.Model):
    category_name = models.CharField(
        max_length=50,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    category_description = models.TextField(
        verbose_name="Описание категории", help_text="Опишите категорию"
    )

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):
    product_name = models.CharField(
        max_length=50,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    product_description = models.TextField(
        max_length=500, verbose_name="Описание продукта ", help_text="Опишите продукт"
    )
    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
        verbose_name="Изображение продукта",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="catalog",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Стоимость",
        help_text="Введите стоимость продукта",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    views_counter = models.PositiveIntegerField(
        verbose_name="Счётчик просмотров",
        help_text="Укажите кол-во просмотров",
        default=0,
    )

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["product_name", "product_description", "price"]

class Version(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name="Наименование продукта",
        related_name="version",
        on_delete=models.SET_NULL,
        **NULLABLE,
    )
    version_number = models.PositiveIntegerField(
        default=0,
        verbose_name="Номер версии продукта",
        help_text="Введите номер версии продукта",
        **NULLABLE,
    )
    version_name = models.CharField(
        max_length=50,
        verbose_name="Наименование версии продукта",
        help_text="Введите наименование версии продукта",
        **NULLABLE,
    )
    version_sign = models.BooleanField(
        verbose_name="признак текущей версии", help_text="Версия активна?", default=True
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["product", "version_number", "version_name"]

    def __str__(self):
        return self.version_name