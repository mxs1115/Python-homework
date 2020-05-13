/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80019
Source Host           : localhost:3306
Source Database       : student

Target Server Type    : MYSQL
Target Server Version : 80019
File Encoding         : 65001

Date: 2020-05-13 21:57:50
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for classes
-- ----------------------------
DROP TABLE IF EXISTS `classes`;
CREATE TABLE `classes` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of classes
-- ----------------------------
INSERT INTO `classes` VALUES ('3', '软件1801');
INSERT INTO `classes` VALUES ('4', '软件1802');

-- ----------------------------
-- Table structure for message_pad
-- ----------------------------
DROP TABLE IF EXISTS `message_pad`;
CREATE TABLE `message_pad` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `content` varchar(255) DEFAULT NULL COMMENT '留言内容',
  `name` varchar(255) DEFAULT NULL COMMENT '留言人',
  `time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '留言时间',
  `is_delete` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of message_pad
-- ----------------------------
INSERT INTO `message_pad` VALUES ('1', '你好', '李明', '2020-05-12 15:12:52', '0');
INSERT INTO `message_pad` VALUES ('2', '哈喽', '张明', '2020-05-12 21:53:17', '0');
INSERT INTO `message_pad` VALUES ('3', '哈哈哈', '李明明', '2020-05-12 15:58:15', '1');
INSERT INTO `message_pad` VALUES ('6', '加油', '王中', '2020-05-13 17:59:44', '1');
INSERT INTO `message_pad` VALUES ('10', '努力', '可之云', '2020-05-13 18:00:28', '1');

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT '',
  `age` tinyint unsigned DEFAULT '0',
  `height` decimal(5,2) DEFAULT NULL,
  `gender` enum('男','女','中性','保密') DEFAULT '保密',
  `cls_id` int unsigned DEFAULT '0',
  `is_delete` bit(1) DEFAULT b'0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of students
-- ----------------------------
INSERT INTO `students` VALUES ('1', '小明', '18', '180.00', '女', '1', '\0');
INSERT INTO `students` VALUES ('2', '小月月', '18', '180.00', '女', '2', '');
INSERT INTO `students` VALUES ('3', '彭于晏', '29', '185.00', '男', '1', '\0');
INSERT INTO `students` VALUES ('4', '刘德华', '59', '175.00', '男', '2', '');
INSERT INTO `students` VALUES ('5', '黄蓉', '38', '160.00', '女', '1', '\0');
INSERT INTO `students` VALUES ('6', '凤姐', '28', '150.00', '保密', '2', '');
INSERT INTO `students` VALUES ('7', '王祖贤', '18', '172.00', '女', '1', '');
INSERT INTO `students` VALUES ('8', '周杰伦', '36', '188.00', '男', '1', '\0');
INSERT INTO `students` VALUES ('9', '程坤', '27', '181.00', '男', '2', '\0');
INSERT INTO `students` VALUES ('10', '刘亦菲', '25', '166.00', '女', '2', '\0');
INSERT INTO `students` VALUES ('11', '金星', '33', '162.00', '中性', '3', '');
INSERT INTO `students` VALUES ('12', '静香', '12', '180.00', '女', '4', '\0');
INSERT INTO `students` VALUES ('13', '郭靖', '12', '170.00', '男', '4', '\0');
INSERT INTO `students` VALUES ('14', '周杰', '34', '176.00', '女', '5', '\0');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', '李明');
INSERT INTO `user` VALUES ('2', '小明');
INSERT INTO `user` VALUES ('3', '李华');
