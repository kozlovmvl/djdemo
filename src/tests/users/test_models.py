import pytest
from django.core.exceptions import ValidationError

from users.models import City, User


@pytest.mark.django_db
def test_invalid_username():
    city = City.objects.create(name="testcity")

    sut = User(username="abcd", email="user@test.host", city=city)

    with pytest.raises(ValidationError):
        sut.save()


@pytest.mark.django_db
def test_valid_username():
    city = City.objects.create(name="testcity")

    sut = User(username="abcde", email="user@test.host", city=city)

    sut.save()

    assert sut.pk is not None
