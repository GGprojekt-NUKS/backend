from typing import Union
from fastapi import FastAPI, HTTPException, status
from database import engine, Base, Forum, Topics
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)
import shemas

app = FastAPI()

#from fastapi_versioning import version, VersionedFastAPI

from fastapi.middleware.cors import CORSMiddleware



# Configure CORS settings
origins = [
    "http://localhost",
    "http://0.0.0.0:8080",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





@app.get("/")
#@version(1)
def read_root():
    return "Moj app"

@app.post("/add", status_code=status.HTTP_201_CREATED)
#@version(1)
def add_text(forum: shemas.Forum):
    """
        API call for adding text
    """
    session = Session(bind=engine, expire_on_commit= False)
    forumDB = Forum(text = forum.text)
    session.add(forumDB)
    session.commit()
    id = forumDB.id
    session.close()
    return f"Created new text with id {id}"

@app.delete("/delete/{id}")
#@version(1)
def delete_text(id: int):
    session = Session(bind=engine, expire_on_commit=False)
    forumDB = session.query(Forum).filter(Forum.id == id).first()
    if not forumDB:
        return f"No text found with ID {id}", 404
    session.delete(forumDB)
    session.commit()
    session.close()
    return f"Deleted zapis with ID {id}"

@app.delete("/delete_topic/{id}")
#@version(1)
def delete_topic(id: int):
    session = Session(bind=engine, expire_on_commit=False)
    topicDB = session.query(Topics).filter(Topics.id == id).first()
    if not topicDB:
        return f"No text found with ID {id}", 404
    session.delete(topicDB)
    session.commit()
    session.close()
    return f"Deleted zapis with ID {id}"


@app.put("/update/{id}")
#@version(1)
def update_text():
    return "Update"

@app.get("/get/{id}")
#@version(1)
def get_text():
    return "get"

@app.get("/text_list")
#@version(1)
def get_all_texts():
    session = Session(bind=engine, expire_on_commit=False)
    forum_list = session.query(Forum).all()
    session.close()
    #return forum_list
    return [forum.text for forum in forum_list]

@app.get("/topic_list")
#@version(1)
def get_all_topics():
    session = Session(bind=engine, expire_on_commit=False)
    topics_list = session.query(Topics).all()
    session.close()
    #return topics_list
    return [topic.topic for topic in topics_list]

#app = VersionedFastAPI(app, version_format="{major}", prefix_format="/v{major}")