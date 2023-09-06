import re
from common.exceptions import IncorrectPasswordException
from django.conf import settings

PASSWORD_RE = re.compile(r"[\w.-]{8,}")


def validate_user_password(password: str, conf_password: str) -> str:
    if not PASSWORD_RE.match(password):
        raise IncorrectPasswordException(
            # "Password min lenght is 8, and it must contains A-Z, a-z, 0-9"
            {"code": settings.STATUS_CODES.get("password_not_valid")}
        )
    if password != conf_password:
        raise IncorrectPasswordException(
            {"code": settings.STATUS_CODES.get("password_mismatch")}
        )
    return password
