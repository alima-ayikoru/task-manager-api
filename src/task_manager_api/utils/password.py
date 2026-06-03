
from pwdlib import PasswordHash

pwd = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return pwd.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd.verify(plain_password, hashed_password)  
