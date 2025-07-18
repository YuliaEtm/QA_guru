import requests
# url = "https://reqres.in/api"
url = "http://127.0.0.1:8000/api"
headers = {'x-api-key': 'reqres-free-v1'}


# def test_get_single_user_micro():
#     param = "users/10"
#     expected_id = 10
#     expected_email = 'byron.fields@reqres.in'
#
#     response = requests.get(f'{url}/{param}', headers=headers)
#     body = response.json()
#     data = body["data"]
#     print(data)
#     # {'id': 10,'email': 'byron.fields@reqres.in','first_name': 'Byron', 'last_name': 'Fields', 'avatar': image.jpg'}
#     assert data["id"] == expected_id
#     assert data['email'] == expected_email

def test_get_users_returns_unique_micro():
    param = "unknown"
    response = requests.get(f'{url}/{param}', headers=headers)
    assert response.status_code == 200
    print(response.text)
    body = response.json()
    assert body['per_page'] == len(body['data'])
