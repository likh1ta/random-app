from fastapi import APIRouter
from models.choices import Choice
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId
router =APIRouter()
#post request method
@router.post("/")
async def post_choice(choice:Choice):
    choice_data = dict(choice)
    choice_data["selected_item"] = choice.selected_item
    collection_name.insert_one(choice_data)
    return choice_data["selected_item"] 
