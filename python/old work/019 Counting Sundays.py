# 19 Counting Sundays

def instructions():
	# 1 Jan 1900 was a Monday.
	# Thirty days has September,
	# April, June and November.
	# All the rest have thirty-one,
	# Saving February alone,
	# Which has twenty-eight, rain or shine.
	# And on leap years, twenty-nine.
	# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

	# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
	pass
pass

sunday = 0
monday = 1
tuesday = 2
wednesday = 3
thursday = 4
friday = 5
saturday = 6

january = 1
february = 2
march = 3
april = 4
may = 5
june = 6
july = 7
august = 8
september = 9
october = 10
november = 11
december = 12

days_in_january = 31
days_in_february = 28
days_in_march = 31
days_in_april = 30
days_in_may = 31
days_in_june = 30
days_in_july = 31
days_in_august = 31
days_in_september = 30
days_in_october = 31
days_in_november = 30
days_in_december = 31

count_of_sundays = 0

date_year = 1900
date_day_of_week = monday




 
for year in range(date_year, 2001):
	if year == 1901:
		count_of_sundays = 0
	#print "year: ", year , "count_of_sundays: ", count_of_sundays
	# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
	date_year_is_leap = False
	if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
		date_year_is_leap = True

	if (date_year_is_leap and year == 2000):
		#print "LEAP year: ", year
		pass


	for month in range(1, 13):
		#print "month: ", month
		#print "count: ", count_of_sundays
		if month == january:
			for day in range(days_in_january):
				if (day == 1 and date_day_of_week == sunday):
					count_of_sundays += 1

				if date_day_of_week != saturday:
					date_day_of_week += 1
				else:
					date_day_of_week = 0

		if month == february:
			if date_year_is_leap:
				days_in_february = 29
			else:
				days_in_february = 28
			for day in range(days_in_february):
				if (day == 1 and date_day_of_week == sunday):
					count_of_sundays += 1

				if date_day_of_week != saturday:
					date_day_of_week += 1
				else:
					date_day_of_week = 0

		if month == march:
			for day in range(days_in_march):
				if (day == 1 and date_day_of_week == sunday):
					count_of_sundays += 1

				if date_day_of_week != saturday:
					date_day_of_week += 1
				else:
					date_day_of_week = 0

		if month == april:
			for day in range(days_in_april):
				if (day == 1 and date_day_of_week == sunday):
					count_of_sundays += 1

				if date_day_of_week != saturday:
					date_day_of_week += 1
				else:
					date_day_of_week = 0

		if month == may:
			for day in range(days_in_may):
				if (day == 1 and date_day_of_week == sunday):
					count_of_sundays += 1

				if date_day_of_week != saturday:
					date_day_of_week += 1
				else:
					date_day_of_week = 0

		if month == june:
			for day in range(days_in_june):
				if (day == 1 and date_day_of_week == sunday):
					count_of_sundays += 1

				if date_day_of_week != saturday:
					date_day_of_week += 1
				else:
					date_day_of_week = 0

		if month == july:
			for day in range(days_in_july):
				if (day == 1 and date_day_of_week == sunday):
					count_of_sundays += 1

				if date_day_of_week != saturday:
					date_day_of_week += 1
				else:
					date_day_of_week = 0

		if month == august:
			for day in range(days_in_august):
				if (day == 1 and date_day_of_week == sunday):
					count_of_sundays += 1

				if date_day_of_week != saturday:
					date_day_of_week += 1
				else:
					date_day_of_week = 0

		if month == september:
			for day in range(days_in_september):
				if (day == 1 and date_day_of_week == sunday):
					count_of_sundays += 1

				if date_day_of_week != saturday:
					date_day_of_week += 1
				else:
					date_day_of_week = 0

		if month == october:
			for day in range(days_in_october):
				if (day == 1 and date_day_of_week == sunday):
					count_of_sundays += 1

				if date_day_of_week != saturday:
					date_day_of_week += 1
				else:
					date_day_of_week = 0

		if month == november:
			for day in range(days_in_november):
				if (day == 1 and date_day_of_week == sunday):
					count_of_sundays += 1

				if date_day_of_week != saturday:
					date_day_of_week += 1
				else:
					date_day_of_week = 0

		if month == december:
			for day in range(days_in_december):
				if (day == 1 and date_day_of_week == sunday):
					count_of_sundays += 1

				if date_day_of_week != saturday:
					date_day_of_week += 1
				else:
					date_day_of_week = 0

print count_of_sundays






