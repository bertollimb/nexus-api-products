from typing import Optional, List
from pydantic import BaseModel, EmailStr, ConfigDict
from schemas.product_schema import ProductBase

class UserSchemaBase(BaseModel):
    id: Optional[int] = None
    name: str
    lastname: str
    email: EmailStr
    is_admin: bool = False

    model_config = ConfigDict(from_attributes=True)

class UserSchemaCreate(UserSchemaBase):
    password: str

class UserSchemaProducts(UserSchemaBase):
    products: Optional[List[ProductBase]]

class UserSchemaUp(UserSchemaBase):
    name: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_admin: Optional[bool] = None

    model_config = ConfigDict(from_attributes=True)

class UserSchemaResponse(UserSchemaBase):
    pass