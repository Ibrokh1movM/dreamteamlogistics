from django import template
from django.utils import timezone

register = template.Library()


@register.filter
def time_since(value):
    now = timezone.now()

    # Agar value datetime bo‘lsa, farqni hisoblaymiz
    if isinstance(value, timezone.datetime):
        diff = now - value
        seconds = diff.total_seconds()
    else:
        # Agar value allaqachon soniyalar bo‘lsa, to‘g‘ridan-to‘g‘ri ishlatamiz
        seconds = float(value)

    if seconds < 60:
        return f"{int(seconds)} soniya"
    elif seconds < 3600:
        minutes = int(seconds // 60)
        return f"{minutes} daqiqa"
    else:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        if minutes > 0:
            return f"{hours} soat {minutes} daqiqa"
        return f"{hours} soat"


@register.filter
def time_diff_seconds(value):
    # Bu filtr faqat soniyalarni qaytaradi
    now = timezone.now()
    if isinstance(value, timezone.datetime):
        diff = now - value
        return diff.total_seconds()
    return 0  # Agar noto‘g‘ri tur kelsa, 0 qaytaradi
