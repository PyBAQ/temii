from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return f"profile_pics/{instance.username}/{filename}"


class User(AbstractUser):
    """
    Default custom user model for temii.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    phone = CharField(_("Phone"), blank=True, max_length=50)
    bio = CharField(_("Bio"), blank=True, max_length=255)
    image = ImageField(_("Image"), default="default.jpg", upload_to=upload_to)

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
