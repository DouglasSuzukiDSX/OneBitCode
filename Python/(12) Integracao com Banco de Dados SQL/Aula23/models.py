from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, MappedAsDataclass
from sqlalchemy import String, Text, ForeignKey

class Base(MappedAsDataclass, DeclarativeBase):
   pass

class Clientes(Base):
   __tablename__ = 'clientes'

   id: Mapped[int] = mapped_column(primary_key=True, init=False)
   nome: Mapped[str] = mapped_column(String(50))
   email: Mapped[Optional[str]] = mapped_column(String(100), unique=True)

   # Relacionamento 1:N (Um cliente possui vários pedidos)
   # Note que usamos 'list["Pedidos"]' porque são vários, e o back_populates aponta para "cliente"
   pedidos: Mapped[list['Pedidos']] = relationship(
      back_populates="cliente",
      init=False, 
      cascade='all, delete-orphan'
   )

class Pedidos(Base):
   __tablename__ = 'pedidos'

   id: Mapped[int] = mapped_column(primary_key=True, init=False)
   item: Mapped[str] = mapped_column(String(50))
   valor: Mapped[float] = mapped_column()

   cliente_id: Mapped[int] = mapped_column(
      ForeignKey("clientes.id", ondelete="CASCADE")
   )

   # Relacionamento N:1 (Vários pedidos pertencem a um cliente)
   # O back_populates aponta para "pedidos" (a lista lá de cima)
   cliente:  Mapped["Clientes"] = relationship(
      back_populates="pedidos", 
      init=False
   )