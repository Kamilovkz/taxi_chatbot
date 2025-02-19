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

d2 = {
    "update_id": 894139849,
    "message": {
        "message_id": 43,
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
        "date": 1739883162,
        "sticker": {
            "width": 512,
            "height": 389,
            "emoji": "😏",
            "set_name": "Shitsshitsshitsshists",
            "is_animated": False,
            "is_video": False,
            "type": "regular",
            "thumbnail": {
                "file_id": "AAMCBAADGQEAAytntIKaKNhjBo3hjYT4m0lXiogi0AAC_QADa65eCRchwD8IWTtOAQAHbQADNgQ",
                "file_unique_id": "AQAD_QADa65eCXI",
                "file_size": 3618,
                "width": 128,
                "height": 97,
            },
            "thumb": {
                "file_id": "AAMCBAADGQEAAytntIKaKNhjBo3hjYT4m0lXiogi0AAC_QADa65eCRchwD8IWTtOAQAHbQADNgQ",
                "file_unique_id": "AQAD_QADa65eCXI",
                "file_size": 3618,
                "width": 128,
                "height": 97,
            },
            "file_id": "CAACAgQAAxkBAAMrZ7SCmijYYwaN4Y2E-JtJV4qIItAAAv0AA2uuXgkXIcA_CFk7TjYE",
            "file_unique_id": "AgAD_QADa65eCQ",
            "file_size": 24182,
        },
    },
}

d3 = {
    "update_id": 894139851,
    "message": {
        "message_id": 45,
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
        "date": 1739883696,
        "photo": [
            {
                "file_id": "AgACAgIAAxkBAAMtZ7SEsO8P8zLJQT0frQLeP0yuH18AAt3mMRshkqhJe0FU3_i92KMBAAMCAANzAAM2BA",
                "file_unique_id": "AQAD3eYxGyGSqEl4",
                "file_size": 1441,
                "width": 90,
                "height": 70,
            },
            {
                "file_id": "AgACAgIAAxkBAAMtZ7SEsO8P8zLJQT0frQLeP0yuH18AAt3mMRshkqhJe0FU3_i92KMBAAMCAANtAAM2BA",
                "file_unique_id": "AQAD3eYxGyGSqEly",
                "file_size": 23892,
                "width": 320,
                "height": 248,
            },
            {
                "file_id": "AgACAgIAAxkBAAMtZ7SEsO8P8zLJQT0frQLeP0yuH18AAt3mMRshkqhJe0FU3_i92KMBAAMCAAN4AAM2BA",
                "file_unique_id": "AQAD3eYxGyGSqEl9",
                "file_size": 114939,
                "width": 800,
                "height": 619,
            },
            {
                "file_id": "AgACAgIAAxkBAAMtZ7SEsO8P8zLJQT0frQLeP0yuH18AAt3mMRshkqhJe0FU3_i92KMBAAMCAAN5AAM2BA",
                "file_unique_id": "AQAD3eYxGyGSqEl-",
                "file_size": 200910,
                "width": 1170,
                "height": 906,
            },
        ],
        "caption": "SUPERASTANA",
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


class Photo(BaseModel):
    file_id: str
    file_unique_id: str
    file_size: int
    width: int
    height: int


class Message(BaseModel):
    message_id: int
    fromTg: From = Field(alias="from")
    chat: Chat
    date: int
    text: str = None
    sticker: dict = None
    photo: list[Photo] = None
    caption: str = None


class Answer(BaseModel):
    update_id: int
    message: Message


# obj = Answer.model_validate(d3)
# print(obj.message.photo[-1])
