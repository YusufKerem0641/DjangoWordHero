-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 29 Nis 2024, 04:08:30
-- Sunucu sürümü: 10.4.28-MariaDB
-- PHP Sürümü: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `deneme`
--
CREATE DATABASE IF NOT EXISTS `deneme` DEFAULT CHARACTER SET utf8 COLLATE utf8_turkish_ci;
USE `deneme`;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kisi`
--

CREATE TABLE `kisi` (
  `id` int(11) NOT NULL,
  `kisiID` int(11) NOT NULL,
  `tckno` bigint(20) NOT NULL,
  `dyil` year(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kullanici`
--

CREATE TABLE `kullanici` (
  `id` int(11) NOT NULL,
  `ad` varchar(50) NOT NULL,
  `soyad` varchar(50) NOT NULL,
  `eposta` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `kullanici`
--

INSERT INTO `kullanici` (`id`, `ad`, `soyad`, `eposta`) VALUES
(1, 'Ahmet', 'Türkmen', 'aturmen@gazi.edu.tr'),
(2, 'Melek', 'Can', 'mcan@gazi.edu.tr'),
(3, 'Rıza', 'Çalık', 'rcalik@gazi.edu.tr'),
(4, 'Selin', 'Gündoğdu', 'sgundogdu@gazi.edu.tr'),
(5, 'Lale', 'Mansur', 'lmans@gmail.com'),
(6, 'Korhan', 'Abay', 'kabay@gmail.com'),
(7, 'Sema', 'Balcı', 'sbalci@gmail.com'),
(8, 'Onur', 'Dönmez', 'odonmez@gmail.com'),
(9, 'Fatih', 'Canbaz', 'canbaz@hotmail.com'),
(10, 'Gülen', 'Kahraman', 'gkahrm@hotmail.com'),
(11, 'Şule', 'Bektaş', 'sbektas@hotmail.com'),
(12, 'Sezer', 'Güven', 'sguven@yahoo.com'),
(13, 'Ebru', 'Güzel', 'eguzel@yahoo.com'),
(14, 'Merve', 'Çakır', 'mcakir@yahoo.com'),
(15, 'Suzan', 'Erciyes', 'suzan@yahoo.com'),
(16, 'Tuğrul', 'Pekcan', 'pekcan@yahoo.com'),
(17, 'Meltem', 'Yılmaz', 'myilmaz@gazi.edu.tr'),
(18, 'Cemil', 'İpek', 'cipek@yahoo.com');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `kisi`
--
ALTER TABLE `kisi`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `kullanici`
--
ALTER TABLE `kullanici`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `kisi`
--
ALTER TABLE `kisi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Tablo için AUTO_INCREMENT değeri `kullanici`
--
ALTER TABLE `kullanici`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
