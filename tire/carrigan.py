from tire.tire import tire
class Carrigan(tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    
    def needs_service(self):
        for i in self.tire_wear:
			if i >= 0.9:
				return True
		return False
