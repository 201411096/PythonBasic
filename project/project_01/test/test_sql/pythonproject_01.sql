CREATE TABLE PRODUCT(
    PRODUCT_ID NUMBER,
    PRODUCT_NAME VARCHAR2(40),
    PRODUCT_PRICE NUMBER,
    PRODUCT_CNT NUMBER,
    CONSTRAINT PRODUCT_PK PRIMARY KEY(PRODUCT_ID)
);

CREATE TABLE ACCOUNT(
    ACCOUNT_ID VARCHAR2(40),
    ACCOUNT_PW VARCHAR2(40),
    ACCOUNT_ADMIN_FLAG VARCHAR2(2),
    CONSTRAINT ACCOUNT_PK PRIMARY KEY(ACCOUNT_ID)
);

ALTER TABLE ACCOUNT ADD ACCOUNT_ADMIN_FLAG VARCHAR2(2);
CREATE SEQUENCE PRODUCT_PRODUCT_ID
START WITH 100;

INSERT INTO ACCOUNT(ACCOUNT_ID, ACCOUNT_PW, ACCOUNT_ADMIN_FLAG) VALUES('admin', '1234', '1');
INSERT INTO ACCOUNT(ACCOUNT_ID, ACCOUNT_PW, ACCOUNT_ADMIN_FLAG) VALUES('aaa', '1234', '0');

INSERT INTO product(PRODUCT_ID, PRODUCT_NAME, PRODUCT_PRICE, PRODUCT_CNT) VALUES (1, '力前1', 3000, 100);
INSERT INTO product(PRODUCT_ID, PRODUCT_NAME, PRODUCT_PRICE, PRODUCT_CNT) VALUES (2, '力前2', 4000, 100);
INSERT INTO product(PRODUCT_ID, PRODUCT_NAME, PRODUCT_PRICE, PRODUCT_CNT) VALUES (3, '力前3', 2000, 100);
INSERT INTO product(PRODUCT_ID, PRODUCT_NAME, PRODUCT_PRICE, PRODUCT_CNT) VALUES (4, '力前4', 1000, 100);
INSERT INTO product(PRODUCT_ID, PRODUCT_NAME, PRODUCT_PRICE, PRODUCT_CNT) VALUES (5, '力前5', 5000, 100);
INSERT INTO product(PRODUCT_ID, PRODUCT_NAME, PRODUCT_PRICE, PRODUCT_CNT) VALUES (6, '力前6', 6000, 100);
INSERT INTO product(PRODUCT_ID, PRODUCT_NAME, PRODUCT_PRICE, PRODUCT_CNT) VALUES (7, '力前7', 7000, 100);
INSERT INTO product(PRODUCT_ID, PRODUCT_NAME, PRODUCT_PRICE, PRODUCT_CNT) VALUES (8, '力前8', 8000, 100);
INSERT INTO product(PRODUCT_ID, PRODUCT_NAME, PRODUCT_PRICE, PRODUCT_CNT) VALUES (9, '力前9', 9000, 100);