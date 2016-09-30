ALTER TABLE `happyhopdb`.`locations`
CHANGE COLUMN `street_number` `latitude` FLOAT NOT NULL ,
CHANGE COLUMN `street_name` `address1` VARCHAR(255) NOT NULL ,
ADD COLUMN `longitude` FLOAT NOT NULL AFTER `latitude`;
