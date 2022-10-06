CREATE DATABASE vulnapi;
use vulnapi;

CREATE TABLE `todos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user` varchar(45) DEFAULT NULL,
  `todo` varchar(45) DEFAULT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `todos`
VALUES 
    (1,'irfan','Buy a Lamp','2019-09-10 00:00:00'),
    (2,'imran','Buy groceries','2020-08-06 00:00:00'),
    (3,'yuga','Buy Laptop','2020-08-07 00:00:00');

