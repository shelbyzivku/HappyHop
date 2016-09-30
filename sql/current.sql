-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema happyhopdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema happyhopdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `happyhopdb` DEFAULT CHARACTER SET utf8 ;
USE `happyhopdb` ;

-- -----------------------------------------------------
-- Table `happyhopdb`.`locations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `happyhopdb`.`locations` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `latitude` DOUBLE NOT NULL,
  `longitude` DOUBLE NOT NULL,
  `address1` VARCHAR(255) NOT NULL,
  `city` VARCHAR(255) NOT NULL,
  `state` VARCHAR(45) NOT NULL,
  `zip_code` INT(11) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 64
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `happyhopdb`.`hhprofiles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `happyhopdb`.`hhprofiles` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `locations_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`, `locations_id`),
  INDEX `fk_hhprofiles_locations1_idx` (`locations_id` ASC),
  CONSTRAINT `fk_hhprofiles_locations1`
    FOREIGN KEY (`locations_id`)
    REFERENCES `happyhopdb`.`locations` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 47
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `happyhopdb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `happyhopdb`.`users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(100) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `user_name` VARCHAR(255) NULL DEFAULT NULL,
  `facebook_id` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `happyhopdb`.`posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `happyhopdb`.`posts` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `content` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `users_id` INT(11) NOT NULL,
  `hhprofiles_id` INT(11) NOT NULL,
  `hhprofiles_locations_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`, `users_id`, `hhprofiles_id`, `hhprofiles_locations_id`),
  INDEX `fk_posts_users1_idx` (`users_id` ASC),
  INDEX `fk_posts_hhprofiles1_idx` (`hhprofiles_id` ASC, `hhprofiles_locations_id` ASC),
  CONSTRAINT `fk_posts_hhprofiles1`
    FOREIGN KEY (`hhprofiles_id` , `hhprofiles_locations_id`)
    REFERENCES `happyhopdb`.`hhprofiles` (`id` , `locations_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_posts_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `happyhopdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `happyhopdb`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `happyhopdb`.`comments` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `content` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `posts_id` INT(11) NOT NULL,
  `posts_users_id` INT(11) NOT NULL,
  `posts_hhprofiles_id` INT(11) NOT NULL,
  `posts_hhprofiles_locations_id` INT(11) NOT NULL,
  `users_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`, `posts_id`, `posts_users_id`, `posts_hhprofiles_id`, `posts_hhprofiles_locations_id`, `users_id`),
  INDEX `fk_comments_posts1_idx` (`posts_id` ASC, `posts_users_id` ASC, `posts_hhprofiles_id` ASC, `posts_hhprofiles_locations_id` ASC),
  INDEX `fk_comments_users1_idx` (`users_id` ASC),
  CONSTRAINT `fk_comments_posts1`
    FOREIGN KEY (`posts_id` , `posts_users_id` , `posts_hhprofiles_id` , `posts_hhprofiles_locations_id`)
    REFERENCES `happyhopdb`.`posts` (`id` , `users_id` , `hhprofiles_id` , `hhprofiles_locations_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `happyhopdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `happyhopdb`.`hhtime`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `happyhopdb`.`hhtime` (
  `id` INT(11) NOT NULL,
  `hhprofiles_id` INT(11) NOT NULL,
  `startime` DATETIME NOT NULL,
  `endtime` DATETIME NOT NULL,
  PRIMARY KEY (`id`, `hhprofiles_id`),
  INDEX `fk_hhtime_hhprofiles_idx` (`hhprofiles_id` ASC),
  CONSTRAINT `fk_hhtime_hhprofiles`
    FOREIGN KEY (`hhprofiles_id`)
    REFERENCES `happyhopdb`.`hhprofiles` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
