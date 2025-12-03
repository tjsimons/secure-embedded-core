from src.security.auth import AuthManager

def test_hash_generates_unique_salt():
    auth = AuthManager()

    h1 = auth.hash_secret("password123")
    h2 = auth.hash_secret("password123")

    # Same password should never generate the same hash twice
    assert h1 != h2


def test_hash_format_contains_salt():
    auth = AuthManager()
    hashed = auth.hash_secret("abc")

    salt, digest = hashed.split(":")

    # Ensure salt exists
    assert len(salt) > 0

    # SHA-256 hex digest should always be 64 characters
    assert len(digest) == 64
