def handlelevel():
	saveData(save)
	if save["levelid"] == 0:
		beginning()
	elif save["levelid"] == 1:
		boss1()
	elif save["levelid"] == 2:
		boss2()
	elif save["levelid"] == 3:
		boss3()
	elif save["levelid"] == 4:
		boss4()
	elif save["levelid"] == 5:
		end()
handlelevel()
