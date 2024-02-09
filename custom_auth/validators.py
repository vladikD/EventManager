from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_image_file_extension(value):
    """
    Валідація, щоб переконатися, що завантажений файл є зображенням.
    """
    allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']  # Список допустимих розширень
    extension = value.name.split('.')[-1]  # Отримання розширення файлу

    if extension.lower() not in allowed_extensions:
        raise ValidationError(
            _('Неприпустиме розширення файлу. Дозволено завантажувати лише JPG, JPEG, PNG та GIF файли.'),
            code='invalid_image_file_extension',
        )
