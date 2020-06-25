/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80019
Source Host           : localhost:3306
Source Database       : python-engineer

Target Server Type    : MYSQL
Target Server Version : 80019
File Encoding         : 65001

Date: 2020-06-25 22:22:41
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for python_engineer_beijing
-- ----------------------------
DROP TABLE IF EXISTS `python_engineer_beijing`;
CREATE TABLE `python_engineer_beijing` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `Position` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Company` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Area` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Money` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Time` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of python_engineer_beijing
-- ----------------------------
INSERT INTO `python_engineer_beijing` VALUES ('1', 'python开发工程师', '北京南天软件有限公司', '北京', '0.8-1.5万/月', '06-25');
INSERT INTO `python_engineer_beijing` VALUES ('2', '视频分析算法工程师', '中讯志远（武汉）科技有限公司', '北京-海淀区', '0.8-2万/月', '06-25');
INSERT INTO `python_engineer_beijing` VALUES ('3', '资深Python工程师', '北京安德信业信息咨询有限责任公司', '北京-海淀区', '2.5-4万/月', '06-25');
INSERT INTO `python_engineer_beijing` VALUES ('4', '大数据挖掘工程师', '湖南金烽信息科技有限公司', '北京', '1.5-3万/月', '06-25');
INSERT INTO `python_engineer_beijing` VALUES ('5', '云BOSS', '亚信科技（中国）有限公司', '北京-海淀区', '1.5-2千/月', '06-25');
INSERT INTO `python_engineer_beijing` VALUES ('6', 'Python开发工程师', '扬州万方电子技术有限责任公司', '北京', '1-1.5万/月', '06-25');
INSERT INTO `python_engineer_beijing` VALUES ('7', '后端开发工程师（Python方向）', '中金智汇科技有限责任公司', '北京-大兴区', '1-2万/月', '06-25');
INSERT INTO `python_engineer_beijing` VALUES ('8', 'Python开发工程师---0201', '北京视野金融信息服务有限公司', '北京-海淀区', '1.5-2.5万/月', '06-24');
INSERT INTO `python_engineer_beijing` VALUES ('9', 'python开发工程师-北京', '中电福富信息科技有限公司', '北京-海淀区', '1-1.5万/月', '06-24');
INSERT INTO `python_engineer_beijing` VALUES ('10', '全栈开发工程师', '博彦科技股份有限公司', '北京-海淀区', '1.5-2.5万/月', '06-24');
INSERT INTO `python_engineer_beijing` VALUES ('11', 'Python开发工程师 数据挖掘', '北京大申烽华科技有限责任公司', '北京-海淀区', '6-8千/月', '06-24');
INSERT INTO `python_engineer_beijing` VALUES ('12', 'Python开发工程师', '随锐科技集团股份有限公司', '北京-海淀区', '2-2.5万/月', '06-24');
INSERT INTO `python_engineer_beijing` VALUES ('13', 'IT开发助理', '上海企顺信息系统有限公司', '北京-海淀区', '0.8-1万/月', '06-24');
INSERT INTO `python_engineer_beijing` VALUES ('14', '爬虫工程师（Java或Python）', '北京三六九数动科技有限公司', '北京', '2.5-3万/月', '06-24');
INSERT INTO `python_engineer_beijing` VALUES ('15', '全栈工程师', '北京智谱华章科技有限公司', '北京-海淀区', '2.5-5万/月', '06-24');
INSERT INTO `python_engineer_beijing` VALUES ('16', '软件开发工程师（初级）', '北京华云星地通科技有限公司', '北京-海淀区', '0.8-1.1万/月', '06-24');
INSERT INTO `python_engineer_beijing` VALUES ('17', '气象算法工程师', '北京华泰德丰技术有限公司', '北京-海淀区', '1.5-3万/月', '06-24');
INSERT INTO `python_engineer_beijing` VALUES ('18', 'PD-DevOps工程师', '北京安德医智科技有限公司', '北京', '1-1.5万/月', '06-24');
INSERT INTO `python_engineer_beijing` VALUES ('19', '技术架构师 (MJ002954)', '广联达', '北京', '3-5万/月', '06-23');
INSERT INTO `python_engineer_beijing` VALUES ('20', 'python开发工程师（舆情方向）', '太极计算机股份有限公司', '北京-朝阳区', '1.1-1.8万/月', '06-22');
INSERT INTO `python_engineer_beijing` VALUES ('21', '后台研发工程师(J10343)', '纵目科技（上海）股份有限公司', '异地招聘', '1.8-2.5万/月', '06-19');
INSERT INTO `python_engineer_beijing` VALUES ('22', '高级Python开发工程师(J11448)', '朗新科技股份有限公司', '北京-朝阳区', '1.5-2万/月', '06-19');
INSERT INTO `python_engineer_beijing` VALUES ('23', 'Python开发工程师', '深圳极联信息技术股份有限公司', '北京-海淀区', '1.2-1.5万/月', '06-18');
INSERT INTO `python_engineer_beijing` VALUES ('24', 'Python开发（情报分析平台）', '北京启明星辰信息安全技术有限公司', '北京-海淀区', '1.2-2万/月', '06-17');
INSERT INTO `python_engineer_beijing` VALUES ('25', 'Python高级开发工程师', '达观数据', '北京', '2-3万/月', '06-16');
INSERT INTO `python_engineer_beijing` VALUES ('26', '数据库云平台架构师', '北京海量数据技术股份有限公司', '北京-海淀区', '1.5-3万/月', '06-13');
INSERT INTO `python_engineer_beijing` VALUES ('27', '安全研发工程师', '北京华清信安科技有限公司', '北京-朝阳区', '0.8-1.2万/月', '06-10');
INSERT INTO `python_engineer_beijing` VALUES ('28', 'Python开发工程师', '北京华文天元信息咨询有限公司', '北京-朝阳区', '0.8-1.5万/月', '06-08');
INSERT INTO `python_engineer_beijing` VALUES ('29', '监控开发工程师', '北京泽塔云科技股份有限公司', '北京-朝阳区', '1.5-2万/月', '06-03');
INSERT INTO `python_engineer_beijing` VALUES ('30', '预研实习生', '北京智通云联科技有限公司', '北京', '1-1.5万/月', '06-02');
INSERT INTO `python_engineer_beijing` VALUES ('31', 'Python研发工程师', '北京新网医讯技术有限公司', '北京-西城区', '0.8-1.2万/月', '05-29');
INSERT INTO `python_engineer_beijing` VALUES ('32', '后端开发工程师(J10347)', '北京创源微致软件有限公司', '北京-海淀区', '1.5-2.5万/月', '05-24');
INSERT INTO `python_engineer_beijing` VALUES ('33', 'Python开发工程师', '上海微创软件股份有限公司北京分公司', '北京', '0.9-1.4万/月', '05-22');
INSERT INTO `python_engineer_beijing` VALUES ('34', 'RPA开发工程师', '上海屹恒信息科技有限公司', '北京-朝阳区', '1-1.5万/月', '05-19');
INSERT INTO `python_engineer_beijing` VALUES ('35', '后台开发工程师', '华录光存储研究院（大连）有限公司', '北京-石景山区', '1-2万/月', '05-15');
INSERT INTO `python_engineer_beijing` VALUES ('36', 'Python开发工程师', '北京华泽云防科技有限公司', '北京-丰台区', '1-1.5万/月', '05-06');
INSERT INTO `python_engineer_beijing` VALUES ('37', '后端开发工程师（广告）', '北京木瓜移动科技股份有限公司', '北京-海淀区', '2-2.5万/月', '05-03');
INSERT INTO `python_engineer_beijing` VALUES ('38', '高级Devops工程师', '北京安德信业信息咨询有限责任公司', '北京-海淀区', '3-4.5万/月', '06-25');
INSERT INTO `python_engineer_beijing` VALUES ('39', 'Python开发工程师', '北京安德医智科技有限公司', '北京', '1-1.8万/月', '06-24');
INSERT INTO `python_engineer_beijing` VALUES ('40', 'Python开发工程师', '太极计算机股份有限公司', '北京-朝阳区', '1.3-2.3万/月', '06-22');
INSERT INTO `python_engineer_beijing` VALUES ('41', '中高级Python开发工程师 (MJ001804)', '北京启明星辰信息安全技术有限公司', '北京', '1.5-2.5万/月', '06-17');
INSERT INTO `python_engineer_beijing` VALUES ('42', '后端开发工程师', '北京创源微致软件有限公司', '北京-海淀区', '1.5-2.5万/月', '05-24');
INSERT INTO `python_engineer_beijing` VALUES ('43', 'python开发工程师（集成2053）', '北京南天软件有限公司', '北京-丰台区', '1-1.5万/月', '05-17');
INSERT INTO `python_engineer_beijing` VALUES ('44', 'python开发工程师', '上海微创软件股份有限公司北京分公司', '北京', '1.2-1.6万/月', '05-15');
INSERT INTO `python_engineer_beijing` VALUES ('45', 'Python开发工程师（实习生）', '北京华泽云防科技有限公司', '北京-丰台区', '4.5-6千/月', '05-06');
