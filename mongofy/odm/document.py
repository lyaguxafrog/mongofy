# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import TypeVar, Optional
from bson import ObjectId
import msgspec
from msgspec import Struct
from msgspec.json import Encoder

from mongofy.instances.sync_instance import Mongofy
from mongofy.odm.encoder import encoder
from mongofy.odm.cursor import Cursor


encoder = Encoder(enc_hook=encoder)


DocumentType = TypeVar("DocumentType", bound="Document")


class Document(Struct):
    """Base document class."""

    _id: Optional[ObjectId] = None

    @property
    def id(self) -> ObjectId:
        """Get model ID."""
        return self._id

    def save(self: DocumentType) -> DocumentType:
        """Save document and return self."""
        data = msgspec.to_builtins(self)

        if "_id" in data:
            data.pop("_id")

        result = Mongofy.get_db()["DEV"].insert_one(data)
        self._id = result.inserted_id
        return self

    @classmethod
    def find_one(cls: type[DocumentType], **query) -> Optional[DocumentType]:
        """Find one document.

        Args:
            query (dict[str, Any]): Query

        Returns:
            Optional[DocumentType]: Document if exist
        """
        qs = Mongofy.get_db()["DEV"].find_one(query)
        return cls(**qs) if qs else None

    @classmethod
    def find(cls: type[DocumentType], **query) -> Cursor:
        """Find something in MongoDB.

        Returns:
            Cursor: Cursor with finding data
        """
        raw = list(Mongofy.get_db()["DEV"].find(query))
        return Cursor(cls, raw)
