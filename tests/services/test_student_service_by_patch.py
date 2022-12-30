import unittest
from unittest.mock import patch, Mock
from my_project.services import student_services


class TestStudentService(unittest.TestCase):

    @patch('my_project.services.student_services.save_student')
    @patch('my_project.services.student_services.find_student_by_id')
    def test_change_name_decorator(self, mock_find_student_by_id, mock_save_student):
        # Setup
        student = Mock(id=1, name='Andy')
        mock_find_student_by_id.return_value = student

        # Action
        student_services.change_name(1, 'JiaYu')

        # Assert
        self.assertEqual('JiaYu', student.name)

    def test_change_name_contextmanager(self):
        # Setup
        student = Mock(id=1, name='Andy')

        with patch('my_project.services.student_services.find_student_by_id') as mock_find_student_by_id, \
                patch('my_project.services.student_services.save_student'):

            mock_find_student_by_id.return_value = student

            # Action
            student_services.change_name(1, 'JiaYu')

        # Assert
        self.assertEqual('JiaYu', student.name)

    @patch('my_project.services.student_services.find_student_by_id')
    def test_change_name_manual(self, mock_find_student_by_id):
        # Setup
        student = Mock(id=1, name='Andy')
        mock_find_student_by_id.return_value = student

        patcher = patch('my_project.services.student_services.save_student')

        # Action
        patcher.start()

        student_services.change_name(1, 'JiaYu')

        patcher.stop()

        # Assert
        self.assertEqual('JiaYu', student.name)
