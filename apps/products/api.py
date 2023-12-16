from django.core.exceptions import ValidationError

MAX_IMAGES_FOR_PRODUCT = 5


def validate_image_count(images):
    if images.count() > MAX_IMAGES_FOR_PRODUCT:
        raise ValidationError(f'Максимальное число изображений на товар: {MAX_IMAGES_FOR_PRODUCT}')
