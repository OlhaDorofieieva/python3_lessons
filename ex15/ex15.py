import requests

class BaseAPI:
    base_url = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def get(endpoint):
        response = requests.get(f"{BaseAPI.base_url}{endpoint}")
        return response

class TestAPI(BaseAPI):
    @staticmethod
    def test_get_posts():
        response = TestAPI.get("/posts")
        assert response.status_code == 200
        assert len(response.json()) > 0

    @staticmethod
    def test_get_post():
        response = TestAPI.get("/posts/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1

    @staticmethod
    def test_create_post():
        data = {"userId": 1, "title": "test title", "body": "test body"}
        response = requests.post(f"{BaseAPI.base_url}/posts", json=data)
        assert response.status_code == 201

    @staticmethod
    def test_update_post():
        data = {"title": "updated title"}
        response = requests.put(f"{BaseAPI.base_url}/posts/1", json=data)
        assert response.status_code == 200

    @staticmethod
    def test_delete_post():
        response = requests.delete(f"{BaseAPI.base_url}/posts/1")
        assert response.status_code == 200

    @staticmethod
    def test_get_users():
        response = TestAPI.get("/users")
        assert response.status_code == 200
        assert len(response.json()) > 0

    @staticmethod
    def test_get_user():
        response = TestAPI.get("/users/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1

    @staticmethod
    def test_get_comments():
        response = TestAPI.get("/comments")
        assert response.status_code == 200
        assert len(response.json()) > 0

    @staticmethod
    def test_get_comment():
        response = TestAPI.get("/comments/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1

    @staticmethod
    def test_get_albums():
        response = TestAPI.get("/albums")
        assert response.status_code == 200
        assert len(response.json()) > 0

    @staticmethod
    def test_get_album():
        response = TestAPI.get("/albums/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1

if __name__ == "__main__":
    TestAPI.test_get_posts()
    TestAPI.test_get_post()
    TestAPI.test_create_post()
    TestAPI.test_update_post()
    TestAPI.test_delete_post()
    TestAPI.test_get_users()
    TestAPI.test_get_user()
    TestAPI.test_get_comments()
    TestAPI.test_get_comment()
    TestAPI.test_get_albums()
    TestAPI.test_get_album()