import os
import customtkinter as ctk
from database.db import DatabaseManager
from gui.main_window import MainWindow



def start_app():
    db_file = "crypto_safe.db"
    first_run = not os.path.exists(db_file)

    db = DatabaseManager(db_file)

    if first_run:
        show_setup_wizard(db)
    else:
        show_main_window()


def show_setup_wizard(db):
    setup = ctk.CTk()
    setup.title("Первоначальная настройка")
    setup.geometry("400x300")

    ctk.CTkLabel(setup, text="Создайте Мастер-Пароль", font=("Arial", 16)).pack(pady=20)

    pwd_entry = ctk.CTkEntry(setup, placeholder_text="Пароль", show="*")
    pwd_entry.pack(pady=10)

    def save_master():
        # В Спринте 1 просто сохраняем (в Спринте 2 добавим Argon2)
        password = pwd_entry.get()
        db.conn.execute("INSERT INTO settings (setting_key, setting_value) VALUES (?, ?)",
                        ("master_hash", password))
        db.conn.commit()
        setup.destroy()
        show_main_window()

    ctk.CTkButton(setup, text="Начать работу", command=save_master).pack(pady=20)
    setup.mainloop()


def show_main_window():
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    start_app()