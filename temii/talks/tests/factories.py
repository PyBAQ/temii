from factory import Faker, Iterator, SubFactory
from factory.django import DjangoModelFactory

from temii.talks.models import Talk
from temii.users.tests.factories import UserFactory


class TalkFactory(DjangoModelFactory):
    name = Faker("name")
    description = Faker("text")
    user = SubFactory(UserFactory)
    language = Iterator(["es", "en"])
    level = Iterator([1, 2, 3])
    comments = Faker("text")

    class Meta:
        model = Talk
