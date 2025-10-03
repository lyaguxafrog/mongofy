# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Union


@dataclass
class BuildClientError(Exception):
    """Exception while errors in instance build."""

    message: Union[str, Exception] = "URI build error."


@dataclass
class MongoConnectionError(Exception):
    """Exception while errors in connection."""

    message: Union[str, Exception] = "Connection error."