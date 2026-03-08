# Part 1: Last Three Average

class StudentMarks:
    def __init__(self, marks):
        self.marks = marks

    def last_three_avg(self):
        try:
            # Use negative indexing to get last 3 marks
            last_three = self.marks[-3:]
            if len(last_three) < 3:
                raise IndexError
            avg = sum(last_three) / 3
            print("Average of last 3 marks is:", avg)
        except IndexError:
            print("Not enough marks to calculate average")

# Example
marks = [50, 60, 70, 80, 90]
student = StudentMarks(marks)
student.last_three_avg()