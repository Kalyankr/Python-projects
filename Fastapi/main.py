from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from ml import nlp

app = FastAPI()


@app.get("/")
def read_main():
    return {"message": "Hello Kalyan"}


class Article(BaseModel):

    content: str
    comments: List[str] = []


@app.post("/article/")
def analyze_article(articles: List[Article]):
    ents = []
    for article in articles:
        doc = nlp(article.content)
        for ent in doc.ents:
            ents.append({"text": ent.text, "label": ent.label_})
    return {"ents": ents}
