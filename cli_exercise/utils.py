import enum
import json
from typing import Optional

import requests


class AuthenticationMethod(enum.Enum):
    TOKEN = 1
    BASIC = 2


def make_authenticated_request(
    url: str,
    password: str,
    auth_method: AuthenticationMethod = AuthenticationMethod.TOKEN,
    **kwargs
) -> Optional[dict]:
    """Make a request to the given URL, returning the response."""

    headers = {}
    username = kwargs.pop("username", None)
    auth = None

    if auth_method == AuthenticationMethod.TOKEN:
        headers["X-Api-Key"] = password

    elif auth_method == AuthenticationMethod.BASIC:
        auth = (username, password)

    res = requests.get(url, headers=headers, auth=auth)

    if res.status_code != 200:
        return None

    try:
        return res.json()
    except json.JSONDecodeError:
        return None


if __name__ == "__main__":
    import sys

    print(make_authenticated_request(sys.argv[1], sys.argv[2]))
