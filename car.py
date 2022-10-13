class Car():
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    
    def needs_service(self):
        return engine.needs_service() or battery.needs_service()
