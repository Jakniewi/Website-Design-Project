-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: menu
-- ------------------------------------------------------
-- Server version	8.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alegen`
--

DROP TABLE IF EXISTS `alegen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alegen` (
  `Nazwa` varchar(255) NOT NULL,
  PRIMARY KEY (`Nazwa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alegen`
--

LOCK TABLES `alegen` WRITE;
/*!40000 ALTER TABLE `alegen` DISABLE KEYS */;
/*!40000 ALTER TABLE `alegen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alegen_danie`
--

DROP TABLE IF EXISTS `alegen_danie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alegen_danie` (
  `AlegenNazwa` varchar(255) NOT NULL,
  `DanieNazwa` varchar(255) NOT NULL,
  PRIMARY KEY (`AlegenNazwa`,`DanieNazwa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alegen_danie`
--

LOCK TABLES `alegen_danie` WRITE;
/*!40000 ALTER TABLE `alegen_danie` DISABLE KEYS */;
/*!40000 ALTER TABLE `alegen_danie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `danie`
--

DROP TABLE IF EXISTS `danie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `danie` (
  `Nazwa` varchar(255) NOT NULL,
  `Koszt` decimal(4,2) NOT NULL,
  `Wegańskie` bit(1) NOT NULL DEFAULT b'0',
  `Koszerne` bit(1) NOT NULL DEFAULT b'0',
  `Halal` bit(1) NOT NULL DEFAULT b'0',
  `Dostępne` bit(1) NOT NULL DEFAULT b'0',
  `Ofeta SezonowaNazwa` varchar(255) NOT NULL,
  `Rodzaj DaniaNazwa` varchar(255) NOT NULL,
  PRIMARY KEY (`Nazwa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `danie`
--

LOCK TABLES `danie` WRITE;
/*!40000 ALTER TABLE `danie` DISABLE KEYS */;
/*!40000 ALTER TABLE `danie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `danie_ocena`
--

DROP TABLE IF EXISTS `danie_ocena`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `danie_ocena` (
  `DanieNazwa` varchar(255) NOT NULL,
  `OcenaWartość` int NOT NULL,
  PRIMARY KEY (`DanieNazwa`,`OcenaWartość`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `danie_ocena`
--

LOCK TABLES `danie_ocena` WRITE;
/*!40000 ALTER TABLE `danie_ocena` DISABLE KEYS */;
/*!40000 ALTER TABLE `danie_ocena` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `danie_składnik`
--

DROP TABLE IF EXISTS `danie_składnik`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `danie_składnik` (
  `DanieNazwa` varchar(255) NOT NULL,
  `SkładnikNazwa` varchar(255) NOT NULL,
  PRIMARY KEY (`DanieNazwa`,`SkładnikNazwa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `danie_składnik`
--

LOCK TABLES `danie_składnik` WRITE;
/*!40000 ALTER TABLE `danie_składnik` DISABLE KEYS */;
/*!40000 ALTER TABLE `danie_składnik` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `konto`
--

DROP TABLE IF EXISTS `konto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `konto` (
  `Login` varchar(255) NOT NULL,
  `Hasło` varchar(255) NOT NULL,
  `Klient` bit(1) NOT NULL,
  `Osoba upoważniona` bit(1) NOT NULL,
  `Właściciel` bit(1) NOT NULL,
  `RestauracjaNazwa` varchar(255) NOT NULL,
  PRIMARY KEY (`Login`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `konto`
--

LOCK TABLES `konto` WRITE;
/*!40000 ALTER TABLE `konto` DISABLE KEYS */;
/*!40000 ALTER TABLE `konto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `konto_danie`
--

DROP TABLE IF EXISTS `konto_danie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `konto_danie` (
  `KontoLogin` varchar(255) NOT NULL,
  `DanieNazwa` varchar(255) NOT NULL,
  PRIMARY KEY (`KontoLogin`,`DanieNazwa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `konto_danie`
--

LOCK TABLES `konto_danie` WRITE;
/*!40000 ALTER TABLE `konto_danie` DISABLE KEYS */;
/*!40000 ALTER TABLE `konto_danie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `konto_ocena`
--

DROP TABLE IF EXISTS `konto_ocena`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `konto_ocena` (
  `KontoLogin` varchar(255) NOT NULL,
  `OcenaWartość` int NOT NULL,
  PRIMARY KEY (`KontoLogin`,`OcenaWartość`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `konto_ocena`
--

LOCK TABLES `konto_ocena` WRITE;
/*!40000 ALTER TABLE `konto_ocena` DISABLE KEYS */;
/*!40000 ALTER TABLE `konto_ocena` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ocena`
--

DROP TABLE IF EXISTS `ocena`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ocena` (
  `Wartość` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`Wartość`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ocena`
--

LOCK TABLES `ocena` WRITE;
/*!40000 ALTER TABLE `ocena` DISABLE KEYS */;
/*!40000 ALTER TABLE `ocena` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ofeta sezonowa`
--

DROP TABLE IF EXISTS `ofeta sezonowa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ofeta sezonowa` (
  `Nazwa` varchar(255) NOT NULL,
  `Początek` date NOT NULL,
  `Koniec` date NOT NULL,
  PRIMARY KEY (`Nazwa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ofeta sezonowa`
--

LOCK TABLES `ofeta sezonowa` WRITE;
/*!40000 ALTER TABLE `ofeta sezonowa` DISABLE KEYS */;
/*!40000 ALTER TABLE `ofeta sezonowa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restauracja`
--

DROP TABLE IF EXISTS `restauracja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restauracja` (
  `Nazwa` varchar(255) NOT NULL,
  `Adres` varchar(255) NOT NULL,
  `Numer kontaktowy` varchar(255) NOT NULL,
  `Godziny otwarcia` varchar(255) NOT NULL,
  `Dni otwarcia` varchar(255) NOT NULL,
  PRIMARY KEY (`Nazwa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restauracja`
--

LOCK TABLES `restauracja` WRITE;
/*!40000 ALTER TABLE `restauracja` DISABLE KEYS */;
/*!40000 ALTER TABLE `restauracja` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rodzaj dania`
--

DROP TABLE IF EXISTS `rodzaj dania`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rodzaj dania` (
  `Nazwa` varchar(255) NOT NULL,
  PRIMARY KEY (`Nazwa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rodzaj dania`
--

LOCK TABLES `rodzaj dania` WRITE;
/*!40000 ALTER TABLE `rodzaj dania` DISABLE KEYS */;
/*!40000 ALTER TABLE `rodzaj dania` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `składnik`
--

DROP TABLE IF EXISTS `składnik`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `składnik` (
  `Nazwa` varchar(255) NOT NULL,
  PRIMARY KEY (`Nazwa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `składnik`
--

LOCK TABLES `składnik` WRITE;
/*!40000 ALTER TABLE `składnik` DISABLE KEYS */;
/*!40000 ALTER TABLE `składnik` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-12  0:02:53
