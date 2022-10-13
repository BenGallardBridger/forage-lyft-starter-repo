from Battery import Battery
from datetime import datetime
class NubbinBattery(Engine):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return (self.current_date - self.last_service_date)/365.2425 >=2
