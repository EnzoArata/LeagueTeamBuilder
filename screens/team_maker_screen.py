import customtkinter
import requests
from PIL import Image
from io import BytesIO
from lib.team_creator import *
from lib.player_card import *

class TeamMaker:
    def __init__(self, root):
        self.root = root

    def define_grid(self, frame, columns, rows):
        for i in range(columns):
            frame.grid_columnconfigure(i, weight=1)
        for i in range(rows):
            frame.grid_rowconfigure(i, weight=1)

    def create_teams(self):
        players = self.get_players()
        if players:
            if self.current_mode == "summoners_rift":
                self.team1, self.team2 = form_random_teams(players)
        else:
            if self.current_mode == "summoners_rift":
                self.team1, self.team2 = form_random_teams()
        if self.current_mode == "summoners_rift":
            for count, player in enumerate(self.team1):
                self.summoners_rift_team1_player_names[count].configure(text=player)
            for count, player in enumerate(self.team2):
                self.summoners_rift_team2_player_names[count].configure(text=player)
            self.clear_player_cards()

    def clear_player_cards(self):
        for card in self.summoners_rift_player_cards:
            card.reset_card()
    
    def get_players(self):
        players = self.player_entry.get()
        split_list = players.split(",")
        return (split_list if len(split_list) > 1 else None)
    


    def setup_summoners_rift_screen(self):

        self.summoners_rift_frame = customtkinter.CTkFrame(master=self.master_frame,border_color="#6C6C87", border_width=2,)
        self.summoners_rift_frame.grid(row=2, column=0,rowspan=16, columnspan=20, sticky="nswe")
        self.define_grid(self.summoners_rift_frame, 1, 2)

        team_1_frame = customtkinter.CTkFrame(master=self.summoners_rift_frame, fg_color="#3f3f54", border_color="#6C6C87", border_width=2,)
        team_1_frame.grid(row=0, column=0, sticky="nsew", columnspan=1, rowspan=1)
        self.define_grid(team_1_frame, 10, 3)

        team1_top_frame = customtkinter.CTkFrame(master=team_1_frame, fg_color="#1f1f21", border_color="#6C6C87", border_width=2,)
        team1_top_frame.grid(row=0, column=0, sticky="nsew", columnspan=2, rowspan=3, pady=5, padx=4)
        team1_top_frame.grid_propagate(False)
        self.define_grid(team1_top_frame, 5, 20)

        team1_top_player_name = customtkinter.CTkLabel(master=team1_top_frame, text="Top", font=("Inter", 20, "bold"), text_color="#6C6C87")
        team1_top_player_name.grid(row=0, column=2, pady=[3,0], padx=5, sticky="n")

        team1_top_player_card = PlayerCard(team1_top_frame, "top", self.min_win_rate, self.max_win_rate, self.min_play_rate, self.max_play_rate)


        team1_jg_frame = customtkinter.CTkFrame(master=team_1_frame, fg_color="#1f1f21", border_color="#6C6C87", border_width=2,)
        team1_jg_frame.grid(row=0, column=2, sticky="nsew", columnspan=2, rowspan=3, pady=5, padx=4)
        team1_jg_frame.grid_propagate(False)
        self.define_grid(team1_jg_frame, 5, 20)

        team1_jg_player_name = customtkinter.CTkLabel(master=team1_jg_frame, text="Jungle", font=("Inter", 20, "bold"), text_color="#6C6C87")
        team1_jg_player_name.grid(row=0, column=2, pady=[3,0], padx=5, sticky="n")

        team1_jg_player_card = PlayerCard(team1_jg_frame, "jg", self.min_win_rate, self.max_win_rate, self.min_play_rate, self.max_play_rate)

        

        team1_mid_frame = customtkinter.CTkFrame(master=team_1_frame, fg_color="#1f1f21", border_color="#6C6C87", border_width=2,)
        team1_mid_frame.grid(row=0, column=4, sticky="nsew", columnspan=2, rowspan=3, pady=5, padx=4)
        team1_mid_frame.grid_propagate(False)
        self.define_grid(team1_mid_frame, 5, 20)

        team1_mid_player_name = customtkinter.CTkLabel(master=team1_mid_frame, text="Mid", font=("Inter", 20, "bold"), text_color="#6C6C87")
        team1_mid_player_name.grid(row=0, column=2, pady=[3,0], padx=5, sticky="n")

        team1_mid_player_card = PlayerCard(team1_mid_frame, "mid", self.min_win_rate, self.max_win_rate, self.min_play_rate, self.max_play_rate)

        team1_bot_frame = customtkinter.CTkFrame(master=team_1_frame, fg_color="#1f1f21", border_color="#6C6C87", border_width=2,)
        team1_bot_frame.grid(row=0, column=6, sticky="nsew", columnspan=2, rowspan=3, pady=5, padx=4)
        team1_bot_frame.grid_propagate(False)
        self.define_grid(team1_bot_frame, 5, 20)

        team1_bot_player_name = customtkinter.CTkLabel(master=team1_bot_frame, text="Bot", font=("Inter", 20, "bold"), text_color="#6C6C87")
        team1_bot_player_name.grid(row=0, column=2, pady=[3,0], padx=5, sticky="n")

        team1_bot_player_card = PlayerCard(team1_bot_frame, "bot", self.min_win_rate, self.max_win_rate, self.min_play_rate, self.max_play_rate)

        team1_sup_frame = customtkinter.CTkFrame(master=team_1_frame, fg_color="#1f1f21", border_color="#6C6C87", border_width=2,)
        team1_sup_frame.grid(row=0, column=8, sticky="nsew", columnspan=2, rowspan=3, pady=5, padx=4)
        team1_sup_frame.grid_propagate(False)
        self.define_grid(team1_sup_frame, 5, 20)

        team1_sup_player_name = customtkinter.CTkLabel(master=team1_sup_frame, text="Support", font=("Inter", 20, "bold"), text_color="#6C6C87")
        team1_sup_player_name.grid(row=0, column=2, pady=[3,0], padx=5, sticky="n")

        team1_sup_player_card = PlayerCard(team1_sup_frame, "sup", self.min_win_rate, self.max_win_rate, self.min_play_rate, self.max_play_rate)

        ############################################################################################

        team_2_frame = customtkinter.CTkFrame(master=self.summoners_rift_frame, fg_color="#3f3f54", border_color="#6C6C87", border_width=2,)
        team_2_frame.grid(row=1, column=0, sticky="nsew", columnspan=1, rowspan=1)
        self.define_grid(team_2_frame, 10, 3)

        team2_top_frame = customtkinter.CTkFrame(master=team_2_frame, fg_color="#1f1f21", border_color="#6C6C87", border_width=2,)
        team2_top_frame.grid(row=0, column=0, sticky="nsew", columnspan=2, rowspan=3, pady=5, padx=4)
        team2_top_frame.grid_propagate(False)
        self.define_grid(team2_top_frame, 5, 20)

        team2_top_player_name = customtkinter.CTkLabel(master=team2_top_frame, text="Top", font=("Inter", 20, "bold"), text_color="#6C6C87")
        team2_top_player_name.grid(row=0, column=2, pady=[3,0], padx=5, sticky="n")

        team2_top_player_card = PlayerCard(team2_top_frame, "top", self.min_win_rate, self.max_win_rate, self.min_play_rate, self.max_play_rate)


        team2_jg_frame = customtkinter.CTkFrame(master=team_2_frame, fg_color="#1f1f21", border_color="#6C6C87", border_width=2,)
        team2_jg_frame.grid(row=0, column=2, sticky="nsew", columnspan=2, rowspan=3, pady=5, padx=4)
        team2_jg_frame.grid_propagate(False)
        self.define_grid(team2_jg_frame, 5, 20)

        team2_jg_player_name = customtkinter.CTkLabel(master=team2_jg_frame, text="Jungle", font=("Inter", 20, "bold"), text_color="#6C6C87")
        team2_jg_player_name.grid(row=0, column=2, pady=[3,0], padx=5, sticky="n")

        team2_jg_player_card = PlayerCard(team2_jg_frame, "jg", self.min_win_rate, self.max_win_rate, self.min_play_rate, self.max_play_rate)

        team2_mid_frame = customtkinter.CTkFrame(master=team_2_frame, fg_color="#1f1f21", border_color="#6C6C87", border_width=2,)
        team2_mid_frame.grid(row=0, column=4, sticky="nsew", columnspan=2, rowspan=3, pady=5, padx=4)
        team2_mid_frame.grid_propagate(False)
        self.define_grid(team2_mid_frame, 5, 20)

        team2_mid_player_name = customtkinter.CTkLabel(master=team2_mid_frame, text="Mid", font=("Inter", 20, "bold"), text_color="#6C6C87")
        team2_mid_player_name.grid(row=0, column=2, pady=[3,0], padx=5, sticky="n")

        team2_mid_player_card = PlayerCard(team2_mid_frame, "mid", self.min_win_rate, self.max_win_rate, self.min_play_rate, self.max_play_rate)

        team2_bot_frame = customtkinter.CTkFrame(master=team_2_frame, fg_color="#1f1f21", border_color="#6C6C87", border_width=2,)
        team2_bot_frame.grid(row=0, column=6, sticky="nsew", columnspan=2, rowspan=3, pady=5, padx=4)
        team2_bot_frame.grid_propagate(False)
        self.define_grid(team2_bot_frame, 5, 20)

        team2_bot_player_name = customtkinter.CTkLabel(master=team2_bot_frame, text="Bot", font=("Inter", 20, "bold"), text_color="#6C6C87")
        team2_bot_player_name.grid(row=0, column=2, pady=[3,0], padx=5, sticky="n")

        team2_bot_player_card = PlayerCard(team2_bot_frame, "bot", self.min_win_rate, self.max_win_rate, self.min_play_rate, self.max_play_rate)

        team2_sup_frame = customtkinter.CTkFrame(master=team_2_frame, fg_color="#1f1f21", border_color="#6C6C87", border_width=2,)
        team2_sup_frame.grid(row=0, column=8, sticky="nsew", columnspan=2, rowspan=3, pady=5, padx=4)
        team2_sup_frame.grid_propagate(False)
        self.define_grid(team2_sup_frame, 5, 20)

        team2_sup_player_name = customtkinter.CTkLabel(master=team2_sup_frame, text="Support", font=("Inter", 20, "bold"), text_color="#6C6C87")
        team2_sup_player_name.grid(row=0, column=2, pady=[3,0], padx=5, sticky="n")

        team2_sup_player_card = PlayerCard(team2_sup_frame, "sup", self.min_win_rate, self.max_win_rate, self.min_play_rate, self.max_play_rate)


        self.summoners_rift_team1_player_names = [team1_top_player_name, team1_jg_player_name, team1_mid_player_name, team1_bot_player_name, team1_sup_player_name]
        self.summoners_rift_team2_player_names = [team2_top_player_name, team2_jg_player_name, team2_mid_player_name, team2_bot_player_name, team2_sup_player_name]


        self.summoners_rift_player_cards = [team1_top_player_card, team1_jg_player_card, team1_mid_player_card, team1_bot_player_card, team1_sup_player_card,
                             team2_top_player_card, team2_jg_player_card, team2_mid_player_card, team2_bot_player_card, team2_sup_player_card]
        
    def setup_arena_screen(self):    
        self.arena_frame = customtkinter.CTkFrame(master=self.master_frame,border_color="#6C6C87", border_width=2,)
        self.arena_frame.grid(row=2, column=0,rowspan=16, columnspan=20, sticky="nswe")
        self.define_grid(self.arena_frame, 2, 2)


        ###########################################################################################################################
        team_1_frame = customtkinter.CTkFrame(master=self.arena_frame, fg_color="#3f3f54", border_color="#6C6C87", border_width=2,)
        team_1_frame.grid(row=0, column=0, sticky="nsew", columnspan=1, rowspan=1)
        self.define_grid(team_1_frame, 10, 3)

        team_1_player_1_frame = customtkinter.CTkFrame(master=team_1_frame, fg_color="#1f1f21", border_color="#6C6C87", border_width=2,)
        team_1_player_1_frame.grid(row=0, column=0, sticky="nsew", columnspan=2, rowspan=3, pady=5, padx=4)
        team_1_player_1_frame.grid_propagate(False)
        self.define_grid(team_1_player_1_frame, 5, 20)

        team_1_player_1_name = customtkinter.CTkLabel(master=team_1_player_1_frame, text="Player 1", font=("Inter", 20, "bold"), text_color="#6C6C87")
        team_1_player_1_name.grid(row=0, column=2, pady=[3,0], padx=5, sticky="n")

        team_1_player_1_card = PlayerCard(team_1_player_1_frame, "top", self.min_win_rate, self.max_win_rate, self.min_play_rate, self.max_play_rate)


        team_1_player_2_frame = customtkinter.CTkFrame(master=team_1_frame, fg_color="#1f1f21", border_color="#6C6C87", border_width=2,)
        team_1_player_2_frame.grid(row=0, column=2, sticky="nsew", columnspan=2, rowspan=3, pady=5, padx=4)
        team_1_player_2_frame.grid_propagate(False)
        self.define_grid(team_1_player_2_frame, 5, 20)

        team_1_player_2_name = customtkinter.CTkLabel(master=team_1_player_2_frame, text="Player 2", font=("Inter", 20, "bold"), text_color="#6C6C87")
        team_1_player_2_name.grid(row=0, column=2, pady=[3,0], padx=5, sticky="n")

        team_1_player_2_card = PlayerCard(team_1_player_2_frame, "top", self.min_win_rate, self.max_win_rate, self.min_play_rate, self.max_play_rate)

        ###########################################################################################################################
        team_2_frame = customtkinter.CTkFrame(master=self.arena_frame, fg_color="#3f3f54", border_color="#6C6C87", border_width=2,)
        team_2_frame.grid(row=0, column=1, sticky="nsew", columnspan=1, rowspan=1)
        self.define_grid(team_2_frame, 10, 3)

        team_2_player_1_frame = customtkinter.CTkFrame(master=team_2_frame, fg_color="#1f1f21", border_color="#6C6C87", border_width=2,)
        team_2_player_1_frame.grid(row=0, column=0, sticky="nsew", columnspan=2, rowspan=3, pady=5, padx=4)
        team_2_player_1_frame.grid_propagate(False)
        self.define_grid(team_2_player_1_frame, 5, 20)

        team_2_player_1_name = customtkinter.CTkLabel(master=team_2_player_1_frame, text="Player 1", font=("Inter", 20, "bold"), text_color="#6C6C87")
        team_2_player_1_name.grid(row=0, column=2, pady=[3,0], padx=5, sticky="n")

        team_2_player_1_card = PlayerCard(team_2_player_1_frame, "top", self.min_win_rate, self.max_win_rate, self.min_play_rate, self.max_play_rate)


        team_2_player_2_frame = customtkinter.CTkFrame(master=team_2_frame, fg_color="#1f1f21", border_color="#6C6C87", border_width=2,)
        team_2_player_2_frame.grid(row=0, column=2, sticky="nsew", columnspan=2, rowspan=3, pady=5, padx=4)
        team_2_player_2_frame.grid_propagate(False)
        self.define_grid(team_2_player_2_frame, 5, 20)

        team_2_player_2_name = customtkinter.CTkLabel(master=team_2_player_2_frame, text="Player 2", font=("Inter", 20, "bold"), text_color="#6C6C87")
        team_2_player_2_name.grid(row=0, column=2, pady=[3,0], padx=5, sticky="n")

        team1_player_2_card = PlayerCard(team_2_player_2_frame, "top", self.min_win_rate, self.max_win_rate, self.min_play_rate, self.max_play_rate)

        ###########################################################################################################################
        team_3_frame = customtkinter.CTkFrame(master=self.arena_frame, fg_color="#3f3f54", border_color="#6C6C87", border_width=2,)
        team_3_frame.grid(row=1, column=0, sticky="nsew", columnspan=1, rowspan=1)
        self.define_grid(team_3_frame, 10, 3)

        team_3_player_1_frame = customtkinter.CTkFrame(master=team_3_frame, fg_color="#1f1f21", border_color="#6C6C87", border_width=2,)
        team_3_player_1_frame.grid(row=0, column=0, sticky="nsew", columnspan=2, rowspan=3, pady=5, padx=4)
        team_3_player_1_frame.grid_propagate(False)
        self.define_grid(team_3_player_1_frame, 5, 20)

        team_3_player_1_name = customtkinter.CTkLabel(master=team_3_player_1_frame, text="Player 1", font=("Inter", 20, "bold"), text_color="#6C6C87")
        team_3_player_1_name.grid(row=0, column=2, pady=[3,0], padx=5, sticky="n")

        team_3_player_1_card = PlayerCard(team_3_player_1_frame, "top", self.min_win_rate, self.max_win_rate, self.min_play_rate, self.max_play_rate)


        team_3_player_2_frame = customtkinter.CTkFrame(master=team_3_frame, fg_color="#1f1f21", border_color="#6C6C87", border_width=2,)
        team_3_player_2_frame.grid(row=0, column=2, sticky="nsew", columnspan=2, rowspan=3, pady=5, padx=4)
        team_3_player_2_frame.grid_propagate(False)
        self.define_grid(team_3_player_2_frame, 5, 20)

        team_3_player_2_name = customtkinter.CTkLabel(master=team_3_player_2_frame, text="Player 2", font=("Inter", 20, "bold"), text_color="#6C6C87")
        team_3_player_2_name.grid(row=0, column=2, pady=[3,0], padx=5, sticky="n")

        team_3_player_2_card = PlayerCard(team_3_player_2_frame, "top", self.min_win_rate, self.max_win_rate, self.min_play_rate, self.max_play_rate)

        ###########################################################################################################################
        team_4_frame = customtkinter.CTkFrame(master=self.arena_frame, fg_color="#3f3f54", border_color="#6C6C87", border_width=2,)
        team_4_frame.grid(row=1, column=1, sticky="nsew", columnspan=1, rowspan=1)
        self.define_grid(team_4_frame, 10, 3)

        team_4_player_1_frame = customtkinter.CTkFrame(master=team_4_frame, fg_color="#1f1f21", border_color="#6C6C87", border_width=2,)
        team_4_player_1_frame.grid(row=0, column=0, sticky="nsew", columnspan=2, rowspan=3, pady=5, padx=4)
        team_4_player_1_frame.grid_propagate(False)
        self.define_grid(team_4_player_1_frame, 5, 20)

        team_4_player_1_name = customtkinter.CTkLabel(master=team_4_player_1_frame, text="Player 1", font=("Inter", 20, "bold"), text_color="#6C6C87")
        team_4_player_1_name.grid(row=0, column=2, pady=[3,0], padx=5, sticky="n")

        team_4_player_1_card = PlayerCard(team_4_player_1_frame, "top", self.min_win_rate, self.max_win_rate, self.min_play_rate, self.max_play_rate)


        team_4_player_2_frame = customtkinter.CTkFrame(master=team_4_frame, fg_color="#1f1f21", border_color="#6C6C87", border_width=2,)
        team_4_player_2_frame.grid(row=0, column=2, sticky="nsew", columnspan=2, rowspan=3, pady=5, padx=4)
        team_4_player_2_frame.grid_propagate(False)
        self.define_grid(team_4_player_2_frame, 5, 20)

        team_4_player_2_name = customtkinter.CTkLabel(master=team_4_player_2_frame, text="Player 2", font=("Inter", 20, "bold"), text_color="#6C6C87")
        team_4_player_2_name.grid(row=0, column=2, pady=[3,0], padx=5, sticky="n")

        team1_player_2_card = PlayerCard(team_4_player_2_frame, "top", self.min_win_rate, self.max_win_rate, self.min_play_rate, self.max_play_rate)

        

        

    def enable_summoners_rift_mode(self):
        if self.current_mode != "summoners_rift":
            self.current_mode = "summoners_rift"
            self.summoners_rift_button.configure(fg_color="#04DA8B")
            self.arena_button.configure(fg_color="#303332")
            self.reset_screen()

    def enable_arena_mode(self):
        if self.current_mode != "arena":
            self.current_mode = "arena"
            self.summoners_rift_button.configure(fg_color="#303332")
            self.arena_button.configure(fg_color="#04DA8B")
            self.reset_screen()

    def reset_screen(self):
        if self.current_mode == "arena":
            self.summoners_rift_frame.grid_forget()
            self.arena_frame.grid(row=2, column=0,rowspan=16, columnspan=20, sticky="nswe")
        if self.current_mode == "summoners_rift":
            self.arena_frame.grid_forget()
            self.summoners_rift_frame.grid(row=2, column=0,rowspan=16, columnspan=20, sticky="nswe")
        
    def setup_team_maker_screen(self, root):
        self.master_frame = customtkinter.CTkFrame(master=root, fg_color="#171721")
        self.master_frame.grid(row=0, column=0, pady=0, padx=0, sticky="nsew")
        self.master_frame.grid_propagate(False)
        self.define_grid(self.master_frame, 20, 20)


        self.player_entry = customtkinter.CTkEntry(master=self.master_frame, placeholder_text="Enter Player Names, seperated by columns", 
                                            font=("Inter", 16, "bold"), placeholder_text_color="#6C6C87", text_color='#FFFFFF', 
                                            height=44, width=700, border_color="#6C6C87", border_width=2, fg_color="#1D1D2C", )
        self.player_entry.grid(row=0, column=0, pady=[0,5], padx=12, columnspan=1,)
        self.player_entry.bind("<Return>", lambda event=None: self.create_teams())

        self.randomize_team_button = customtkinter.CTkButton(master=self.master_frame, text="Randomize Teams", font=("Inter", 16, "bold"),
                                        command=self.create_teams, fg_color="#04DA8B", text_color="#FFFFFF", height=45, width=250 )
        self.randomize_team_button.grid(row=0, column=1, pady=5, padx=12, columnspan=1)

                #####################################################################################################################

        settings_frame = customtkinter.CTkFrame(master=self.master_frame, fg_color="#323259", border_color="#6C6C87", border_width=2,
                                             height=70,width=350)
        settings_frame.grid(row=1, column=0, sticky="nsew", columnspan=2, rowspan=1, pady=3)
        #settings_frame.grid_propagate(False)
        self.define_grid(settings_frame, 10, 1)

        win_rate_label = customtkinter.CTkLabel(master=settings_frame, text="Settings", font=("Inter", 18, "bold"),
                                              text_color="#a1a1b3", height=5)
        win_rate_label.grid(row=0, column=0, pady=[0,0], padx=0,)

        min_win_label = customtkinter.CTkLabel(master=settings_frame, text="Win Rate Min", font=("Inter", 14, "bold"),
                                              text_color="#a1a1b3", height=5)
        min_win_label.grid(row=0, column=1, pady=[0,0], padx=2, stick="e")

        self.min_win_rate = customtkinter.CTkEntry(master=settings_frame, font=("Inter", 14, "bold"), text_color="#a1a1b3",
                                                    height=5, width=40)
        self.min_win_rate.grid(row=0, column=2, stick="w")
        self.min_win_rate.insert(0, "40")

        max_win_label = customtkinter.CTkLabel(master=settings_frame, text="Win Rate Max", font=("Inter", 14, "bold"),
                                              text_color="#a1a1b3", height=5)
        max_win_label.grid(row=0, column=3, pady=[0,0], padx=2, stick="e")

        self.max_win_rate = customtkinter.CTkEntry(master=settings_frame, font=("Inter", 14, "bold"), text_color="#a1a1b3",
                                                    height=5, width=40)
        self.max_win_rate.grid(row=0, column=4, stick="w")
        self.max_win_rate.insert(0, "60")

        min_play_label = customtkinter.CTkLabel(master=settings_frame, text="Play Rate Min", font=("Inter", 14, "bold"),
                                              text_color="#a1a1b3", height=5)
        min_play_label.grid(row=0, column=6, pady=[0,0], padx=2, stick="e")

        self.min_play_rate = customtkinter.CTkEntry(master=settings_frame, font=("Inter", 14, "bold"), text_color="#a1a1b3",
                                                    height=5, width=40)
        self.min_play_rate.grid(row=0, column=7, stick="w")
        self.min_play_rate.insert(0, "0.00")

        max_play_label = customtkinter.CTkLabel(master=settings_frame, text="Play Rate Max", font=("Inter", 14, "bold"),
                                              text_color="#a1a1b3", height=5)
        max_play_label.grid(row=0, column=8, pady=[0,0], padx=2, stick="e")
        

        self.max_play_rate = customtkinter.CTkEntry(master=settings_frame, font=("Inter", 14, "bold"), text_color="#a1a1b3",
                                                    height=5, width=40)
        self.max_play_rate.grid(row=0, column=9, stick="w")
        self.max_play_rate.insert(0, "25.00")

        #####################################################################################################################

        mode_button_frame = customtkinter.CTkFrame(master=self.master_frame, fg_color="#171721", 
                                                   border_color="#6C6C87", border_width=2, height=60)
        mode_button_frame.grid_propagate(False)
        mode_button_frame.grid(row=20, column=0, columnspan=1, rowspan=1, sticky="nsew")
        self.define_grid(mode_button_frame, 2, 1)

        self.summoners_rift_button = customtkinter.CTkButton(master=mode_button_frame, text="Summoners Rift", font=("Inter", 16, "bold"),
                                        command=self.enable_summoners_rift_mode, fg_color="#04DA8B", text_color="#FFFFFF", height=45, width=150 )
        self.summoners_rift_button.grid(row=0, column=0, pady=2, padx=2, columnspan=1)

        self.arena_button = customtkinter.CTkButton(master=mode_button_frame, text="Arena", font=("Inter", 16, "bold"),
                                        command=self.enable_arena_mode, fg_color="#303332", text_color="#FFFFFF", height=45, width=150 )
        self.arena_button.grid(row=0, column=1, pady=2, padx=2, columnspan=1)
        


        patch_label = customtkinter.CTkLabel(master=self.master_frame, text="-- Patch 14.07 --  4/16/2024  -- Enzo Arata --",
                                              font=("Inter", 12, "bold"), text_color="#6C6C87", width = 500)
        patch_label.grid(row=20, column=1, pady=[0,0], padx=5, sticky="nesw")

        self.setup_summoners_rift_screen()
        self.setup_arena_screen()
        self.current_mode = "summoners_rift"
        self.reset_screen()
        return self.master_frame