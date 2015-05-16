import csv
import json
import string

class txt_To_Json:
	# """docstring for csv_To_Json"""
	def __init__(self, Location):
		# super(csv_To_Json, self).__init__()
		self.Location = Location
	def transform(self):
		file_feedback=open('feedback.txt','r')
		#jsonfile=open('J_feedback.txt','w')

		#/**Save first line for out json Key!**/
		line = file_feedback.readline()
		Key = line.split()
		while True:
			data_line = file_feedback.readline()
			#if load file is done 
			if data_line == "":
				break

			# print data_line

			data_array=data_line.split()

			i=0
			dic_data={}
			data=[]
			for i in range(7):
				data.append({Key[i]:data_array[i]})
				# print json.dumps('[Key[i]':data_array[i]])
				# print json.dumps([{'a':"A",'b':(2,4),'c':3.0}])
				print data
			
			#Only return one line data
			dic_data={'feedback':data}
			return dic_data



		return data

		
