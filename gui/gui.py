import tkinter
import tkinter.messagebox
import tkinter.ttk
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: "blue" (standard), "green", "dark-blue"


class Sidebar(customtkinter.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # create sidebar widgets
        self.logo_label = customtkinter.CTkLabel(
            self,
            text="Automação OLX",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.appearance_mode_label = customtkinter.CTkLabel(
            self, text="Modo:", anchor="w"
        )
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            self,
            values=["Light", "Dark"],
            command=self.master.change_appearance_mode_event,
        )
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(
            self, text="UI Scaling:", anchor="w"
        )
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(
            self,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.master.change_scaling_event,
        )
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Automação de Busca de Carros na OLX")
        self.geometry(f"{1100}x{380}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar
        self.sidebar = Sidebar(self, width=140, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")

        # # create main entry and button
        # self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        # self.entry.grid(
        #     row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew"
        # )

        self.main_button_1 = customtkinter.CTkButton(
            master=self,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            text="Buscar"
        )
        self.main_button_1.grid(
            row=3, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew"
        )

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.tabview.add("Opções")
        self.tabview.add("Opções Avançadas")
        self.tabview.tab("Opções").grid_columnconfigure(
            0, weight=1
        )  # configure grid of individual tabs
        self.tabview.tab("Opções Avançadas").grid_columnconfigure(0, weight=1)

        self.optionmenu_frame = customtkinter.CTkFrame(self.tabview.tab("Opções"))
        self.optionmenu_frame.grid(row=0, column=0, padx=20, pady=(20, 10))

        # self.optionmenu_scrollbar = tkinter.Scrollbar(self.optionmenu_frame, orient=tkinter.VERTICAL)
        # self.optionmenu_scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.optionmenu_1 = tkinter.ttk.Combobox(
            self.optionmenu_frame,
            values=[
                "ACURA",
                "AGRALE",
                "ALFA ROMEO",
                "AM GEN",
                "AMERICAR",
                "ASIA MOTORS",
                "ASTON MARTIN",
                "AUDI",
                "BABY",
                "BENTLEY",
                "BMW",
                "BRM",
                "BUGGY",
                "BUGRE",
                "BYD",
                "CAB MOTORS",
                "CADILLAC",
                "CBT JIPE",
                "CHANA",
                "CHANGAN",
                "CHERY",
                "CHEVROLET",
                "CHRYSLER",
                "CITROEN",
                "CROSS LANDER",
                "D4D",
                "DACON",
                "DAEWOO",
                "DAIHATSU",
                "DFSK",
                "DKW VEMAG",
                "DODGE",
                "EFFA",
                "ENGESA",
                "ENVEMO",
                "FERRARI",
                "FIAT",
                "FIBRAVAN",
                "FORD",
                "FOTON",
                "FYBER",
                "GEELY",
                "GREAT WALL",
                "GURGEL",
                "GWM",
                "HAFEI",
                "HITECH ELETRIC",
                "HONDA",
                "HYUNDAI",
                "INFINITI",
                "ISUZU",
                "IVECO",
                "JAC",
                "JAGUAR",
                "JEEP",
                "JINBEI",
                "JPX",
                "KIA MOTORS",
                "LADA",
                "LAMBORGHINI",
                "LAND ROVER",
                "LANDWIND",
                "LEXUS",
                "LIFAN",
                "LOBINI",
                "LOTUS",
                "MAHINDRA",
                "MASERATI",
                "MATRA",
                "MAZDA",
                "MCLAREN",
                "MERCEDES-BENZ",
                "MERCURY",
                "MG",
                "MINI",
                "MITSUBISHI",
                "MIURA",
                "MON",
                "MP LAFER",
                "NISSAN",
                "PEUGEOT",
                "PLYMOUTH",
                "PONTIAC",
                "PORSCHE",
                "PUMA",
                "RAM",
                "RELY",
                "RENAULT",
                "RIVIAN",
                "ROLLS-ROYCE",
                "ROVER",
                "SAAB",
                "SATURN",
                "SEAT",
                "SERES",
                "SHINERAY",
                "SMART",
                "SSANGYONG",
                "SUBARU",
                "SUNBEAM TALBOT",
                "SUZUKI",
                "SWELL MINI VEICULOS",
                "TAC",
                "TESLA",
                "TOYOTA",
                "TROLLER",
                "VENTURA",
                "VOLKSWAGEN",
                "VOLVO",
                "WAKE",
                "WALK",
                "WILLYS OVERLAND",
            ],
        )

        # self.optionmenu_1.pack()
        self.optionmenu_1.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

        self.combobox_1 = customtkinter.CTkComboBox(
            self.tabview.tab("Opções"),
            values=["Value 1", "Value 2", "Value Long....."],
        )
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.string_input_button = customtkinter.CTkButton(
            self.tabview.tab("Opções"),
            text="Open CTkInputDialog",
            command=self.open_input_dialog_event,
        )
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.label_tab_2 = customtkinter.CTkLabel(
            self.tabview.tab("Opções Avançadas"), text="CTkLabel on Opções Avançadas"
        )
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # set default values
        self.sidebar.appearance_mode_optionemenu.set("Dark")
        self.sidebar.scaling_optionemenu.set("100%")
        self.optionmenu_1.set("Marca")
        self.combobox_1.set("CTkComboBox")
        self.textbox.insert(
            "0.0",
            "Automação OLX\n\n"
            + "ANTES DE INICIAR SUA BUSCA, FAÇA O LOGIN COM SUA CONTA NOS SITES DA OLX E DO WHATSAPP!.\n\n"
            + "Bem-vindo ao mecanismo automático de busca de carros. Aqui facilitaremos seu trabalho enviando mensagens automáticas pelo WhatsApp para os vendedores da OLX que se adequem aos campos a serem selecionados por você.\n\n",
        )

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(
            text="Type in a number:", title="CTkInputDialog"
        )
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()
