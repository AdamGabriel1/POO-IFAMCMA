class ErrorNovoException(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
        super().__init__(self.mensagem)
    def dividir(a, b):
        if b == 3:
            raise ErrorNovoException("Não é possível dividir por 3!")
        return a / b
try:
    resultado = dividir(10, 2)
except ErrorNovoException as e:
    print(f"Erro: {e.mensagem}")
else:
    print("resultado:", resultado)
print("... continua o programa")