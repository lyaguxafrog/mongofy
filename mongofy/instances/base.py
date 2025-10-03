# -*- coding: utf-8 -*-

from typing import Optional
from abc import abstractmethod, ABC

from pymongo import MongoClient

from mongofy.exceptions import BuildClientError


class BaseMongofy(ABC):
    """Base Mongofy instance."""

    def __init__(
        self,
        uri: Optional[str] = None,
        host: Optional[str] = None,
        port: Optional[int] = None,
        user: Optional[str] = None,
        password: Optional[str] = None,
        client: Optional[MongoClient] = None,
    ) -> None:
        """Constructor.

        Args:
            uri (str | None): URI to your mongo
            host (str | None): Host
            port (int | None): Mongo port
            user (str | None): User if needed
            password (str | None): Password id needed
            client (MongoClient | None): Pymongo client

        Raises:
            BuildClientError: If error while setup
        """
        if not client:
            _uri = uri if uri else self._uri_builder(host, port, user, password)  # type: ignore
        elif client:
            self.__client = client
        else:
            raise BuildClientError("Please, setup your mongo connection!")

    @staticmethod
    def _uri_builder(
        host: str, port: int, user: Optional[str], password: Optional[str]
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

    @abstractmethod
    def init(self) -> None:
        """Init connection scope."""
        raise NotImplementedError

    @abstractmethod
    def close(self) -> None:
        """Close connection scope."""
        raise NotImplementedError
