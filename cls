[33mcommit ccf1be2d50dd0ff52b977588eab288ee1354776c[m[33m ([m[1;36mHEAD[m[33m -> [m[1;32mrefactor/isolated-tests[m[33m, [m[1;31morigin/main[m[33m, [m[1;31morigin/HEAD[m[33m, [m[1;32mmain[m[33m)[m
Author: Matheus bertolli <matheusbertollianastacio@gmail.com>
Date:   Tue Jul 21 13:22:53 2026 +0100

    fix: correct typo in test function names

[1mdiff --git a/tests/test_products.py b/tests/test_products.py[m
[1mindex cf6da93..326dcb4 100644[m
[1m--- a/tests/test_products.py[m
[1m+++ b/tests/test_products.py[m
[36m@@ -1,5 +1,3 @@[m
[31m-import py[m
[31m-[m
 async def test_create_product(client):[m
     response = await client.post("/api/v1/products/", json={[m
         "name": "Notebook",[m
[36m@@ -23,7 +21,7 @@[m [masync def test_get_product_not_found(client):[m
     response = await client.get("/api/v1/products/10")[m
     assert response.status_code == 404[m
 [m
[31m-async def test_uptade_product_without_token(client):[m
[32m+[m[32masync def test_update_product_without_token(client):[m
     response = await client.put("/api/v1/products/1", json={[m
         "name": "Smartphone",[m
         "price": 1200.0,[m
[36m@@ -31,7 +29,7 @@[m [masync def test_uptade_product_without_token(client):[m
     })[m
     assert response.status_code == 401[m
 [m
[31m-async def test_uptade_product_with_token(client):[m
[32m+[m[32masync def test_update_product_with_token(client):[m
     await client.post("/api/v1/users/signup", json={[m
         "name": "Bruna",[m
         "lastname": "Bertolli",[m
[1mdiff --git a/tests/test_users.py b/tests/test_users.py[m
[1mindex d2b5882..6cbcee2 100644[m
[1m--- a/tests/test_users.py[m
[1m+++ b/tests/test_users.py[m
[36m@@ -1,5 +1,3 @@[m
[31m-import pytest [m
[31m-[m
 USER_DATA = {[m
     "name": "Matheus",[m
     "lastname": "Anastácio",[m
