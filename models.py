from sqlalchemy import Column, ForeignKey, String, create_engine,Integer
from sqlalchemy.orm import sessionmaker, declarative_base,relationship


db_user = "sqlite:///database.db"
engine = create_engine(db_user)

Base = declarative_base()

class Actor(Base):
    __tablename__='actors'
    id = Column(Integer, primary_key= True)
    name = Column(String)
    movie = relationship("Movie",back_populates='actor',secondary='movieactors')


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    actor = relationship("Actor",back_populates='movie',secondary='movieactors')

class MovieRelation(Base):
    __tablename__ = 'movieactors'
    id = Column(Integer, primary_key= True)
    actor_id = Column("actors_id",Integer, ForeignKey('actors.id'))
    movie_id = Column("movie_id", Integer, ForeignKey("movies.id"))


    

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

drishyam = Movie(name = 'drishyam')
drishyam2 = Movie(name = 'drishyam2')
cidmoosa = Movie(name = 'cidmoosa')

Dileep = Actor(name = 'dileep')
Mohanlal = Actor(name = "Mohanlal")

Mohanlal.movie.append(drishyam)
Mohanlal.movie.append(drishyam2)
Dileep.movie.append(cidmoosa)

session.add_all([Mohanlal,Dileep])
session.commit()