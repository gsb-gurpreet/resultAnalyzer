import json

new_students = []

with open("sanitized.json", 'r') as student_file:
	students = json.load(student_file)

for student in students:
	new_subjects = []
	for subject in student['subjects']:
		new_subject = {}
		new_subject['code'] = subject['code']
		new_subject['is_pass'] = subject['is_pass']
		new_subject['obtained_marks'] = subject['obtained_marks']
		if subject['type'] == "PP":
			new_subject['oe_marks'] = subject['oe_marks']
			new_subject['th_marks'] = subject['th_marks']
		new_subjects.append(new_subject)

	new_student = {}
	new_student['branch']		= student['branch']
#	new_student['mom_name']		= student['mom_name']
	new_student['perma_reg_num']= student['perma_reg_num']
	new_student['student_name']	= student['student_name']
	new_student['total_marks']	= student['total_marks']
	new_student['subjects'] = new_subjects
	new_students.append(new_student)
	
print(json.dumps(new_students, sort_keys = True, indent = 4, separators=(', ',': ')))
		
