from tkinter import *
from HA import HA
import json
from math import ceil, floor, sqrt


class TkHA:
    def __init__(self, config_json_file, full_screen = False):
        config = json.load(open(config_json_file))
        self._ha = HA(config["url"], config["token"])

        # Build frame
        self.tk = Tk()
        self.tk.attributes("-fullscreen", config['fullScreen'])
        self.tk.geometry(config['resolution'])

        buttons = config["buttons"]
        
        num_cols = ceil(sqrt(len(buttons)))
        num_rows = ceil(len(buttons) / num_cols)

        self.tk.columnconfigure(tuple(range(num_cols)), weight=1)
        self.tk.rowconfigure(tuple(range(num_rows)), weight=1)
        
        for col in range(num_cols):
            for row in range(num_rows):
                idx = col + row*num_cols
                if (idx < len(buttons)):
                    button = buttons[idx]
                    btn = Button(text=button["name"], command=lambda light_entites = button["light_entities"]: self.toggle_lights(light_entites))
                    btn.grid(column=col,row=row,sticky="EWNS")
                else:
                    btn = Button(text = "empty")
                    btn.config(state="disabled")

    def toggle_lights(self, entity_ids):
        for entity_id in entity_ids:
            self._ha.toggle(entity_id)

if __name__ == "__main__":
    tkha_window = TkHA("config.json")
    tkha_window.tk.mainloop()
