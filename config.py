import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///pizza_restaurant.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
