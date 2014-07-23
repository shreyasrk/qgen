from flask import Flask
from py2neo import neo4j

app = Flask(__name__)
app.config.from_object('config')
db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

from app import views
