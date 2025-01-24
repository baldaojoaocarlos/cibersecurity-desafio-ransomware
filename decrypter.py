import os
import pyaes

# Nome do arquivo criptografado
file_name = "teste.txt.ransomwaretroll"

# Chave para descriptografia (deve ter 16, 24 ou 32 bytes)
key = b"testeransomwares"

# Verificar se a chave tem o tamanho correto
if len(key) not in [16, 24, 32]:
    raise ValueError("Chave inválida: A chave deve ter 16, 24 ou 32 bytes.")

try:
    # Abrir o arquivo criptografado
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Descriptografar os dados
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    # Remover o arquivo criptografado
    os.remove(file_name)

    # Criar o arquivo descriptografado
    new_file_name = "teste.txt"
    with open(new_file_name, "wb") as new_file:
        new_file.write(decrypt_data)

    print(f"Arquivo '{new_file_name}' criado com sucesso.")

except FileNotFoundError:
    print(f"Erro: Arquivo '{file_name}' não encontrado.")
except OSError as e:
    print(f"Erro ao remover o arquivo: {e}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
