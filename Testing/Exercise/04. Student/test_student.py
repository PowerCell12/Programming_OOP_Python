import unittest
from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self): ## IF ERROR REMOVE STUDENT AND THE FIRST CHECK
        self.student = Student("John")
        self.student1 = Student("Peter", {"Math": ["Perfect", "Hello"], "English": ["What", "Gees"]})

    def test_if_not_courses(self):
        self.assertEqual(self.student.name, "John")
        self.assertEqual(self.student.courses, {})

    def test_if_courses(self):
        self.assertEqual(self.student1.name, "Peter")
        self.assertEqual(self.student1.courses, {"Math": ["Perfect", "Hello"], "English": ["What", "Gees"]})


    def test_if_course_in_all_courses(self):
        result = self.student1.enroll("Math", ["poor"])
        self.assertEqual(result, "Course already added. Notes have been updated.")

        self.assertEqual(self.student1.courses["Math"], ["Perfect", "Hello", "poor"])

    def test_check_if_add_course_equal_to_nothing(self):
        result  = self.student1.enroll("Physics", ["anime", "comics"])

        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student1.courses["Physics"], ["anime", "comics"])

    def test_check_if_add_course_equal_to_Y(self): ## if error remove
        result  = self.student1.enroll("Physics", ["anime", "comics"], "Y")

        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student1.courses["Physics"], ["anime", "comics"])


    def test_if_enrool_suc(self):
        result = self.student1.enroll("Chemistry", ["webtoons", "manga"], "X")
        self.assertEqual(result, "Course has been added.")
        self.assertEqual(self.student1.courses["Chemistry"], [])


    def test_add_notes_if_suc(self):
        result = self.student1.add_notes("Math", ["manga", "comics"])
        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(self.student1.courses["Math"], ["Perfect", "Hello", ["manga", "comics"]])

    def test_add_notes_error(self):

        with self.assertRaises(Exception) as ex:
            self.student1.add_notes("Physics", "webcooms")

        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")


    def test_leave_course_if_suc(self):
        result = self.student1.leave_course("Math")
        self.assertEqual(result, "Course has been removed")
        self.assertNotIn("Math", self.student1.courses)

    def test_leave_course_if_failed(self):

        with self.assertRaises(Exception) as ex:
            self.student1.leave_course("Physics")

        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")



if __name__ == "__main__":
    unittest.main()