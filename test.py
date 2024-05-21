from sqlalchemy import create_engine, text
import time
import random

random.seed(time.time())

time.sleep(5) # wait for the database to be ready

engine = create_engine("postgresql+psycopg2://user:password@db:5432/mydb")
conn = engine.connect()

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

    conn.execute(text("DROP TABLE IF EXISTS some_table"))
    conn.commit()

    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": random.randint(1, 100), "y": random.randint(1, 100)} for _ in range(3)],
    )
    conn.commit()

    # select all rows from the table
    result = conn.execute(text("SELECT * FROM some_table"))
    for row in result:
        print(f"x: {row.x}, y: {row.y}")

print("Done!")