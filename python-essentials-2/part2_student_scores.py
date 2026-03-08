# Part 2: Highest of Last Two Scores

class StudentScores:
    def __init__(self, scores):
        self.scores = scores

    def highest_last_two(self):
        try:
            last_two = self.scores[-2:]
            if len(last_two) < 2:
                raise IndexError
            highest = max(last_two)
            print("Highest score among last two is:", highest)
        except IndexError:
            print("Not enough scores to find highest value")

# Example
scores = [45, 67, 89, 72]
student = StudentScores(scores)
student.highest_last_two()