#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pydantic import BaseModel
from typing import Optional
from db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, JSON, Boolean
	
class TodoList_create(BaseModel):

	name: str


class TodoList_update(BaseModel):

	name: Optional[str] = None


class TodoList(Base):

	__tablename__ = 'TodoList'

	id = Column(Integer, primary_key=True, index=True)

	name= Column(String(255), nullable= False)
