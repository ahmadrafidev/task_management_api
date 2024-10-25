from django.test import SimpleTestCase
from unittest.mock import patch
from rest_framework.test import APIClient
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse

class TaskAPITest(SimpleTestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.task_list_url = reverse('task-list')
        self.task_detail_url = lambda id: reverse('task-detail', args=[id])

    @patch('tasks.views.TaskViewSet.get_queryset')
    def test_get_task_list(self, mock_get_queryset):
        mock_get_queryset.return_value = []
        response = self.client.get(self.task_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], [])
        
    @patch('tasks.views.TaskViewSet.create')
    def test_create_task(self, mock_create):
        mock_create.return_value = Response({
            "id": 1,
            "title": "New Task",
            "description": "This is a new task",
            "is_completed": False
        }, status=status.HTTP_201_CREATED)
        
        data = {
            "title": "New Task",
            "description": "This is a new task",
            "is_completed": False
        }
        response = self.client.post(self.task_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Task")