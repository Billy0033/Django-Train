from django.db import models

# CharField — обычное строковое поле ограниченной длины. 
# Максимально допустимая длина сохраняемого значения указывается параметром max_length конструктора;

# TextField — текстовое поле неограниченной длины, или memo-поле;

# FloatField — поле для хранения вещественных чисел ;

# DateTimeField — поле для хранения временно´й отметки. Присвоив параметру
# auto_now_add конструктора значение True, мы предпишем Django при создании
# новой записи заносить в это поле текущие дату и время. А параметр db_index
# при присваивании ему значения True укажет создать для этого поля индекс (при
# выводе объявлений мы будем сортировать их по убыванию даты публикации,
# и индекс здесь пригодится).


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')


    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']
