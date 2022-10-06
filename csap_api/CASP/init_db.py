import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="casp",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

cur = conn.cursor()

#user queries
cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
                                 'name varchar (20) NOT NULL,'
                                 'email varchar (30) NOT NULL,'
                                 'password varchar (100) NOT NULL,'
                                 'role varchar (10) NOT NULL,'
                                 'key varchar (64) DEFAULT user NOT NULL,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

cur.execute('INSERT INTO users (name, email, password, role, key)'
            'VALUES (%s, %s, %s, %s, %s)',
            ('Bob',
             'bob@hackify.com',
             '717bff3c235ca17998f38ebcff4202b3',
             'superadmin',
             '5Jtg7P1djtYiCAIWX7ks5Oi5LrlY3ddYfTEMRAAgp9w')
            )

cur.execute('INSERT INTO users (name, email, password, role, key)'
            'VALUES (%s, %s, %s, %s, %s)',
            ('Tom',
             'tom@hackify.com',
             '11223344',
             'admin',
             '8OK3-M2H5UWyF60hiayz7ScGrcVfEEikEx97R0tHzsk')
            )

# Product queries
cur.execute('DROP TABLE IF EXISTS products;')
cur.execute('CREATE TABLE products (product_id serial PRIMARY KEY,'
                                 'product_name varchar (20) NOT NULL,'
                                 'price INT NOT NULL,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

conn.commit()
cur.close()
conn.close()