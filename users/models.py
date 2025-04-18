from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import random
import string


def generate_order_id():
    while True:
        characters = string.ascii_uppercase + string.digits
        order_id = ''.join(random.choices(characters, k=5))
        if not Order.objects.filter(order_id=order_id).exists():
            return order_id


class UserManager(BaseUserManager):
    def create_user(self, login, password=None, **extra_fields):
        if not login:
            raise ValueError('The Login field must be set')
        user = self.model(login=login, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('status', 'admin')
        return self.create_user(login, password, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
    class StatusChoices(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        DIRECTOR = 'direktor', 'Direktor'
        MANAGER = 'manager', 'Manager'
        BUGALTER = 'bugalter', 'Bugalter'
        DISPECHER = 'dispecher', 'Dispecher'
        FILTER = 'filter', 'Filter'
        PERSON = 'person', 'Person'

    login = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.PERSON)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.full_name


class Order(models.Model):
    order_id = models.CharField(max_length=5, unique=True, default=generate_order_id, editable=False)
    qayerdan = models.CharField(max_length=100)
    qayerga = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    client = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manager = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='managed_orders',
                                limit_choices_to={'status': 'manager'})
    close_order_status = models.BooleanField(default=False)
    filter_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Buyurtma #{self.order_id} - {self.client}"

    class Meta:
        ordering = ['-created_at']


class OrderClosure(models.Model):
    class PriceTuriChoices(models.TextChoices):
        PERECHESLENIYA = 'perechesleniya', 'Perechesleniya'
        YATT = 'yatt', 'YATT'
        NAXT = 'naxt', 'Naxt'

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='closure')
    dispecher = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='closed_orders',
                                  limit_choices_to={'status': 'dispecher'})
    closed_at = models.DateTimeField(auto_now_add=True)
    close_price = models.DecimalField(max_digits=10, decimal_places=2)
    price_turi = models.CharField(max_length=20, choices=PriceTuriChoices.choices,
                                  default=PriceTuriChoices.PERECHESLENIYA)

    def __str__(self):
        return f"Buyurtma #{self.order.order_id} yopildi - {self.dispecher.full_name}"

    class Meta:
        ordering = ['-closed_at']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.order.close_order_status = True
        self.order.save()


class FilterData(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='filter_data')
    firma_nomi = models.CharField(max_length=100, blank=True, null=True)
    firma_inn = models.CharField(max_length=20, blank=True, null=True)
    boss_or_bugalter_number = models.CharField(max_length=20, blank=True, null=True)
    dispecher_fullname = models.CharField(max_length=100)
    manager_fullname = models.CharField(max_length=100)
    filtered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Filtr #{self.order.order_id}"


class Accounting(models.Model):
    class PaymentStatusChoices(models.TextChoices):
        JARAYONDA = 'jarayonda', 'Jarayonda'
        TOLANDI = 'tolandi', 'TolandI'

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='accounting')
    manager_price = models.DecimalField(max_digits=10, decimal_places=2)
    dispecher_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=20, choices=OrderClosure.PriceTuriChoices.choices)
    payment_status = models.CharField(max_length=20, choices=PaymentStatusChoices.choices,
                                      default=PaymentStatusChoices.JARAYONDA)
    updated_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True,
                                   limit_choices_to={'status': 'bugalter'},
                                   related_name='accounting_updates')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Hisob #{self.order.order_id} - {self.order.client}"

    class Meta:
        ordering = ['-updated_at']


class ChatMessage(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='chat_messages', null=True, blank=True)
    user_name = models.CharField(max_length=100, default="Anonim")  # Yangi maydon
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name}: {self.content}"

    class Meta:
        ordering = ['created_at']
