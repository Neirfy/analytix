from jose import jwt


def decode_token(
    token: str,
    key: dict,
):
    return jwt.decode(
        token,
        key,
        algorithms=["RS256"],
        audience="gateway",
        issuer="authn",
    )
