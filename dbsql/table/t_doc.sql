DROP TABLE IF EXISTS `t_doc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_doc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `access_level` varchar(64) DEFAULT NULL,
  `access_passwd` varchar(200) DEFAULT NULL,
  `author_id` int(11) NOT NULL,
  `author_name` varchar(200) DEFAULT NULL,
  `pv_num` int(11) DEFAULT NULL,
  `praise_num` int(11) DEFAULT NULL,
  `dispraise_num` int(11) DEFAULT NULL,
  `delete_flag` varchar(16) DEFAULT NULL,
  `delete_date` datetime DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `update_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_t_doc_author_id` (`author_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
