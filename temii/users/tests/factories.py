from collections.abc import Sequence
from typing import Any

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from factory import Faker, LazyAttribute, post_generation
from factory.django import DjangoModelFactory, ImageField


class UserFactory(DjangoModelFactory):
    username = Faker("user_name")
    email = Faker("email")
    name = Faker("name")
    phone = Faker("phone_number")
    bio = Faker("text")
    image = LazyAttribute(lambda _: ContentFile(ImageField()._make_data({"width": 300, "height": 300}), "example.jpg"))

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        password = (
            extracted
            if extracted
            else Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).evaluate(None, None, extra={"locale": None})
        )
        self.set_password(password)

    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]
