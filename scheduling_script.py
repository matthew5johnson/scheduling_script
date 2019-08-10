def get_franchise_name(franchise):
	if franchise == 1:
		return('Matt & Ross')
	elif franchise == 2:
		return('Scott & James')
	elif franchise == 3:
		return('Doug')
	elif franchise == 4:
		return('Crockett')
	elif franchise == 5:
		return('Blake')
	elif franchise == 6:
		return('Kfish')
	elif franchise == 7:
		return('Kyle')
	elif franchise == 8:
		return('Gaudet & Cameron')
	elif franchise == 9:
		return('RTRO')
	elif franchise == 10:
		return('Mitch')
	elif franchise == 11:
		return('Nick & Mickey')
	elif franchise == 12:
		return('Joseph & Mike')


schedules_2018 = {
    "Matt_and_Ross": [11, 5, 9, 8, 4, 2, 10, 7, 3, 12, 6, 11, 4],
    "Scott_and_James": [9, 4, 6, 11, 5, 1, 12, 3, 10, 7, 8, 9, 5],
    "Doug": [4, 9, 10, 5, 6, 7, 8, 2, 1, 11, 12, 4, 6],
	"Crockett": [3, 2, 8, 7, 1, 10, 9, 5, 12, 6, 11, 3, 1],
	"Blake": [10, 1, 11, 3, 2, 12, 6, 4, 7, 8, 9, 10, 2],
	"Kfish": [12, 7, 2, 9, 3, 8, 5, 10, 11, 4, 1, 12, 3],
	"Kyle": [8, 6, 12, 4, 9, 3, 11, 1, 5, 2, 10, 8, 9],
	"Gaudet_and_Cameron": [7, 12, 4, 1, 10, 6, 3, 11, 9, 5, 2, 7, 10],
	"RTRO": [2, 3, 1, 6, 7, 11, 4, 12, 8, 10, 5, 2, 7],
	"Mitch": [5, 11, 3, 12, 8, 4, 1, 6, 2, 9, 7, 5, 8],
	"Nick_and_Mickey": [1, 10, 5, 2, 12, 9, 7, 8, 6, 3, 4, 1, 12],
	"Joseph_and_Mike": [6, 8, 7, 10, 11, 5, 2, 9, 4, 1, 3, 6, 11]
}

def scheduling_algo(year):
	iterations = year - 2018

	new_schedules = {
		"Matt_and_Ross": [],
		"Scott_and_James": [],
		"Doug": [],
		"Crockett": [],
		"Blake": [],
		"Kfish": [],
		"Kyle": [],
		"Gaudet_and_Cameron": [],
		"RTRO": [],
		"Mitch": [],
		"Nick_and_Mickey": [],
		"Joseph_and_Mike": []
}
	rivals = {
		"Matt_and_Ross": [],
		"Scott_and_James": [],
		"Doug": [],
		"Crockett": [],
		"Blake": [],
		"Kfish": [],
		"Kyle": [],
		"Gaudet_and_Cameron": [],
		"RTRO": [],
		"Mitch": [],
		"Nick_and_Mickey": [],
		"Joseph_and_Mike": []
	}
	for franchise in schedules_2018:
		rivals[franchise] = schedules_2018[franchise][4]
			
	### Do this one time for every added year
	### This gets you the raw rotational schedule
	for franchise in schedules_2018:
		holding_schedule = []
		sched_list = schedules_2018[franchise]
		for i in range(1,12):
			if i != 4:
				new_schedules[franchise].append(sched_list[i])
	if year > 2019:
		iterations = year - 2019
		for i in range(0,iterations):
			for franchise in new_schedules:
				reference_list = new_schedules[franchise]
				new_last_opponent = new_schedules[franchise][0]
				for i in range(1, 12):
					new_schedules[franchise].append(reference_list[i])
				new_schedules[franchise] = new_schedules[franchise][10:19]
				new_schedules[franchise].append(new_last_opponent)
	
	for franchise in new_schedules:
		new_schedules[franchise].append(new_schedules[franchise][0])
		new_schedules[franchise].append(rivals[franchise])
		new_schedules[franchise].insert(4, rivals[franchise])

	### Convert numbers to franchise names:
	for franchise in new_schedules:
		print("{} {} schedule:".format(year, franchise))
		their_printed_schedule = []
		for weeks in new_schedules[franchise]:
			their_printed_schedule.append(get_franchise_name(weeks))
		print(their_printed_schedule)





scheduling_algo(2019)
