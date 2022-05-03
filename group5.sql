-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 04, 2022 at 12:42 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `group5`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `UserId` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `First_Name` varchar(100) NOT NULL,
  `Last_Name` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Phone_Number` varchar(100) NOT NULL,
  `Billing_Address` varchar(100) NOT NULL,
  `Zip` int(5) NOT NULL,
  `CIty` varchar(100) NOT NULL,
  `State` varchar(100) NOT NULL,
  `Card_Name` varchar(100) NOT NULL,
  `Card_Number` int(30) NOT NULL,
  `Shipping_Address` varchar(100) NOT NULL,
  `Shipping_Zip` int(5) NOT NULL,
  `Order` varchar(100) NOT NULL,
  `Num_Order` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`UserId`, `Password`, `First_Name`, `Last_Name`, `Email`, `Phone_Number`, `Billing_Address`, `Zip`, `CIty`, `State`, `Card_Name`, `Card_Number`, `Shipping_Address`, `Shipping_Zip`, `Order`, `Num_Order`) VALUES
('', '5436', 'rushma', 'parajuli', 'rushma.parajuli123@gmail.com', '467087679989', '940 N Jackson Street', 39759, 'Starkville', 'Mississippi', '0', 75038, '0', 9, '', 0);

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `ISBN` varchar(100) NOT NULL,
  `Price` int(100) NOT NULL,
  `Title` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`ISBN`, `Price`, `Title`) VALUES
('9780385539258', 36, 'A Little Life'),
('9758978321978', 26, 'The Silence of the Lambs'),
('9879235983794', 21, 'Hannibal Rising'),
('9776352716714', 25, 'Red Dragon'),
('97080385539258', 36, 'A Little Life'),
('56789098655 25 Alchemist', 0, '');

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `ItemName` varchar(100) NOT NULL,
  `ItemID` varchar(100) NOT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `Category` varchar(100) NOT NULL,
  `Price` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cart`
--

INSERT INTO `cart` (`ItemName`, `ItemID`, `quantity`, `Category`, `Price`) VALUES
('Red Dragon', '54718', '5', '1', 25),
('Dune', '53238', '4', '2', 15),
('Red Dragon', '54718', '5', '1', 25),
('Red Dragon', '54718', '5', '1', 25),
('Red Dragon', '54718', '5', '1', 25);

-- --------------------------------------------------------

--
-- Table structure for table `comics`
--

CREATE TABLE `comics` (
  `Title` varchar(100) NOT NULL,
  `Publisher` varchar(100) NOT NULL,
  `price` int(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `ItemName` varchar(100) NOT NULL,
  `ItemID` int(100) NOT NULL,
  `stock` varchar(100) DEFAULT NULL,
  `Category` varchar(100) NOT NULL,
  `Price` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`ItemName`, `ItemID`, `stock`, `Category`, `Price`) VALUES
('Red Dragon', 54718, '5', '1', '25'),
('Hannibal Rising', 67638, '20', '1', '5.99'),
('Dune', 53238, '4', '2', '14.99'),
('Batman and the Joker', 54362, '10', '3', '5');

-- --------------------------------------------------------

--
-- Table structure for table `movies`
--

CREATE TABLE `movies` (
  `Name` varchar(100) NOT NULL,
  `Type` varchar(100) NOT NULL,
  `Price` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `movies`
--

INSERT INTO `movies` (`Name`, `Type`, `Price`) VALUES
('The Silence of the Lambs', 'Crime', '5.99'),
('The Shawshank Redemption', 'Drama', '4.99'),
('Dune', 'Sci-Fi', '8.99'),
('Interstellar', 'Sci-Fi', '7.99'),
('Identity', 'Thriller', '4.99'),
('The Godfather', 'Drama', '6.99'),
('Troy', 'Historical-Drama', '5.99');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
