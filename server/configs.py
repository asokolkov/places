import os


APP_NAME = os.getenv('APP_NAME', 'Places Server')
API_VERSION = os.getenv('API_VERSION', '1.0')

JWT_SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
JWT_ALGORITHM = 'HS256'
JWT_TOKEN_EXPIRE_DAYS = 30
