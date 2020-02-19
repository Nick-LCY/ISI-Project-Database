CREATE TABLE product (
	id int(8) AUTO_INCREMENT,
	name varchar(256) NOT NULL,
	category varchar(256) NOT NULL,
	price decimal(10, 2) NOT NULL,
	out_of_stock boolean NOT NULL DEFAULT true,
	thumbnail_location varchar(256) NOT NULL,
	CONSTRAINT product_id_pk PRIMARY KEY(id)
);
CREATE TABLE user (
	id int(8) AUTO_INCREMENT,
	name varchar(64) NOT NULL,
	email varchar(64) NOT NULL,
	pwd varchar(256) NOT NULL,
	shipping_addr varchar(256) NOT NULL,
	is_vendor boolean NOT NULL DEFAULT false,
	token varchar(64),
	create_time varchar(64),
	CONSTRAINT user_id_pk PRIMARY KEY(id),
	CONSTRAINT user_email_uc UNIQUE (email)
);
CREATE TABLE product_photograph (
	id int(8) AUTO_INCREMENT,
	file_location varchar(256) NOT NULL,
	sequence int(4) NOT NULL,
	product_id int(8) NOT NULL,
	CONSTRAINT product_photograph_id_pk PRIMARY KEY(id),
	CONSTRAINT product_photograph_sequence_product_id_unique
	UNIQUE(sequence, product_id),
	CONSTRAINT product_photograph_product_id_fk FOREIGN KEY(product_id)
	REFERENCES product(id)
);
CREATE TABLE product_description (
	id int(8) AUTO_INCREMENT,
	attribute_name varchar(256) NOT NULL,
	attribute_value varchar(256) NOT NULL,
	sequence int(4) NOT NULL,
	product_id int(8) NOT NULL,
	CONSTRAINT product_description_id_pk PRIMARY KEY(id),
	CONSTRAINT product_description_sequence_product_id_unique
	UNIQUE(sequence, product_id),
	CONSTRAINT product_description_product_id_fk
	FOREIGN KEY(product_id) REFERENCES product(id)
);
CREATE TABLE notification (
	id int(8) AUTO_INCREMENT,
	content varchar(1024) NOT NULL,
	is_read boolean NOT NULL DEFAULT false,
	user_id int(8) NOT NULL,
	CONSTRAINT notification_id_pk PRIMARY KEY(id),
	CONSTRAINT notification_user_id_fk
	FOREIGN KEY(user_id) REFERENCES user(id)
);
CREATE TABLE shopping_cart_item (
	user_id int(8),
	product_id int(8),
	quantity int(4) NOT NULL,
	CONSTRAINT shopping_cart_item_product_id_user_id_pk
	PRIMARY KEY(product_id, user_id),
	CONSTRAINT shopping_cart_item_user_id_fk
	FOREIGN KEY(user_id) REFERENCES user(id),
	CONSTRAINT shopping_cart_item_product_id_fk
	FOREIGN KEY(product_id) REFERENCES product(id)
);
CREATE TABLE purchase_order (
	id int(8),
	total_amount decimal(10, 2) NOT NULL,
	purchase_date varchar(64) NOT NULL,
	shipment_date varchar(64),
	cancel_date varchar(64),
	cancelled_by int(1),
	status int(1) NOT NULL,
	user_id int(8) NOT NULL,
	CONSTRAINT purchse_order_id_pk PRIMARY KEY(id),
	CONSTRAINT purchase_order_user_id_fk
	FOREIGN KEY(user_id) REFERENCES user(id)
);
CREATE TABLE purchase_detail (
	purchase_order_id int(8),
	product_id int(8),
	product_name varchar(256) NOT NULL,
	product_price decimal(10, 2) NOT NULL,
	quantity int(4) NOT NULL,
	CONSTRAINT purchase_detail_purchase_order_id_product_id_pk
	PRIMARY KEY(purchase_order_id, product_id),
	CONSTRAINT purchase_detail_purchase_order_id_fk
	FOREIGN KEY(purchase_order_id) REFERENCES purchase_order(id)
);
CREATE TABLE review (
	product_id int(8),
	purchase_order_id int(8),
	stars int (1) NOT NULL DEFAULT 5,
	review varchar(1024),
	CONSTRAINT reveiw_product_id_purchase_order_id_pk
	PRIMARY KEY(purchase_order_id, product_id),
	CONSTRAINT review_pks_fk FOREIGN KEY(purchase_order_id, product_id)
	REFERENCES purchase_detail(purchase_order_id, product_id)
);