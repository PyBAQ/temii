from django.urls import reverse


class TestTalkAdmin:
    def test_changelist(self, admin_client):
        url = reverse("admin:talks_talk_changelist")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_search(self, admin_client):
        url = reverse("admin:talks_talk_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == 200

    def test_add(self, admin_client):
        url = reverse("admin:talks_talk_add")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_view_user(self, admin_client, talk):
        url = reverse("admin:talks_talk_change", kwargs={"object_id": talk.pk})
        response = admin_client.get(url)
        assert response.status_code == 200
