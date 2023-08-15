import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    history = HistoryModel.list_as_json()
    json_data = json.loads(history)
    expected = [
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        },
    ]
    assert len(json_data) == 2
    assert (
        json_data[0]["text_to_translate"] == expected[0]["text_to_translate"]
    )
    assert json_data[1]["translate_to"] == expected[1]["translate_to"]
