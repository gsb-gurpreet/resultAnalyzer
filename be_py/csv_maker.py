import json

branches = []

with open("sanitized.json", 'r') as student_file:
	students = json.load(student_file)

def print_headder(student_index):
	headder = "student_name, perma_reg_num, "
	for subject in students[student_index]['subjects']:
		headder = headder + subject['code'] + 'obtained_marks, '
		headder = headder + subject['code'] + 'is_pass, '
	headder = headder + 'total_marks'
	print(headder)

print(students[0]['branch'] + '\n')
print_headder(0)

for i in range(len(students)):
	line = ""
	if i > 5: # magic no. 
		if students[i]['branch'] != students[i - 1]['branch']:
			print('\n' + '\n' + students[i]['branch'] + '\n')
			print_headder(i)
	line = line + students[i]['student_name'] + ', '
	line = line + students[i]['perma_reg_num'] + ', '
	
	for subject in students[i]['subjects']:
		line = line + str(subject['obtained_marks']) + ', '
		line = line + str(subject['is_pass']) + ', '
	line = line + str(students[i]['total_marks'])
	print(line)
