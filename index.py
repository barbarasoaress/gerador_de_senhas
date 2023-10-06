import random
import string

def gerar_senha(comprimento, usar_letras=True, usar_numeros=True, usar_simbolos=True):
    caracteres = ""
    
    if usar_letras:
        caracteres += string.ascii_letters
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation
    
    if not caracteres:
        print("Erro: Você deve escolher pelo menos um tipo de caractere.")
        return None
    
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

if __name__ == "__main__":
    comprimento = int(input("Digite o comprimento da senha desejada: "))
    usar_letras = input("Incluir letras? (sim/não): ").lower() == "sim"
    usar_numeros = input("Incluir números? (sim/não): ").lower() == "sim"
    usar_simbolos = input("Incluir símbolos? (sim/não): ").lower() == "sim"
    
    senha = gerar_senha(comprimento, usar_letras, usar_numeros, usar_simbolos)
    
    if senha:
        print(f"Sua senha gerada: {senha}")
