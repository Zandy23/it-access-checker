-- IT Access Checker Database
-- Created by Zandy - Phoenix, SA
CREATE DATABASE IT_Access_DB;
GO
USE IT_Access_DB;
GO
CREATE TABLE Users (
  ID INT PRIMARY KEY,
  Name VARCHAR(50),
  Age INT,
  HasAccess VARCHAR(10)
);
GO
INSERT INTO Users VALUES (1, 'Zandy', 22, 'YES');
INSERT INTO Users VALUES (2, 'TestUser', 16, 'NO');
GO
SELECT * FROM Users;