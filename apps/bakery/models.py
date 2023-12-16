from django.db import models
from django.contrib.gis.db import models as point_models
from model_utils import Choices

from apps.users.models import User


class Bakery(models.Model):
    name = models.TextField()
    coordinates = point_models.PointField(
        srid=4326,
        dim=3
    )
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100, blank=True, null=True)
    street_address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    rating = models.PositiveSmallIntegerField()

    instagram_id = models.CharField()
    kakao_channel_url = models.URLField()
    number = models.CharField()

    def __str__(self):
        return f"{self.city} {self.state_province} {self.street_address}"


class Cake(models.Model):
    CATEGORY_CHOICES = Choices(
        ('base', '기본'),
        ('birthday', '생일'),
        ('anniversary', '기념일'),
        ('lover', '연인'),
        ('admission', '합격'),
        ('graduation', '졸업'),
        ('discharge', '전역'),
    )

    name = models.TextField()
    image = models.URLField()
    price = models.PositiveSmallIntegerField()
    bakery_id = models.PositiveBigIntegerField()
    bakery_name = models.TextField()
    category = models.CharField(
        choices=CATEGORY_CHOICES,
        default=CATEGORY_CHOICES.base,
        max_length=20
    )
    view_count = models.PositiveIntegerField()
    like_count = models.PositiveIntegerField()
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Review(models.Model):
    user_id = models.PositiveBigIntegerField()
    user_nickname = models.TextField()

    cake_id = models.PositiveBigIntegerField()
    cake_name = models.TextField()
    cake_image = models.URLField()

    rating = models.PositiveSmallIntegerField()
    content = models.TextField()


class CakeLikeRelation(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cake_like_relation'
    )
    cake = models.ForeignKey(
        Cake,
        on_delete=models.CASCADE,
        related_name='cake_like_relation'
    )
