from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Text

class Base(DeclarativeBase):
   pass 

class Usuario(Base):
   __tablename__ = "usuarios"

   id: Mapped[int] = mapped_column(primary_key=True)
   nome: Mapped[str] = mapped_column(String(50))
   email: Mapped[Optional[str]] = mapped_column(String(100), unique=True)
   telefone: Mapped[str] = mapped_column(Text)

   def __repr__(self) -> str:
      return f"Usuario(id={self.id!r}, nome={self.nome!r}, email={self.email!r})"