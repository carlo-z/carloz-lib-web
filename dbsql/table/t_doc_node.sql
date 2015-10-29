DROP TABLE IF EXISTS `t_doc_node`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_doc_node` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `doc_id` int(11) NOT NULL,
  `doc_nav_id` int(11) DEFAULT NULL,
  `node_title` varchar(200) NOT NULL,
  `tag_list` varchar(1024) DEFAULT NULL,
  `order_by_owner` int(11) DEFAULT NULL,
  `keywords` varchar(200) DEFAULT NULL,
  `contents` varchar(1000) DEFAULT NULL,
  `img` varchar(2048) DEFAULT NULL,
  `abstract` varchar(400) DEFAULT NULL,
  `access_level` varchar(64) DEFAULT NULL,
  `access_passwd` varchar(200) DEFAULT NULL,
  `delete_flag` varchar(16) DEFAULT NULL,
  `delete_date` datetime DEFAULT NULL,
  `editor_code` varchar(64) DEFAULT NULL,
  `body_source` text,
  `body_default` text,
  `body_simple` text,
  `create_time` datetime DEFAULT NULL,
  `create_user_id` int(11) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `update_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_t_doc_node_doc_id` (`doc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;