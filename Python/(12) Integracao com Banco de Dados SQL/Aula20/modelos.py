from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, MappedAsDataclass
from sqlalchemy import String, Text, ForeignKey

class Base(MappedAsDataclass, DeclarativeBase):
   pass 

class Usuario(Base):
   __tablename__ = "usuarios"

   id: Mapped[int] = mapped_column(primary_key=True, init=False)
   nome: Mapped[str] = mapped_column(String(50))
   email: Mapped[Optional[str]] = mapped_column(String(100), unique=True)
   telefone: Mapped[str] = mapped_column(Text)

   enderecos: Mapped[list["Endereco"]] = relationship(back_populates="usuario", init=False)

   def __repr__(self) -> str:
      return f"Usuario(id={self.id!r}, nome={self.nome!r}, email={self.email!r})"

class Endereco(Base):
   __tablename__ = "enderecos"

   id: Mapped[int] = mapped_column(primary_key=True, init=False)
   rua: Mapped[str] = mapped_column(String(100))
   usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id", ondelete="CASCADE"), init=False)

   usuario: Mapped["Usuario"] = relationship(back_populates="enderecos", init=False, cascade="all, delete-orphan")
   
if __name__ == "__main__":
   usuario = Usuario(nome='Carlos', telefone='3456', email='')
   endereco = Endereco(rua='Rua das Flores')

   usuario.enderecos.append(endereco)

   print(endereco.usuario.nome)