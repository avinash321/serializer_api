Serializer API

When you return data from a FastAPI endpoint, 
it automatically serializes (converts) the Python object into JSON using jsonable_encoder under the hood.


Python Type  -->    JSON Equivalent   --> jsonable_encoder

dict         -->    object  {"name": "Avinash"} → {"name": "Avinash"}
list         -->    array   ["apple", "banana"] → ["apple", "banana"]
tuple        -->    array   ("a", "b") → ["a", "b"]
set          -->    array   {"a", "b"} → ["a", "b"]
str          -->    string  "Avinash" → "Avinash"
int, float   -->    number  42 → 42
bool         -->    boolean True → true, False → false
None         -->    null    None → null

Pydantic models are automatically JSON-serializable — FastAPI calls .model_dump()
Pydantic Model / dataclass  -->   object  User(name="Avinash") → {"name": "Avinash"}
Custom Class (non-Pydantic) -->   Not JSON serializable  --> You must convert it manually (e.g. return my_obj.__dict__)
datetime, date, time        -->   string (ISO format)    --> datetime(2025, 10, 27) → "2025-10-27T00:00:00"
Decimal, UUID               -->   string or number (depending) --> Decimal("2.5") → 2.5, UUID("...") → "..."
