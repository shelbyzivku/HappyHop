-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema happyhopdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema happyhopdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `happyhopdb` DEFAULT CHARACTER SET utf8 ;
USE `happyhopdb` ;

-- -----------------------------------------------------
-- Table `happyhopdb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `happyhopdb`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL COMMENT '	',
  `password` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `happyhopdb`.`locations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `happyhopdb`.`locations` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `street_number` INT NOT NULL,
  `street_name` VARCHAR(255) NOT NULL,
  `city` VARCHAR(255) NOT NULL,
  `state` VARCHAR(45) NOT NULL,
  `zip_code` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `happyhopdb`.`hhprofiles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `happyhopdb`.`hhprofiles` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` VARCHAR(45) NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `locations_id` INT NOT NULL,
  PRIMARY KEY (`id`, `locations_id`),
  INDEX `fk_hhprofiles_locations1_idx` (`locations_id` ASC),
  CONSTRAINT `fk_hhprofiles_locations1`
    FOREIGN KEY (`locations_id`)
    REFERENCES `happyhopdb`.`locations` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `happyhopdb`.`hhtime`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `happyhopdb`.`hhtime` (
  `id` INT NOT NULL,
  `hhprofiles_id` INT NOT NULL,
  `hhschedule` VARCHAR(9999) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`, `hhprofiles_id`),
  INDEX `fk_hhtime_hhprofiles_idx` (`hhprofiles_id` ASC),
  CONSTRAINT `fk_hhtime_hhprofiles`
    FOREIGN KEY (`hhprofiles_id`)
    REFERENCES `happyhopdb`.`hhprofiles` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `happyhopdb`.`posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `happyhopdb`.`posts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `users_id` INT NOT NULL,
  `hhprofiles_id` INT NOT NULL,
  `hhprofiles_locations_id` INT NOT NULL,
  PRIMARY KEY (`id`, `users_id`, `hhprofiles_id`, `hhprofiles_locations_id`),
  INDEX `fk_posts_users1_idx` (`users_id` ASC),
  INDEX `fk_posts_hhprofiles1_idx` (`hhprofiles_id` ASC, `hhprofiles_locations_id` ASC),
  CONSTRAINT `fk_posts_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `happyhopdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_posts_hhprofiles1`
    FOREIGN KEY (`hhprofiles_id` , `hhprofiles_locations_id`)
    REFERENCES `happyhopdb`.`hhprofiles` (`id` , `locations_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `happyhopdb`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `happyhopdb`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `posts_id` INT NOT NULL,
  `posts_users_id` INT NOT NULL,
  `posts_hhprofiles_id` INT NOT NULL,
  `posts_hhprofiles_locations_id` INT NOT NULL,
  `users_id` INT NOT NULL,
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
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
