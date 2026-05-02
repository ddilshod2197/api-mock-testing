import unittest
from unittest.mock import patch, MagicMock
import requests

class TestAPI(unittest.TestCase):
    def test_get_user(self):
        with patch('requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.json.return_value = {'name': 'John Doe', 'email': 'john@example.com'}
            mock_get.return_value = mock_response
            response = requests.get('https://api.example.com/user')
            self.assertEqual(response.json(), {'name': 'John Doe', 'email': 'john@example.com'})

    def test_post_user(self):
        with patch('requests.post') as mock_post:
            mock_response = MagicMock()
            mock_response.json.return_value = {'message': 'User created successfully'}
            mock_post.return_value = mock_response
            data = {'name': 'Jane Doe', 'email': 'jane@example.com'}
            response = requests.post('https://api.example.com/user', json=data)
            self.assertEqual(response.json(), {'message': 'User created successfully'})

if __name__ == '__main__':
    unittest.main()
```

```python
import unittest
from unittest.mock import patch, MagicMock
import requests

class TestAPI(unittest.TestCase):
    def test_get_user(self):
        with patch('requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.json.return_value = {'name': 'John Doe', 'email': 'john@example.com'}
            mock_get.return_value = mock_response
            response = requests.get('https://api.example.com/user')
            self.assertEqual(response.json(), {'name': 'John Doe', 'email': 'john@example.com'})

    def test_post_user(self):
        with patch('requests.post') as mock_post:
            mock_response = MagicMock()
            mock_response.json.return_value = {'message': 'User created successfully'}
            mock_post.return_value = mock_response
            data = {'name': 'Jane Doe', 'email': 'jane@example.com'}
            response = requests.post('https://api.example.com/user', json=data)
            self.assertEqual(response.json(), {'message': 'User created successfully'})

if __name__ == '__main__':
    unittest.main()
