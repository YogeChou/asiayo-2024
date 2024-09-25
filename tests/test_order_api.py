
def test_post_orders_ok(test_client, order):
    response = test_client.post("/api/orders", json=order)
    assert response.status_code == 201


def test_post_orders_invalid_request(test_client, order):
    order["currency"] = "KRD"
    response = test_client.post("/api/orders", json=order)
    assert response.status_code == 400
