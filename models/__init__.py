#!/usr/bin/python3
"""
Creates a database storage session
"""

from models.engine.db_storage import Storage
storage = Storage()
storage.reload()
