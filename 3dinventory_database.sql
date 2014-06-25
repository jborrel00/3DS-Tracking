create database 3dsystems;
use 3dsystems
create table 3ds_tracking (item varchar(30), item_id varchar(30), event varchar(30), in_out varchar(10), time date, location varchar(30), contact varchar(30), id int primary key auto_increment);
insert into 3ds_tracking (item,item_id,event,in_out,time,location,contact) values ('sense','sense-h','comiccon','out',current_date(),'san diego','joeb');
