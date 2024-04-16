from lib.scraper import *
from lib.analyze import *
from lib.team_creator import *
from screens.team_maker_screen import *
import customtkinter

class MainApp:
    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.root = customtkinter.CTk(fg_color='#171721')

        # Set the window size
        window_width = 1000
        window_height = 800

        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate x and y coordinates
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # Set the geometry and center the window
        self.root.geometry(f'{window_width}x{window_height}+{x}+{y}')

        # Other configurations
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.resizable(False, False)
        self.root.bind("<Configure>", self.on_configure)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.title("Inhouse Team Creator")

        teamMaker = TeamMaker(self.root)

        self.team_maker_screen = teamMaker.setup_team_maker_screen(self.root)
        self.team_maker_screen.grid(row=0, column=0, sticky="nsew")

    def on_close(self):
        self.close_app()

    def close_app(self):
        self.root.destroy()
    
    def on_configure(self, event):
        if event.widget == self.root:
            time.sleep(0.01)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    # team1, team2 = form_random_teams()
    # team1, team2 = assign_champions(team1, team2)
    # print(team1)
    # print(team2)
    #write_all_roles_data()
    app = MainApp()
    app.run()