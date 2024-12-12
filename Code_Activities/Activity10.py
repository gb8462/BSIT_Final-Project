def act10():
    QDll = input("Are you a student of DLL? (Yes/No): ")

    if QDll.lower() == "yes":
    	print("Welcome Student of DLL :D")
    	lucena = input("are you from Lucena? (Yes/No): ")
    	if lucena.lower() == "yes":
    		print("Please Fillup this current form!")
    		level = input("what is your current year level in DLL:\nF-freshmen\nS-sophomore\nJ-junior\nR-senior\n Please Fillup this needed form: ")
    		if level.lower() == "f":
    			print("Hello Freshmen!")
    		elif level.lower() == "s":
    			print("Hello Sophomore!")
    		elif level.lower() == "j":
    			print("Hello Junior!")
    		elif level.lower() == "r":
    			print("hello Senior!")
    		else:
    			print("Invalid Input!")
    		scholar = input("Do you need this scholarship?(yes/no): ")
    		if scholar.lower() == "yes":
    			print("Scholarship Granted!")
    		else:
    			print("Okay")
    	else:
    		print("okay!")
    else:
    	print("okay have a nice day Adios!")