with open('python_cheat_sheet.pdf',"rb") as binary_file:
	#Read the whole file at once
	data=binary_file.read()
	print(data)

	#Seek position and read N bytes
	binary_file.seek(0)
	couple_bytes=binary_file.read(2)
	print(couple_bytes)
