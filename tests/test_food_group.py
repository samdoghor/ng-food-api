"""
Food Group Test
"""
import unittest
from unittest.mock import patch
from models import GroupModel
from resources import GroupResource


class GroupResourceTest(unittest.TestCase):

    def setUp(self):
        self.group_resource = GroupResource()

    def test_create(self):
        # Mock the GroupModel.save() method
        with patch.object(GroupModel, 'save') as mock_save:
            response = self.group_resource.create(
                name="Test Group", description="Test Description")

            # Assert that the GroupModel.save() method was called
            mock_save.assert_called_once()

            # Assert the expected response
            expected_response = {
                'Message': 'Test Group Group was created successfully'
            }
            self.assertEqual(response, (expected_response, 200))

    def test_read_all(self):
        # Mock the GroupModel.query.all() method
        with patch.object(GroupModel.query, 'all') as mock_query:
            # Mock the return value of the query
            mock_query.return_value = [
                GroupModel(name="Group 1", description="Description 1"),
                GroupModel(name="Group 2", description="Description 2")
            ]

            response = self.group_resource.read_all()

            # Assert the expected response
            expected_response = {
                'Code': 200,
                'Code Type': 'Success',
                'Data': [
                    {
                        'id': mock_query.return_value[0].id,
                        'name': mock_query.return_value[0].name,
                        'description': mock_query.return_value[0].description
                    },
                    {
                        'id': mock_query.return_value[1].id,
                        'name': mock_query.return_value[1].name,
                        'description': mock_query.return_value[1].description
                    }
                ]
            }
            self.assertEqual(response, (expected_response, 200))

    # Add more test methods for other functions in the GroupResource class


if __name__ == '__main__':
    unittest.main()
