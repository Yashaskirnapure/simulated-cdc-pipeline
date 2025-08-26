import time
import random
import psycopg2
from faker import Faker

fake = Faker()

conn = psycopg2.connect(
    host="localhost",
    port=5440,
    dbname="cdc_db",
    user="cdc_user",
    password="cdc_password"
)
conn.autocommit = True
cur = conn.cursor()

def insert_customer():
    name = fake.name()
    email = fake.unique.email()
    cur.execute(
        "INSERT INTO customers (name, email) VALUES (%s, %s) RETURNING id",
        (name, email)
    )
    return cur.fetchone()[0]

def insert_product():
    name = fake.word().capitalize()
    price = random.randint(10, 1000)
    stock = random.randint(1, 50)
    cur.execute(
        "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s) RETURNING id",
        (name, price, stock)
    )
    return cur.fetchone()[0]

def insert_order(customer_id, product_id):
    quantity = random.randint(1, 5)
    cur.execute("SELECT price FROM products WHERE id = %s", (product_id,))
    price = cur.fetchone()[0]
    total = price * quantity
    cur.execute(
        "INSERT INTO orders (customer_id, product_id, quantity, total) VALUES (%s, %s, %s, %s) RETURNING id",
        (customer_id, product_id, quantity, total)
    )
    return cur.fetchone()[0]

if __name__ == "__main__":
    product_ids = [insert_product() for _ in range(5)]
    customer_ids = [insert_customer() for _ in range(10)]
    order_ids = []

    while True:
        burst_size = random.randint(1, 5)

        for _ in range(burst_size):
            action = random.choices(
                ["order", "customer", "product"],
                weights=[0.80, 0.15, 0.05],
                k=1
            )[0]

            if action == "order" and customer_ids and product_ids:
                customer_id = random.choice(customer_ids)
                product_id = random.choice(product_ids)
                oid = insert_order(customer_id, product_id)
                order_ids.append(oid)
                print(f"[ORDER] customer {customer_id} -> product {product_id}")

            elif action == "customer":
                cid = insert_customer()
                customer_ids.append(cid)
                print(f"[CUSTOMER] new signup {cid}")

            elif action == "product":
                pid = insert_product()
                product_ids.append(pid)
                print(f"[PRODUCT] new product {pid}")

            time.sleep(random.uniform(0.1, 0.5))

        time.sleep(random.uniform(1, 6))