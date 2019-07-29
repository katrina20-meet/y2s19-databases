from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

#main class
class articles:
   def __init__(self, id, name, topic, rating):
       self.art_id= id
       self.art_name= name
       self.art_topic = topic
       self.art_rating = rating


Base = declarative_base()


#class inheriting from base
class Knowledge(Base):
	
	__tablename__ = 'Articles'
	art_id = Column(Integer, primary_key=True)
	art_top = Column(String)
	art_name = Column(String)
	art_rating = Column(Integer)

	def __repr__(self):

		if (self.art_rating<=7): 
			return("Unfortunately, this article does not have a better rating. Maybe, this is an article that should be replaced soon!")
		return("article ID: {}\n If you want to learn about {}, you should look at the Wikipedia article called {}\n.We gave this article a rating of {} out of 10!").format(
				 self.art_id, self.art_top, self.art_name, self.art_rating)
		
	
		



know= Knowledge(art_id=1,art_name="penglings", art_top="penguins", art_rating=9)	
print(know)