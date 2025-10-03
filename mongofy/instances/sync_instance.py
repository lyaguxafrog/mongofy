# -*- coding: utf-8 -*-

from typing import Optional

from pymongo import MongoClient
from pymongo.database import Database

from mongofy.instances.base import BaseMongofy
from mongofy.exceptions import BuildClientError, MongoConnectionError


class Mongofy(BaseMongofy):
    """Main Mongofy instance."""

    _client: Optional[MongoClient] = None
    _db: Optional[Database] = None

    @classmethod
    def init(
        cls,
        uri: Optional[str] = None,
        host: Optional[str] = None,
        port: Optional[int] = None,
        user: Optional[str] = None,
        password: Optional[str] = None,
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
