import os
from homeassistant_api import Client

class HA:
    def __init__(self, url, token):
        
        self.client = Client(url, token)
        
        self.light_service = self.client.get_domain("light")
        self.switch_service = self.client.get_domain("switch")
        
    def toggle(self, id):
        if id.startswith("light"):
            self.light_service.toggle(entity_id=id)
        elif id.startswith("switch"):
            self.switch_service.toggle(entity_id=id)
       
if __name__ == "__main__":
    ha = HA()
    ha.turn_off("light.family_room_dimmer")
