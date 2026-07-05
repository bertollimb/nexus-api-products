from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def check_password(password: str, hash_password: str) -> bool:
    """
    Function to verify if the password is correct by comparing the plain-text password provided by the user with the password hash stored in the database during account creation.
    """
    if not password or not hash_password:
        return False
    
    return pwd_context.verify(password, hash_password)

def generate_hash_password(password: str) -> str:
    """
    Function that generates and returns the password hash.
    """
    return pwd_context.hash(password)
