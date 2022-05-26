import time
import random
from Model.Aircraft import Aircraft

class Glider(Aircraft):

    def __init__(self, model, registration, cockpit_crew, length, height, MTOW,
    OEW, wingspan, range, cruise_speed, cruise_altitude,
    engines, last_maintnance_date, flying_hours, is_active, owner, launch_type) -> None:
        super().__init__(model, registration, cockpit_crew, length, height, MTOW,
        OEW, wingspan, 0, range, cruise_speed, cruise_altitude,
        engines, last_maintnance_date, flying_hours, 0,
        0, 0, is_active, owner)
        self.launch_type = launch_type
        

    def __str__(self) -> str:
        return f"""Aircraft {self.model} with registration {self.registration} specifications:
Cockpit crew: {self.cockpit_crew}
Length: {self.length}m
Height: {self.height}m
MTOW(Maximum TakeOff Weight): {self.MTOW}kg
OEW(Operating Empty Weight): {self.OEW}kg
Wingspan: {self.wingspan}m
Fuel capacity: {self.fuel_capacity}l
Range: {self.range}km
Cruise speed: {self.cruise_speed}km/h
Cruise altitude: {self.cruise_altitude}ft
Engines: {self.engines}
Last maintnance date: {self.last_maintnance_date}
Total hours flown: {self.flying_hours}h
Fuel burn per hour: {self.fuel_burn_per_hour}kgs
Owner: {self.owner} 
Launch type: {self.launch_type} 
"""


    def fly(self, origin, destination, distance):
        if self.is_active:
                print(f"Glider {self.model} with registration {self.registration} is taking off from {origin} \n")

                if random.random() > 0.99995:
                    print(f"Glider {self.model} with registration {self.registration} has crashed \n Reason: Unknown")
                    self.is_active = False
                else:
                    for i in range(5):
                        time.sleep(1)
                        print(". . . ")
                    print("\n")
                    
                    print(f"Glider {self.model} with registration {self.registration} landed in {destination} \n")
        else:
            raise Exception("The airframe is not active")    


    def refuel(self):
        raise Exception("There's no need to refuel a glider")

