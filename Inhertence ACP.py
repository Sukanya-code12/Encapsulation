class vehicle:
    def __init__(self):
        print("Vehicle is ready")
    def name(self):
        print("Vehicle")
class bus(vehicle):
    def __init__(self):
        super().__init__()
        print("Bus is ready")
    def name(self):
        print("Bus")
Bus= bus()
Bus.name