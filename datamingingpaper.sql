/*
Navicat MySQL Data Transfer

Source Server         : Django项目部署
Source Server Version : 50560
Source Host           : 10.0.86.245:3306
Source Database       : datamingingpaper

Target Server Type    : MYSQL
Target Server Version : 50560
File Encoding         : 65001

Date: 2019-06-01 12:51:31
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`) USING BTREE,
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissions_ibfk_1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_ibfk_2` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`) USING BTREE,
  CONSTRAINT `auth_permission_ibfk_1` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '4', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '4', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '4', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can view content type', '4', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('17', 'Can add session', '5', 'add_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can change session', '5', 'change_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete session', '5', 'delete_session');
INSERT INTO `auth_permission` VALUES ('20', 'Can view session', '5', 'view_session');
INSERT INTO `auth_permission` VALUES ('21', 'Can add 用户信息', '6', 'add_userprofile');
INSERT INTO `auth_permission` VALUES ('22', 'Can change 用户信息', '6', 'change_userprofile');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete 用户信息', '6', 'delete_userprofile');
INSERT INTO `auth_permission` VALUES ('24', 'Can add 邮箱验证码', '7', 'add_emailverifyrecord');
INSERT INTO `auth_permission` VALUES ('25', 'Can change 邮箱验证码', '7', 'change_emailverifyrecord');
INSERT INTO `auth_permission` VALUES ('26', 'Can delete 邮箱验证码', '7', 'delete_emailverifyrecord');
INSERT INTO `auth_permission` VALUES ('27', 'Can view 邮箱验证码', '7', 'view_emailverifyrecord');
INSERT INTO `auth_permission` VALUES ('28', 'Can view 用户信息', '6', 'view_userprofile');
INSERT INTO `auth_permission` VALUES ('29', 'Can add Bookmark', '8', 'add_bookmark');
INSERT INTO `auth_permission` VALUES ('30', 'Can change Bookmark', '8', 'change_bookmark');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete Bookmark', '8', 'delete_bookmark');
INSERT INTO `auth_permission` VALUES ('32', 'Can add User Setting', '9', 'add_usersettings');
INSERT INTO `auth_permission` VALUES ('33', 'Can change User Setting', '9', 'change_usersettings');
INSERT INTO `auth_permission` VALUES ('34', 'Can delete User Setting', '9', 'delete_usersettings');
INSERT INTO `auth_permission` VALUES ('35', 'Can add User Widget', '10', 'add_userwidget');
INSERT INTO `auth_permission` VALUES ('36', 'Can change User Widget', '10', 'change_userwidget');
INSERT INTO `auth_permission` VALUES ('37', 'Can delete User Widget', '10', 'delete_userwidget');
INSERT INTO `auth_permission` VALUES ('38', 'Can add log entry', '11', 'add_log');
INSERT INTO `auth_permission` VALUES ('39', 'Can change log entry', '11', 'change_log');
INSERT INTO `auth_permission` VALUES ('40', 'Can delete log entry', '11', 'delete_log');
INSERT INTO `auth_permission` VALUES ('41', 'Can view Bookmark', '8', 'view_bookmark');
INSERT INTO `auth_permission` VALUES ('42', 'Can view log entry', '11', 'view_log');
INSERT INTO `auth_permission` VALUES ('43', 'Can view User Setting', '9', 'view_usersettings');
INSERT INTO `auth_permission` VALUES ('44', 'Can view User Widget', '10', 'view_userwidget');
INSERT INTO `auth_permission` VALUES ('45', 'Can add captcha store', '12', 'add_captchastore');
INSERT INTO `auth_permission` VALUES ('46', 'Can change captcha store', '12', 'change_captchastore');
INSERT INTO `auth_permission` VALUES ('47', 'Can delete captcha store', '12', 'delete_captchastore');
INSERT INTO `auth_permission` VALUES ('48', 'Can view captcha store', '12', 'view_captchastore');
INSERT INTO `auth_permission` VALUES ('49', 'Can add 机构国家分布表', '13', 'add_affdistribute');
INSERT INTO `auth_permission` VALUES ('50', 'Can change 机构国家分布表', '13', 'change_affdistribute');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete 机构国家分布表', '13', 'delete_affdistribute');
INSERT INTO `auth_permission` VALUES ('52', 'Can view 机构国家分布表', '13', 'view_affdistribute');

-- ----------------------------
-- Table structure for `captcha_captchastore`
-- ----------------------------
DROP TABLE IF EXISTS `captcha_captchastore`;
CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hashkey` (`hashkey`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of captcha_captchastore
-- ----------------------------
INSERT INTO `captcha_captchastore` VALUES ('66', 'RWME', 'rwme', '9745237a5f9508a0b9050976a32ee2dc2e3ca944', '2019-05-24 14:16:53.000000');
INSERT INTO `captcha_captchastore` VALUES ('67', 'VGXF', 'vgxf', '22b70db308e83989e07fbc0f7f7e379bfb677d27', '2019-06-01 11:37:28.000000');

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`) USING BTREE,
  KEY `django_admin_log_user_id_c564eba6_fk_users_userprofile_id` (`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_ibfk_1` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('12', 'captcha', 'captchastore');
INSERT INTO `django_content_type` VALUES ('4', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('5', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('13', 'statistic', 'affdistribute');
INSERT INTO `django_content_type` VALUES ('7', 'users', 'emailverifyrecord');
INSERT INTO `django_content_type` VALUES ('6', 'users', 'userprofile');
INSERT INTO `django_content_type` VALUES ('8', 'xadmin', 'bookmark');
INSERT INTO `django_content_type` VALUES ('11', 'xadmin', 'log');
INSERT INTO `django_content_type` VALUES ('9', 'xadmin', 'usersettings');
INSERT INTO `django_content_type` VALUES ('10', 'xadmin', 'userwidget');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-03-03 16:47:07.012991');
INSERT INTO `django_migrations` VALUES ('2', 'contenttypes', '0002_remove_content_type_name', '2019-03-03 16:47:09.479043');
INSERT INTO `django_migrations` VALUES ('3', 'auth', '0001_initial', '2019-03-03 16:47:16.846500');
INSERT INTO `django_migrations` VALUES ('4', 'auth', '0002_alter_permission_name_max_length', '2019-03-03 16:47:17.696202');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0003_alter_user_email_max_length', '2019-03-03 16:47:17.742179');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0004_alter_user_username_opts', '2019-03-03 16:47:17.997131');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0005_alter_user_last_login_null', '2019-03-03 16:47:18.281947');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0006_require_contenttypes_0002', '2019-03-03 16:47:18.362898');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0007_alter_validators_add_error_messages', '2019-03-03 16:47:18.638084');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0008_alter_user_username_max_length', '2019-03-03 16:47:18.886060');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0009_alter_user_last_name_max_length', '2019-03-03 16:47:18.938074');
INSERT INTO `django_migrations` VALUES ('12', 'users', '0001_initial', '2019-03-03 16:47:29.540537');
INSERT INTO `django_migrations` VALUES ('13', 'admin', '0001_initial', '2019-03-03 16:47:33.262424');
INSERT INTO `django_migrations` VALUES ('14', 'admin', '0002_logentry_remove_auto_add', '2019-03-03 16:47:33.359377');
INSERT INTO `django_migrations` VALUES ('15', 'captcha', '0001_initial', '2019-03-03 16:47:34.527321');
INSERT INTO `django_migrations` VALUES ('16', 'sessions', '0001_initial', '2019-03-03 16:47:35.846716');
INSERT INTO `django_migrations` VALUES ('17', 'users', '0002_auto_20190218_1650', '2019-03-03 16:47:36.055731');
INSERT INTO `django_migrations` VALUES ('18', 'users', '0003_banner_emailverifyrecord', '2019-03-03 16:47:37.780696');
INSERT INTO `django_migrations` VALUES ('19', 'users', '0004_auto_20190219_2200', '2019-03-03 16:47:38.009408');
INSERT INTO `django_migrations` VALUES ('20', 'users', '0005_auto_20190223_2347', '2019-03-03 16:47:38.054384');
INSERT INTO `django_migrations` VALUES ('21', 'users', '0006_delete_banner', '2019-03-03 16:47:38.481137');
INSERT INTO `django_migrations` VALUES ('22', 'xadmin', '0001_initial', '2019-03-03 16:47:51.794849');
INSERT INTO `django_migrations` VALUES ('23', 'xadmin', '0002_log', '2019-03-03 16:47:57.203146');
INSERT INTO `django_migrations` VALUES ('24', 'xadmin', '0003_auto_20160715_0100', '2019-03-03 16:48:02.145478');
INSERT INTO `django_migrations` VALUES ('25', 'users', '0007_auto_20190303_1706', '2019-03-03 17:06:45.865178');
INSERT INTO `django_migrations` VALUES ('26', 'statistic', '0001_initial', '2019-03-25 00:29:09.929313');
INSERT INTO `django_migrations` VALUES ('27', 'statistic', '0002_affdistribute_count11', '2019-03-25 17:09:22.342530');
INSERT INTO `django_migrations` VALUES ('28', 'statistic', '0002_affdistribute_count', '2019-03-25 17:14:05.681162');
INSERT INTO `django_migrations` VALUES ('29', 'statistic', '0003_delete_affdistribute', '2019-03-25 17:15:25.921679');
INSERT INTO `django_migrations` VALUES ('30', 'statistic', '0004_affdistribute', '2019-03-25 17:16:22.142994');
INSERT INTO `django_migrations` VALUES ('31', 'statistic', '0005_delete_affdistribute', '2019-03-25 17:17:02.965977');
INSERT INTO `django_migrations` VALUES ('32', 'statistic', '0002_delete_affdistribute', '2019-03-25 17:20:45.954786');
INSERT INTO `django_migrations` VALUES ('33', 'statistic', '0003_affdistribute', '2019-03-25 18:01:21.632490');
INSERT INTO `django_migrations` VALUES ('34', 'users', '0008_auto_20190424_1701', '2019-04-24 17:01:46.104556');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('3euvrpkzrug5dutt0dsjs7d7xvgcunxv', 'NWY3NGQ2MGY5ZjgzMzM0NzI0NGQ5MTgwOTA3ZjBiNmMxNjUzODFlYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3MuQ3VzdG9tQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjE1MmYwOTI1ZWE1MmMxMDZlMGYyYmFlMzhiYzk3N2I3YmYzZjk4M2MiLCJMSVNUX1FVRVJZIjpbWyJ1c2VycyIsInVzZXJwcm9maWxlIl0sIiJdfQ==', '2019-03-20 13:11:29.385861');
INSERT INTO `django_session` VALUES ('gxobrguun0stuqwm6gpqfggqwliwy9lp', 'NWY3NGQ2MGY5ZjgzMzM0NzI0NGQ5MTgwOTA3ZjBiNmMxNjUzODFlYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3MuQ3VzdG9tQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjE1MmYwOTI1ZWE1MmMxMDZlMGYyYmFlMzhiYzk3N2I3YmYzZjk4M2MiLCJMSVNUX1FVRVJZIjpbWyJ1c2VycyIsInVzZXJwcm9maWxlIl0sIiJdfQ==', '2019-03-26 11:28:01.208786');
INSERT INTO `django_session` VALUES ('h3h4ail94hklnaivqtzecsq8oseo0m7f', 'MTM4YjAxNWRkZDUxYzg0MGY5MDMyYjc1MzdjMjcxNTFkMDE1MDYxMjp7Il9hdXRoX3VzZXJfaWQiOiIxOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJzLnZpZXdzLkN1c3RvbUJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NzU2ZDc3MzFkNGI4MjNmYWExYWEyMDQwY2I3YmU0Y2NmNzAyODEyIiwibmF2X21lbnUiOiJbe1widGl0bGVcIjogXCJcdTc1MjhcdTYyMzdcdTdiYTFcdTc0MDZcIiwgXCJtZW51c1wiOiBbe1widGl0bGVcIjogXCJcdTc1MjhcdTYyMzdcdTRmZTFcdTYwNmZcIiwgXCJ1cmxcIjogXCIveGFkbWluL3VzZXJzL3VzZXJwcm9maWxlL1wiLCBcImljb25cIjogXCJmYSBmYS11c2VyXCIsIFwib3JkZXJcIjogM30sIHtcInRpdGxlXCI6IFwiXHU5MGFlXHU3YmIxXHU5YThjXHU4YmMxXHU3ODAxXCIsIFwidXJsXCI6IFwiL3hhZG1pbi91c2Vycy9lbWFpbHZlcmlmeXJlY29yZC9cIiwgXCJpY29uXCI6IG51bGwsIFwib3JkZXJcIjogNX1dLCBcImZpcnN0X2ljb25cIjogXCJmYSBmYS11c2VyXCIsIFwiZmlyc3RfdXJsXCI6IFwiL3hhZG1pbi91c2Vycy91c2VycHJvZmlsZS9cIn0sIHtcInRpdGxlXCI6IFwiXHU3YmExXHU3NDA2XCIsIFwibWVudXNcIjogW3tcInRpdGxlXCI6IFwiXHU2NWU1XHU1ZmQ3XHU4YmIwXHU1ZjU1XCIsIFwidXJsXCI6IFwiL3hhZG1pbi94YWRtaW4vbG9nL1wiLCBcImljb25cIjogXCJmYSBmYS1jb2dcIiwgXCJvcmRlclwiOiA3fV0sIFwiZmlyc3RfaWNvblwiOiBcImZhIGZhLWNvZ1wiLCBcImZpcnN0X3VybFwiOiBcIi94YWRtaW4veGFkbWluL2xvZy9cIn0sIHtcInRpdGxlXCI6IFwiXHU4YmE0XHU4YmMxXHU1NDhjXHU2Mzg4XHU2NzQzXCIsIFwibWVudXNcIjogW3tcInRpdGxlXCI6IFwiXHU3ZWM0XCIsIFwidXJsXCI6IFwiL3hhZG1pbi9hdXRoL2dyb3VwL1wiLCBcImljb25cIjogXCJmYSBmYS1ncm91cFwiLCBcIm9yZGVyXCI6IDJ9LCB7XCJ0aXRsZVwiOiBcIlx1Njc0M1x1OTY1MFwiLCBcInVybFwiOiBcIi94YWRtaW4vYXV0aC9wZXJtaXNzaW9uL1wiLCBcImljb25cIjogXCJmYSBmYS1sb2NrXCIsIFwib3JkZXJcIjogNH1dLCBcImZpcnN0X2ljb25cIjogXCJmYSBmYS1ncm91cFwiLCBcImZpcnN0X3VybFwiOiBcIi94YWRtaW4vYXV0aC9ncm91cC9cIn1dIiwiTElTVF9RVUVSWSI6W1sidXNlcnMiLCJlbWFpbHZlcmlmeXJlY29yZCJdLCIiXX0=', '2019-06-15 11:48:51.000000');
INSERT INTO `django_session` VALUES ('n7fcz82kh6y6ykcccnstc5257fpon2pp', 'YmJkMmMzNDAyZTQ4NGYyNWI2ZjRjZDQ2MGI1ZjcxN2U2ZjJkZDdiMjp7Il9hdXRoX3VzZXJfaWQiOiIxOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJzLnZpZXdzLkN1c3RvbUJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NzU2ZDc3MzFkNGI4MjNmYWExYWEyMDQwY2I3YmU0Y2NmNzAyODEyIn0=', '2019-05-17 14:30:10.753544');
INSERT INTO `django_session` VALUES ('sbnwas7uh2tqyopc4e9t8qaxnm66aap1', 'MGYyZTBhMjIxOGYyZDI2NmNhZGQ1N2E1OWU4N2MzZmVkOGM5MmFlMTp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJzLnZpZXdzLkN1c3RvbUJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiODc4YzhmMGE2M2VlMzNiNTYyYWM4NjE1OWMyNGYxMzQ4ZTVjOTVmIn0=', '2019-03-20 14:16:03.529972');
INSERT INTO `django_session` VALUES ('v4xjafi263z2lqirgsraebvj2kbpj177', 'NzQwMDE5ODc3NDgxOTBlNjcxMGNkYzJhMWNiNWEyMWJmMWQ0NjQ5NDp7fQ==', '2019-03-20 14:10:25.331528');

-- ----------------------------
-- Table structure for `statistic_affdistribute`
-- ----------------------------
DROP TABLE IF EXISTS `statistic_affdistribute`;
CREATE TABLE `statistic_affdistribute` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `affiliation` varchar(220) NOT NULL,
  `country` varchar(20) NOT NULL,
  `count` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=270 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of statistic_affdistribute
-- ----------------------------
INSERT INTO `statistic_affdistribute` VALUES ('1', 'Carnegie Mellon University', 'United States', '26');
INSERT INTO `statistic_affdistribute` VALUES ('2', 'University of California', 'United States', '15');
INSERT INTO `statistic_affdistribute` VALUES ('3', 'IBM', 'United States', '14');
INSERT INTO `statistic_affdistribute` VALUES ('4', 'University of Pittsburgh', 'United States', '10');
INSERT INTO `statistic_affdistribute` VALUES ('5', 'Stanford University', 'United States', '9');
INSERT INTO `statistic_affdistribute` VALUES ('6', 'Duke University', 'United States', '9');
INSERT INTO `statistic_affdistribute` VALUES ('7', 'University of Southern California', 'United States', '8');
INSERT INTO `statistic_affdistribute` VALUES ('8', 'University of Maryland', 'United States', '7');
INSERT INTO `statistic_affdistribute` VALUES ('9', 'University of Texas at Austin', 'United States', '7');
INSERT INTO `statistic_affdistribute` VALUES ('10', 'Cornell University', 'United States', '6');
INSERT INTO `statistic_affdistribute` VALUES ('11', 'MIT', 'United States', '5');
INSERT INTO `statistic_affdistribute` VALUES ('12', 'Arizona State University', 'United States', '5');
INSERT INTO `statistic_affdistribute` VALUES ('13', 'University of Minnesota', 'United States', '5');
INSERT INTO `statistic_affdistribute` VALUES ('14', 'Georgia Institute of Technology', 'United States', '5');
INSERT INTO `statistic_affdistribute` VALUES ('15', 'Harvard University', 'United States', '5');
INSERT INTO `statistic_affdistribute` VALUES ('16', 'University of Washington', 'United States', '5');
INSERT INTO `statistic_affdistribute` VALUES ('17', 'Microsoft', 'United States', '5');
INSERT INTO `statistic_affdistribute` VALUES ('18', 'Rutgers University', 'United States', '4');
INSERT INTO `statistic_affdistribute` VALUES ('19', 'Northwestern University', 'United States', '4');
INSERT INTO `statistic_affdistribute` VALUES ('20', 'Rensselaer Polytechnic Institute', 'United States', '4');
INSERT INTO `statistic_affdistribute` VALUES ('21', 'University of Michigan', 'United States', '4');
INSERT INTO `statistic_affdistribute` VALUES ('22', 'University of Massachusetts Amherst', 'United States', '4');
INSERT INTO `statistic_affdistribute` VALUES ('23', 'Purdue University', 'United States', '4');
INSERT INTO `statistic_affdistribute` VALUES ('24', 'Virginia Tech', 'United States', '4');
INSERT INTO `statistic_affdistribute` VALUES ('25', 'University of Illinois at Chicago', 'United States', '3');
INSERT INTO `statistic_affdistribute` VALUES ('26', 'University of Illinois at Urbana-Champaign', 'United States', '3');
INSERT INTO `statistic_affdistribute` VALUES ('27', 'University of Pennsylvania', 'United States', '3');
INSERT INTO `statistic_affdistribute` VALUES ('28', 'Washington University in St. Louis', 'United States', '3');
INSERT INTO `statistic_affdistribute` VALUES ('29', 'Columbia University', 'United States', '3');
INSERT INTO `statistic_affdistribute` VALUES ('30', 'Iowa State University', 'United States', '3');
INSERT INTO `statistic_affdistribute` VALUES ('31', 'Google', 'United States', '3');
INSERT INTO `statistic_affdistribute` VALUES ('32', 'Tufts University', 'United States', '2');
INSERT INTO `statistic_affdistribute` VALUES ('33', 'University of Texas at Dallas', 'United States', '2');
INSERT INTO `statistic_affdistribute` VALUES ('34', 'Texas A&amp;M University', 'United States', '2');
INSERT INTO `statistic_affdistribute` VALUES ('35', 'University of Marylandollege Park', 'United States', '2');
INSERT INTO `statistic_affdistribute` VALUES ('36', 'California Institute of Technology', 'United States', '2');
INSERT INTO `statistic_affdistribute` VALUES ('37', 'OpenAI', 'United States', '2');
INSERT INTO `statistic_affdistribute` VALUES ('38', 'Rochester Institute of Technology', 'United States', '2');
INSERT INTO `statistic_affdistribute` VALUES ('39', 'Johns Hopkins University', 'United States', '2');
INSERT INTO `statistic_affdistribute` VALUES ('40', 'Stony Brook University', 'United States', '2');
INSERT INTO `statistic_affdistribute` VALUES ('41', 'University of Colorado Boulder', 'United States', '2');
INSERT INTO `statistic_affdistribute` VALUES ('42', 'George Mason University', 'United States', '2');
INSERT INTO `statistic_affdistribute` VALUES ('43', 'The Ohio State University', 'United States', '2');
INSERT INTO `statistic_affdistribute` VALUES ('44', 'Vassar College', 'United States', '2');
INSERT INTO `statistic_affdistribute` VALUES ('45', 'Facebook AI Research', 'United States', '2');
INSERT INTO `statistic_affdistribute` VALUES ('46', 'The University of North Carolina at Chapel Hill', 'United States', '2');
INSERT INTO `statistic_affdistribute` VALUES ('47', 'University of South Carolina', 'United States', '2');
INSERT INTO `statistic_affdistribute` VALUES ('48', 'New Jersey Institute of Technology', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('49', 'R7 Speech Sciences', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('50', 'ENS and UC Davis', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('51', 'Vanderbilt University', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('52', 'University of Virginia', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('53', 'Oregon State University', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('54', 'Swarthmore College', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('55', 'University of New Hampshire', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('56', 'State University of New York at Buffalo', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('57', 'U.S. Army Research Laboratory', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('58', 'Vicarious AI', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('59', 'University of Notre Dame', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('60', 'Cardiogram', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('61', 'Missouri University of Science and Technology', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('62', 'University of Connecticut', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('63', 'University of North Florida', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('64', 'Samsung Research America', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('65', 'Appier Inc.', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('66', 'The University of Tennessee, Knoxville', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('67', 'Pennsylvania State University', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('68', 'Toyota Technological Institute at Chicago', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('69', 'The University of Texas at Dallas', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('70', 'Binghamton University', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('71', 'SIFT,LLC', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('72', 'University of Pennsylvania, Honda Research Institute', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('73', 'HRL Laboratories,LLC', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('74', 'Brown University, Providence,Rhode Island', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('75', 'The University of Texas at Arlington', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('76', 'Information Sciences Institute', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('77', 'University of Michigan, Ann Arbor', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('78', 'Netflix Inc.', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('79', 'Rice University', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('80', 'AT&amp;T Labs Research', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('81', 'Toyota Technical Institute at Chicago', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('82', 'Princeton University', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('83', 'University of Texas at Arlington', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('84', 'Syracuse University', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('85', 'University of North Carolina at Chapel Hill', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('86', 'The Pennsylvania State University', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('87', 'University of Wisconsin-Madison', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('88', 'Snap Inc.', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('89', 'University of Illinois at Urbana–Champaign', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('90', 'Siemens Healthineers', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('91', 'IHMC', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('92', 'University of Massachusetts Boston', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('93', 'University of Rochester', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('94', 'Information Sciences Institute, USC', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('95', 'North Carolina State University', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('96', 'Allen Institute for Artificial Intelligence', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('97', 'Wright State University', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('98', 'University of Illinois at Urbana Champaign', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('99', 'University of Colorado at Boulder', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('100', 'Bloomberg LP', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('101', 'Yale University', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('102', 'University of Utah', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('103', 'University of Oregon', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('104', 'University of Colorado, Boulder', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('105', 'Clemson University', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('106', 'UC Irvine', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('107', 'The University of Memphis', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('108', 'Colorado School of Mines', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('109', 'University of Marylandaltimore County', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('110', 'University of Central Florida', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('111', 'The University of Texas at Austin', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('112', 'VMware Research', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('113', 'Georgia Tech', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('114', 'New York University Tandon School of Engineering', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('115', 'Amazon', 'United States', '1');
INSERT INTO `statistic_affdistribute` VALUES ('116', 'Chinese Academy of Sciences', 'China', '40');
INSERT INTO `statistic_affdistribute` VALUES ('117', 'Tsinghua University', 'China', '38');
INSERT INTO `statistic_affdistribute` VALUES ('118', 'Shanghai Jiao Tong University', 'China', '21');
INSERT INTO `statistic_affdistribute` VALUES ('119', 'Peking University', 'China', '20');
INSERT INTO `statistic_affdistribute` VALUES ('120', 'Beihang University', 'China', '14');
INSERT INTO `statistic_affdistribute` VALUES ('121', 'Zhejiang University', 'China', '12');
INSERT INTO `statistic_affdistribute` VALUES ('122', 'University of Science and Technology of China', 'China', '12');
INSERT INTO `statistic_affdistribute` VALUES ('123', 'Nanjing University', 'China', '11');
INSERT INTO `statistic_affdistribute` VALUES ('124', 'Fudan University', 'China', '9');
INSERT INTO `statistic_affdistribute` VALUES ('125', 'Sun Yat-sen University', 'China', '9');
INSERT INTO `statistic_affdistribute` VALUES ('126', 'Northeastern University', 'China', '7');
INSERT INTO `statistic_affdistribute` VALUES ('127', 'Tianjin University', 'China', '7');
INSERT INTO `statistic_affdistribute` VALUES ('128', 'Xidian University', 'China', '7');
INSERT INTO `statistic_affdistribute` VALUES ('129', 'Harbin Institute of Technology', 'China', '6');
INSERT INTO `statistic_affdistribute` VALUES ('130', 'Beijing Institute of Technology', 'China', '6');
INSERT INTO `statistic_affdistribute` VALUES ('131', 'East China Normal University', 'China', '5');
INSERT INTO `statistic_affdistribute` VALUES ('132', 'University of Electronic Science and Technology of China', 'China', '5');
INSERT INTO `statistic_affdistribute` VALUES ('133', 'Nankai University', 'China', '5');
INSERT INTO `statistic_affdistribute` VALUES ('134', 'Tencent', 'China', '5');
INSERT INTO `statistic_affdistribute` VALUES ('135', 'Alibaba Group', 'China', '5');
INSERT INTO `statistic_affdistribute` VALUES ('136', 'Southeast University', 'China', '4');
INSERT INTO `statistic_affdistribute` VALUES ('137', 'Xiamen University', 'China', '4');
INSERT INTO `statistic_affdistribute` VALUES ('138', 'National University of Defense Technology', 'China', '4');
INSERT INTO `statistic_affdistribute` VALUES ('139', 'Soochow University', 'China', '3');
INSERT INTO `statistic_affdistribute` VALUES ('140', 'Dalian University of Technology', 'China', '3');
INSERT INTO `statistic_affdistribute` VALUES ('141', 'Nanjing University of Science and Technology', 'China', '3');
INSERT INTO `statistic_affdistribute` VALUES ('142', 'Beijing University of Posts and Telecommunications', 'China', '2');
INSERT INTO `statistic_affdistribute` VALUES ('143', 'Wuhan University', 'China', '2');
INSERT INTO `statistic_affdistribute` VALUES ('144', 'Anhui University', 'China', '2');
INSERT INTO `statistic_affdistribute` VALUES ('145', 'South China University of Technology', 'China', '2');
INSERT INTO `statistic_affdistribute` VALUES ('146', 'Huazhong University of Science and Technology', 'China', '2');
INSERT INTO `statistic_affdistribute` VALUES ('147', 'Beijing Etrol Technologies Co., Ltd.', 'China', '2');
INSERT INTO `statistic_affdistribute` VALUES ('148', 'Beijing Electronic Science and Technology Institute', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('149', 'Ant Financial Services Group', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('150', 'Shandong University', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('151', 'iDST', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('152', 'JD.com', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('153', 'Hebei University of Technology', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('154', 'South China Normal University', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('155', 'Jilin University', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('156', 'Beijing University of Technology', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('157', 'Jianghan University', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('158', 'Guangdong University of Technology', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('159', 'Jinan University', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('160', 'ShanghaiTech University', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('161', 'University of Macau', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('162', 'Tianjin University of Technology', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('163', 'Nanjing University of Posts and Telecommunications', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('164', 'Nanjing University of Aeronautics and Astronautics', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('165', 'Chongqing University', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('166', 'Baidu', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('167', 'UESTC', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('168', 'School of Automation, Northwestern Polytechnical University', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('169', 'Hefei University of Technology', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('170', 'Beijing Samsung Telecommunication', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('171', 'SenseTime Group Limited', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('172', 'Center for Research on Intelligent Perception and Computing', 'China', '1');
INSERT INTO `statistic_affdistribute` VALUES ('173', 'Nanyang Technological University', 'Singapore', '21');
INSERT INTO `statistic_affdistribute` VALUES ('174', 'National University of Singapore', 'Singapore', '6');
INSERT INTO `statistic_affdistribute` VALUES ('175', 'Singapore Management University', 'Singapore', '4');
INSERT INTO `statistic_affdistribute` VALUES ('176', 'Singapore University of Technology and Design', 'Singapore', '3');
INSERT INTO `statistic_affdistribute` VALUES ('177', 'Institute of High Performance Computing, A*STAR', 'Singapore', '1');
INSERT INTO `statistic_affdistribute` VALUES ('178', 'The University of Hong Kong', 'Hong Kong', '12');
INSERT INTO `statistic_affdistribute` VALUES ('179', 'The Hong Kong Polytechnic University', 'Hong Kong', '7');
INSERT INTO `statistic_affdistribute` VALUES ('180', 'Hong Kong University of Science and Technology', 'Hong Kong', '6');
INSERT INTO `statistic_affdistribute` VALUES ('181', 'Hong Kong Baptist University', 'Hong Kong', '4');
INSERT INTO `statistic_affdistribute` VALUES ('182', 'City University of Hong Kong', 'Hong Kong', '1');
INSERT INTO `statistic_affdistribute` VALUES ('183', 'The University of Technology Sydney', 'Australia', '8');
INSERT INTO `statistic_affdistribute` VALUES ('184', 'The University of New South Wales', 'Australia', '4');
INSERT INTO `statistic_affdistribute` VALUES ('185', 'Data61', 'Australia', '4');
INSERT INTO `statistic_affdistribute` VALUES ('186', 'Australian National University', 'Australia', '3');
INSERT INTO `statistic_affdistribute` VALUES ('187', 'The University of Sydney', 'Australia', '3');
INSERT INTO `statistic_affdistribute` VALUES ('188', 'The University of Melbourne', 'Australia', '3');
INSERT INTO `statistic_affdistribute` VALUES ('189', 'UNSW Sydney', 'Australia', '3');
INSERT INTO `statistic_affdistribute` VALUES ('190', 'CSIRO', 'Australia', '3');
INSERT INTO `statistic_affdistribute` VALUES ('191', 'The University of Adelaide', 'Australia', '2');
INSERT INTO `statistic_affdistribute` VALUES ('192', 'University of Wollongong', 'Australia', '2');
INSERT INTO `statistic_affdistribute` VALUES ('193', 'Griffith University', 'Australia', '2');
INSERT INTO `statistic_affdistribute` VALUES ('194', 'Monash University', 'Australia', '1');
INSERT INTO `statistic_affdistribute` VALUES ('195', 'The University of Queensland', 'Australia', '1');
INSERT INTO `statistic_affdistribute` VALUES ('196', 'Gold Coast Campus', 'Australia', '1');
INSERT INTO `statistic_affdistribute` VALUES ('197', 'University of Oxford', 'United Kingdom', '10');
INSERT INTO `statistic_affdistribute` VALUES ('198', 'Imperial College London', 'United Kingdom', '3');
INSERT INTO `statistic_affdistribute` VALUES ('199', 'University College London', 'United Kingdom', '3');
INSERT INTO `statistic_affdistribute` VALUES ('200', 'Cardiff University', 'United Kingdom', '2');
INSERT INTO `statistic_affdistribute` VALUES ('201', 'University of Edinburgh', 'United Kingdom', '2');
INSERT INTO `statistic_affdistribute` VALUES ('202', 'DeepMind', 'United Kingdom', '2');
INSERT INTO `statistic_affdistribute` VALUES ('203', 'University of Southampton', 'United Kingdom', '1');
INSERT INTO `statistic_affdistribute` VALUES ('204', 'University of Sheffield', 'United Kingdom', '1');
INSERT INTO `statistic_affdistribute` VALUES ('205', 'Oxford University', 'United Kingdom', '1');
INSERT INTO `statistic_affdistribute` VALUES ('206', 'Queen Mary University of London', 'United Kingdom', '1');
INSERT INTO `statistic_affdistribute` VALUES ('207', 'PROWLER.io', 'United Kingdom', '1');
INSERT INTO `statistic_affdistribute` VALUES ('208', 'The University of Liverpool', 'United Kingdom', '1');
INSERT INTO `statistic_affdistribute` VALUES ('209', 'University of Kent, UK', 'United Kingdom', '1');
INSERT INTO `statistic_affdistribute` VALUES ('210', 'University of East Anglia', 'United Kingdom', '1');
INSERT INTO `statistic_affdistribute` VALUES ('211', 'University of Cambridge', 'United Kingdom', '1');
INSERT INTO `statistic_affdistribute` VALUES ('212', 'Northwestern Polytechnical University', 'United Kingdom', '1');
INSERT INTO `statistic_affdistribute` VALUES ('213', 'The University of Tokyo', 'Japan', '10');
INSERT INTO `statistic_affdistribute` VALUES ('214', 'Nara Institute of Science and Technology', 'Japan', '3');
INSERT INTO `statistic_affdistribute` VALUES ('215', 'Nippon Telegraph and Telephone Corporation', 'Japan', '2');
INSERT INTO `statistic_affdistribute` VALUES ('216', 'Advanced Telecommunications Research Institute International (ATR)', 'Japan', '1');
INSERT INTO `statistic_affdistribute` VALUES ('217', 'Tokyo Institute of Technology', 'Japan', '1');
INSERT INTO `statistic_affdistribute` VALUES ('218', 'Nagoya Institute of Technology', 'Japan', '1');
INSERT INTO `statistic_affdistribute` VALUES ('219', 'RIKEN AIP', 'Japan', '1');
INSERT INTO `statistic_affdistribute` VALUES ('220', 'Hokkaido University', 'Japan', '1');
INSERT INTO `statistic_affdistribute` VALUES ('221', 'scouty Inc.', 'Japan', '1');
INSERT INTO `statistic_affdistribute` VALUES ('222', 'SOKENDAI (The Graduate University for Advanced Studies)', 'Japan', '1');
INSERT INTO `statistic_affdistribute` VALUES ('223', 'National Institute of Advanced Industrial Science and Technology', 'Japan', '1');
INSERT INTO `statistic_affdistribute` VALUES ('224', 'Keio University', 'Japan', '1');
INSERT INTO `statistic_affdistribute` VALUES ('225', 'R&amp;D Group, Hitachi', 'Japan', '1');
INSERT INTO `statistic_affdistribute` VALUES ('226', 'Osaka University', 'Japan', '1');
INSERT INTO `statistic_affdistribute` VALUES ('227', 'Fujitsu Laboratories Ltd.', 'Japan', '1');
INSERT INTO `statistic_affdistribute` VALUES ('228', 'Tohoku University', 'Japan', '1');
INSERT INTO `statistic_affdistribute` VALUES ('229', 'Yokohama National University', 'Japan', '1');
INSERT INTO `statistic_affdistribute` VALUES ('230', 'National Institute of Information and Communications Technology', 'Japan', '1');
INSERT INTO `statistic_affdistribute` VALUES ('231', 'TU Dortmund University', 'Germany', '3');
INSERT INTO `statistic_affdistribute` VALUES ('232', 'University of Freiburg', 'Germany', '2');
INSERT INTO `statistic_affdistribute` VALUES ('233', 'Leipzig University', 'Germany', '2');
INSERT INTO `statistic_affdistribute` VALUES ('234', 'TU Darmstadt', 'Germany', '2');
INSERT INTO `statistic_affdistribute` VALUES ('235', 'Max Planck Institute for Software Systems (MPI-SWS)', 'Germany', '1');
INSERT INTO `statistic_affdistribute` VALUES ('236', 'TU Berlin', 'Germany', '1');
INSERT INTO `statistic_affdistribute` VALUES ('237', 'University of Tübingen', 'Germany', '1');
INSERT INTO `statistic_affdistribute` VALUES ('238', 'Heinrich-Heine-Universität Düsseldorf', 'Germany', '1');
INSERT INTO `statistic_affdistribute` VALUES ('239', 'University of Bremen', 'Germany', '1');
INSERT INTO `statistic_affdistribute` VALUES ('240', 'Max Planck Institute for Informatics', 'Germany', '1');
INSERT INTO `statistic_affdistribute` VALUES ('241', 'Technical University of Munich', 'Germany', '1');
INSERT INTO `statistic_affdistribute` VALUES ('242', 'Paderborn University', 'Germany', '1');
INSERT INTO `statistic_affdistribute` VALUES ('243', 'MPI-SWS', 'Germany', '1');
INSERT INTO `statistic_affdistribute` VALUES ('244', 'University of Mannheim', 'Germany', '1');
INSERT INTO `statistic_affdistribute` VALUES ('245', 'Technische Universität Darmstadt', 'Germany', '1');
INSERT INTO `statistic_affdistribute` VALUES ('246', 'University of Passau', 'Germany', '1');
INSERT INTO `statistic_affdistribute` VALUES ('247', 'Bielefeld University', 'Germany', '1');
INSERT INTO `statistic_affdistribute` VALUES ('248', 'Max Planck Institute Informatics', 'Germany', '1');
INSERT INTO `statistic_affdistribute` VALUES ('249', 'Ulm University', 'Germany', '1');
INSERT INTO `statistic_affdistribute` VALUES ('250', 'JMU Würzburg', 'Germany', '1');
INSERT INTO `statistic_affdistribute` VALUES ('251', 'CISPA, Saarland University', 'Germany', '1');
INSERT INTO `statistic_affdistribute` VALUES ('252', 'University of Heidelberg', 'Germany', '1');
INSERT INTO `statistic_affdistribute` VALUES ('253', 'Hasso Plattner Institute', 'Germany', '1');
INSERT INTO `statistic_affdistribute` VALUES ('254', 'Indian Institute of Science', 'India', '3');
INSERT INTO `statistic_affdistribute` VALUES ('255', 'IIT Bombay', 'India', '3');
INSERT INTO `statistic_affdistribute` VALUES ('256', 'IIIT Delhi', 'India', '3');
INSERT INTO `statistic_affdistribute` VALUES ('257', 'Tata Institute of Fundamental Research, Mumbai', 'India', '2');
INSERT INTO `statistic_affdistribute` VALUES ('258', 'Indian Institute of Technology Madras', 'India', '2');
INSERT INTO `statistic_affdistribute` VALUES ('259', 'Indian Institute of Science (IISc), Bangalore', 'India', '2');
INSERT INTO `statistic_affdistribute` VALUES ('260', 'Tata Consultancy Services', 'India', '1');
INSERT INTO `statistic_affdistribute` VALUES ('261', 'University of Toronto', 'Canada', '3');
INSERT INTO `statistic_affdistribute` VALUES ('262', 'University of Alberta', 'Canada', '3');
INSERT INTO `statistic_affdistribute` VALUES ('263', 'University of British Columbia', 'Canada', '3');
INSERT INTO `statistic_affdistribute` VALUES ('264', 'McGill University', 'Canada', '3');
INSERT INTO `statistic_affdistribute` VALUES ('265', 'University of Waterloo', 'Canada', '2');
INSERT INTO `statistic_affdistribute` VALUES ('266', 'York University', 'Canada', '1');
INSERT INTO `statistic_affdistribute` VALUES ('267', 'National Research Council of Canada', 'Canada', '1');
INSERT INTO `statistic_affdistribute` VALUES ('268', 'Dalhousie University', 'Canada', '1');
INSERT INTO `statistic_affdistribute` VALUES ('269', 'Quest University Canada', 'Canada', '1');

-- ----------------------------
-- Table structure for `users_emailverifyrecord`
-- ----------------------------
DROP TABLE IF EXISTS `users_emailverifyrecord`;
CREATE TABLE `users_emailverifyrecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `send_type` varchar(10) NOT NULL,
  `send_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_emailverifyrecord
-- ----------------------------
INSERT INTO `users_emailverifyrecord` VALUES ('4', 'NbmzFV1MSXnPAV8b', '806990106@qq.com', 'register', '2019-03-06 13:39:56.466363');
INSERT INTO `users_emailverifyrecord` VALUES ('5', 'ijFhcTd1fOiSJK3q', '806990106@qq.com', 'register', '2019-03-06 13:48:06.554412');
INSERT INTO `users_emailverifyrecord` VALUES ('6', 'bbt7XrpH3Oj2R9zH', '806990106@qq.com', 'register', '2019-03-06 14:01:24.030501');
INSERT INTO `users_emailverifyrecord` VALUES ('7', 'HyiAn8BndikeqPxP', '806990106@qq.com', 'register', '2019-03-06 14:09:05.418572');
INSERT INTO `users_emailverifyrecord` VALUES ('8', '5sW8pnzyz4NwHDO6', '806990106@qq.com', 'register', '2019-03-06 14:14:25.121324');
INSERT INTO `users_emailverifyrecord` VALUES ('9', 'q4SVVpGqKcZudWoP', '806990106@qq.com', 'register', '2019-03-06 14:15:46.893148');
INSERT INTO `users_emailverifyrecord` VALUES ('10', 'oUriLp3ysQAcyxkL', 'lin@foxmail.com', 'register', '2019-04-17 11:50:51.878253');
INSERT INTO `users_emailverifyrecord` VALUES ('11', 'Zrcq6VdhOhROxkwA', 'ling@foxmail.com', 'register', '2019-04-17 11:51:49.940044');
INSERT INTO `users_emailverifyrecord` VALUES ('12', 'C28ag3s7ksDgYhkm', '806990106@qq.com', 'register', '2019-04-22 21:42:40.577705');
INSERT INTO `users_emailverifyrecord` VALUES ('13', 'vVbUvREwWCyTjb7e', '806990106@qq.com', 'register', '2019-04-22 21:54:00.721263');
INSERT INTO `users_emailverifyrecord` VALUES ('14', '4B2iONYOZN0dLpTj', '806990106@qq.com', 'register', '2019-04-22 22:00:19.811988');
INSERT INTO `users_emailverifyrecord` VALUES ('15', 'KWPckEO9ptd9qCyk', '806990106@qq.com', 'register', '2019-04-22 22:08:49.692400');
INSERT INTO `users_emailverifyrecord` VALUES ('16', 'ZxXKmTf2N7SX88bP', '806990106@qq.com', 'register', '2019-04-22 22:10:35.841870');
INSERT INTO `users_emailverifyrecord` VALUES ('17', 'aGLoLJhwK8C3gNOA', '806990106@qq.com', 'register', '2019-04-22 22:23:52.197163');
INSERT INTO `users_emailverifyrecord` VALUES ('18', 'PDrtNzfwNrFWTWYT', '806990106@qq.com', 'forget', '2019-04-22 22:25:38.313401');
INSERT INTO `users_emailverifyrecord` VALUES ('19', 'OIEXYNcMWiRSuNH1', '8888888@qq.com', 'register', '2019-04-24 12:08:09.121799');
INSERT INTO `users_emailverifyrecord` VALUES ('20', 'fA7CZyy5C6a5IVWn', 'shiliang5804@foxmail.com', 'register', '2019-04-24 18:48:53.967293');
INSERT INTO `users_emailverifyrecord` VALUES ('21', 'ptLLhXw0gbhx7q57', 'shiliang6402@foxmail.com', 'register', '2019-04-30 23:23:39.132007');
INSERT INTO `users_emailverifyrecord` VALUES ('22', 'l8udEP48k7kuaGqX', 'shiliang6402@foxmail.com', 'forget', '2019-05-01 10:30:21.312610');
INSERT INTO `users_emailverifyrecord` VALUES ('23', 'LjIWJ7M8fhQ8GIxT', 'shiliang6402@foxmail.com', 'forget', '2019-05-01 10:31:42.848339');
INSERT INTO `users_emailverifyrecord` VALUES ('24', 'FJczm9lvWWuTkQPJ', '2313696922@qq.com', 'register', '2019-05-03 14:01:11.246533');
INSERT INTO `users_emailverifyrecord` VALUES ('25', 'QBkqoMOiSm7c7RJ1', '540378302@qq.com', 'register', '2019-05-16 23:22:52.000000');
INSERT INTO `users_emailverifyrecord` VALUES ('26', 'QSPNk40Xr4zh5coh', '540378302@qq.com', 'register', '2019-05-16 23:41:22.000000');
INSERT INTO `users_emailverifyrecord` VALUES ('27', '6ncahDBqirBbRZGN', '540378302@qq.com', 'register', '2019-05-16 23:44:41.000000');
INSERT INTO `users_emailverifyrecord` VALUES ('28', 'iMvmTREIoDGDImvF', '540378302@qq.com', 'register', '2019-05-16 23:48:27.000000');
INSERT INTO `users_emailverifyrecord` VALUES ('29', 'hzqyfZMSVPfo3bKo', '540378302@qq.com', 'forget', '2019-05-17 00:37:04.000000');
INSERT INTO `users_emailverifyrecord` VALUES ('30', 'ZoI4KpqWULGDaGrG', '540378302@qq.com', 'register', '2019-05-17 17:27:11.000000');

-- ----------------------------
-- Table structure for `users_userprofile`
-- ----------------------------
DROP TABLE IF EXISTS `users_userprofile`;
CREATE TABLE `users_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `nick_name` varchar(50) NOT NULL,
  `birthday` date DEFAULT NULL,
  `gender` varchar(6) NOT NULL,
  `address` varchar(100) DEFAULT NULL,
  `mobile` varchar(11) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_userprofile
-- ----------------------------
INSERT INTO `users_userprofile` VALUES ('1', 'pbkdf2_sha256$100000$8rDr0bxCFsBp$eIqDRI+qk0dJ4JRxwoPFUNjW22WogK+EgSaFpzWCQYI=', '2019-04-17 12:25:01.573290', '1', 'shiliang@foxmail.com', '', '', 'shiliang@foxmail.com', '1', '1', '2019-03-06 13:07:19.133721', '', null, 'male', '', null, 'media/image/default/Entity/user_default.png');
INSERT INTO `users_userprofile` VALUES ('18', 'pbkdf2_sha256$100000$vGSDGDU3qYR9$3PuaiB+bB1+7tsKCf9JoTCHsSvN1MIHjstcqUl68F2M=', '2019-06-01 11:44:21.000000', '1', '806990106@qq.com', '', '若水', '806990106@qq.com', '1', '1', '2019-04-03 10:52:00.000000', 'Sparks_fly', '2018-04-23', 'male', '北京市海淀区中关村', '13811112222', 'image/2019/06/default_middile_7.png');
INSERT INTO `users_userprofile` VALUES ('20', 'pbkdf2_sha256$100000$p58RjT0A44YY$GozgqZMp9Ufks9aaJP/xI9qiVxzrvChY742Qm+xeRwk=', '2019-04-24 18:51:00.000000', '1', 'shiliang5804@foxmail.com', '', '', 'shiliang5804@foxmail.com', '1', '1', '2019-04-24 18:48:00.000000', '池里的鱼', '2019-04-10', 'female', '贵州', null, 'image/2019/04/default_middile_8_yBrSeed.png');
INSERT INTO `users_userprofile` VALUES ('21', 'pbkdf2_sha256$100000$xQ0tzL2LU0cu$AV6HKJcl2bPuo9RJ057FVgMCASMb8g/N9gKc2KsZta4=', '2019-06-01 11:43:44.000000', '0', 'shiliang6402@foxmail.com', '', '', 'shiliang6402@foxmail.com', '0', '1', '2019-04-30 23:23:38.869160', '', null, 'male', null, null, 'image/default/Entity/user_default.png');
INSERT INTO `users_userprofile` VALUES ('22', 'pbkdf2_sha256$100000$9cKHzhYx2kk4$vsDbIl4UoYgLb1Dl0O2kpBQsOwW59Y9Z916l8XDILk0=', null, '0', '2313696922@qq.com', '', '', '2313696922@qq.com', '0', '0', '2019-05-03 14:01:00.000000', 'mtb', null, 'male', null, null, 'image/2019/05/default_middile_2.png');
INSERT INTO `users_userprofile` VALUES ('27', 'pbkdf2_sha256$100000$jzeyTMf61f6G$R+v00CUqO/TOIkXbsxnILk+Pi5uxmkUT69yGa8pwVaQ=', '2019-05-17 17:27:41.000000', '0', '540378302@qq.com', '', '', '540378302@qq.com', '0', '1', '2019-05-17 17:27:11.000000', '', null, 'male', null, null, 'image/default/Entity/user_default.png');

-- ----------------------------
-- Table structure for `users_userprofile_groups`
-- ----------------------------
DROP TABLE IF EXISTS `users_userprofile_groups`;
CREATE TABLE `users_userprofile_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_groups_userprofile_id_group_id_823cf2fc_uniq` (`userprofile_id`,`group_id`) USING BTREE,
  KEY `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id` (`group_id`) USING BTREE,
  CONSTRAINT `users_userprofile_groups_ibfk_1` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `users_userprofile_groups_ibfk_2` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_userprofile_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `users_userprofile_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `users_userprofile_user_permissions`;
CREATE TABLE `users_userprofile_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_user_p_userprofile_id_permissio_d0215190_uniq` (`userprofile_id`,`permission_id`) USING BTREE,
  KEY `users_userprofile_us_permission_id_393136b6_fk_auth_perm` (`permission_id`) USING BTREE,
  CONSTRAINT `users_userprofile_user_permissions_ibfk_1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_userprofile_user_permissions_ibfk_2` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_userprofile_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `xadmin_bookmark`
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_bookmark`;
CREATE TABLE `xadmin_bookmark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `url_name` varchar(64) NOT NULL,
  `query` varchar(1000) NOT NULL,
  `is_share` tinyint(1) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_bookmark_content_type_id_60941679_fk_django_co` (`content_type_id`) USING BTREE,
  KEY `xadmin_bookmark_user_id_42d307fc_fk_users_userprofile_id` (`user_id`) USING BTREE,
  CONSTRAINT `xadmin_bookmark_ibfk_1` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_bookmark_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_bookmark
-- ----------------------------

-- ----------------------------
-- Table structure for `xadmin_log`
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_log`;
CREATE TABLE `xadmin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `ip_addr` char(39) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` varchar(32) NOT NULL,
  `message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` (`content_type_id`) USING BTREE,
  KEY `xadmin_log_user_id_bb16a176_fk_users_userprofile_id` (`user_id`) USING BTREE,
  CONSTRAINT `xadmin_log_ibfk_1` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_log_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_log
-- ----------------------------
INSERT INTO `xadmin_log` VALUES ('1', '2019-04-24 11:12:20.303653', '127.0.0.1', '18', '806990106@qq.com', 'change', '修改 last_login，nick_name，address 和 image', '6', '18');
INSERT INTO `xadmin_log` VALUES ('2', '2019-04-24 11:26:01.159742', '127.0.0.1', '18', '806990106@qq.com', 'change', '修改 last_login，nick_name，address 和 image', '6', '18');
INSERT INTO `xadmin_log` VALUES ('3', '2019-04-24 12:01:51.052403', '127.0.0.1', '18', '806990106@qq.com', 'change', '修改 last_login，last_name，email，date_joined，nick_name，birthday，address，mobile 和 image', '6', '18');
INSERT INTO `xadmin_log` VALUES ('4', '2019-04-24 18:58:37.665413', '127.0.0.1', '20', 'shiliang5804@foxmail.com', 'change', '修改 last_login，is_superuser，is_staff 和 image', '6', '18');
INSERT INTO `xadmin_log` VALUES ('5', '2019-05-01 15:36:54.113557', '127.0.0.1', '18', '806990106@qq.com', 'change', '修改 last_login，last_name 和 image', '6', '18');
INSERT INTO `xadmin_log` VALUES ('6', '2019-05-01 15:38:19.139602', '127.0.0.1', null, '', 'delete', '批量删除 3 个 用户信息', null, '18');
INSERT INTO `xadmin_log` VALUES ('7', '2019-05-01 15:46:12.758166', '127.0.0.1', null, '', 'delete', '批量删除 3 个 邮箱验证码', null, '18');
INSERT INTO `xadmin_log` VALUES ('8', '2019-05-03 14:26:20.247919', '127.0.0.1', '22', '2313696922@qq.com', 'change', '修改 nick_name 和 image', '6', '18');

-- ----------------------------
-- Table structure for `xadmin_usersettings`
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_usersettings`;
CREATE TABLE `xadmin_usersettings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(256) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_usersettings_user_id_edeabe4a_fk_users_userprofile_id` (`user_id`) USING BTREE,
  CONSTRAINT `xadmin_usersettings_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_usersettings
-- ----------------------------
INSERT INTO `xadmin_usersettings` VALUES ('1', 'dashboard:home:pos', '', '1');
INSERT INTO `xadmin_usersettings` VALUES ('2', 'dashboard:home:pos', '', '18');
INSERT INTO `xadmin_usersettings` VALUES ('3', 'site-theme', 'https://bootswatch.com/3/cerulean/bootstrap.min.css', '18');

-- ----------------------------
-- Table structure for `xadmin_userwidget`
-- ----------------------------
DROP TABLE IF EXISTS `xadmin_userwidget`;
CREATE TABLE `xadmin_userwidget` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` varchar(256) NOT NULL,
  `widget_type` varchar(50) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_userwidget_user_id_c159233a_fk_users_userprofile_id` (`user_id`) USING BTREE,
  CONSTRAINT `xadmin_userwidget_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of xadmin_userwidget
-- ----------------------------
