# -*- coding: utf-8 -*-

from bson import ObjectId


def encoder(obj: ObjectId) -> str:
    """Encode object id."""
    if isinstance(obj, ObjectId):
        return str(obj)
    else:
        raise ValueError(f"Unsupported type: {type(obj)}")
