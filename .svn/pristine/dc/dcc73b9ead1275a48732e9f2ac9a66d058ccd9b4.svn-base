DROP TABLE IF EXISTS `t_user_storage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_user_storage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_storage_id` int(11) DEFAULT NULL,
  `owner_id` int(11) NOT NULL,
  `storage_type` varchar(200) DEFAULT NULL,
  `access_key` varchar(400) DEFAULT NULL,
  `secret_key` varchar(400) DEFAULT NULL,
  `bucket_name` varchar(200) DEFAULT NULL,
  `access_level` varchar(64) DEFAULT NULL,
  `use_flag` varchar(64) DEFAULT NULL,
  `download_url` varchar(1024) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `update_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_t_user_storage_owner_id` (`owner_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;