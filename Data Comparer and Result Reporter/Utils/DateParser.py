class DateParser:

	@staticmethod	
	def breakdown(name):
		l= [4,7,10,13,16,20]
		for i in l:
			if i in [4,7]:
				name = name[:i] + "-" + name[i:]
			if i ==10:
				name = name[:i] + " " + name[i:]
			if i in [13,16]:
				name = name[:i] + ":" + name[i:]
			if i == 20:
				name = name[:i] + "." + name[i:]
		return name

	@staticmethod
	def getDates(name):
		under =0
		end = ""
		start =""
		tabName = ""		
		for char in name:
			if char == '_':
				under+=1
			if under == 0:
				tabName +=char
			if under == 3:
				end += char
			if under == 4:
				start+=char
		#print(start[1:])
		#print(end[1:])
		start = start[1:]
		end = end[1:]
		if len(start) == 20:
			start += '000'
		return tabName,DateParser.breakdown(start),DateParser.breakdown(end)