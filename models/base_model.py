#!/usr/bin/python3
"""Base Model class for other classes"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Base class for all classes"""

    def __init__(self):
        """Instastiate the base model"""
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """Override the str representation of class"""
        return f"[{type(self).__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        """Updates updated_at attr with current time"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Returns dict containing key/values of instance"""
        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        cls_dict = self.__dict__.copy()
        cls_dict["__class__"] = type(self).__name__
        cls_dict["created_at"] = cls_dict["created_at"].strftime(fmt)
        cls_dict["updated_at"] = cls_dict["updated_at"].strftime(fmt)
        return cls_dict
