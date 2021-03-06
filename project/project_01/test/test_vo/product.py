import cx_Oracle as oci

class Product:
    def __init__(self, id, name, price, cnt):
        self.id = id
        self.name = name
        self.price = price
        self.cnt = cnt
    @staticmethod
    def select_product():
        conn = oci.connect("hrr/hrr@192.168.56.1:1521/xe")
#       conn = oci.connect("scott/tiger@192.168.0.18:1521/orcl")
        cursor = conn.cursor()
        sql = """
            SELECT * FROM
            PRODUCT
        """
        cursor.execute(sql)
        datas = cursor.fetchall()
        resultList = []
        for data in datas:
            tempProduct = Product(data[0], data[1], data[2], data[3])
            resultList.append(tempProduct)

        cursor.close()
        conn.close()
        return resultList
    @staticmethod
    def insert_product(name, price, cnt):
        conn = oci.connect("hrr/hrr@192.168.56.1:1521/xe")
        cursor = conn.cursor()
        sql = """
            INSERT INTO product(PRODUCT_ID, PRODUCT_NAME, PRODUCT_PRICE, PRODUCT_CNT) 
            VALUES (PRODUCT_PRODUCT_ID.nextval, :name, :price, :cnt)
        """
        cursor.execute(sql, (name, price, cnt))
        cursor.close()
        conn.commit()
        conn.close()
    @staticmethod
    def update_product(productId, name, price, cnt):
        print("update_product 확인", "productId :", productId, "name :", name)
        conn = oci.connect("hrr/hrr@192.168.56.1:1521/xe")
        cursor = conn.cursor()
        sql = """
            UPDATE product 
            set PRODUCT_NAME = :name, PRODUCT_PRICE = :price, PRODUCT_CNT=:cnt
            where PRODUCT_ID = :productId
        """
        cursor.execute(sql, (name, price, cnt, productId))
        cursor.close()
        conn.commit()
        conn.close()
    @staticmethod
    def delete_product(productId):
        conn = oci.connect("hrr/hrr@192.168.56.1:1521/xe")
        cursor = conn.cursor()
        sql = """
            DELETE from product 
            where PRODUCT_ID = :productId
        """
        cursor.execute(sql, (productId, ))
        cursor.close()
        conn.commit()
        conn.close()
# 1. 데이터 받아와서 확인
# list = Product.select_product()
# for idx, item in enumerate(list):
#     print(idx, item.name)

# 2. 데이터 입력
#Product.insert_product("테스트제품1", 1500, 20)

# 3. 데이터 수정
# Product.update_product(102, "테스트제품11", 2500, 30)

# 4. 데이터 삭제
# Product.delete_product(102)