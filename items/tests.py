from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item
from django.utils import timezone


class ItemTests(APITestCase):

    def setUp(self):
        """Create some initial items for testing."""
        for i in range(1, 26):
            Item.objects.create(
                name=f'Item {i:02}',
                description=f'Description for item {i}',
                created_at=timezone.now(),
                updated_at=timezone.now()
            )

    def test_create_item(self):
        """Test creating a new item."""
        data = {'name': 'New Item', 'description': 'A brand new item'}
        response = self.client.post('/api/items/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 26)
        self.assertEqual(Item.objects.last().name, 'New Item')

    def test_list_items(self):
        """Test listing all items."""
        response = self.client.get('/api/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 10)

    def test_list_items_pagination(self):
        """Test pagination for listing items."""
        response = self.client.get('/api/items/?page=2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 10)

        response = self.client.get('/api/items/?page=4')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_items_ordering(self):
        """Test ordering of items."""
        response = self.client.get('/api/items/?ordering=-created_at')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for i in range(len(response.data['results']) - 1):
            item1 = response.data['results'][i]
            item2 = response.data['results'][i + 1]
            self.assertGreaterEqual(item1['created_at'], item2['created_at'])

    def test_list_items_search(self):
        """Test searching for items."""
        response = self.client.get('/api/items/?search=Item 1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data['results']), 0)

        response = self.client.get(
            '/api/items/?search=Description for item 20')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data['results']), 0)

        response = self.client.get('/api/items/?search=Nonexistent')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 0)

    def test_retrieve_item(self):
        """Test retrieving a specific item."""
        item = Item.objects.first()
        response = self.client.get(f'/api/items/{item.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], item.name)

    def test_update_item(self):
        """Test updating an existing item."""
        item = Item.objects.first()
        data = {'name': 'Updated Item', 'description': 'Updated description'}
        response = self.client.put(f'/api/items/{item.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        item.refresh_from_db()
        self.assertEqual(item.name, 'Updated Item')
        self.assertEqual(item.description, 'Updated description')

    def test_delete_item(self):
        """Test deleting an item."""
        item = Item.objects.first()
        response = self.client.delete(f'/api/items/{item.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.filter(id=item.id).count(), 0)

    def test_invalid_page_number(self):
        """Test providing an invalid page number."""
        response = self.client.get('/api/items/?page=abc')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
