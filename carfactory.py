from datetime import datetime
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.SpindlerBattery import SpindlerBattery
from battery.NubbinBattery import NubbinBattery


class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        calliope_Engine = CapuletEngine(current_mileage, last_service_mileage)
        calliope_Battery = SpindlerBattery(current_date, last_service_date)
        return Car(calliope_Engine,calliope_Battery)
        
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        glissade_Engine = WilloughbyEngine(current_mileage, last_service_mileage)
        glissade_Battery = SpindlerBattery(current_date, last_service_date)
        return Car(glissade_Engine,glissade_Battery)
        
    def create_palindrome(current_date, last_service_date, warning_light_on):
        palindrome_Engine = SternmanEngine(warning_light_on)
        palindrome_Battery = SpindlerBattery(current_date, last_service_date)
        return Car(palindrome_Engine,palindrome_Battery)
        
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        rorschach_Engine = WilloughbyEngine(current_mileage, last_service_mileage)
        rorschach_Battery = NubbinBattery(current_date, last_service_date)
        return Car(rorschach_Engine,rorschach_Battery)
        
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        thovex_Engine = CapuletEngine(current_mileage, last_service_mileage)
        thovex_Battery = NubbinBattery(current_date, last_service_date)
        return Car(thovex_Engine,thovex_Battery) 