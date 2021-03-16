import bcrypt

from src.service.singleton import Logger


class Security:
    @staticmethod
    def get_hashed_password(plain_text_password: str):
        # Hash a password for the first time
        #   (Using bcrypt, the salt is saved into the hash itself)
        return bcrypt.hashpw(plain_text_password.encode(), bcrypt.gensalt())

    @staticmethod
    def check_password(plain_text_password: str, hashed_password: bytes) -> bool:
        # Check hashed password. Using bcrypt, the salt is saved into the hash itself
        try:
            return bcrypt.checkpw(plain_text_password.encode(), hashed_password)
        except Exception as e:
            Logger.instance().info(e, exc_info=True)
            return False
