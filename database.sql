CREATE DATABASE library_db;
USE library_db;
CREATE TABLE Books(book_id INT auto_increment primary key,
title VARCHAR(200),
author VARCHAR(100),
genre VARCHAR(50),
total_copies INT,
available_copies INT);

CREATE TABLE Members(member_id INT auto_increment primary key,
name VARCHAR(100),
email VARCHAR(100),
phone VARCHAR(15),
join_date DATE);

CREATE TABLE Transactions(txn_id INT auto_increment primary key,
book_id INT,
member_id INT,
issue_date DATE,
due_date DATE,
return_date DATE,
fine DECIMAL(6,2),
foreign key (book_id) references Books(book_id),
foreign key (member_id) references Members(member_id)
);
