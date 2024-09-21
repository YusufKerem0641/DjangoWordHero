-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 16 May 2024, 10:56:36
-- Sunucu sürümü: 10.4.32-MariaDB
-- PHP Sürümü: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `imdb`
--
CREATE DATABASE IF NOT EXISTS `imdb` DEFAULT CHARACTER SET utf8 COLLATE utf8_turkish_ci;
USE `imdb`;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `elestirmen`
--

CREATE TABLE `elestirmen` (
  `elestirmenID` int(11) NOT NULL,
  `elestirmenAdi` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `elestirmen`
--

INSERT INTO `elestirmen` (`elestirmenID`, `elestirmenAdi`) VALUES
(1, 'Tolga Güyer'),
(2, 'Murat Soydan'),
(3, 'Meltem Dönmez'),
(4, 'Kemal Ulutürk');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `filmbilgi`
--

CREATE TABLE `filmbilgi` (
  `filmID` int(11) NOT NULL,
  `filmAdi` varchar(50) NOT NULL,
  `yapimYili` year(4) NOT NULL,
  `yonetmen` int(11) NOT NULL,
  `yapimci` int(11) NOT NULL,
  `yayinSirketi` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `filmbilgi`
--

INSERT INTO `filmbilgi` (`filmID`, `filmAdi`, `yapimYili`, `yonetmen`, `yapimci`, `yayinSirketi`) VALUES
(1, 'Rebel Moon', '2023', 1, 1, 1),
(2, 'Fifth Element', '1997', 4, 2, 2);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `filmyorum`
--

CREATE TABLE `filmyorum` (
  `yorumID` int(11) NOT NULL,
  `filmID` int(11) NOT NULL,
  `elestirmenID` int(11) NOT NULL,
  `yildizSayisi` tinyint(4) NOT NULL,
  `yorum` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `filmyorum`
--

INSERT INTO `filmyorum` (`yorumID`, `filmID`, `elestirmenID`, `yildizSayisi`, `yorum`) VALUES
(1, 1, 1, 7, 'Modern bir 7 samuray hikayesi...'),
(2, 2, 1, 10, 'Gelmiş geçmiş en iyi bilim kurgu filmi...'),
(3, 1, 2, 8, 'Oldukça iyi bir fantastik hikaye.'),
(4, 2, 2, 6, 'Kurgusu fazlaca karışık bir görsel şölen.'),
(5, 1, 3, 3, 'Beğenmedim pek');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `yapimci`
--

CREATE TABLE `yapimci` (
  `yapimciID` int(11) NOT NULL,
  `yapimciAdi` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `yapimci`
--

INSERT INTO `yapimci` (`yapimciID`, `yapimciAdi`) VALUES
(1, 'Sarah Bowen'),
(2, 'Patrice Ledoux');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `yayinci`
--

CREATE TABLE `yayinci` (
  `yayinciID` int(11) NOT NULL,
  `yayinciAdi` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `yayinci`
--

INSERT INTO `yayinci` (`yayinciID`, `yayinciAdi`) VALUES
(1, 'Warner Bros'),
(2, 'Paramount'),
(3, 'Sony'),
(4, 'Universal'),
(5, '20th Century Fox'),
(6, 'Columbia'),
(7, 'Pixar'),
(8, 'Walt Disney');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `yonetmen`
--

CREATE TABLE `yonetmen` (
  `yonetmenID` int(11) NOT NULL,
  `yonetmenAdi` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `yonetmen`
--

INSERT INTO `yonetmen` (`yonetmenID`, `yonetmenAdi`) VALUES
(1, 'Zack Snyder'),
(2, 'Ridley Scott'),
(3, 'Peter Jackson'),
(4, 'Luc Besson'),
(5, 'Tim Burton'),
(7, 'Martin Scorsese');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `elestirmen`
--
ALTER TABLE `elestirmen`
  ADD PRIMARY KEY (`elestirmenID`);

--
-- Tablo için indeksler `filmbilgi`
--
ALTER TABLE `filmbilgi`
  ADD PRIMARY KEY (`filmID`),
  ADD KEY `yapimci` (`yapimci`),
  ADD KEY `yayinSirketi` (`yayinSirketi`),
  ADD KEY `yonetmen` (`yonetmen`) USING BTREE;

--
-- Tablo için indeksler `filmyorum`
--
ALTER TABLE `filmyorum`
  ADD PRIMARY KEY (`yorumID`),
  ADD KEY `elestirmenID` (`elestirmenID`),
  ADD KEY `filmID` (`filmID`);

--
-- Tablo için indeksler `yapimci`
--
ALTER TABLE `yapimci`
  ADD PRIMARY KEY (`yapimciID`);

--
-- Tablo için indeksler `yayinci`
--
ALTER TABLE `yayinci`
  ADD PRIMARY KEY (`yayinciID`);

--
-- Tablo için indeksler `yonetmen`
--
ALTER TABLE `yonetmen`
  ADD PRIMARY KEY (`yonetmenID`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `elestirmen`
--
ALTER TABLE `elestirmen`
  MODIFY `elestirmenID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Tablo için AUTO_INCREMENT değeri `filmbilgi`
--
ALTER TABLE `filmbilgi`
  MODIFY `filmID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Tablo için AUTO_INCREMENT değeri `filmyorum`
--
ALTER TABLE `filmyorum`
  MODIFY `yorumID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Tablo için AUTO_INCREMENT değeri `yapimci`
--
ALTER TABLE `yapimci`
  MODIFY `yapimciID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Tablo için AUTO_INCREMENT değeri `yayinci`
--
ALTER TABLE `yayinci`
  MODIFY `yayinciID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Tablo için AUTO_INCREMENT değeri `yonetmen`
--
ALTER TABLE `yonetmen`
  MODIFY `yonetmenID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Dökümü yapılmış tablolar için kısıtlamalar
--

--
-- Tablo kısıtlamaları `filmbilgi`
--
ALTER TABLE `filmbilgi`
  ADD CONSTRAINT `filmbilgi_ibfk_2` FOREIGN KEY (`yapimci`) REFERENCES `yapimci` (`yapimciID`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `filmbilgi_ibfk_3` FOREIGN KEY (`yayinSirketi`) REFERENCES `yayinci` (`yayinciID`) ON UPDATE NO ACTION,
  ADD CONSTRAINT `filmbilgi_ibfk_4` FOREIGN KEY (`yonetmen`) REFERENCES `yonetmen` (`yonetmenID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Tablo kısıtlamaları `filmyorum`
--
ALTER TABLE `filmyorum`
  ADD CONSTRAINT `filmyorum_ibfk_1` FOREIGN KEY (`elestirmenID`) REFERENCES `elestirmen` (`elestirmenID`) ON DELETE NO ACTION ON UPDATE CASCADE,
  ADD CONSTRAINT `filmyorum_ibfk_2` FOREIGN KEY (`filmID`) REFERENCES `filmbilgi` (`filmID`) ON DELETE NO ACTION ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
