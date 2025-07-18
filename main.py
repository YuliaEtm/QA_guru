from fastapi import FastAPI

app = FastAPI()


# @app.get("/api/users/10")
# def get_get_single_user():
#     return {
#         "data": {
#             "id": 10,
#             "email": "byron.fields@reqres.in",
#             "first_name": "Byron",
#             "last_name": "Fields",
#             "avatar": "https://reqres.in/img/faces/10-image.jpg"
#         },
#         "support": {
#             "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
#             "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
#         }
#     }

@app.get("/api/unknown")
def get_users_returns_unique():
    return {"page": 1, "per_page": 6, "total": 12, "total_pages": 2,
            "data": [{"id": 1, "name": "cerulean", "year": 2000, "color": "#98B2D1", "pantone_value": "15-4020"},
                     {"id": 2, "name": "fuchsia rose", "year": 2001, "color": "#C74375", "pantone_value": "17-2031"},
                     {"id": 3, "name": "true red", "year": 2002, "color": "#BF1932", "pantone_value": "19-1664"},
                     {"id": 4, "name": "aqua sky", "year": 2003, "color": "#7BC4C4", "pantone_value": "14-4811"},
                     {"id": 5, "name": "tigerlily", "year": 2004, "color": "#E2583E", "pantone_value": "17-1456"},
                     {"id": 6, "name": "blue turquoise", "year": 2005, "color": "#53B0AE", "pantone_value": "15-5217"}],
            "support": {"url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
                        "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."}}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

    # uvicorn main:app --reload (запуск терминал)
