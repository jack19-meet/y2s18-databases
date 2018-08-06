from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
    __tablename__ = "knowledge"
    topic_id = Column(Integer, primary_key=True)
    topic = Column(String)
    title = Column(String)
    rate = Column(Integer)

    def __repr__(self):
        return ("if you want to learn about {}\n" "open {}\n" "it is rated at {}").format(
            self.topic,
            self.title,
            self.rate)
k2 = Knowledge(topic="blllm", title="tarararara", rate=10)
print(k2)     
  