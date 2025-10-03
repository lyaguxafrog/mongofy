# -*- coding: utf-8 -*-

from typing import Any
from abc import abstractmethod, ABC

from mongofy.exceptions import BuildClientError


class BaseMongofy(ABC):
    """Base Mongofy instance."""

    @classmethod
    @abstractmethod
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
        raise NotImplementedError

    @abstractmethod
    def close(self) -> None:
        """Close connection."""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_db(cls) -> Any:
        """DB Getter."""
        raise NotImplementedError

    @staticmethod
    def _uri_builder(
        host: str, port: int, user: str | None, password: str | None
    ) -> str:
        """Build base mongo db uri.

        Args:
            host (str): Mongodb host
            port (int): Mongodb port
            user (str | None): User if needed
            password (str | None): Password if needed

        Returns:
            str: Mongodb uri

        Raises:
            ValueError: If cant build uri
        """
        if not user and not password:
            return f"mongodb://{host}:{port}"
        elif (user and not password) or (not user and password):
            raise BuildClientError(
                f"Cant connect to mongo with: user: {user} and password: {password}."
            )
        else:
            return f"mongodb://{user}:{password}@{host}:{port}"
