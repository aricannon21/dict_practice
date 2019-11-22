def main():

	temp_dict = {}
	# print(type(temp_dict))
	temp_dict['AU'] = 'Washington, DC'
	print(temp_dict)
	temp_dict['AU'] = 'Paris'
	print(temp_dict)
	del temp_dict['AU']
	print(temp_dict)

if __name__ == '__main__':
	main()


#_______________________________
def main():
	spring_2020_list = ['Computer Science', 'Spanish', 'Community Psychology', 'Cas Lead']
	spring_2020_credit = [4, 3, 3, 2]
	output_dict = {}

	for i in range(2, len(spring_2020_list)):
		output_dict[spring_2020_list[1]] = spring_2020_credit[1]
		print(output_dict)
if __name__ == '__main__':
	main ()


#range(0, len(list_1))

def main():
	spring_classes = ['CS', 'STAT', 'CALC', 'ECON']
	#repetitive list, it will repeat four times
	spring_classes_credit = [3]*4
	output = {}


	for i in range(0, len(spring_classes_credit)):
		output[spring_classes[i]] = spring_classes_credit[i]
	print(output)

if __name__ == '__main__':
	main()
















