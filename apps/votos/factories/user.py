import factory

from django.contrib import auth


class UserFactory(factory.DjangoModelFactory):

    class Meta:
        model = auth.get_user_model()

    username = factory.Sequence(lambda n: "Agent {0}".format(str(n)))
    email = factory.Sequence(lambda n: "{0}@1.com".format(str(n)))
    password = factory.PostGenerationMethodCall('set_password',
                                                '1234')
