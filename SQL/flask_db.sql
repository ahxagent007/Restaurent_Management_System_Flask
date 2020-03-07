-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 22, 2020 at 06:57 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `dish`
--

CREATE TABLE `dish` (
  `dish_id` int(11) NOT NULL,
  `dish_price` int(11) NOT NULL,
  `dish_name` varchar(255) NOT NULL,
  `dish_pic` varchar(300) DEFAULT NULL,
  `dish_des` varchar(300) DEFAULT NULL,
  `isAvailable` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dish`
--

INSERT INTO `dish` (`dish_id`, `dish_price`, `dish_name`, `dish_pic`, `dish_des`, `isAvailable`) VALUES
(1, 12312, 'Burger', '1581357945912.png', 'asdasdas ', 'Available'),
(2, 12312, 'pizza', '1581357973705.png', 'asdasdas ', 'Available'),
(3, 12312, 'Chicken Burger', '1581357999011.png', 'asdasdas ', 'Available'),
(4, 1223, 'Beef Burger', '1581358020693.jpg', 'asd asdas dwq e123 123', 'Unavailable'),
(5, 1223, 'Chowmeen', '1581358030076.jpg', 'asd asdas dwq e123 123', 'Unavailable'),
(6, 1223, 'Faluda', '1581358058234.jpg', 'asd asdas dwq e123 123', 'Unavailable'),
(7, 444, 'Biriani', '1581358237803.jpg', 'jhj fgjfg jfg jfg', 'Unavailable'),
(8, 444, 'Kacchi', '1581358254037.jpg', 'jhj fgjfg jfg jfg', 'Unavailable'),
(9, 350, 'Chicken Polao', '1581451270589.png', 'Kacchi Biriani', 'Available'),
(10, 350, 'strawberry ice-cream', '1581451470200.png', 'Kacchi Biriani', 'Available'),
(11, 350, 'coke', '1581451543315.png', 'Kacchi Biriani', 'Available'),
(12, 222, '7up', '1581451621748.png', 'kasdkaosd 2222', 'Available'),
(13, 222, 'fanta', '1581451650113.png', 'kasdkaosd 2222', 'Available'),
(14, 222, 'Dew', '1581451716972.png', 'kasdkaosd 2222', 'Available');

-- --------------------------------------------------------

--
-- Table structure for table `dish_menu`
--

CREATE TABLE `dish_menu` (
  `dish_id` int(11) NOT NULL,
  `menu_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dish_menu`
--

INSERT INTO `dish_menu` (`dish_id`, `menu_id`) VALUES
(14, 2);

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `user_id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`user_id`, `email`, `password`) VALUES
(1, 'asd@asd.com', '7815696ecbf1c96e6894b779456d330e'),
(2, 'nibir@nibir.com', '123456789'),
(7, 'ahx.agent007@gmail.com', '<md5 HASH object @ 0x0000020C1FA53370>'),
(8, 'heilboy.xian@gmail.com', '<md5 HASH object @ 0x000002066A81FAD0>');

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE `menu` (
  `menu_id` int(11) NOT NULL,
  `menu_name` varchar(255) NOT NULL,
  `isAvailable` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`menu_id`, `menu_name`, `isAvailable`) VALUES
(1, 'Indian', 'Available'),
(2, 'Bangla', 'Available');

-- --------------------------------------------------------

--
-- Table structure for table `message`
--

CREATE TABLE `message` (
  `msg` text NOT NULL,
  `msg_id` int(11) NOT NULL,
  `from_user` int(11) NOT NULL,
  `to_user` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `message`
--

INSERT INTO `message` (`msg`, `msg_id`, `from_user`, `to_user`) VALUES
('message is dummy messagw', 1, 2, 1),
('There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don\'t look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn\'t anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc', 2, 2, 1),
('mea asdssasdasd ge isdummy messasdgwsd asdaasdasd sad', 3, 2, 1),
('dasf sdg dfgh df gaf gdf gafd gdf g', 4, 5, 3),
('dasf sdg dfgh df gaf gdf gafd gdf gasdasdasd', 5, 3, 55);

-- --------------------------------------------------------

--
-- Table structure for table `offers`
--

CREATE TABLE `offers` (
  `offer_id` int(11) NOT NULL,
  `discount` int(11) NOT NULL,
  `date_from` date DEFAULT NULL,
  `date_to` date DEFAULT NULL,
  `offer_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `offers`
--

INSERT INTO `offers` (`offer_id`, `discount`, `date_from`, `date_to`, `offer_name`) VALUES
(1, 20, '2020-02-12', '2020-02-18', '2020 Offer');

-- --------------------------------------------------------

--
-- Table structure for table `offers_dishes`
--

CREATE TABLE `offers_dishes` (
  `offer_id` int(11) NOT NULL,
  `dish_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `order_id` int(11) NOT NULL,
  `order_date` varchar(100) NOT NULL,
  `total_bill` int(11) NOT NULL,
  `VAT` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `pay_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order`
--

INSERT INTO `order` (`order_id`, `order_date`, `total_bill`, `VAT`, `user_id`, `pay_id`) VALUES
(1, '2020-02-09', 505, 15, 1, 0),
(14, '21-02-2020 14:50:28', 36936, 0, 14, 0),
(15, '21-02-2020 15:44:46', 36936, 0, 1, 0),
(16, '21-02-2020 15:46:13', 62783, 0, 6, 0),
(17, '21-02-2020 15:59:23', 283176, 0, 7, 0),
(18, '21-02-2020 16:08:41', 2017, 0, 7, 0),
(19, '21-02-2020 16:09:24', 13979, 0, 7, 0),
(20, '22-02-2020 22:21:16', 1231200, 0, 8, 0);

-- --------------------------------------------------------

--
-- Table structure for table `ordered_dishes`
--

CREATE TABLE `ordered_dishes` (
  `order_id` int(11) NOT NULL,
  `dish_id` int(11) NOT NULL,
  `order_comment` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ordered_dishes`
--

INSERT INTO `ordered_dishes` (`order_id`, `dish_id`, `order_comment`) VALUES
(1, 1, 'comment here'),
(14, 2, 'asdasd'),
(14, 2, 'asdasd'),
(14, 2, 'asdasd'),
(15, 2, 'aaaazzzz'),
(15, 2, 'aaaazzzz'),
(15, 2, 'aaaazzzz'),
(16, 2, 'aszxzxc'),
(16, 2, 'aszxzxc'),
(16, 2, 'aszxzxc'),
(16, 6, 'asa'),
(16, 2, ''),
(16, 2, ''),
(17, 2, ''),
(17, 2, 'asd'),
(18, 6, ''),
(18, 7, ''),
(18, 9, ''),
(19, 2, ''),
(19, 6, ''),
(19, 7, ''),
(20, 2, 'Extraaa spiceeee');

-- --------------------------------------------------------

--
-- Table structure for table `orders_tables`
--

CREATE TABLE `orders_tables` (
  `table_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `pay_id` int(11) NOT NULL,
  `pay_method` varchar(10) NOT NULL,
  `pay_timestamp` timestamp NOT NULL DEFAULT current_timestamp(),
  `txn` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`pay_id`, `pay_method`, `pay_timestamp`, `txn`) VALUES
(1, 'bKash', '2020-02-08 18:13:43', 'WkX7&R98XC'),
(2, 'CASH', '2020-02-08 18:13:43', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL,
  `product_cat` varchar(50) NOT NULL,
  `product_quantity` int(11) NOT NULL,
  `stockStatus` varchar(20) DEFAULT NULL,
  `product_des` varchar(255) DEFAULT NULL,
  `product_pic` varchar(255) DEFAULT NULL,
  `product_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `product_cat`, `product_quantity`, `stockStatus`, `product_des`, `product_pic`, `product_name`) VALUES
(1, 'Vegitable', 0, NULL, 'asdasd', '1582291479760.jpg', 'asdas'),
(2, 'Vegitable', 222, NULL, 'chicken meat', '1582308445385.jpg', 'Chicken'),
(3, 'Vegitable', 333, NULL, 'feeeb', '1582308462001.jpg', 'beef'),
(4, 'Vegitable', 41, NULL, 'asdasdas d', '1582308481458.jpg', 'product 02'),
(5, 'Vegitable', 7, NULL, 'asdasdas', '1582309908376.png', 'ending soon');

-- --------------------------------------------------------

--
-- Table structure for table `table`
--

CREATE TABLE `table` (
  `table_id` int(11) NOT NULL,
  `chair` int(11) NOT NULL,
  `table_no` varchar(20) NOT NULL,
  `vacancy` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `table`
--

INSERT INTO `table` (`table_id`, `chair`, `table_no`, `vacancy`) VALUES
(1, 8, 'E55', 'YES'),
(2, 4, 'E05', 'YES');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `phone_no` varchar(20) DEFAULT NULL,
  `email` varchar(150) NOT NULL,
  `type` varchar(20) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `phone_no`, `email`, `type`, `address`, `name`) VALUES
(1, '132165465', 'xian@xian.com', 'EMP', 'Azimpur', 'Xian'),
(2, '135646', 'nibir@nibir.com', 'EMP', 'mirpur', 'Nibir'),
(3, '4564563456', 'asd@asd', 'CUS', 'Dont  know', 'Niloy'),
(4, '7637', 'asd@asd', 'CUS', 'Dont  know', 'Nigga'),
(5, '7637', 'asd@asd', 'CUS', 'Dont  know', 'Emon'),
(6, '7637', 'asd@asd', 'CUS', 'Dont  know', 'Lal Mia'),
(7, '01764009201', 'ahx.agent007@gmail.com', 'EMP', '68, New Polton, Azimpur, Dhaka-1205, Bangladesh', 'Abir Hosain Xian'),
(8, '01673398900', 'heilboy.xian@gmail.com', 'CUS', '212/1, west Monipur, MIrpur-02,, Dhaka-1206', 'Abir Hossain Xian');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dish`
--
ALTER TABLE `dish`
  ADD PRIMARY KEY (`dish_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`menu_id`);

--
-- Indexes for table `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`msg_id`);

--
-- Indexes for table `offers`
--
ALTER TABLE `offers`
  ADD PRIMARY KEY (`offer_id`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`order_id`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`pay_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `table`
--
ALTER TABLE `table`
  ADD PRIMARY KEY (`table_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dish`
--
ALTER TABLE `dish`
  MODIFY `dish_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `menu`
--
ALTER TABLE `menu`
  MODIFY `menu_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `message`
--
ALTER TABLE `message`
  MODIFY `msg_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `offers`
--
ALTER TABLE `offers`
  MODIFY `offer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `order`
--
ALTER TABLE `order`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `pay_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `table`
--
ALTER TABLE `table`
  MODIFY `table_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
