-- 生成时间 2018/10/25
-- Server version: 8.0.11 MySQL Community Server - GPL
-- 命令行执行 source /Users/kobe24/Desktop/YeCloud/SQL/create_table.sql; 

create database user;
show databases;
use user;

create table userinfo (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

show tables;

insert into userinfo values(0,'zhc','zhc131180176');
select * from userinfo;

