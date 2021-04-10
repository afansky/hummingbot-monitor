create DATABASE hummingbot;

USE hummingbot;

create TABLE `bots` (
  `timeof` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `name` varchar(60) NOT NULL,
  `trades` int NOT NULL,
  KEY `index1` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;