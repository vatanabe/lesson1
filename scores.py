scores_line = [{'school_class': '4a', 'scores': [2,4,2,4]}, {'school_class': '5b', 'scores': [3,5,3,5,3, 5]}, {'school_class': '6c', 'scores': [1,3,1,3,1,3,1,3]}]
#line1 = [2,4,2,4]
def average(list):
	numbers_score = len(list)
	clas_evaluation = 0
	for scores in range(numbers_score):
		clas_evaluation = clas_evaluation + list[scores]
		clas_evaluation_average = (clas_evaluation / numbers_score)
	return str(clas_evaluation_average)
#print(average(line1))
numbers=len(scores_line)
school_evaluation = 0
for clas in range (numbers):
	clas_score_dictionary=(scores_line[clas])
	clas_score = clas_score_dictionary['scores']
	name_clas = clas_score_dictionary['school_class']
	print(school_evaluation + int(average(clas_score))
#	print('средняя оценка в классе ' + name_clas + ':  ' + average(clas_score))