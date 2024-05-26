import tkinter
import tkinter.messagebox
import tkinter.ttk
from typing import Union, Tuple, Optional
import json
import customtkinter
from customtkinter import (
    CTkLabel,
    CTkButton,
    ThemeManager,
    CTkToplevel,
    CTkFont,
)
import os
from PIL import ImageTk

from olx3 import send_olx_message_automation

# Read the JSON file
with open("brand-model-dict.json", "r") as file:
    brand_model_dict = json.load(file)
# print(brand_model_dict)

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
            self, text="Tema:", anchor="w"
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


class OptionsTabView(customtkinter.CTkTabview):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(row=0, column=2, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.add("Opções")
        self.add("Opções Avançadas")
        self.tab("Opções").grid_columnconfigure(0, weight=1)
        self.tab("Opções Avançadas").grid_columnconfigure(0, weight=1)

        # brand select
        self.brand_label = customtkinter.CTkLabel(
            self.tab("Opções"), text="Marca:", anchor="w"
        )
        self.brand_label.grid(row=0, column=0)

        self.brand_option_frame = customtkinter.CTkFrame(self.tab("Opções"))
        self.brand_option_frame.grid(row=1, column=0)
        self.brand_option = tkinter.ttk.Combobox(
            self.brand_option_frame,
            values=list(brand_model_dict),
        )
        self.brand_option.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        self.brand_option.bind("<<ComboboxSelected>>", self.update_car_models)

        # car model select
        self.car_model_label = customtkinter.CTkLabel(
            self.tab("Opções"), text="Modelo:", anchor="w"
        )
        self.car_model_label.grid(row=2, column=0)

        self.car_model_option_frame = customtkinter.CTkFrame(self.tab("Opções"))
        self.car_model_option_frame.grid(row=3, column=0)

        self.car_model_option = tkinter.ttk.Combobox(
            self.car_model_option_frame,
            values=[],
        )
        self.car_model_option.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

        self.test_mode_switch_var = customtkinter.StringVar(value="on")
        self.test_mode_switch = customtkinter.CTkSwitch(
            self.tab("Opções"),
            text="Modo de Teste",
            variable=self.test_mode_switch_var,
            onvalue="on",
            offvalue="off",
        )
        self.test_mode_switch.grid(row=4, column=0, sticky="s", pady=(10, 0))

        # ---------------------------------------------------

        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            master=self.tab("Opções Avançadas"), width=200, height=200
        )

        self.min_km_label = customtkinter.CTkLabel(
            self.tab("Opções Avançadas"), text="Kilometragem mínima:"
        )
        self.min_km_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 0))

        self.min_km = tkinter.ttk.Combobox(
            self.tab("Opções Avançadas"),
            values=[
                "---",
                "0",
                "5.000",
                "10.000",
                "20.000",
                "30.000",
                "40.000",
                "60.000",
                "80.000",
                "100.000",
                "120.000",
                "140.000",
                "160.000",
                "180.000",
                "200.000",
                "250.000",
                "300.000",
                "400.000",
                "500.000",
            ],
        )
        self.min_km.grid(row=0, column=1, padx=(10, 10), pady=(10, 0), sticky="ne")

        self.max_km_label = customtkinter.CTkLabel(
            self.tab("Opções Avançadas"), text="Kilometragem máxima:"
        )
        self.max_km_label.grid(row=1, column=0, padx=(10, 10), pady=(10, 0))

        self.max_km = tkinter.ttk.Combobox(
            self.tab("Opções Avançadas"),
            values=[
                "---",
                "0",
                "5.000",
                "10.000",
                "20.000",
                "30.000",
                "40.000",
                "60.000",
                "80.000",
                "100.000",
                "120.000",
                "140.000",
                "160.000",
                "180.000",
                "200.000",
                "250.000",
                "300.000",
                "400.000",
                "500.000",
            ],
        )
        self.max_km.grid(row=1, column=1, padx=(10, 10), pady=(10, 0), sticky="ne")

        self.min_year_label = customtkinter.CTkLabel(
            self.tab("Opções Avançadas"), text="Ano mínimo:"
        )
        self.min_year_label.grid(row=2, column=0, padx=(10, 10), pady=(10, 0))

        self.min_year = tkinter.ttk.Combobox(
            self.tab("Opções Avançadas"),
            values=[
                "---",
                "1950 ou anterior",
                "1951",
                "1952",
                "1953",
                "1954",
                "1955",
                "1956",
                "1957",
                "1958",
                "1959",
                "1960",
                "1961",
                "1962",
                "1963",
                "1964",
                "1965",
                "1966",
                "1967",
                "1968",
                "1969",
                "1970",
                "1971",
                "1972",
                "1973",
                "1974",
                "1975",
                "1976",
                "1977",
                "1978",
                "1979",
                "1980",
                "1981",
                "1982",
                "1983",
                "1984",
                "1985",
                "1986",
                "1987",
                "1988",
                "1989",
                "1990",
                "1991",
                "1992",
                "1993",
                "1994",
                "1995",
                "1996",
                "1997",
                "1998",
                "1999",
                "2000",
                "2001",
                "2002",
                "2003",
                "2004",
                "2005",
                "2006",
                "2007",
                "2008",
                "2009",
                "2010",
                "2011",
                "2012",
                "2013",
                "2014",
                "2015",
                "2016",
                "2017",
                "2018",
                "2019",
                "2020",
                "2021",
                "2022",
                "2023",
                "2024",
                "2025",
            ],
        )
        self.min_year.grid(row=2, column=1, padx=(10, 10), pady=(10, 0), sticky="ne")

        self.max_year_label = customtkinter.CTkLabel(
            self.tab("Opções Avançadas"), text="Ano máximo:"
        )
        self.max_year_label.grid(row=3, column=0, padx=(10, 10), pady=(10, 0))

        self.max_year = tkinter.ttk.Combobox(
            self.tab("Opções Avançadas"),
            values=[
                "---",
                "1950 ou anterior",
                "1951",
                "1952",
                "1953",
                "1954",
                "1955",
                "1956",
                "1957",
                "1958",
                "1959",
                "1960",
                "1961",
                "1962",
                "1963",
                "1964",
                "1965",
                "1966",
                "1967",
                "1968",
                "1969",
                "1970",
                "1971",
                "1972",
                "1973",
                "1974",
                "1975",
                "1976",
                "1977",
                "1978",
                "1979",
                "1980",
                "1981",
                "1982",
                "1983",
                "1984",
                "1985",
                "1986",
                "1987",
                "1988",
                "1989",
                "1990",
                "1991",
                "1992",
                "1993",
                "1994",
                "1995",
                "1996",
                "1997",
                "1998",
                "1999",
                "2000",
                "2001",
                "2002",
                "2003",
                "2004",
                "2005",
                "2006",
                "2007",
                "2008",
                "2009",
                "2010",
                "2011",
                "2012",
                "2013",
                "2014",
                "2015",
                "2016",
                "2017",
                "2018",
                "2019",
                "2020",
                "2021",
                "2022",
                "2023",
                "2024",
                "2025",
            ],
        )
        self.max_year.grid(row=3, column=1, padx=(10, 10), pady=(10, 0), sticky="ne")

        self.max_price_label = customtkinter.CTkLabel(
            self.tab("Opções Avançadas"), text="Preço máximo:"
        )
        self.max_price_label.grid(row=4, column=0, padx=(10, 10), pady=(10, 0))
        self.max_price = customtkinter.CTkEntry(
            self.tab("Opções Avançadas"), placeholder_text="..."
        )
        self.max_price.grid(row=4, column=1, padx=(10, 10), pady=(10, 0), sticky="ne")

        self.pf_adds_switch_var = customtkinter.StringVar(value="on")
        self.pf_adds_switch = customtkinter.CTkSwitch(
            self.tab("Opções Avançadas"),
            text="Permitir anúncios particulares",
            variable=self.pf_adds_switch_var,
            onvalue="on",
            offvalue="off",
        )
        self.pf_adds_switch.grid(row=5, column=0, columnspan=2, sticky="n")

        self.professional_adds_switch_var = customtkinter.StringVar(value="off")
        self.professional_adds_switch = customtkinter.CTkSwitch(
            self.tab("Opções Avançadas"),
            text="Permitir anúncios profissionais",
            variable=self.professional_adds_switch_var,
            onvalue="on",
            offvalue="off",
        )
        self.professional_adds_switch.grid(row=6, column=0, columnspan=2, sticky="n")

        # Inicial config
        self.brand_option.set("Marca")
        self.car_model_option.set("Modelo")
        self.min_km.set("---")
        self.max_km.set("---")
        self.min_year.set("---")
        self.max_year.set("---")

    def update_car_models(self, _):
        """Updates car model list based on brand."""
        selected_brand = self.brand_option.get()
        car_models = brand_model_dict[selected_brand]
        self.car_model_option["values"] = car_models


class MyInputDialog(CTkToplevel):
    """
    Dialog with extra window, message, entry widget, cancel and ok button.
    For detailed information check out the documentation.
    """

    def __init__(
        self,
        fg_color: Optional[Union[str, Tuple[str, str]]] = None,
        text_color: Optional[Union[str, Tuple[str, str]]] = None,
        button_fg_color: Optional[Union[str, Tuple[str, str]]] = None,
        button_hover_color: Optional[Union[str, Tuple[str, str]]] = None,
        button_text_color: Optional[Union[str, Tuple[str, str]]] = None,
        entry_fg_color: Optional[Union[str, Tuple[str, str]]] = None,
        entry_border_color: Optional[Union[str, Tuple[str, str]]] = None,
        entry_text_color: Optional[Union[str, Tuple[str, str]]] = None,
        title: str = "CTkDialog",
        font: Optional[Union[tuple, CTkFont]] = None,
        text: str = "CTkDialog",
    ):
        super().__init__(fg_color=fg_color)

        self._fg_color = (
            ThemeManager.theme["CTkToplevel"]["fg_color"]
            if fg_color is None
            else self._check_color_type(fg_color)
        )
        self._text_color = (
            ThemeManager.theme["CTkLabel"]["text_color"]
            if text_color is None
            else self._check_color_type(button_hover_color)
        )
        self._button_fg_color = (
            ThemeManager.theme["CTkButton"]["fg_color"]
            if button_fg_color is None
            else self._check_color_type(button_fg_color)
        )
        self._button_hover_color = (
            ThemeManager.theme["CTkButton"]["hover_color"]
            if button_hover_color is None
            else self._check_color_type(button_hover_color)
        )
        self._button_text_color = (
            ThemeManager.theme["CTkButton"]["text_color"]
            if button_text_color is None
            else self._check_color_type(button_text_color)
        )
        self._entry_fg_color = (
            ThemeManager.theme["CTkEntry"]["fg_color"]
            if entry_fg_color is None
            else self._check_color_type(entry_fg_color)
        )
        self._entry_border_color = (
            ThemeManager.theme["CTkEntry"]["border_color"]
            if entry_border_color is None
            else self._check_color_type(entry_border_color)
        )
        self._entry_text_color = (
            ThemeManager.theme["CTkEntry"]["text_color"]
            if entry_text_color is None
            else self._check_color_type(entry_text_color)
        )

        self._user_input: Union[str, None] = None
        self._running: bool = False
        self._title = title
        self._text = text
        self._font = font

        self.title(self._title)
        self.lift()  # lift window on top
        self.attributes("-topmost", True)  # stay on top
        self.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.after(
            10, self._create_widgets
        )  # create widgets with slight delay, to avoid white flickering of background
        self.resizable(False, False)
        self.grab_set()  # make other windows not clickable

    def _create_widgets(self):
        self.grid_columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)

        self._label = CTkLabel(
            master=self,
            width=300,
            wraplength=300,
            fg_color="transparent",
            text=self._text,
            font=self._font,
        )
        self._label.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

        self._ok_button = CTkButton(
            master=self,
            width=100,
            border_width=0,
            text="Ok",
            font=self._font,
            command=self._ok_event,
        )
        self._ok_button.grid(
            row=2, column=0, columnspan=1, padx=(20, 10), pady=(0, 20), sticky="ew"
        )

        self._cancel_button = CTkButton(
            master=self,
            width=100,
            border_width=0,
            text="Cancel",
            font=self._font,
            command=self._cancel_event,
        )
        self._cancel_button.grid(
            row=2, column=1, columnspan=1, padx=(10, 20), pady=(0, 20), sticky="ew"
        )

    def _ok_event(self, event=None):
        self.grab_release()
        self.destroy()

    def _on_closing(self):
        self.grab_release()
        self.destroy()

    def _cancel_event(self):
        self.grab_release()
        self.destroy()

    def get_input(self):
        self.master.wait_window(self)
        return self._user_input


class App(customtkinter.CTk):
    """Main application."""

    def __init__(self):
        super().__init__()

        # configure window
        self.title("Automação de Busca de Carros na OLX")
        self.geometry(f"{1100}x{425}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar
        self.sidebar = Sidebar(self, width=140, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(
            master=self,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            text="Buscar",
            command=self.start_scraping,
        )
        self.main_button_1.grid(
            row=3, column=2, columnspan=1, padx=(5, 20), pady=(20, 20), sticky="nsew"
        )
        # create main entry and button
        self.message_entry = customtkinter.CTkEntry(
            self,
            placeholder_text="Escreva aqui a mensagem a ser enviada aos vendedores",
        )
        self.message_entry.grid(
            row=3, column=1, columnspan=1, padx=(20, 5), pady=(20, 20), sticky="nsew"
        )

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.options_tab_view = OptionsTabView(self)

        # set default values
        self.sidebar.appearance_mode_optionemenu.set("Dark")
        self.sidebar.scaling_optionemenu.set("100%")
        self.textbox.insert(
            "0.0",
            "Automação de busca de carros OLX\n\n"
            + "ANTES DE INICIAR SUA BUSCA, FAÇA O LOGIN COM SUA CONTA NOS SITES DA OLX E DO WHATSAPP!.\n\n"
            + "Bem-vindo ao mecanismo automático de busca de carros. Aqui facilitaremos seu trabalho enviando mensagens automáticas pelo WhatsApp para os vendedores da OLX que se adequem aos campos a serem selecionados por você.\n\n",
        )

        # App logo
        self.iconpath = ImageTk.PhotoImage(file=os.path.join("images", "olx.png"))
        self.wm_iconbitmap()
        self.iconphoto(False, self.iconpath)

    def start_scraping(self):
        send_olx_message_automation(
            {
                "brand": self.options_tab_view.brand_option.get().lower(),
                "model": self.options_tab_view.car_model_option.get().lower(),
                "minKm": convert_to_olx_km(self.options_tab_view.min_km.get()),
                "maxKm": convert_to_olx_km(self.options_tab_view.max_km.get()),
                "minYear": convert_to_olx_year(self.options_tab_view.min_year.get()),
                "maxYear": convert_to_olx_year(self.options_tab_view.max_year.get()),
                "maxPrice": (
                    int(self.options_tab_view.max_price.get())
                    if self.options_tab_view.max_price.get()
                    else None
                ),
                "message": self.message_entry.get(),
                "allowPrivateAds": self.options_tab_view.pf_adds_switch.get() == "on",
                "allowProfessionalAds": self.options_tab_view.professional_adds_switch.get()
                == "on",
                "test_mode": self.options_tab_view.test_mode_switch.get() == "on",
            }
        )

    def open_input_dialog_event(self):
        """Opens confirmation pop up."""
        dialog = MyInputDialog(text="Começar a busca?", title="Confirmação")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """Changes colorscheme."""
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        """Changes application scale."""
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


def convert_to_olx_year(year):
    if year == "---":
        return None
    if year == "1950 ou anterior":
        return 1950 - 1950
    return int(year) - 1950


def convert_to_olx_km(km):
    if km == "---":
        return None
    return int(km.replace(".", ""))


if __name__ == "__main__":
    # print(brand_model_dict)
    app = App()
    app.mainloop()
