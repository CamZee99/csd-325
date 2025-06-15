# Define student class
class Student:
  def __init__(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name
      self.grade_points = 0
      self.credits = 0
      self.gpa = 0

  def calculate_gpa(self):
      if self.credits != 0:
          self.gpa = self.grade_points / self.credits
      else:
          self.gpa = 0

  def get_gpa(self):
      return self.gpa

  def student_year(self):
      if self.credits < 30:
          return "Year one"
      elif self.credits < 60:
          return "Year Two"
      elif self.credits < 90:
          return "Year Three"
      else:
          return "Year Four"

class DeclaredStudent(Student):
  def __init__(self, first_name, last_name, concentration):
      super().__init__(first_name, last_name)
      self.concentration = concentration

def letter_to_grade_points(letter_grade):
  grade_conversion = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
  return grade_conversion.get(letter_grade.upper(), 0.0)
  # Create Main program
def main():
  # Ask the user for the first and last name of the student
  first_name = input("Enter the first name of the student: ")
  last_name = input("Enter the last name of the student: ")
  concentration = input("Enter the student's declared concentration: ")

  # Create the Declared Student object
  student = DeclaredStudent(first_name, last_name, concentration)
    
  # Create a loop to input course details
  credits = 0
  while credits != -1:
      credits = float(input("Enter the credits for the course (or -1 to end): "))
      if credits != -1:
          letter_grade = input("Enter the letter grade for the course (A, B, C, D, F): ")
          grade_points = letter_to_grade_points(letter_grade)
  # Update the student's grade points and credits
          student.grade_points += credits * grade_points
          student.credits += credits

  # Calculate the student's cumulative GPA
  student.calculate_gpa()

  # Determine the student's year
  year = student.student_year()

  # Display the student's details
  print(f"\n{student.first_name} {student.last_name} ({student.concentration})")
  print(f"Cumulative GPA: {student.get_gpa():.2f}")
  print(f"Student Year: {year}")

if __name__ == "__main__":
  main()
