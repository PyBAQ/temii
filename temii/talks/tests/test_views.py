import pytest
from django.test import RequestFactory

from temii.talks.forms import NewTalkForm
from temii.talks.tests.factories import TalkFactory
from temii.talks.views import TalkCreateView
from temii.users.models import User

pytestmark = pytest.mark.django_db


class TestTalkCreateView:
    def test_form_valid(self, user: User, rf: RequestFactory):
        view = TalkCreateView()
        talk = TalkFactory()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        # Initialize the form
        form = NewTalkForm(instance=talk)
        form.cleaned_data = {}
        view.form_valid(form)

        assert form.instance.user == request.user
