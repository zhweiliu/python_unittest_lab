import unittest
from unittest.mock import Mock
from my_project.services import student_services


class TestStudentService(unittest.TestCase):

    def test_change_name_with_record(self):
        # Setup
        student_services.find_student_by_id = Mock()
        # student_services.find_student_by_id.return_value = Student(1, 'Andy')
        student = Mock(id=1, name='Andy')
        student_services.find_student_by_id.return_value = student

        student_services.save_student = Mock()

        # Action
        student_services.change_name(1, 'JiaYu')

        # Assert
        self.assertEqual('JiaYu', student.name)
        student_services.save_student.assert_called()

    def test_change_name_without_record(self):
        # Setup
        student_services.find_student_by_id = Mock()
        student_services.find_student_by_id.return_value = None

        student_services.save_student = Mock()

        # Action
        student_services.change_name(1, 'JiaYu')

        # Assert
        student_services.save_student.assert_not_called()
