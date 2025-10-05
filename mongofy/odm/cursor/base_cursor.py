# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Generic, Any

from mongofy.__types__ import DocumentType


class BaseCursor(ABC, Generic[DocumentType]):
    """Base cursor class."""

    def __init__(
        self, model: type[DocumentType], raw_data: list[dict[str, Any]]
    ) -> None:
        """Constructor.

        Args:
            model: (type[DocumentType]): Type of document
            raw_data: (list[dict[str, Any]]): Raw data from finding
        """
        self.model = model
        self._data = raw_data

    @abstractmethod
    def to_list(self) -> list[DocumentType]:
        """Make list of result."""
        raise NotImplementedError
