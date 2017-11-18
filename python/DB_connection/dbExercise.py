from __future__ import print_function
import sqlite3

class DbConnector:
	def __init__(self, dbName):
		self.dbName = dbName
		self.con = None
		self.cur = None

	def connect(self):
		try:
			self.con = sqlite3.connect(self.dbName)
			self.cur = self.con.cursor()
			print("Connection opened successful")
		except:
			print("Error opening the connection")

	def close(self):
		try:
			self.cur.close()
			self.con.close()
			print("Connection closed successful")
		except:
			print("Error closing the connection")

	def getData(self, query):
		self.cur.execute(query)
		return self.cur.fetchall()

	def insertData(self, query, table, inputs):
		self.cur.execute(query, inputs)
		self.con.commit()
		newQuery = "SELECT * FROM " + table
		return self.getData(newQuery)

	def printData(self, rows, header):
		print(header)
		for row in rows:
			print(row)
		print("\n")

	def getStudentsCourses(self):
		query = "SELECT students.first_name, students.last_name, " \
		"courses.description FROM ((students INNER JOIN student_courses " \
		"ON students.id = student_courses.student_id) INNER JOIN courses " \
		"ON student_courses.course_id = courses.id)"
		rows = self.getData(query)
		header = "FirstName LastName CourseDescrtion"
		self.printData(rows, header) 

	def getStudentsTeachers(self):
		query = "SELECT students.first_name, teachers.Name " \
		"FROM students INNER JOIN teachers ON " \
		"students.teacher_id = teachers.id"
		rows = self.getData(query)
		header = "StudentFirstName TeacherName"
		self.printData(rows, header)

	def insertStudent(self, inputs):
		query = "INSERT INTO students VALUES(?, ?, ?, ?, ?)"
		rows = self.insertData(query, "students", inputs)
		header = "ID FirstName LastName DateBirthDay TeacherId"
		self.printData(rows, header)


if __name__ == '__main__':

	dbName = "school.db"

	dbCon = DbConnector(dbName)
	dbCon.connect()
	
	'''

	Get all the students (FirstName,
	LastName) with their courses description.

	'''

	dbCon.getStudentsCourses()

	'''
	Get the Students (FirstName) and the
	teachers name.

	'''
	dbCon.getStudentsTeachers()

	'''
	Create a Function to add a new student.
	'''
	inputs = (5, 'Pedro', 'Sanchez', "1995-09-12", 2)
	dbCon.insertStudent(inputs)

	# Close the connections pls
	dbCon.close()