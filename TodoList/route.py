from fastapi import APIRouter,Depends, HTTPException 
from security import *
from TodoList.model import TodoList, TodoList_create, TodoList_update 
from db import get_db
from requests import Session

TodoList_router = APIRouter(prefix="/TodoList", tags=['TodoList'], dependencies=[Depends(get_current_active_user)])


@TodoList_router.get("/")
async def get_all_TodoList(db: Session = Depends(get_db)):
	db_TodoList = db.query(TodoList).all()	
	return db_TodoList

@TodoList_router.get("/{id}")
async def get_TodoList_by_id(id: int, db: Session = Depends(get_db)):
	db_TodoList = db.query(TodoList).filter(TodoList.id == id).first()
	if not db_TodoList:
		raise HTTPException(status_code=404, detail="TodoList not found")
	return TodoList

@TodoList_router.post("/")
async def create_TodoList(TodoList_post: TodoList_create, db: Session = Depends(get_db)):
	db_TodoList = TodoList(**TodoList_post.model_dump())
	db.add(db_TodoList)
	db.commit()
	db.refresh(db_TodoList)
	return db_TodoList

@TodoList_router.put("/{id}")
async def update_TodoList(id: int, TodoList_put: TodoList_update, db: Session = Depends(get_db)):
	db_TodoList = db.query(TodoList).filter(TodoList.id == id).first()
	if not db_TodoList:
		raise HTTPException(status_code=404, detail="TodoList not found")
	for key, value in TodoList_update.model_dump().items():
		if value is not None:
			setattr(TodoList, key, value)
	db.commit()
	db.refresh(db_TodoList)
	return db_TodoList

@TodoList_router.delete("/{id}")
async def delete_TodoList(id: int, db: Session = Depends(get_db)):
	db_TodoList = db.query(TodoList).filter(TodoList.id == id).first()
	if not TodoList:
		raise HTTPException(status_code=404, detail="TodoList not found")
	db.delete(db_TodoList)
	db.commit()
	return {"message": "TodoList deleted successfully"}

@TodoList_router.get("/{name}")
async def get_TodoList_by_name(name: str, db: Session = Depends(get_db)):
	db_TodoList = db.query(TodoList).filter(TodoList.name == name).all()	
	if not db_TodoList:
		raise HTTPException(status_code=404, detail="TodoList not found")
	return db_TodoList
