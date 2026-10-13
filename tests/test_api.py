from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient


mock_model = MagicMock()
mock_model.predict_proba.return_value = [[0.9, 0.1]]

mock_scaler = MagicMock()
mock_scaler.transform.side_effect = lambda value: value

with patch("joblib.load", side_effect=[mock_model, mock_scaler]):
    import router as router_module
    from main import app


client = TestClient(app)


def build_transaction():
    return {
        "amount": 149.62,
        "time": 0,
        "v1": -1.359807,
        "v2": -0.072781,
        "v3": 2.536347,
        "v4": 1.378155,
        "v5": -0.338321,
        "v6": 0.462388,
        "v7": 0.239599,
        "v8": 0.098698,
        "v9": 0.363787,
        "v10": 0.090794,
        "v11": -0.5516,
        "v12": -0.617801,
        "v13": -0.99139,
        "v14": -0.311169,
        "v15": 1.468177,
        "v16": -0.470401,
        "v17": 0.207971,
        "v18": 0.025791,
        "v19": 0.403993,
        "v20": 0.251412,
        "v21": -0.018307,
        "v22": 0.277838,
        "v23": -0.110474,
        "v24": 0.066928,
        "v25": 0.128539,
        "v26": -0.189115,
        "v27": 0.133558,
        "v28": -0.021053,
    }


def build_stored_transaction(transaction_id=2, is_flagged=False):
    transaction = build_transaction()
    transaction.update(
        {
            "id": transaction_id,
            "fraud_score": 0.1,
            "is_flagged": is_flagged,
        }
    )
    return transaction


def make_connection(fetchone_value=None, fetchall_value=None):
    cursor = MagicMock()
    cursor.fetchone.return_value = fetchone_value
    cursor.fetchall.return_value = fetchall_value or []

    connection = MagicMock()
    connection.cursor.return_value = cursor

    return connection, cursor


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_get_all_transactions():
    row = build_stored_transaction()
    connection, _ = make_connection(fetchall_value=[row])

    with patch.object(router_module, "get_connection", return_value=connection):
        response = client.get("/transactions")

    assert response.status_code == 200
    assert response.json()[0]["id"] == 2


def test_get_transaction_by_id():
    row = build_stored_transaction()
    connection, _ = make_connection(fetchone_value=row)

    with patch.object(router_module, "get_connection", return_value=connection):
        response = client.get("/transactions/2")

    assert response.status_code == 200
    assert response.json()["id"] == 2


def test_get_missing_transaction_returns_404():
    connection, _ = make_connection(fetchone_value=None)

    with patch.object(router_module, "get_connection", return_value=connection):
        response = client.get("/transactions/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Transaction not found"}


def test_create_transaction():
    connection, cursor = make_connection(fetchone_value=(3,))

    with patch.object(router_module, "get_connection", return_value=connection):
        response = client.post("/transactions", json=build_transaction())

    assert response.status_code == 200
    assert response.json()["id"] == 3
    assert response.json()["is_flagged"] is True
    connection.commit.assert_called_once()
    cursor.close.assert_called_once()
    connection.close.assert_called_once()
