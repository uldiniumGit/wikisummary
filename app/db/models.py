from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True, index=True)
    title = Column(String)
    content = Column(Text)
    parent_id = Column(Integer, ForeignKey("articles.id", ondelete="CASCADE"), nullable=True)

    children = relationship("Article", backref="parent", cascade="all, delete")
    summary = relationship("Summary", back_populates="article", uselist=False)


class Summary(Base):
    __tablename__ = "summaries"

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey("articles.id", ondelete="CASCADE"), unique=True)
    content = Column(Text)

    article = relationship("Article", back_populates="summary")
