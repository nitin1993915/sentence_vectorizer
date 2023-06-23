from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_vectorize_sentence():
    response = client.post(
        "/nlp/v1/vectorize_text",
        json={"sentence_text": "AI is amazing!"},
    )
    assert response.status_code == 200



def test_sent_vector_length():
    response = client.post(
        "/nlp/v1/vectorize_text",
        json={"sentence_text": "AI is amazing!"},
    )
    assert response.status_code == 200
    assert len(response.json()["sentence_vector"]) == 500


def test_sent_vector_type():
    response = client.post(
        "/nlp/v1/vectorize_text",
        json={"sentence_text": "AI is amazing!"},
    )
    assert response.status_code == 200
    assert isinstance(response.json()["sentence_vector"][0], float)


def test_bad_input_type():
    response = client.post(
        "/nlp/v1/vectorize_text",
        json={"sentence_text": []},
    )
    assert response.status_code == 422


def test_empty_payload():
    response = client.post(
        "/nlp/v1/vectorize_text",
        json={},
    )
    assert response.status_code == 422
    assert response.json()["detail"] == [
        {
            "loc": [
                "body",
                "sentence_text"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        }
    ]
