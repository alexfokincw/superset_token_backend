import requests

import settings


def get_access_token(
    session, base_url: str, user: str, password: str, origin_url: str
) -> str:
    # Login credentials and endpoint
    login_url = f"{base_url}/api/v1/security/login"
    login_payload = {
        "username": user,
        "password": password,
        "provider": "db",
        # "refresh": True
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Access-Control-Allow-Origin": origin_url,
    }

    try:
        response = session.post(login_url, json=login_payload, headers=headers)
        response_data = response.json()
        access_token = response_data["access_token"]
        # refresh_token = response_data['refresh_token']
    except requests.exceptions.HTTPError as err:
        print(f"{__name__} HTTP Error: {err}")
        return ""
    except requests.exceptions.ConnectionError as err:
        print(f"{__name__} Connection Error: {err}")
        return ""
    except requests.exceptions.Timeout as err:
        print(f"{__name__} Timeout Error: {err}")
        return ""
    except requests.exceptions.RequestException as err:
        print(f"{__name__} Something wrong with request: {err}")
        return ""

    return access_token


def get_csrf_token(session, base_url: str, access_token: str) -> str:
    csrf_url = f"{base_url}/api/v1/security/csrf_token"
    headers = {"Authorization": f"Bearer {access_token}"}

    try:
        response = session.get(csrf_url, headers=headers)
    except requests.exceptions.HTTPError as err:
        print(f"{__name__} HTTP Error: {err}")
        return ""
    except requests.exceptions.ConnectionError as err:
        print(f"{__name__} Connection Error: {err}")
        return ""
    except requests.exceptions.Timeout as err:
        print(f"{__name__} Timeout Error: {err}")
        return ""
    except requests.exceptions.RequestException as err:
        print(f"{__name__} Something wrong with request: {err}")
        return ""

    try:
        return response.json()["result"]
    except KeyError:
        print("KeyError: The JSON response did not contain `result` field")
    except ValueError:
        print("ValueError: Invalid JSON response")

    return ""


def get_guest_token(
    session,
    base_url: str,
    access_token: str,
    csrf_token: str,
    dashboard_id: str,
    user_first_name: str,
    user_last_name: str,
    user: str,
) -> str:
    guest_token_url = f"{base_url}/api/v1/security/guest_token"
    guest_token_payload = {
        "resources": [{"id": dashboard_id, "type": "dashboard"}],
        "rls": [],
        "user": {
            "first_name": user_first_name,
            "last_name": user_last_name,
            "username": user,
        },
    }
    headers = {
        "Authorization": f"Bearer {access_token}",
        "X-CSRFToken": csrf_token,
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    try:
        response = session.post(
            guest_token_url, json=guest_token_payload, headers=headers
        )
    except requests.exceptions.HTTPError as err:
        print(f"{__name__} HTTP Error: {err}")
        return ""
    except requests.exceptions.ConnectionError as err:
        print(f"{__name__} Connection Error: {err}")
        return ""
    except requests.exceptions.Timeout as err:
        print(f"{__name__} Timeout Error: {err}")
        return ""
    except requests.exceptions.RequestException as err:
        print(f"{__name__} Something wrong with request: {err}")
        return ""

    try:
        return response.json()["token"]
    except KeyError:
        print("KeyError: The JSON response did not contain `token` field")
    except ValueError:
        print("ValueError: Invalid JSON response")

    return ""


def get_token():
    session = requests.Session()

    access_token = get_access_token(
        session,
        base_url=settings.SUPERSET_BASE_URL,
        user=settings.SUPERSET_USER,
        password=settings.SUPERSET_PASSWORD,
        origin_url=settings.FRONTEND_BASE_URL,
    )

    csrf_token = get_csrf_token(
        session, base_url=settings.SUPERSET_BASE_URL, access_token=access_token
    )

    dashboard_id = "3b821ae2-5863-437a-862a-0545be074563"
    return get_guest_token(
        session,
        base_url=settings.SUPERSET_BASE_URL,
        access_token=access_token,
        csrf_token=csrf_token,
        dashboard_id=dashboard_id,
        user_first_name=settings.SUPERSET_FIRST_NAME,
        user_last_name=settings.SUPERSET_LAST_NAME,
        user=settings.SUPERSET_USER,
    )
