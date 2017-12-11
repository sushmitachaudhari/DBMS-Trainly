
--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `UserID` varchar(240) NOT NULL,
  `FirstName` varchar(120) DEFAULT NULL,
  `LastName` varchar(120) DEFAULT NULL,
  `Password` varchar(120) DEFAULT NULL,
  `ProfilePic` blob,
  `Street` varchar(120) DEFAULT NULL,
  `City` varchar(120) DEFAULT NULL,
  `Postal Code` varchar(120) DEFAULT NULL,
  `Country` varchar(120) DEFAULT NULL,
  `usertype` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`UserID`)
) ;


--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `AdminID` varchar(240) NOT NULL,
  `Role` varchar(120) NOT NULL,
  `Date` date NOT NULL,
  `Grantor` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`AdminID`),
  KEY `Grantor` (`Grantor`),
  CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`AdminID`) REFERENCES `user` (`UserID`),
  CONSTRAINT `admin_ibfk_2` FOREIGN KEY (`Grantor`) REFERENCES `admin` (`AdminID`)
) ;

--
-- Table structure for table `answer`
--



--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
CREATE TABLE `course` (
  `CourseID` int(11) NOT NULL,
  `Name` varchar(120) NOT NULL,
  `Description` varchar(240) NOT NULL,
  `Icon` varchar(120) DEFAULT NULL,
  `Cost` int(11) NOT NULL,
  `PrimaryTopic` varchar(120) NOT NULL,
  PRIMARY KEY (`CourseID`)
);




--
-- Table structure for table `enrollcourse`
--

DROP TABLE IF EXISTS `enrollcourse`;
CREATE TABLE `enrollcourse` (
  `CourseID` int(11) NOT NULL,
  `UserID` varchar(120) NOT NULL,
  `Date` date NOT NULL,
  `Payment Code` int(11) NOT NULL,
  `Interested` varchar(20) DEFAULT NULL,
  `CourseStatus` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`CourseID`,`UserID`),
  KEY `UserID` (`UserID`),
  CONSTRAINT `enrollcourse_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`),
  CONSTRAINT `enrollcourse_ibfk_2` FOREIGN KEY (`CourseID`) REFERENCES `course` (`CourseID`)
) ;



--
-- Table structure for table `certification`
--

DROP TABLE IF EXISTS `certification`;
CREATE TABLE `certification` (
  `CourseID` int(11) NOT NULL,
  `UserId` varchar(120) NOT NULL,
  `CertificationNo` varchar(120) NOT NULL,
  PRIMARY KEY (`UserId`,`CourseID`,`CertificationNo`),
  CONSTRAINT `certification_ibfk_1` FOREIGN KEY (`UserId`, `CourseID`) REFERENCES `enrollcourse` (`UserID`, `CourseID`)
) ;


--
-- Table structure for table `faculty`
--

DROP TABLE IF EXISTS `faculty`;
CREATE TABLE `faculty` (
  `FacultyID` varchar(120) NOT NULL,
  `validatoradmin` varchar(120) DEFAULT NULL,
  `Title` varchar(120) NOT NULL,
  `Website` varchar(120) NOT NULL,
  `Affiliation` varchar(120) NOT NULL,
  `Status` varchar(120) NOT NULL,
  PRIMARY KEY (`FacultyID`),
  KEY `ValidatorAdmin` (`validatoradmin`),
  CONSTRAINT `faculty_ibfk_1` FOREIGN KEY (`FacultyID`) REFERENCES `user` (`UserID`),
  CONSTRAINT `faculty_ibfk_2` FOREIGN KEY (`ValidatorAdmin`) REFERENCES `admin` (`AdminID`)
) ;


--
-- Table structure for table `create_course`
--

DROP TABLE IF EXISTS `create_course`;
CREATE TABLE `create_course` (
  `UserID` varchar(120) NOT NULL,
  `CourseID` int(11) NOT NULL,
  `CreationDate` date NOT NULL,
  PRIMARY KEY (`UserID`,`CourseID`),
  KEY `CourseID` (`CourseID`),
  CONSTRAINT `create_course_ibfk_1` FOREIGN KEY (`CourseID`) REFERENCES `course` (`CourseID`),
  CONSTRAINT `create_course_ibfk_2` FOREIGN KEY (`UserID`) REFERENCES `faculty` (`FacultyID`)
) ;



--
-- Table structure for table `material`
--

DROP TABLE IF EXISTS `material`;
CREATE TABLE `material` (
  `Order` int(11) NOT NULL,
  `CourseID` int(11) NOT NULL,
  `Name` varchar(120) NOT NULL,
  `MaterialType` varchar(120) NOT NULL,
  PRIMARY KEY (`Order`,`CourseID`),
  KEY `CourseID` (`CourseID`),
  CONSTRAINT `material_ibfk_1` FOREIGN KEY (`CourseID`) REFERENCES `course` (`CourseID`)
) ;

--
-- Table structure for table `link`
--

DROP TABLE IF EXISTS `link`;
CREATE TABLE `link` (
  `Order` int(11) NOT NULL,
  `CourseID` int(11) NOT NULL,
  `URL` varchar(120) NOT NULL,
  `VideoTag` text,
  PRIMARY KEY (`Order`,`CourseID`),
  CONSTRAINT `link_ibfk_1` FOREIGN KEY (`Order`, `CourseID`) REFERENCES `material` (`Order`, `CourseID`)
) ;


--
-- Table structure for table `downloadable`
--

DROP TABLE IF EXISTS `downloadable`;
CREATE TABLE `downloadable` (
  `Order` int(11) NOT NULL,
  `CourseID` int(11) NOT NULL,
  `Path` varchar(120) NOT NULL,
  `Size` varchar(120) NOT NULL,
  `Type` varchar(120) NOT NULL,
  PRIMARY KEY (`Order`,`CourseID`),
  CONSTRAINT `downloadable_ibfk_1` FOREIGN KEY (`Order`, `CourseID`) REFERENCES `material` (`Order`, `CourseID`)
) ;

--
-- Table structure for table `phoneno`
--


DROP TABLE IF EXISTS `phoneno`;
CREATE TABLE `phoneno` (
  `UserID` varchar(120) NOT NULL,
  `PhoneNo` int(11) NOT NULL,
  PRIMARY KEY (`UserID`,`PhoneNo`),
  CONSTRAINT `phoneno_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`)
) ;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
CREATE TABLE `post` (
  `Order` int(11) NOT NULL,
  `CourseID` int(11) NOT NULL,
  `Text` varchar(240) DEFAULT NULL,
  PRIMARY KEY (`Order`,`CourseID`),
  CONSTRAINT `post_ibfk_1` FOREIGN KEY (`Order`, `CourseID`) REFERENCES `material` (`Order`, `CourseID`)
) ;
--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
CREATE TABLE `question` (
  `UserID` varchar(120) NOT NULL,
  `QuestionID` int(11) NOT NULL,
  `MOrderID` int(11) NOT NULL,
  `MCourseID` int(11) NOT NULL,
  `Question` varchar(240) NOT NULL,
  `Visiblity` text NOT NULL,
  `TotalLike` int(11) NOT NULL,
  PRIMARY KEY (`UserID`,`QuestionID`,`MOrderID`,`MCourseID`),
  KEY `MCourseID` (`MCourseID`),
  CONSTRAINT `question_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`),
  CONSTRAINT `question_ibfk_2` FOREIGN KEY (`MCourseID`) REFERENCES `material` (`CourseID`)
) ;

--
-- Table structure for table `answer`
--
DROP TABLE IF EXISTS `answer`;
CREATE TABLE `answer` (
  `UserID` varchar(120) NOT NULL,
  `QuestionID` int(11) NOT NULL,
  `MOrderID` int(11) NOT NULL,
  `MCourseID` int(11) NOT NULL,
  `FacultyID` varchar(120) NOT NULL,
  `Answer` varchar(240) NOT NULL,
  PRIMARY KEY (`UserID`,`QuestionID`,`MOrderID`,`MCourseID`,`FacultyID`),
  KEY `FacultyID` (`FacultyID`),
  CONSTRAINT `answer_ibfk_1` FOREIGN KEY (`FacultyID`) REFERENCES `faculty` (`FacultyID`),
  CONSTRAINT `answer_ibfk_2` FOREIGN KEY (`UserID`, `QuestionID`, `MOrderID`, `MCourseID`) REFERENCES `question` (`UserID`, `QuestionID`, `MOrderID`, `MCourseID`)
) ;


--
-- Table structure for table `sectopic`
--
DROP TABLE IF EXISTS `sectopic`;
CREATE TABLE `sectopic` (
  `CourseID` int(11) NOT NULL,
  `Topic` varchar(120) NOT NULL,
  PRIMARY KEY (`CourseID`,`Topic`),
  CONSTRAINT `sectopic_ibfk_1` FOREIGN KEY (`CourseID`) REFERENCES `course` (`CourseID`)
) ;



--
-- Table structure for table `completion`
--

DROP TABLE IF EXISTS `completion`;
CREATE TABLE `completion` (
  `Order` int(11) NOT NULL,
  `CourseID` int(11) NOT NULL,
  `UserID` varchar(120) NOT NULL,
  `Date` date NOT NULL,
  `Status` varchar(120) NOT NULL,
  `Rating` int(11) DEFAULT NULL,
  `Comments` varchar(240) DEFAULT NULL,
  `TotalScore` int(11) DEFAULT NULL,
  PRIMARY KEY (`Order`,`CourseID`,`UserID`),
  KEY `completion_ibfk_2` (`UserID`),
  CONSTRAINT `completion_ibfk_1` FOREIGN KEY (`Order`, `CourseID`) REFERENCES `material` (`Order`, `CourseID`),
  CONSTRAINT `completion_ibfk_2` FOREIGN KEY (`UserID`) REFERENCES `enrollcourse` (`UserID`)
) ;

alter TABLE `user`add column `salt` varchar(255) NOT NULL;

