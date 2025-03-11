#!/usr/bin/python3
"""
Creates a database storage session
"""

from models.engine.db_storage import DB_storage
storage = DB_storage()
storage.reload()
