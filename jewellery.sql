-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 27, 2022 at 07:09 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jewellery`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_login`
--

CREATE TABLE `admin_login` (
  `id` int(11) NOT NULL,
  `username` varchar(100) COLLATE utf16_bin NOT NULL,
  `password` varchar(255) COLLATE utf16_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_bin;

--
-- Dumping data for table `admin_login`
--

INSERT INTO `admin_login` (`id`, `username`, `password`) VALUES
(1, 'admin@administration.com', 'pbkdf2:sha256:260000$SpqctB4F0MQcTghW$b085601ecc4f8bc287be61f0f253fc5d34937439e22aaeaee10af98785331ecd');

-- --------------------------------------------------------

--
-- Table structure for table `delivery_login`
--

CREATE TABLE `delivery_login` (
  `id` int(11) NOT NULL,
  `username` varchar(100) COLLATE utf16_bin NOT NULL,
  `password` varchar(255) COLLATE utf16_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_bin;

--
-- Dumping data for table `delivery_login`
--

INSERT INTO `delivery_login` (`id`, `username`, `password`) VALUES
(1, 'deliverer@delivery.com', 'pbkdf2:sha256:260000$Cer9Cx12lRyeHlEb$04f6945165d8d6132a4d2202b13797683cd2fb6d5996bedb364c83f9e3b548e1');

-- --------------------------------------------------------

--
-- Table structure for table `history`
--

CREATE TABLE `history` (
  `id` int(11) NOT NULL,
  `itemId` int(11) NOT NULL,
  `item` varchar(255) NOT NULL,
  `customer` varchar(255) NOT NULL,
  `size` varchar(255) NOT NULL,
  `method` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `delivery` varchar(255) NOT NULL,
  `count` varchar(255) NOT NULL,
  `price` int(11) NOT NULL,
  `date` varchar(255) NOT NULL,
  `contact` varchar(20) NOT NULL,
  `status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `history`
--

INSERT INTO `history` (`id`, `itemId`, `item`, `customer`, `size`, `method`, `location`, `delivery`, `count`, `price`, `date`, `contact`, `status`) VALUES
(1, 1, 'Decent', 'linda@gmail.com', '3', 'Cash On Delivery', 'Spanish Town', 'Knutford express', '3', 60, '27/11/22', '', 'pending'),
(2, 4, 'Collar', 'linda@gmail.com', 'Standard', 'Bank Transfer', 'Kingstone', 'Bank Transfer', '3', 105, '27/11/22', '', 'delivered'),
(3, 2, 'Cuff', 'linda@gmail.com', '1', 'Cash On Delivery', 'Spanish Town', 'Knutford express', '1', 15, '27/11/22', '', 'cancelled'),
(4, 5, 'Moon', 'linda@gmail.com', 'Standard', 'Cash On Delivery', 'Spanish Town', 'Zipmail', '2', 80, '27/11/22', '', 'delivery failed'),
(5, 5, 'Moon', 'linda@gmail.com', 'Standard', 'Cash On Delivery', 'Spanish Town', 'Knutford express', '2', 80, '27/11/22', '+12343212376', 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `id` int(11) NOT NULL,
  `type` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `count` int(11) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`id`, `type`, `name`, `count`, `price`) VALUES
(1, 1, 'Decent', 36, 20),
(2, 1, 'Cuff', 37, 15),
(3, 1, 'Gemstone', 0, 65),
(4, 2, 'Collar', 88, 35),
(5, 2, 'Moon', 40, 40);

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE `items` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `items`
--

INSERT INTO `items` (`id`, `name`) VALUES
(1, 'braclets'),
(2, 'necklace');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`id`, `username`, `password`) VALUES
(1, 'linda@gmail.com', 'pbkdf2:sha256:260000$MmmaxPfSfrgaJUUr$f594e5faa18f2ee003e79c2eca445e00bc55e1d00c20c9c871aa6548a2dd2a7d');

-- --------------------------------------------------------

--
-- Table structure for table `profile`
--

CREATE TABLE `profile` (
  `id` int(11) NOT NULL,
  `loginid` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `contact` varchar(255) NOT NULL,
  `birthday` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `profile`
--

INSERT INTO `profile` (`id`, `loginid`, `name`, `contact`, `birthday`, `gender`) VALUES
(1, 'linda@gmail.com', 'Linda John', '+12343212376', '04/11/1995', 'Female');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_login`
--
ALTER TABLE `admin_login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `delivery_login`
--
ALTER TABLE `delivery_login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `history`
--
ALTER TABLE `history`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `profile`
--
ALTER TABLE `profile`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_login`
--
ALTER TABLE `admin_login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `delivery_login`
--
ALTER TABLE `delivery_login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `history`
--
ALTER TABLE `history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `items`
--
ALTER TABLE `items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `profile`
--
ALTER TABLE `profile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
