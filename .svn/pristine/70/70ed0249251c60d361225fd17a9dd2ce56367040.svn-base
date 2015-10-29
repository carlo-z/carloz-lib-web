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
) ENGINE=InnoDB AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;