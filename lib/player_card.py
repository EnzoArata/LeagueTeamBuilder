import customtkinter
import requests
from PIL import Image
from io import BytesIO
from lib.team_creator import *
from lib.util import *


class PlayerCard:
    def __init__(self, master_frame, role):
        self.role = role
        self.wacky_enabled = False
        self.wacky_value = 0
        self.champ_image = customtkinter.CTkImage(Image.open(os.path.join(SCRIPT_DIR, "blank.png")), size=(100,100))
        
        self.champ_image_label = customtkinter.CTkLabel(master=master_frame, text="", image=self.champ_image, height=1, )
        self.champ_image_label.grid(row=1, column=0, pady=0, padx=5, columnspan=5, rowspan=5, sticky="nesw")

        self.champ_name = customtkinter.CTkLabel(master=master_frame, text="-", font=("Inter", 20, "bold"), text_color="#6C6C87",
                                                    height=20, width=150)
        self.champ_name.grid(row=6, column=2, pady=[3,0], padx=5, sticky="n")

        self.win_rate = customtkinter.CTkLabel(master=master_frame, text="-", font=("Inter", 18, "bold"), text_color="#6C6C87",
                                                    height=20, width=60)
        self.win_rate.grid(row=7, column=2, pady=[3,0], padx=5, sticky="n")

        self.pick_rate = customtkinter.CTkLabel(master=master_frame, text="-", font=("Inter", 14, "bold"), text_color="#6C6C87",
                                                    height=10, width=10)
        self.pick_rate.grid(row=10, column=2, pady=[1,0], padx=3, sticky="n",)

        # self.ban_rate = customtkinter.CTkLabel(master=master_frame, text="-", font=("Inter", 14, "bold"), text_color="#6C6C87",
        #                                             height=10, width=10)
        # self.ban_rate.grid(row=10, column=3, pady=[1,0], padx=3, sticky="n", columnspan=2)

        self.pick_champ_button = customtkinter.CTkButton(master=master_frame, text="Roll", font=("Inter", 16, "bold"),
                                         command=self.roll_champ, fg_color="#3b0c0f", text_color="#FFFFFF", height=40, width=40 )
        self.pick_champ_button.grid(row=18, column=2, pady=5, padx=12, columnspan=1)

    
    def roll_champ(self):
        def update_label_color(val):
            val_float = float(val)
            if val_float > 50:
                green_intensity = max(255 - int(255 * (val_float - 50) / 50) ** 2, 0)  # Ensure intensity is within valid range
                return f"#20b3{green_intensity:02x}"
            else:
                red_intensity = max(255 - int(255 * (50 - val_float) / 50) ** 2, 0)  # Ensure intensity is within valid range
            return f"#c9{red_intensity:02x}21"
        if self.wacky_enabled:
            champion = pick_random_champ(self.role, self.wacky_value)
        else:
            champion = pick_random_champ(self.role)
        #print(champion)
        self.champ_name.configure(text = champion['name'])
        self.win_rate.configure(text = "WR " +champion['winrate'] + "%", text_color = update_label_color(champion['winrate']))
        self.pick_rate.configure(text = "PR " +champion['pick_rate'])
        #self.ban_rate.configure(text = "BR " +champion['ban_rate'])
        url = champion['img_src']
        response = requests.get(url)
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        new_champ_image = customtkinter.CTkImage(image, size=(100,100))
        self.champ_image_label.configure(image=new_champ_image)

    def reset_card(self):
        self.champ_name.configure(text = "-")
        self.win_rate.configure(text = "-")
        self.pick_rate.configure(text = "-")
        self.champ_image_label.configure(image=self.champ_image)