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
	knowledge=session.query(Knowledge).filter(Knowledge.rating<threshold).all()

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(topic=topic).delete()
	session.commit()

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

def edit_article_rating(update_rating,article_title):
	art_rate=session.query(Knowledge).filter_by(topic=article_title).first()
	art_rate.rating=update_rating
	session.commit()


def delete_article_by_rating(threshold):
	session.query(Knowledge).filter(Knowledge.rating<threshold).delete()
	session.commit()

def get_top_rated_5():
	knowledge=query_all_articles()

	
delete_all_articles()
#add_article("birds", "birds are nice", 7)
#add_article("idk", "idk, google it",4)
#edit_article_rating(10,"birds")
#delete_article_by_topic("birds")

print(query_all_articles())		
