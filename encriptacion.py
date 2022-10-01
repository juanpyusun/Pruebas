from passlib.context import CryptContext
contexto= CryptContext(
    schemes= ["pbkdf2_sha256"],
    default= "pbkdf2_sha256",
)
texto="ruban flores"
texto_encriptado =contexto.hash(texto)
print(texto_encriptado)