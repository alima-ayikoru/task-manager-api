from passlib.context import CryptContext
import hashlib
import base64

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    # pre-hash to bypass the 72-byte limit
    digest = hashlib.sha256(password.encode()).digest()
    prehashed = base64.b64encode(digest).decode()
    hashed_password = pwd.hash(prehashed)
    return hashed_password


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd.verify(plain_password, hashed_password)
