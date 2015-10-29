-- MySQL dump 10.13  Distrib 5.5.41, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: carloblog
-- ------------------------------------------------------
-- Server version	5.5.41-0ubuntu0.12.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `t_article`
--

DROP TABLE IF EXISTS `t_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) DEFAULT NULL,
  `article_type` varchar(200) NOT NULL,
  `title` varchar(200) NOT NULL,
  `tag_list` varchar(1024) DEFAULT NULL,
  `keywords` varchar(200) DEFAULT NULL,
  `abstract` text,
  `editor_code` varchar(64) DEFAULT NULL,
  `body_source` text,
  `body_default` text,
  `body_simple` text,
  `author_id` int(11) NOT NULL,
  `author_domain` varchar(200) NOT NULL,
  `author_name` varchar(200) DEFAULT NULL,
  `access_level` varchar(64) DEFAULT NULL,
  `access_passwd` varchar(200) DEFAULT NULL,
  `pv_num` int(11) DEFAULT NULL,
  `agree_num` int(11) DEFAULT NULL,
  `disagree_num` int(11) DEFAULT NULL,
  `comment_num` int(11) DEFAULT NULL,
  `collection_num` int(11) DEFAULT NULL,
  `pv_user_list` text,
  `agree_user_list` text,
  `disagree_user_list` text,
  `comment_user_list` text,
  `collection_user_list` text,
  `attachment_num` int(11) DEFAULT NULL,
  `attachment_size` varchar(200) DEFAULT NULL,
  `delete_flag` varchar(16) DEFAULT NULL,
  `delete_date` datetime DEFAULT NULL,
  `layout_width_start` int(11) DEFAULT NULL,
  `layout_width_end` int(11) DEFAULT NULL,
  `css_file_url` text,
  `from_url` text,
  `img` text,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_t_article_author_domain` (`author_domain`),
  KEY `ix_t_article_author_id` (`author_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `t_article_comment`
--

DROP TABLE IF EXISTS `t_article_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_article_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment_id` int(11) DEFAULT NULL,
  `article_id` int(11) NOT NULL,
  `sequence_of_article` int(11) NOT NULL,
  `to_comment_id` int(11) DEFAULT NULL,
  `to_sequence_of_article` int(11) DEFAULT NULL,
  `to_comment_body` text,
  `to_comment_delete_flag` varchar(16) DEFAULT NULL,
  `from_user_id` int(11) DEFAULT NULL,
  `from_user_domain` varchar(200) DEFAULT NULL,
  `from_user_name` varchar(200) DEFAULT NULL,
  `to_user_id` int(11) DEFAULT NULL,
  `to_user_domain` varchar(200) DEFAULT NULL,
  `to_user_name` varchar(200) DEFAULT NULL,
  `editor_code` varchar(64) DEFAULT NULL,
  `body_source` text,
  `body_default` text,
  `body_simple` text,
  `agree_num` int(11) DEFAULT NULL,
  `disagree_num` int(11) DEFAULT NULL,
  `agree_user_list` text,
  `disagree_user_list` text,
  `delete_flag` varchar(16) DEFAULT NULL,
  `delete_date` datetime DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_t_article_comment_article_id` (`article_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `t_doc_node`
--

DROP TABLE IF EXISTS `t_doc_node`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_doc_node` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `node_id` int(11) DEFAULT NULL,
  `node_name` varchar(200) NOT NULL,
  `node_type` varchar(64) DEFAULT NULL,
  `node_level` int(11) DEFAULT NULL,
  `sequence_in_level` int(11) DEFAULT NULL,
  `father_node_id` int(11) DEFAULT NULL,
  `article_id` int(11) DEFAULT NULL,
  `author_id` int(11) NOT NULL,
  `author_domain` varchar(200) NOT NULL,
  `author_name` varchar(200) DEFAULT NULL,
  `tag_list` varchar(1024) DEFAULT NULL,
  `keywords` varchar(200) DEFAULT NULL,
  `abstract` text,
  `access_level` varchar(64) DEFAULT NULL,
  `access_passwd` varchar(200) DEFAULT NULL,
  `pv_num` int(11) DEFAULT NULL,
  `praise_num` int(11) DEFAULT NULL,
  `dispraise_num` int(11) DEFAULT NULL,
  `comment_num` int(11) DEFAULT NULL,
  `collection_num` int(11) DEFAULT NULL,
  `attachment_num` int(11) DEFAULT NULL,
  `attachment_size` varchar(200) DEFAULT NULL,
  `delete_flag` varchar(16) DEFAULT NULL,
  `delete_date` datetime DEFAULT NULL,
  `layout_width_start` int(11) DEFAULT NULL,
  `layout_width_end` int(11) DEFAULT NULL,
  `css_file_url` text,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_t_doc_node_author_domain` (`author_domain`),
  KEY `ix_t_doc_node_author_id` (`author_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `t_global_nav`
--

DROP TABLE IF EXISTS `t_global_nav`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_global_nav` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `globalnav_id` int(11) DEFAULT NULL,
  `node_name` varchar(200) NOT NULL,
  `node_level` int(11) DEFAULT NULL,
  `sequence_in_level` int(11) DEFAULT NULL,
  `father_nav_id` int(11) DEFAULT NULL,
  `owner_role` varchar(64) DEFAULT NULL,
  `owner_id` int(11) NOT NULL,
  `owner_domain` varchar(200) NOT NULL,
  `owner_name` varchar(200) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_t_global_nav_owner_domain` (`owner_domain`),
  KEY `ix_t_global_nav_owner_id` (`owner_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `t_qiniu_storage`
--

DROP TABLE IF EXISTS `t_qiniu_storage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_qiniu_storage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storage_id` int(11) DEFAULT NULL,
  `owner_id` int(11) NOT NULL,
  `access_key` varchar(400) DEFAULT NULL,
  `secret_key` varchar(400) DEFAULT NULL,
  `bucket_name` varchar(200) DEFAULT NULL,
  `access_level` varchar(64) DEFAULT NULL,
  `use_flag` varchar(64) DEFAULT NULL,
  `download_url` varchar(1024) DEFAULT NULL,
  `private_download_url` varchar(1024) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `update_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_t_qiniu_storage_owner_id` (`owner_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `t_role`
--

DROP TABLE IF EXISTS `t_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_code` varchar(200) NOT NULL,
  `permissions` varchar(600) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `update_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `t_storage_file_key`
--

DROP TABLE IF EXISTS `t_storage_file_key`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_storage_file_key` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storage_file_key_id` int(11) DEFAULT NULL,
  `owner_id` int(11) NOT NULL,
  `storage_type` varchar(64) NOT NULL,
  `storage_id` int(11) NOT NULL,
  `for_what` varchar(64) NOT NULL,
  `for_what_id` int(11) DEFAULT NULL,
  `for_what_status` varchar(64) DEFAULT NULL,
  `original_name` text,
  `file_key` text,
  `file_type` varchar(64) DEFAULT NULL,
  `file_size` varchar(200) DEFAULT NULL,
  `download_url` text,
  `can_delete` varchar(64) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `update_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_t_storage_file_key_owner_id` (`owner_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `t_tag`
--

DROP TABLE IF EXISTS `t_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag_id` int(11) DEFAULT NULL,
  `tag_name` varchar(200) NOT NULL,
  `use_num` int(11) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `update_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_t_tag_tag_name` (`tag_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `t_test`
--

DROP TABLE IF EXISTS `t_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `test_body` varchar(600) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `update_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `t_user`
--

DROP TABLE IF EXISTS `t_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `email` varchar(200) NOT NULL,
  `role_code` varchar(200) DEFAULT NULL,
  `unique_domain` varchar(200) DEFAULT NULL,
  `nikename` varchar(200) DEFAULT NULL,
  `truename` varchar(200) DEFAULT NULL,
  `id_number` int(11) DEFAULT NULL,
  `phone` varchar(24) DEFAULT NULL,
  `wechat` varchar(200) DEFAULT NULL,
  `qq` varchar(24) DEFAULT NULL,
  `address` varchar(600) DEFAULT NULL,
  `storage_type` varchar(64) NOT NULL,
  `status` varchar(200) DEFAULT NULL,
  `last_ip` varchar(64) DEFAULT NULL,
  `last_login_time` datetime DEFAULT NULL,
  `passwd1` varchar(500) NOT NULL,
  `passwd2` varchar(500) DEFAULT NULL,
  `passwd3` varchar(500) DEFAULT NULL,
  `passwd4` varchar(500) DEFAULT NULL,
  `passwd5` varchar(500) DEFAULT NULL,
  `passwd6` varchar(500) DEFAULT NULL,
  `passwd7` varchar(500) DEFAULT NULL,
  `passwd8` varchar(500) DEFAULT NULL,
  `passwd9` varchar(500) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `update_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_t_user_unique_domain` (`unique_domain`),
  KEY `ix_t_user_email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-07-13 23:14:59
