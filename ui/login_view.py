import tkinter as tk
from tkinter import ttk, messagebox

class LoginView(ttk.Frame):
    def __init__(self, master, servicio, al_ingresar_exitoso):
        super().__init__(master, padding="20")
        self.servicio = servicio
        self.al_ingresar_exitoso = al_ingresar_exitoso

        self.crear_componentes()

    def crear_componentes(self):
        lbl_titulo = ttk.Label(self, text="Restaurante App", font=("Helvetica", 16, "bold"))
        lbl_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        lbl_user = ttk.Label(self, text="Usuario:")
        lbl_user.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.ent_user = ttk.Entry(self)
        self.ent_user.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        lbl_pass = ttk.Label(self, text="Contraseña:")
        lbl_pass.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.ent_pass = ttk.Entry(self, show="*")
        self.ent_pass.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        btn_ingresar = ttk.Button(self, text="Iniciar Sesión", command=self.procesar_login)
        btn_ingresar.grid(row=3, column=0, columnspan=2, pady=(15, 0))

    def procesar_login(self):
        username = self.ent_user.get().strip()
        password = self.ent_pass.get().strip()

        if not username or not password:
            messagebox.showwarning("Atención", "Por favor, llene todos los campos.")
            return

        usuario = self.servicio.validar_acceso(username, password)
        if usuario:
            self.ent_user.delete(0, tk.END)
            self.ent_pass.delete(0, tk.END)
            self.al_ingresar_exitoso(usuario)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")