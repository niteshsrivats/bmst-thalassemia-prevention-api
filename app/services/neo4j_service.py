import os

from neo4j import GraphDatabase


class Neo4JService:
    client = None

    @classmethod
    def connect(cls):
        if cls.client is not None:
            return

        cls.client = GraphDatabase.driver(
            os.getenv("NEO4J_URI"),
            auth=(os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD")),
        )
