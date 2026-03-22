from contextlib import nullcontext

import pytest
from django.core.exceptions import ValidationError

from users.models import User


@pytest.mark.django_db
@pytest.mark.parametrize(
    argnames=("username", "expect"),
    argvalues=(
        ("abcd", pytest.raises(ValidationError)),
        ("abcde", nullcontext()),
    ),
)
def test_validation_username(username, expect):
    sut = User(username=username, email="user@test.host", city_id=1)

    with expect:
        sut.clean()
