from Test import Test
# import datetime


class Student:
    def __init__(self, username, test_history=[]):
        self.username = username
        self.test_history = test_history

    def add_test(self, test):
        self.test_history.append(test)
        self.write_test_history()


    def write_test_history(self, test):
        file = open("test_history.txt", "a")
        file.write(f"{test}\n")
        file.close()

    def read_test_history(self):
        try:
            with open("test_history.txt", "r") as file:
                lines = file.readlines()
            for line in lines:
                print(line.rstrip())
        except FileNotFoundError:
            with open("test_history.txt", "w") as file:
                file.write(f"Test history for {self.username}\n")

    def __str__(self):
        return f"{self.username}"

    def print_test_history(self):
        try:
            file = open("test_history.txt", "r")
            for line in file:
                print(line)
        except FileNotFoundError:
            with open("test_history.txt", "w") as file:
                file.write(f"Test history for {self.username}\n")

    def add_test(self, test):
        self.test_history.append(self.username, test)


student = Student("John", 20)
game1 = Test(student.username,"2020-01-02",70, "8:50")
game2 = Test(student.username,"2020-01-03",80, "8:40")
student.write_test_history(game1)
student.print_test_history()
student2 = Student("Mary", 18)
game3= Test(student2.username,"2020-01-04",90, "11:30")
student2.write_test_history(game3)
student2.print_test_history()