# -*- coding: utf-8 -*-

from mongofy.odm.cursor.base_cursor import BaseCursor
from mongofy.odm.document import DocumentType


class Cursor(BaseCursor):
    """Mongo query cursor."""

    def to_list(self) -> list[DocumentType]:
        """Make cursor to list."""
        return [self.model(**doc) for doc in self._data]
