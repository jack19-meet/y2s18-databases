from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic,title,rating):
	article=Knowledge(topic=topic, title=title, rating=rating)
	session.add(article)
	session.commit()

def query_all_articles():
	knowledge=session.query(Knowledge).all()
	return knowledge

def query_article_by_topic(topic):
	knowledge=session.query(Knowledge).filter_by(topic=topic)
	return knowledge

def query_article_by_rating(threshold):
	knowledge=session.query(Knowledge).filter(Knowledge.rate<threshold).all()

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(topic=topic).delete()
	session.commit()

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

def edit_article_rating(update_rating,article_title):
	art_rate=session.query(Knowledge).filter_by(title=article_title).first()
	art_rate.rating=update_rating
	session.commit()
	
#delete_all_articles()
#add_article("birds", "birds are nice", 7)
edit_article_rating(10,"birds")
print(query_all_articles())	