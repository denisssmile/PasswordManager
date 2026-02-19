import customtkinter as ctk

#тема dark, light, ssystem
ctk.set_appearance_mode("dark")
#blue, green, dark-blue
ctk.set_default_color_theme("blue")


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CryptoSafe Manager")
        self.geometry("800x500")

        # Создаем сетку (Grid) 1x2 (Левое меню и правая часть)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 1. Левая панель навигации
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")

        self.logo_label = ctk.CTkLabel(self.navigation_frame, text="CryptoSafe",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20)

        self.btn_vault = ctk.CTkButton(self.navigation_frame, text="Хранилище", fg_color="transparent", border_width=1)
        self.btn_vault.grid(row=1, column=0, padx=20, pady=10)

        self.btn_settings = ctk.CTkButton(self.navigation_frame, text="Настройки", fg_color="transparent",
                                          border_width=1)
        self.btn_settings.grid(row=2, column=0, padx=20, pady=10)

        # 2. Правая панель (Контент)
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Заголовок
        self.label_title = ctk.CTkLabel(self.home_frame, text="Ваши пароли", font=ctk.CTkFont(size=24))
        self.label_title.pack(pady=10)

        # Кнопка добавления (красивая, с закруглением)
        self.add_button = ctk.CTkButton(self.home_frame, text="+ Добавить запись", command=self.add_entry_event)
        self.add_button.pack(pady=10)

        # Поле ввода поиска
        self.search_entry = ctk.CTkEntry(self.home_frame, placeholder_text="Поиск...")
        self.search_entry.pack(fill="x", padx=20, pady=10)

    def add_entry_event(self):
        print("Нажата кнопка добавления!")


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()