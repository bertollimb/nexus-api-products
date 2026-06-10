from fastapi import APIRouter, HTTPException, status, Response
from typing import Dict
from schemas.product_schema import ProductBase, ProductCreate, ProductResponse

router = APIRouter()

#DB fake (In memory)

products: Dict[int, dict] = {}

# GET PRODUCTS
@router.get('/', response_model=Dict[int, ProductResponse])
async def get_products():
    """
    Retrieve a list of all products.
    """
    return products

# GET PRODUCT
@router.get('/{product_id}', response_model=ProductResponse)
async def get_product(product_id: int):
    """
    Retrieve a single product by ID.
    """
    try:
        product = products[product_id]
        return {**product, "id": product_id}
    except KeyError:
        raise HTTPException(detail='Product not found', 
                            status_code=status.HTTP_404_NOT_FOUND)
    
# POST PRODUCTS
@router.post('/', status_code=status.HTTP_201_CREATED)
async def post_products(product: ProductCreate):
    """
    Create a new product.

    - **name**: product name
    - **price**: price of product
    - **description**: brief description of the product
    """

    next_id = max(products.keys()) + 1 if products else 1

    product_data = product.model_dump()
    product_data.pop("id", None)
    products[next_id] = product_data
    return product_data

# DELETE PRODUCTS
@router.delete('/{product_id}')
async def delete_product(product_id: int):
    """
    Delete a product by ID.
    """

    if product_id in products:
        del products[product_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(detail='Product not found.',
                             status_code=status.HTTP_404_NOT_FOUND)
    



