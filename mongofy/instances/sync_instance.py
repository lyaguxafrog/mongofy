# -*- coding: utf-8 -*-

from typing import Optional

from pymongo import MongoClient
from pymongo.collection import Collection

from mongofy.instances.base import BaseMongofy
from mongofy.exceptions import BuildClientError


class Mongofy(BaseMongofy):
    """Main Mongofy instance."""

    _client: Optional[MongoClient] = None
    _db: Optional[Collection] = None

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

    def close(self) -> None:
        """Close mongo connection."""
        self._client.close()  # type: ignore
