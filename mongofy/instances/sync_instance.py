# -*- coding: utf-8 -*-


from pymongo import MongoClient
from pymongo.database import Database

from mongofy.instances.base import BaseMongofy
from mongofy.exceptions import BuildClientError, MongoConnectionError


class Mongofy(BaseMongofy):
    """Main Mongofy instance."""

    _client: MongoClient | None = None
    _db: Database | None = None

    @classmethod
    def init(
        cls,
        uri: str | None = None,
        host: str | None = None,
        port: int | None = None,
        user: str | None = None,
        password: str | None = None,
        db_name: str = "db",
    ) -> None:
        """Init mongo connection.

        Args:
            uri (str | None): URI to connection
            host (str | None): Mongodb host
            port (int | None): Mongodb port
            user (str | None): Mongo user if needed
            password (str | None): Mongo password if needed
            db_name (str): Database name
        """
        if uri:
            cls._client = MongoClient(uri)
        elif host and port:
            uri = cls._uri_builder(host, port, user, password)
            cls._client = MongoClient(uri)
        else:
            raise BuildClientError(f"Error while building client: {uri}")

        cls._db = cls._client[db_name]

    @classmethod
    def get_db(cls) -> Database:
        """Get current db.

        Returns:
            Database: Current database

        Raises:
            MongoConnectionError: If mongodb not initialized
        """
        if cls._db is None:
            raise MongoConnectionError("MongoDB not initialized.")
        return cls._db

    def close(self) -> None:
        """Close mongo connection."""
        self._client.close()  # type: ignore
