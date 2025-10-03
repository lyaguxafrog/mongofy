# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Union


@dataclass
class BuildClientError(Exception):
    """Exception while errors in instance build."""

    message: Union[str, Exception] = "URI build error."