import requests


def test_user_data():
    # url = "https://reqres.in/api/users/2"
    url = " http://127.0.0.1:8000/api/users/2"
    headers = {'x-api-key': 'reqres-free-v1'}
    expected_id = 2
    expected_email = "janet.weaver@reqres.in"

    response = requests.get(url, headers=headers)
    print(response.text)
    body = response.json()
    data = body["data"]

    assert data["id"] == expected_id