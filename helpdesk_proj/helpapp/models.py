from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Ticket(models.Model):
    OPEN_STATUS = 'Открыта'
    REOPENED_STATUS = 'Переоткрыта'
    RESOLVED_STATUS = 'Решено'
    CLOSED_STATUS = 'Закрыта'
    DUPLICATE_STATUS = 'Дубль'

    STATUS_CHOICES = (
        (OPEN_STATUS, 'Открыта'),
        (REOPENED_STATUS, 'Переоткрыта'),
        (RESOLVED_STATUS, 'Решено'),
        (CLOSED_STATUS, 'Закрыта'),
        (DUPLICATE_STATUS, 'Дубль')
    )

    CRITICAL = 'Критическая'
    HIGH = 'Высокая'
    NORMAL = 'Обыная'
    LOW = 'Низкая'
    VERY_LOW = 'Очень низкая'

    PRIORITY_CHOICES = (
        (CRITICAL, '1. Критическая'),
        (HIGH, '2. Высокая'),
        (NORMAL, '3. Обыная'),
        (LOW, '4. Низкая'),
        (VERY_LOW, '5. Очень низкая')
    )

    title = models.CharField(
        'Тема', max_length=200
    )

    created = models.DateTimeField(
        'Создано',
        blank=True,
        help_text='Дата создания заявки'
    )

    modified = models.DateTimeField(
        'Изменено',
        blank=True,
        help_text='Дата последнего создания заявки.'
    )

    submitter_email = models.EmailField(
        'Электронная почта отправителя',
        blank=True,
        null=True,
        help_text='Электронная почта отправителя'
    )

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assigned_to',
        blank=True,
        null=True,
        verbose_name='Назначен'
    )

    status = models.CharField(
        'Статус',
        choices=STATUS_CHOICES,
        default=OPEN_STATUS,
        max_length=32
    )

    description = models.TextField(
        'Описание',
        blank=True,
        null=True,
        help_text='Описание заявки'
    )

    resolution = models.TextField(
        'Решение',
        blank=True,
        null=True,
        help_text='Решение сотрудника'
    )

    priority = models.CharField(
        'Приоритет',
        choices=PRIORITY_CHOICES,
        default='Обыная',
        blank='Обыная',
        max_length=32
    )
