-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 31, 2024 at 10:06 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbgroup12`
--

-- --------------------------------------------------------

--
-- Table structure for table `administrator`
--

CREATE TABLE `administrator` (
  `adminID` bigint(20) NOT NULL,
  `name` varchar(250) NOT NULL,
  `position` varchar(15) NOT NULL,
  `contactInformation` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `administrator`
--

INSERT INTO `administrator` (`adminID`, `name`, `position`, `contactInformation`) VALUES
(1, 'Travis Scott', 'Head', '123456'),
(2, 'Al Jerms', 'Secretary', '234567');

-- --------------------------------------------------------

--
-- Table structure for table `exception`
--

CREATE TABLE `exception` (
  `exceptionID` bigint(20) NOT NULL,
  `dateStart` date NOT NULL,
  `dateEnd` date NOT NULL,
  `studentID` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `pending`
--

CREATE TABLE `pending` (
  `studentID` bigint(12) NOT NULL,
  `name` varchar(75) NOT NULL,
  `section` varchar(10) NOT NULL,
  `violation` varchar(50) NOT NULL,
  `dateAndTime` datetime NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `schoolrules`
--

CREATE TABLE `schoolrules` (
  `ruleID` bigint(20) NOT NULL,
  `description` varchar(500) NOT NULL,
  `category` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `schoolrules`
--

INSERT INTO `schoolrules` (`ruleID`, `description`, `category`) VALUES
(12, 'Bullying and Harassment: Schools typically prohibit bullying, harassment, and any form of discrimination.', 'Major'),
(13, 'Dress Code: Many schools have guidelines on appropriate attire to maintain a focused and professional learning environment.', 'Minor');

-- --------------------------------------------------------

--
-- Table structure for table `securityguard`
--

CREATE TABLE `securityguard` (
  `guardID` bigint(20) NOT NULL,
  `name` varchar(250) NOT NULL,
  `contactNumber` bigint(20) NOT NULL,
  `shift` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `securityguard`
--

INSERT INTO `securityguard` (`guardID`, `name`, `contactNumber`, `shift`) VALUES
(32, 'Lady Gaurd', 123443, '0000-00-00'),
(33, 'Chip Gaurd', 122265, '0000-00-00');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `studentID` bigint(20) NOT NULL,
  `name` varchar(250) NOT NULL,
  `section` varchar(8) NOT NULL,
  `contactInformation` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`studentID`, `name`, `section`, `contactInformation`) VALUES
(220000001005, 'Earl D. Ang', 'BSIT_2A', '09994824332'),
(220000002183, 'Kobe J. Corpuz', 'BSIT_2B', '9922516022'),
(220000002436, 'Myk Lorence N. Palado', 'BSIT_2B', '09466800117');

-- --------------------------------------------------------

--
-- Table structure for table `violation`
--

CREATE TABLE `violation` (
  `violationID` bigint(20) NOT NULL,
  `description` varchar(500) NOT NULL,
  `ruleID` bigint(20) NOT NULL,
  `adminID` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `violation`
--

INSERT INTO `violation` (`violationID`, `description`, `ruleID`, `adminID`) VALUES
(23, 'Bullying', 12, 1),
(24, 'Dress Code', 13, 2);

-- --------------------------------------------------------

--
-- Table structure for table `violationdetails`
--

CREATE TABLE `violationdetails` (
  `reportID` bigint(20) NOT NULL,
  `date` date NOT NULL,
  `venue` varchar(250) NOT NULL,
  `time` date NOT NULL,
  `status` tinyint(1) NOT NULL,
  `sanctions` varchar(50) NOT NULL,
  `studentID` bigint(20) NOT NULL,
  `violationID` bigint(20) NOT NULL,
  `guardID` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `violationdetails`
--

INSERT INTO `violationdetails` (`reportID`, `date`, `venue`, `time`, `status`, `sanctions`, `studentID`, `violationID`, `guardID`) VALUES
(1, '2023-01-01', 'School', '0000-00-00', 0, 'One week suspension', 220000002436, 23, 32);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `administrator`
--
ALTER TABLE `administrator`
  ADD PRIMARY KEY (`adminID`);

--
-- Indexes for table `exception`
--
ALTER TABLE `exception`
  ADD PRIMARY KEY (`exceptionID`),
  ADD KEY `fk_studentID` (`studentID`);

--
-- Indexes for table `schoolrules`
--
ALTER TABLE `schoolrules`
  ADD PRIMARY KEY (`ruleID`);

--
-- Indexes for table `securityguard`
--
ALTER TABLE `securityguard`
  ADD PRIMARY KEY (`guardID`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`studentID`);

--
-- Indexes for table `violation`
--
ALTER TABLE `violation`
  ADD PRIMARY KEY (`violationID`),
  ADD KEY `fk_ruleID` (`ruleID`),
  ADD KEY `fk_adminID` (`adminID`);

--
-- Indexes for table `violationdetails`
--
ALTER TABLE `violationdetails`
  ADD PRIMARY KEY (`reportID`),
  ADD KEY `fk_violationID` (`violationID`),
  ADD KEY `fk_guardID` (`guardID`),
  ADD KEY `fk_studentID1` (`studentID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `administrator`
--
ALTER TABLE `administrator`
  MODIFY `adminID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `exception`
--
ALTER TABLE `exception`
  MODIFY `exceptionID` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `schoolrules`
--
ALTER TABLE `schoolrules`
  MODIFY `ruleID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `securityguard`
--
ALTER TABLE `securityguard`
  MODIFY `guardID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `studentID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=220000002437;

--
-- AUTO_INCREMENT for table `violation`
--
ALTER TABLE `violation`
  MODIFY `violationID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `violationdetails`
--
ALTER TABLE `violationdetails`
  MODIFY `reportID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `exception`
--
ALTER TABLE `exception`
  ADD CONSTRAINT `fk_studentID` FOREIGN KEY (`studentID`) REFERENCES `student` (`studentID`);

--
-- Constraints for table `violation`
--
ALTER TABLE `violation`
  ADD CONSTRAINT `fk_adminID` FOREIGN KEY (`adminID`) REFERENCES `administrator` (`adminID`),
  ADD CONSTRAINT `fk_ruleID` FOREIGN KEY (`ruleID`) REFERENCES `schoolrules` (`ruleID`);

--
-- Constraints for table `violationdetails`
--
ALTER TABLE `violationdetails`
  ADD CONSTRAINT `fk_guardID` FOREIGN KEY (`guardID`) REFERENCES `securityguard` (`guardID`),
  ADD CONSTRAINT `fk_studentID1` FOREIGN KEY (`studentID`) REFERENCES `student` (`studentID`),
  ADD CONSTRAINT `fk_violationID` FOREIGN KEY (`violationID`) REFERENCES `violation` (`violationID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
