from typing import List

from fastapi import APIRouter, HTTPException, Depends, status, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.product_model import ProductModel
from schemas.product_schema import ProductBase, ProductCreate, ProductResponse
from core.deps import get_session

router = APIRouter()

# GET PRODUCTS
@router.get('/', response_model=List[ProductResponse])
async def get_products(db: AsyncSession = Depends(get_session)):
    """
    Retrieve a list of all products.
    """

    async with db as session:
        query = select(ProductModel)
        result = await session.execute(query)
        products: List[ProductModel] = result.scalars().all()

        return products

# GET PRODUCT
@router.get('/{product_id}', response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def get_product(product_id: int, db: AsyncSession = Depends(get_session)):
    """
    Retrieve a single product by ID.
    """
    async with db as session:
        query = select(ProductModel).filter(ProductModel.id == product_id)
        result = await session.execute(query)
        product = result.scalars().unique().one_or_none()

        if product:
            return product
        else:
            raise HTTPException(detail='product not found.', 
                                status_code=status.HTTP_404_NOT_FOUND)
    
# POST PRODUCTS
@router.post('/', response_model=ProductResponse , status_code=status.HTTP_201_CREATED)
async def post_products(product: ProductCreate, db: AsyncSession = Depends(get_session)):
    """
    Create a new product.

    - **name**: product name
    - **price**: price of product
    - **description**: brief description of the product
    """

    new_product = ProductModel(name=product.name, price=product.price, description=product.description)
    
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)

    return new_product

# DELETE PRODUCTS
@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, db: AsyncSession = Depends(get_session)):
    """
    Delete a product by ID.
    """

    async with db as session:
        query = select(ProductModel).filter(ProductModel.id == product_id)
        result = await session.execute(query)
        product_del: ProductModel = result.scalars().unique().one_or_none()

        if product_del:
            await session.delete(product_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Product not found.',
                                 status_code=status.HTTP_404_NOT_FOUND)
        

   
    



