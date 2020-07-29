"""Exceptions for LTA Datamall API client"""


class LtapysgError(Exception):
    """General exception"""

    pass


class LtapysgConnectionError(LtapysgError):
    """Connection error occurs"""

    pass
