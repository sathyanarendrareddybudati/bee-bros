from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DECIMAL,TIMESTAMP, text, VARCHAR

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    full_name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    phone_number = Column(String(20))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))