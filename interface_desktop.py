import customtkinter as ctk

# Configuração visual (Dark Mode)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AppBancario(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Marzliak Digital Bank - Pro")
        self.geometry("500x400")

        # Título Principal
        self.label_titulo = ctk.CTkLabel(self, text="🏦 Sistema Bancário Pro", font=("Roboto", 24, "bold"))
        self.label_titulo.pack(pady=20)

        # Campo de Entrada (Saldo/Valor)
        self.entry_valor = ctk.CTkEntry(self, placeholder_text="Digite o valor (Ex: 100.00)", width=300)
        self.entry_valor.pack(pady=10)

        # Botão de Depósito
        self.btn_deposito = ctk.CTkButton(self, text="Realizar Depósito", command=self.depositar, fg_color="green", hover_color="#228B22")
        self.btn_deposito.pack(pady=10)

        # Botão de Saque
        self.btn_saque = ctk.CTkButton(self, text="Realizar Saque", command=self.sacar, fg_color="red", hover_color="#8B0000")
        self.btn_saque.pack(pady=10)

        # Área de Extrato (Simulada)
        self.textbox_extrato = ctk.CTkTextbox(self, width=350, height=120)
        self.textbox_extrato.pack(pady=20)
        self.textbox_extrato.insert("0.0", "=== Extrato Digital ===\nBem-vindo ao seu banco!")

    def depositar(self):
        valor = self.entry_valor.get()
        if valor:
            self.textbox_extrato.insert("end", f"\nDepósito: R$ {valor}")
            print(f"Depósito de R$ {valor} enviado para a API")
        
    def sacar(self):
        valor = self.entry_valor.get()
        if valor:
            self.textbox_extrato.insert("end", f"\nSaque: R$ {valor}")
            print(f"Saque de R$ {valor} enviado para a API")

if __name__ == "__main__":
    app = AppBancario()
    app.mainloop()
