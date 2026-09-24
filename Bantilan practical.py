print("--- INITIALIZING DROPBPOX FOR STUDENTS ---")

class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self._files = []
        self._grade = None

    def __validate_grade(self, score):
        if 0 <= score <= 100:
            return True
        else:
            return False

    def __check_submission_status(self):
        if self._files:
            return True
        else:
            return False

    def __is_duplicate(self, filename):
        if filename in self._files:
            return True
        else:
            return False

    def add_file(self, filename):
        if self._grade is not None:
            print("Warning: Cannot add file to graded assignment.")
        elif self.__is_duplicate(filename):
            print("Warning: File already submitted.")
        else:
            self._files.append(filename)
            print("File added successfully.")

    def remove_file(self, filename):
        if self._grade is not None:
            print("Warning: Cannot remove file from graded assignment.")
        elif filename in self._files:
            self._files.remove(filename)
            print("File removed successfully.")
        else:
            print("Warning: File not found.")

    def assign_grade(self, score):
        if not self.__check_submission_status():
            print("No files submitted.")
        elif not self.__validate_grade(score):
            print("Invalid grade.")
        else:
            self._grade = score
            print("Grade assigned successfully.")

    def get_grade(self):
        return self._grade

    def view_files(self):
        return self._files.copy()

    def get_status_report(self):
        return {
            "student_id": self.student_id,
            "student_name": self.student_name,
            "assignment_title": self._assignment_title,
            "due_date": self._due_date,
            "is_submitted": self.__check_submission_status(),
            "file_count": len(self._files),
            "grade": self._grade,
        }


student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-10-01")
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-103", due_date="2026-10-01")
student3 = AssignmentSubmission(student_name="Juan dela Cruz", student_id="pshs-1033-x", assignment_title="CS 101", due_date="2026-10-01")
student4 = AssignmentSubmission(student_name="Maria Santos", student_id="pshs-1044-x", assignment_title="CS 101", due_date="2026-10-01")
student5 = AssignmentSubmission(student_name="Jose Reyes", student_id="pshs-1055-x", assignment_title="CS 101", due_date="2026-10-01")
print()

print("--- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2:Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.docx")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py")  
print(f"Juan's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf")
print()

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100) 
print()

print("--- FINAL SYSTEM REPORT---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())


