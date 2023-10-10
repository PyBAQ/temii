import pytest

from temii.talks.models import Talk
from temii.talks.tests.factories import TalkFactory
from temii.users.models import User
from temii.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


@pytest.fixture
def talk(db) -> Talk:
    return TalkFactory()
