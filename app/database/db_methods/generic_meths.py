from peewee import *

from app.database.models import *


def add_record(model: BaseModel, **kwargs):
    try:
        model.create(**kwargs)
    except Exception as e:
        print(f"kwargs: {kwargs}, Error: {e}")

def delete_record(model: BaseModel, record_id: int):
    try:
        model.delete_by_id(record_id)
    except Exception as e:
        print(f"record_id: {record_id}, Error: {e}")

def update_record(model: BaseModel, update_id: int, **kwargs):
    try:
        model.update(**kwargs).where(model.id == update_id).execute()
    except Exception as e:
        print(f"record_id: {update_id}, kwargs: {kwargs}, Error: {e}")

def select_all(model: BaseModel):
    try:
        return model.select().execute()
    except Exception as e:
        print(f"Error: {e}")