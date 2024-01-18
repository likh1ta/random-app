def individual_serial(choice)->dict:
   return{
    "id": str(choice["_id"]),
    "category":choice["category"],
    "items":choice["items"],
    "selected_item":choice["selected_item"]
}
def list_serial(choices)-> list:
   return[individual_serial(choice) for choice in choices]
