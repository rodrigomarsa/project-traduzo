from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test):
    user = UserModel(
        {"name": "test_admin", "level": "admin", "token": "test_token"}
    )
    user.save()
    history = HistoryModel(
        {
            "text_to_translate": "Test translation",
            "translate_from": "en",
            "translate_to": "pt",
        }
    )
    history.save()
    response = app_test.delete(
        f"/admin/history/{history.id}",
        headers={
            "Authorization": "test_token",
            "User": "test_admin",
        },
    )
    assert response.status_code == 204
    assert response.json is None
