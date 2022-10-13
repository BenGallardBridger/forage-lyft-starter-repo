from tire.tire import tire
class Octoprime(tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    
    def needs_service(self):
		total = 0
        for i in self.tire_wear:
			total += i
		if total >= 3:
			return True
		else:
			return False