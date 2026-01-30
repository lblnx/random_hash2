import hashlib
import secrets
import sys

def buscar_hash():
    limit = 1000
    
    print(f"Iniciando búsqueda de hash (Máximo {limit} intentos)...")

    for i in range(limit):
        # Generar datos aleatorios
        random_data = secrets.token_bytes(32)
        
        # Crear el hash MD5 (32 caracteres hex)
        hash_result = hashlib.md5(random_data).hexdigest()
        
        # Verificar si empieza con dos ceros
        if hash_result.startswith("00"):
            print(f"¡Éxito! Hash encontrado en el intento #{i + 1}")
            print(f"Hash: {hash_result}")
            # Salir con código 0 indica éxito al sistema operativo/CI
            sys.exit(0)

    # Si termina el ciclo sin éxito
    print("Fallo: No se encontró un hash válido después de 1000 intentos.")
    sys.exit(1)

if __name__ == "__main__":
    buscar_hash()