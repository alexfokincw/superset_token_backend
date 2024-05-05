from src.token_generator import get_token


class TestGetToken:
    def test_get_token(self):
        token = get_token()

        assert (
            len(token) > 0
        ), f"token is empty"
