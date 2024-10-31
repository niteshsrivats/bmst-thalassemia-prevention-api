import os

from firebase_admin import App, auth, credentials, initialize_app


class FirebaseService:
    _app: App = None

    @classmethod
    def init(cls):
        if os.getenv("K_SERVICE") is None:
            credential = credentials.Certificate(os.getenv("FIREBASE_CONFIG"))
            cls._app = initialize_app(credential=credential)
        else:
            cls._app = initialize_app()

    @classmethod
    def get_firebase_token(cls, user_id: str):
        return auth.create_custom_token(user_id)

    @classmethod
    def refresh_firebase_token(cls, token: str):
        # TODO: Handle revoked tokens
        result = auth.verify_id_token(token, check_revoked=True)
        return cls.get_firebase_token(result.get("uid"))
