import requests


# def test_get_single_user_micro():
#     # url = "https://reqres.in/api/users/2"
#     url = " http://127.0.0.1:8000/api/users/10"
#     headers = {'x-api-key': 'reqres-free-v1'}
#     expected_id = 10
#     expected_email = "janet.weaver@reqres.in"
#
#     response = requests.get(url, headers=headers)
#     print(response.text)
#     body = response.json()
#     data = body["data"]
#
#     assert data["id"] == expected_id


def test_get_users_returns_unique_users_micro():
    # url = "https://reqres.in/api/unknown"
    url = "http://127.0.0.1:8000/api/unknown"
    headers = {'x-api-key': 'reqres-free-v1'}
    response = requests.get(url=url, headers=headers)
    assert response.status_code == 200
    print(response.text)
    body = response.json()
    assert body['per_page'] == len(body['data'])
