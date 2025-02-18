from pydantic import BaseModel, Field


d = {
    "update_id": 894139834,
    "message": {
        "message_id": 12,
        "from": {
            "id": 398685944,
            "is_bot": False,
            "first_name": "Melon",
            "username": "qweerty01",
            "language_code": "en",
        },
        "chat": {
            "id": 398685944,
            "first_name": "Melon",
            "username": "qweerty01",
            "type": "private",
        },
        "date": 1739854810,
        "text": "sada",
    },
}


class From(BaseModel):
    from_id: int = Field(alias="id")
    is_bot: bool
    first_name: str
    username: str
    last_name: str = None
    language_code: str


class Chat(BaseModel):
    chat_id: int = Field(alias="id")
    first_name: str
    username: str
    type: str


class Message(BaseModel):
    message_id: int
    fromTg: From = Field(alias="from")
    chat: Chat
    date: int
    text: str


class Answer(BaseModel):
    update_id: int
    message: Message


# obj = Answer.model_validate(d)
# print(obj.message.chat.chat_id)
