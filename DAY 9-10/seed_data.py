# from faker import Faker
# import uuid
# from db import SessionLocal
# import crud, schemas

# faker=Faker()
# db=SessionLocal()
# data_size=500

# for _ in range(data_size):
#     items=[
#         {
#             "product_id":uuid.uuid4(),
#             "name":faker.word(),
#             "quantity":faker.random_int(1,5),
#             "price":round(faker.random_number(3)+faker.random.random(),2)
#         }
#         for __ in range(faker.random_int(1,4))
#     ]

#     order_in=schemas.OrderCreate(
#         customer_id=uuid.uuid4(),
#         items=[schemas.Item(**i) for i in items],
#         payment_method=faker.random_element(["credit_card", "paypal", "upi"]),
#         shipping_address=faker.address()
#     )

#     crud.createOrder(db,order_in)
# db.close()

# seed_data.py
import uuid
from faker import Faker
from pydantic import ValidationError

from db import engine, SessionLocal
from models import Base
from crud import create_order
from schemas import OrderCreate, Item

# ensure table exists
Base.metadata.create_all(bind=engine)

faker = Faker()
db = SessionLocal()
DATA_SIZE = 500

def main():
    seeded = 0

    for _ in range(DATA_SIZE):
        raw_items = []
        for __ in range(faker.random_int(1, 4)):
            raw_items.append({
                "product_id": uuid.uuid4(),
                "name": faker.pystr(min_chars=2, max_chars=100),
                "quantity": faker.random_int(1, 5),
                "price": round(faker.random_number(3) + faker.random.random(), 2),
            })

        try:
            items = [Item(**it) for it in raw_items]
            order_in = OrderCreate(
                customer_id=uuid.uuid4(),
                items=items,
                payment_method=faker.random_element(["credit_card", "paypal", "upi"]),
                shipping_address=faker.address(),
            )
            create_order(db, order_in)
            seeded += 1

        except ValidationError as ve:
            print("ValidationError—skipping:", ve)
            continue

    print(f"Seeded {seeded}/{DATA_SIZE} orders.")
    db.close()

if __name__ == "__main__":
    main()