# -*- coding: utf-8 -*-

"""All Mongofy exceptions."""

from .instance import BuildClientError, MongoConnectionError


__all__ = [
    "BuildClientError",
    "MongoConnectionError"
]