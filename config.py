import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    UPLOAD_FOLDER = os.path.join('myapp', 'static', 'uploads')
    print(UPLOAD_FOLDER)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
