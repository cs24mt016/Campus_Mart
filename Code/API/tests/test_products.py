import pytest
import requests
from unittest.mock import patch

BASE_URL = "http://127.0.0.1:5000"  # Update with your actual base URL

@pytest.fixture
def sample_products():
    return {
        "products": [
            {
                "listingID": 1,
                "title": "Laptop",
                "selling_price": 50000,
                "description": "A high-performance laptop.",
                "imageURLs": '["https://images.unsplash.com/photo-1542751110-70e56cd58e6e"]'
            },
            {
                "listingID": 2,
                "title": "Smartphone",
                "selling_price": 30000,
                "description": "A latest model smartphone.",
                "imageURLs": '["https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0"]'
            }
        ]
    }

def test_fetch_products_success(sample_products):
    # Mocking the requests.get method to return a predefined response
    with patch('requests.get') as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = sample_products
        
        response = requests.get(f"{BASE_URL}/products")
        assert response.ok
        assert response.json() == sample_products


def test_fetch_products_failure():
    # Mocking the requests.get method to simulate a failure
    with patch('requests.get') as mock_get:
        mock_get.return_value.ok = False
        mock_get.return_value.status_text = "Not Found"
        
        response = requests.get(f"{BASE_URL}/products")
        assert not response.ok
        assert response.status_text == "Not Found"