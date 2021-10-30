class Note:

	def init_from_str(string: str):
		params = string.split("&")
		date = params[3].split(".")
		return Note(params[1], params[0], params[2], date)

	def __init__(self, 
				surname: str, 
				name: str, 
				tel, 
				birth: list[int]) -> None:
		self.surname = surname.capitalize()
		self.name = name.capitalize()
		self.tel = tel
		self.birth = birth

	def __str__(self):
		return "{}&{}&{}&{}.{}.{}". \
			format(self.name, self.surname, self.tel, self.birth[0], self.birth[1], self.birth[2])

	def pretty(self):
		return "{} {} Phone: {} Date Of Birth: {}.{}.{}". \
			format(self.name, self.surname, self.tel, self.birth[0], self.birth[1], self.birth[2])

	def to_string(self):
		return self.__str__()

	def days_past(self):
		return int(self.birth[2]) * 365 + int(self.birth[1]) * 30 + int(self.birth[0])
