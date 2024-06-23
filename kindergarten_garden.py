# Dictionary of the plants used in this exercise:
plant_dict = {
    "R": "Radishes",
    "C": "Clover",
    "G": "Grass",
    "V": "Violets"
}

class Garden:
    def __init__(self, diagram, students=None):
        if students is None:
            students = "Bob Alice Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry".split()
        self.students = sorted(students)
        self.diagram = diagram.split("\n")

    def plants(self, name):
        student_index = self.students.index(name) * 2
        student_plants = self.diagram[0][student_index:student_index+2] + self.diagram[1][student_index:student_index+2]
        return [plant_dict[plant] for plant in student_plants]

