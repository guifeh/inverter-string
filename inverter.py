def inverter_string(s):
    """Inverte os caracteres de uma string."""
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

def main():
    # Solicita ao usuário para informar uma string
    string_original = input("Digite a string que deseja inverter: ")
    
    # Inverte a string
    resultado = inverter_string(string_original)
    
    # Exibe o resultado
    print(f"String original: {string_original}")
    print(f"String invertida: {resultado}")

    input("\nPressione qualquer tecla para sair...")

if __name__ == "__main__":
    main()
