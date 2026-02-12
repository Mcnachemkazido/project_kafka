

def init_db(conn):
    conn.select_db("new")
    cursor = conn.cursor()
    cursor.execute("""CREATE DATABASE if NOT EXISTS new""")
    conn.select_db("new")

    cursor.execute("""CREATE TABLE if NOT EXISTS customers ( 
        type VARCHAR(200),
        customerNumber INT,
        customerName VARCHAR(200),
        contactLastName  VARCHAR(200),
        contactFirstName VARCHAR(200),
        phone VARCHAR(200),
        addressLine1 VARCHAR(200),
        addressLine2 VARCHAR(200),
        city VARCHAR(200),
        state VARCHAR(200),
        postalCode VARCHAR(200),
        country VARCHAR(200),
        salesRepEmployeeNumber INT ,
        creditLimit VARCHAR(200))""")

    cursor.execute("""
    CREATE TABLE if NOT EXISTS orders ( 
    type varchar(200),
    orderNumber INT,
    orderDate varchar(200),
    requiredDate varchar(200),
    shippedDate  varchar(200),
    status varchar(200),
    comments varchar(200),
    customerNumber INT)""")

    conn.commit()
    cursor.close()


def insert_customers(conn, item):
    conn.select_db("new")
    cursor = conn.cursor()
    sql = """INSERT INTO  customers ( type,  customerNumber ,customerName,
                 contactLastName  , contactFirstName, phone, addressLine1,  addressLine2
                , city,state, postalCode ,   country,salesRepEmployeeNumber , creditLimit)
                 VALUES (%s, %s,%s, %s,%s, %s,%s,%s, %s,%s, %s,%s, %s,%s)"""

    values = (item["type"], item["customerNumber"], item["customerName"],
              item["contactLastName"], item["contactFirstName"], item["phone"],
              item["addressLine1"],
              item["addressLine2"], item["city"], item["state"],
              item["postalCode"], item["country"], item["salesRepEmployeeNumber"],
              item["creditLimit"]
              )
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()


def insert_orders(conn, item):
    cursor = conn.cursor()
    sql = """INSERT INTO  orders  ( type,  orderNumber , orderDate,
                  requiredDate ,shippedDate, status, comments,  customerNumber )
                 VALUES (%s, %s,%s, %s,%s, %s,%s,%s)"""

    values = (item["type"], item["orderNumber"], item["orderDate"],
              item["requiredDate"], item["shippedDate"], item["status"],
              item["comments"],item["customerNumber"])

    cursor.execute(sql, values)
    conn.commit()
    cursor.close()

