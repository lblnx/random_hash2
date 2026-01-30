import hashlib
import secrets
import sys

def buscar_hash():
    limit = 1000
    
    print(f"Iniciando búsqueda de hash (Máximo {limit} intentos)...")

    for i in range(limit):
        random_data = secrets.token_bytes(32)
        hash_result = hashlib.md5(random_data).hexdigest()
        if hash_result.startswith("00"):
            print(f"¡Éxito! Hash encontrado en el intento #{i + 1}")
            print(f"Hash: {hash_result}")
            sys.exit(0)
    print("Fallo: No se encontró un hash válido después de 1000 intentos.")
    sys.exit(1)

if __name__ == "__main__":
    buscar_hash()