import os
import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Restaurante App")
        self.geometry("500x400")
        self.resizable(False, False)

        base_dir = os.path.dirname(__file__)
        ruta_usuarios = os.path.join(base_dir, "datos", "usuarios.json")
        ruta_productos = os.path.join(base_dir, "datos", "productos.json")

        self.servicio = RestauranteServicio(ruta_usuarios, ruta_productos)

        self.login_view = LoginView(self, self.servicio, self.mostrar_main_view)
        self.main_view = MainView(self, self.servicio, self.mostrar_login_view)

        self.mostrar_login_view()

    def mostrar_login_view(self):
        self.main_view.pack_forget()
        self.login_view.pack(fill="both", expand=True)

    def mostrar_main_view(self, usuario):
        self.login_view.pack_forget()
        self.main_view.set_usuario(usuario)
        self.main_view.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()