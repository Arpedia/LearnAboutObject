import pandas
import re

class Seiseki():
	def __init__(self, name = "", number = 0, grade = {}):
		self.__name = name
		self.__number = number
		self.__grade = grade

	def setName(self, name):
		self.__name = name
		return self.__name

	def getName(self):
		return self.__name
	
	name = property(getName, setName)

	def setNumber(self, num):
		self.__number = num
		return self.__number

	def getNumber(self):
		return self.__number

	number = property(getNumber, setNumber)

	def setGrade(self, result):
		self.__grade = result
		return self.__grade

	def getGrade(self):
		return self.__grade

	grade = property(getGrade, setNumber)

	def examTotal(self):
		total = 0
		for score in self.grade.values():
			total += score
		return total

	def examAve(self):
		return self.examTotal() / len(self.grade)

def readTSV():
	try:
		tsv = pandas.read_table('Seiseki.txt', encoding = 'utf-8', dtype={'名前':'S','ID':'S','国語':'S','数学':'S','英語':'S','物理':'S','通信工学':'S'})
		#tsv = pandas.read_table('Seiseki-e.txt', encoding = 'utf-8', dtype={'名前':'S','ID':'S','国語':'S','数学':'S','英語':'S','物理':'S','通信工学':'S'})
		data = tsv.fillna("-0").values.tolist()
		pattern = r"(.*),([12][09][0-9][0-9]e[0-9][0-9]),([0-9]{1,2}),([0-9]{1,2}),([0-9]{1,2}),([0-9]{1,2})"

		for row,i in zip(data,range(len(data))):
			print(row)
			matches  = re.match(pattern, ','.join(row))
			if not(matches):
				print("Error: 値が不正です。")
				del data[i]
		return data
	except FileNotFoundError:
		print("Error: File is not found.")
		exit()

data = readTSV()
students = []

for row in data :
	stu = Seiseki(row[0], row[1])
	subject = ['国語','数学','英語','物理','通信工学']
	dict = {}
	for sub,score in zip(subject, row[2:]):
		dict[sub] = int(score)
	stu.setGrade(dict)
	students.append(stu)

for stu in students:
	print(str(stu.number) + ' ' + str(stu.name) + ' : ' + str(stu.examAve()))