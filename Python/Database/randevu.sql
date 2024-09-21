-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 23 May 2024, 16:13:13
-- Sunucu sürümü: 10.4.28-MariaDB
-- PHP Sürümü: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `randevu`
--
CREATE DATABASE IF NOT EXISTS `randevu` DEFAULT CHARACTER SET utf8 COLLATE utf8_turkish_ci;
USE `randevu`;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `bolum`
--

CREATE TABLE `bolum` (
  `id` int(11) NOT NULL,
  `ad` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `bolum`
--

INSERT INTO `bolum` (`id`, `ad`) VALUES
(1, 'Dahiliye'),
(2, 'Göz'),
(3, 'Cildiye'),
(4, 'Nöroloji'),
(6, 'Ortopedi');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `doktor`
--

CREATE TABLE `doktor` (
  `id` int(11) NOT NULL,
  `bolum_id` int(11) NOT NULL,
  `ad` varchar(50) NOT NULL,
  `soyad` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `doktor`
--

INSERT INTO `doktor` (`id`, `bolum_id`, `ad`, `soyad`) VALUES
(1, 1, 'Kemal', 'Tarcan'),
(2, 1, 'Selim', 'Güngör'),
(4, 2, 'Fırat', 'Saylan'),
(5, 2, 'Nermin', 'Salepci'),
(6, 4, 'Nurhan', 'Mertol'),
(7, 4, 'Murat', 'Sönmez'),
(8, 6, 'Nazan', 'Dalkılıç'),
(9, 6, 'Fatih', 'Günal'),
(10, 4, 'Ceyda', 'Sönmez'),
(11, 2, 'Kerim', 'Can'),
(12, 4, 'Tufan', 'Adıgüzel'),
(13, 3, 'Mehmet', 'Günal'),
(14, 3, 'Meltem', 'Bayrak');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `doktor_uygun_gunler`
--

CREATE TABLE `doktor_uygun_gunler` (
  `ID` int(11) NOT NULL,
  `doktorID` int(11) DEFAULT NULL,
  `gunNo` tinyint(4) NOT NULL,
  `saatNo` tinyint(4) NOT NULL,
  `uygun` tinyint(4) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `doktor_uygun_gunler`
--

INSERT INTO `doktor_uygun_gunler` (`ID`, `doktorID`, `gunNo`, `saatNo`, `uygun`) VALUES
(2, 1, 1, 2, 0),
(3, 1, 1, 5, 1),
(4, 1, 3, 1, 0),
(5, 1, 3, 6, 0),
(6, 2, 1, 1, 1),
(7, 2, 1, 2, 0),
(8, 2, 1, 3, 0),
(9, 2, 1, 6, 0),
(10, 2, 2, 3, 0),
(11, 2, 2, 6, 0),
(12, 2, 2, 7, 0),
(13, 2, 3, 1, 0),
(14, 2, 3, 2, 0),
(15, 2, 3, 3, 0),
(16, 2, 3, 6, 0),
(17, 2, 4, 5, 0),
(18, 2, 4, 6, 0),
(19, 2, 4, 7, 0),
(20, 2, 5, 2, 0),
(21, 2, 5, 3, 0),
(22, 2, 5, 4, 0),
(23, 4, 1, 1, 0),
(24, 4, 1, 2, 0),
(25, 4, 1, 5, 0),
(26, 4, 2, 2, 0),
(27, 4, 2, 3, 0),
(28, 4, 2, 6, 0),
(29, 4, 5, 5, 0),
(30, 4, 5, 6, 0),
(31, 4, 5, 7, 0),
(32, 5, 1, 1, 0),
(33, 5, 1, 2, 0),
(34, 5, 1, 3, 0),
(35, 5, 1, 5, 0),
(36, 5, 1, 6, 0),
(37, 5, 4, 1, 0),
(38, 5, 4, 4, 0),
(39, 5, 4, 5, 0),
(40, 5, 5, 1, 0),
(41, 5, 5, 2, 0),
(42, 6, 1, 2, 0),
(43, 6, 1, 3, 0),
(44, 6, 1, 4, 0),
(45, 6, 2, 1, 0),
(46, 6, 2, 3, 0),
(47, 6, 2, 4, 0),
(48, 6, 3, 3, 0),
(49, 6, 3, 4, 0),
(50, 6, 3, 5, 0),
(51, 6, 4, 2, 0),
(52, 6, 5, 1, 0),
(53, NULL, 0, 0, 0),
(54, 7, 1, 1, 0),
(55, 7, 2, 1, 0),
(56, 7, 0, 0, 0),
(57, 7, 3, 1, 0),
(58, 7, 3, 2, 0),
(59, 7, 3, 3, 0),
(60, 7, 3, 4, 0);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `hasta`
--

CREATE TABLE `hasta` (
  `tc_kimlik` char(11) NOT NULL,
  `ad` varchar(50) NOT NULL,
  `soyad` varchar(50) NOT NULL,
  `telefon` char(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `hasta`
--

INSERT INTO `hasta` (`tc_kimlik`, `ad`, `soyad`, `telefon`) VALUES
('10293847586', 'Muhittin', 'Şahin', '222'),
('72635241634', 'Fatih', 'Erkoç', '555'),
('82736453421', 'Melek', 'Yalvaç', '111'),
('85746591023', 'Nurdan', 'Ersan', '222');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `randevular`
--

CREATE TABLE `randevular` (
  `id` int(11) NOT NULL,
  `hasta` char(11) NOT NULL,
  `doktor` int(11) NOT NULL,
  `gun` tinyint(4) NOT NULL,
  `saatNo` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `randevular`
--

INSERT INTO `randevular` (`id`, `hasta`, `doktor`, `gun`, `saatNo`) VALUES
(12, '10293847586', 1, 1, 5),
(13, '10293847586', 2, 1, 1);

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `bolum`
--
ALTER TABLE `bolum`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `doktor`
--
ALTER TABLE `doktor`
  ADD PRIMARY KEY (`id`),
  ADD KEY `bolum_id` (`bolum_id`);

--
-- Tablo için indeksler `doktor_uygun_gunler`
--
ALTER TABLE `doktor_uygun_gunler`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `doktorID` (`doktorID`);

--
-- Tablo için indeksler `hasta`
--
ALTER TABLE `hasta`
  ADD PRIMARY KEY (`tc_kimlik`);

--
-- Tablo için indeksler `randevular`
--
ALTER TABLE `randevular`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hasta` (`hasta`,`doktor`),
  ADD KEY `doktor` (`doktor`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `bolum`
--
ALTER TABLE `bolum`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Tablo için AUTO_INCREMENT değeri `doktor`
--
ALTER TABLE `doktor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Tablo için AUTO_INCREMENT değeri `doktor_uygun_gunler`
--
ALTER TABLE `doktor_uygun_gunler`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- Tablo için AUTO_INCREMENT değeri `randevular`
--
ALTER TABLE `randevular`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Dökümü yapılmış tablolar için kısıtlamalar
--

--
-- Tablo kısıtlamaları `doktor`
--
ALTER TABLE `doktor`
  ADD CONSTRAINT `doktor_ibfk_1` FOREIGN KEY (`bolum_id`) REFERENCES `bolum` (`id`);

--
-- Tablo kısıtlamaları `doktor_uygun_gunler`
--
ALTER TABLE `doktor_uygun_gunler`
  ADD CONSTRAINT `doktor_uygun_gunler_ibfk_1` FOREIGN KEY (`doktorID`) REFERENCES `doktor` (`id`) ON DELETE SET NULL ON UPDATE SET NULL;

--
-- Tablo kısıtlamaları `randevular`
--
ALTER TABLE `randevular`
  ADD CONSTRAINT `randevular_ibfk_1` FOREIGN KEY (`hasta`) REFERENCES `hasta` (`tc_kimlik`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `randevular_ibfk_2` FOREIGN KEY (`doktor`) REFERENCES `doktor` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
