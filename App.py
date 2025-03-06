import customtkinter as ctk
from Dashboard import create_dashboard
from LoginPage import LoginPage


def main():
    app = ctk.CTk()
    app.title("Dashboard")

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    def show_dashboard():
        for widget in app.winfo_children():
            widget.destroy()
        create_dashboard(app)

    login_page = LoginPage(app, show_dashboard)
    login_page.pack(fill="both", expand=True)

    app.mainloop()


if __name__ == "__main__":
    main()