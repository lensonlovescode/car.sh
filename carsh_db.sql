CREATE DATABASE  IF NOT EXISTS `carsh` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `carsh`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: carsh
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
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `name` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES ('Estate','0054d437-54a3-4327-aa12-37129e2b7ffe'),('Trailer','09f0fa43-9a73-4dd9-b48a-dd5edd2f85ed'),('Luxury','130d96fb-db1d-43bb-8da8-0106efefde89'),('4x4','16caba21-11b1-43fb-a709-9d42e3c88539'),('Convertible','2afd96e3-fe09-4ab9-84af-712be5f47921'),('Truck','3d2379d2-613c-48e0-9725-9672bd6cb974'),('Manual','49d572fe-4436-454e-afdf-b611f9f006ba'),('SUV','61f7b7c8-ae84-492a-9539-447aea0ab72d'),('Mini SUV','6670a2f6-7af5-4c88-ae2a-5b91a13da275'),('Tourer','71f2877e-9091-4e96-a69e-502071eef23f'),('Hatchback','7d651926-c178-4614-a0df-d5a6c472ddb4'),('Executive','862fc2c8-94df-4d71-8a63-ecf91c2fe9d0'),('Small','8b06f42b-f440-4d60-b964-205be22e1de2'),('Sports','9f17bfa8-aa44-41aa-b08f-3c6101302502'),('GT','a76e6c05-4801-47f8-b6a4-55f5ee53f46c'),('HyperCar','c4a691b2-f6f5-4474-a143-176d68dc428d'),('7-Seater','ddf7f394-c0df-4c63-85b6-f99f5bd8edd0'),('Automatic','e2b7c830-fc6f-4d1a-93a2-0531d3d36fea'),('Sedan','e9e81084-b7ee-47fa-80e5-0055142d2170'),('Coupe','ee6895c9-7a41-4ad7-840a-4436198d811a');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fuel_types`
--

DROP TABLE IF EXISTS `fuel_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fuel_types` (
  `name` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fuel_types`
--

LOCK TABLES `fuel_types` WRITE;
/*!40000 ALTER TABLE `fuel_types` DISABLE KEYS */;
INSERT INTO `fuel_types` VALUES ('Electric','1a5029c9-a78c-4f4b-89f1-82d909887884'),('Diesel','61954266-c515-4a93-95de-246a1fdcc1f9'),('Petrol','abd6727c-5148-4c7c-8252-40c404059633'),('Hybrid','dca5082a-155f-4c08-a596-2b64978ce9c3');
/*!40000 ALTER TABLE `fuel_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manufacturers`
--

DROP TABLE IF EXISTS `manufacturers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manufacturers` (
  `name` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manufacturers`
--

LOCK TABLES `manufacturers` WRITE;
/*!40000 ALTER TABLE `manufacturers` DISABLE KEYS */;
INSERT INTO `manufacturers` VALUES ('Hummer','010d5f31-6e72-4aa3-ad13-868da489c6df'),('Alpine','0228e5aa-4f2b-4aac-a849-8b458865cc5d'),('BMW','06cdf0c5-38bc-4141-a35e-c43468c64c33'),('McLaren','170a484c-4334-4fe0-bcdb-a5f6e9d9acd7'),('Daihatsu','191398bf-5c72-4ff4-99db-8633411c86cf'),('Volkswagen','207cae9e-04b6-467c-a67c-afbf0a36ca5e'),('Dodge','236038c0-fdd2-439c-922e-ff8d444372dd'),('Jaguar','2555c3bf-a907-4b86-922d-879c153dd066'),('Bugatti','263da4b3-915a-4f83-9842-4f13aab93cfe'),('Lamborghini','295f9df9-ad37-4281-91ed-23fc5337fc65'),('Subaru','2c5383e2-cc12-495f-b628-3cc69fe29705'),('Mazda','2ecabc0c-f13a-4f12-b2de-14574c621ff8'),('Volvo','318d11d5-5edd-48f3-bec8-6549a519bdc7'),('Maybach','34ad8cea-789a-474a-a130-2ed416c6f9ae'),('Chrysler','38a6401d-dc1f-4dd2-a2ae-8d936258b10f'),('Rolls-Royce','417ef885-bf81-4fa8-9476-001acb8f9fe2'),('Fiat','4648fe8b-1ea6-4ed2-815b-6939a0a8ac26'),('Toyota','4658e5d3-23de-415a-bd4d-322055f4356b'),('BYD','49632c36-bc09-4623-88e1-878b80116959'),('Mitsubishi','600d2e33-e7f6-4fe1-a02a-bd27dd89df0c'),('Tesla','6b06e9e4-6b96-4c64-8d7d-427d3edac5dc'),('Peugeot','6e6ea26c-9d93-4aa5-b165-15ba4893bc8c'),('Honda','6f382e6f-f61a-4dab-9744-8b999977d474'),('Ford','78cebced-ea7b-40a8-97c8-146167781c8d'),('Mahindra','8025b290-e969-43fe-898b-ce017b78eb1b'),('Audi','81552096-6bb9-4340-96cd-c1f58ecd334e'),('Lexus','824d8774-2135-4dff-9428-5e9869df3d80'),('Buick','833f33ca-f838-43e0-82b3-5b083077a833'),('Datsun','851f3eae-161c-4774-ac36-def273695aa6'),('Mercedes-Benz','8c0d273e-0af0-447f-8ea9-55d5f172d470'),('Isuzu','8e724d9b-436d-4388-8a0c-53b44ea9deac'),('Alfa Romeo','92340e42-e581-4c14-a036-6a8e6cc6ea67'),('Bentley','982ef209-f1fb-4f5b-b309-b4f701756df3'),('Dacia','99f9452d-3882-4628-a575-cc916ec19a11'),('Kia','a0c4b90d-6429-45b7-be70-50fcff9436b5'),('Land Rover','ab2b7b65-ca73-4446-8a14-1f80a5dc1b2c'),('Fisker','abff192f-2384-4b1a-b469-9f02929ed799'),('Volvo','b1adf4c9-62d3-4f92-ab1d-9405903f8d4e'),('Abarth','b2ca342f-9267-438f-bf7b-861bf87f4c64'),('Renault','bc6c2a42-3900-43b9-a979-8687fe2f2f99'),('Cardillac','c2500499-5071-4fba-87e3-0eb484a2a69a'),('','c6ec4180-2e37-4528-920e-15d8e7b2efeb'),('Porsche','c81ab052-d667-4cff-ba3e-be2d426410e9'),('Citroen','cb414c4e-9b60-4557-b6b9-0e0b8aeaeae6'),('Hyundai','cccda686-b390-4ec7-8336-c7139aa86bf6'),('Mercedes-AMG','cf363e1d-9486-44ff-a74c-0b9c50351c4c'),('Cupra','d023c111-1320-4cf1-8514-548665b72e49'),('Rover','d48a9700-6fd3-4b33-b8ad-814a8d464f32'),('Chevrolet','da4c8c93-8bf9-43f3-85ae-5497b8001af5'),('Aston Martin','dea30080-e827-454c-9b44-23fbd9f796ea'),('Suzuki','e8448c00-d9f9-46c1-8fbd-311cb96d93a1'),('Jeep','ec0507d9-b96f-4381-92ac-0c8478ea1955'),('Nissan','f5999f1e-f01e-46b5-903c-5827827353c5'),('DS','f6902c94-5e6e-4605-b648-093958c7a05f');
/*!40000 ALTER TABLE `manufacturers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `models`
--

DROP TABLE IF EXISTS `models`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `models` (
  `name` varchar(60) NOT NULL,
  `base_price` int NOT NULL,
  `ignition` varchar(60) NOT NULL,
  `engine_capacity` int DEFAULT NULL,
  `category_id` varchar(60) NOT NULL,
  `fuel_type_id` varchar(60) NOT NULL,
  `manufacturer_id` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  KEY `fuel_type_id` (`fuel_type_id`),
  KEY `manufacturer_id` (`manufacturer_id`),
  CONSTRAINT `models_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `models_ibfk_2` FOREIGN KEY (`fuel_type_id`) REFERENCES `fuel_types` (`id`),
  CONSTRAINT `models_ibfk_3` FOREIGN KEY (`manufacturer_id`) REFERENCES `manufacturers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `models`
--

LOCK TABLES `models` WRITE;
/*!40000 ALTER TABLE `models` DISABLE KEYS */;
INSERT INTO `models` VALUES ('BMW Z3',1200000,'coil-on-plug',1795,'130d96fb-db1d-43bb-8da8-0106efefde89','abd6727c-5148-4c7c-8252-40c404059633','06cdf0c5-38bc-4141-a35e-c43468c64c33','0afc012f-f95b-454f-bbc0-9fa4ac1d7c03'),('BMW XM',30000000,'coil-on-plug',4395,'61f7b7c8-ae84-492a-9539-447aea0ab72d','dca5082a-155f-4c08-a596-2b64978ce9c3','06cdf0c5-38bc-4141-a35e-c43468c64c33','11f8f7d9-9f8a-4950-91f2-a6dbf0b2e37a'),('Aston Martin Rapide',29000000,'coil-on-plug',5935,'130d96fb-db1d-43bb-8da8-0106efefde89','abd6727c-5148-4c7c-8252-40c404059633','dea30080-e827-454c-9b44-23fbd9f796ea','13f62e68-b5fd-40b1-9fcd-b95c624685ef'),('Aston Martin DBX',29080628,'coil-on-plug',3982,'130d96fb-db1d-43bb-8da8-0106efefde89','abd6727c-5148-4c7c-8252-40c404059633','dea30080-e827-454c-9b44-23fbd9f796ea','175938bd-93e5-4df3-b984-3d8005f462c8'),('Aston Martin Vanquish',56000000,'coil-on-plug',5204,'130d96fb-db1d-43bb-8da8-0106efefde89','abd6727c-5148-4c7c-8252-40c404059633','dea30080-e827-454c-9b44-23fbd9f796ea','1795a4c6-b6c1-4322-9fac-fdf559123c36'),('Bentley Bentayga',28358425,'coil-on-plug',3996,'61f7b7c8-ae84-492a-9539-447aea0ab72d','abd6727c-5148-4c7c-8252-40c404059633','982ef209-f1fb-4f5b-b309-b4f701756df3','24cebc76-95f2-41e8-aaf9-194376e8681d'),('Aston Martin Vantage',27000000,'coil-on-plug',3982,'130d96fb-db1d-43bb-8da8-0106efefde89','abd6727c-5148-4c7c-8252-40c404059633','dea30080-e827-454c-9b44-23fbd9f796ea','26907120-e29b-4775-bd4f-41ae1f67bff2'),('BMW Z4',8134655,'coil-on-plug',1998,'130d96fb-db1d-43bb-8da8-0106efefde89','dca5082a-155f-4c08-a596-2b64978ce9c3','06cdf0c5-38bc-4141-a35e-c43468c64c33','2cd89895-a555-4b8b-a072-38490ad746b7'),('Bentley Mulsanne',31080000,'coil-on-plug',6752,'e9e81084-b7ee-47fa-80e5-0055142d2170','abd6727c-5148-4c7c-8252-40c404059633','982ef209-f1fb-4f5b-b309-b4f701756df3','2fc1f288-a1da-433d-b452-35409df66699'),('BMW 2-Series',6000000,'coil-on-plug',1998,'ee6895c9-7a41-4ad7-840a-4436198d811a','abd6727c-5148-4c7c-8252-40c404059633','06cdf0c5-38bc-4141-a35e-c43468c64c33','37384584-41b8-4776-9bd2-72b767955ea2'),('BYD Seal',7500000,'electric motor',0,'e9e81084-b7ee-47fa-80e5-0055142d2170','1a5029c9-a78c-4f4b-89f1-82d909887884','49632c36-bc09-4623-88e1-878b80116959','3745bfe0-f6be-498f-a577-cd59f40f73a3'),('Cadillac SRX',4500000,'coil-on-plug',3000,'61f7b7c8-ae84-492a-9539-447aea0ab72d','abd6727c-5148-4c7c-8252-40c404059633','c2500499-5071-4fba-87e3-0eb484a2a69a','398a011e-c458-4137-90a4-b1080be05d46'),('Audi A5',4500000,'coil-on-plug',1984,'862fc2c8-94df-4d71-8a63-ecf91c2fe9d0','abd6727c-5148-4c7c-8252-40c404059633','81552096-6bb9-4340-96cd-c1f58ecd334e','3f776a34-f89d-4931-ae6c-56f10437d80a'),('Abarth 500',2950000,'coil-on-plug',1368,'7d651926-c178-4614-a0df-d5a6c472ddb4','abd6727c-5148-4c7c-8252-40c404059633','b2ca342f-9267-438f-bf7b-861bf87f4c64','40a177f1-31d6-4add-8dad-28c1f3761ba9'),('Cadillac XLR',4000000,'coil-on-plug',4565,'130d96fb-db1d-43bb-8da8-0106efefde89','abd6727c-5148-4c7c-8252-40c404059633','c2500499-5071-4fba-87e3-0eb484a2a69a','45e0cc11-8396-4dff-be75-d21e4aabb70f'),('Audi A4',1990000,'coil-on-type',1984,'130d96fb-db1d-43bb-8da8-0106efefde89','abd6727c-5148-4c7c-8252-40c404059633','81552096-6bb9-4340-96cd-c1f58ecd334e','4b813792-c5af-4489-b122-f1b09c09374e'),('Bentley Flying Spur',33000000,'coil-on-plug',3996,'130d96fb-db1d-43bb-8da8-0106efefde89','abd6727c-5148-4c7c-8252-40c404059633','982ef209-f1fb-4f5b-b309-b4f701756df3','4dfc8fb0-0b8b-4a58-b38c-d05f7a32216e'),('Cardillac CTS',4208478,'coil-on-plug',1998,'e9e81084-b7ee-47fa-80e5-0055142d2170','abd6727c-5148-4c7c-8252-40c404059633','c2500499-5071-4fba-87e3-0eb484a2a69a','5f81cd15-31fd-4351-9127-36029d4c4ef2'),('Abarth 124 Spider',5500000,'coil-on-plug',1368,'9f17bfa8-aa44-41aa-b08f-3c6101302502','abd6727c-5148-4c7c-8252-40c404059633','b2ca342f-9267-438f-bf7b-861bf87f4c64','61e82a12-8976-4df7-9d9e-b7da4e94a9c4'),('Abarth Grande Punto',2500000,'coil-on-plug',1368,'7d651926-c178-4614-a0df-d5a6c472ddb4','abd6727c-5148-4c7c-8252-40c404059633','b2ca342f-9267-438f-bf7b-861bf87f4c64','6370a398-bbe6-466a-9448-35a58433cf9a'),('Alfa Romeo Brera',3500000,'coil-on-plug',1742,'ee6895c9-7a41-4ad7-840a-4436198d811a','abd6727c-5148-4c7c-8252-40c404059633','92340e42-e581-4c14-a036-6a8e6cc6ea67','650c9590-71a4-48f9-abf9-a9a5c102db1e'),('Alfa Romeo 156',1800000,'coil-on-plug',1598,'e9e81084-b7ee-47fa-80e5-0055142d2170','abd6727c-5148-4c7c-8252-40c404059633','92340e42-e581-4c14-a036-6a8e6cc6ea67','68192993-6546-48f1-9470-34d06ca5f627'),('BYD Dolphin',7500000,'electric motor',0,'7d651926-c178-4614-a0df-d5a6c472ddb4','1a5029c9-a78c-4f4b-89f1-82d909887884','49632c36-bc09-4623-88e1-878b80116959','6a5d9888-553a-4187-b888-09986b8d6ac8'),('Audi A2',1000000,'coil-on-plug',1390,'7d651926-c178-4614-a0df-d5a6c472ddb4','abd6727c-5148-4c7c-8252-40c404059633','81552096-6bb9-4340-96cd-c1f58ecd334e','7067b99b-3973-4c78-b05b-716a6b0c86da'),('Audi A6',3320000,'coil-on-plug',1984,'862fc2c8-94df-4d71-8a63-ecf91c2fe9d0','abd6727c-5148-4c7c-8252-40c404059633','81552096-6bb9-4340-96cd-c1f58ecd334e','7305f8c0-64a4-4dc4-9b5f-b07869f8d2bf'),('Alfa Romeo Giulietta',3000000,'coil-on-plug',1368,'7d651926-c178-4614-a0df-d5a6c472ddb4','abd6727c-5148-4c7c-8252-40c404059633','92340e42-e581-4c14-a036-6a8e6cc6ea67','75198380-05b0-4263-b9a3-7a725ea93a90'),('BYD Seal U',6610500,'electric motor',0,'61f7b7c8-ae84-492a-9539-447aea0ab72d','1a5029c9-a78c-4f4b-89f1-82d909887884','49632c36-bc09-4623-88e1-878b80116959','7613e7bc-4687-4e2d-80fa-dd00bd3ba0b6'),('Bugatti Chiron',400000000,'coil-on-plug',7993,'c4a691b2-f6f5-4474-a143-176d68dc428d','abd6727c-5148-4c7c-8252-40c404059633','263da4b3-915a-4f83-9842-4f13aab93cfe','775cd773-54a8-4781-acd6-7186f67e151c'),('Aston Martin DB11',20000000,'coil-on-plug',3982,'9f17bfa8-aa44-41aa-b08f-3c6101302502','abd6727c-5148-4c7c-8252-40c404059633','dea30080-e827-454c-9b44-23fbd9f796ea','7c171b7d-9b79-4bdd-aade-8c6abedb1eee'),('Audi A1',1280000,'coil-on-plug',999,'7d651926-c178-4614-a0df-d5a6c472ddb4','abd6727c-5148-4c7c-8252-40c404059633','81552096-6bb9-4340-96cd-c1f58ecd334e','7e2e2e9b-0782-42da-b509-fd4a795f093d'),('Audi A3',4000000,'coil-on-plug',1984,'e9e81084-b7ee-47fa-80e5-0055142d2170','abd6727c-5148-4c7c-8252-40c404059633','81552096-6bb9-4340-96cd-c1f58ecd334e','8137e8c9-f262-4c67-a9f0-cb5102e85f65'),('Aston Martin DBS',30000000,'coil-on-plug',5204,'71f2877e-9091-4e96-a69e-502071eef23f','abd6727c-5148-4c7c-8252-40c404059633','dea30080-e827-454c-9b44-23fbd9f796ea','87a6ae02-983f-49b5-b45b-c6689f7fa803'),('Audi A7',4450000,'coil-on-plug',2995,'130d96fb-db1d-43bb-8da8-0106efefde89','abd6727c-5148-4c7c-8252-40c404059633','81552096-6bb9-4340-96cd-c1f58ecd334e','88b846eb-96d1-4dc3-b50a-ef42010fd513'),('Bentley Continental Flying Spur',20000000,'coil-on-plug',5998,'e9e81084-b7ee-47fa-80e5-0055142d2170','abd6727c-5148-4c7c-8252-40c404059633','982ef209-f1fb-4f5b-b309-b4f701756df3','8e900380-7dd2-4216-bdbd-89a2472612f4'),('Alfa Romeo Giulia',6500000,'coil-on-plug',1995,'9f17bfa8-aa44-41aa-b08f-3c6101302502','abd6727c-5148-4c7c-8252-40c404059633','92340e42-e581-4c14-a036-6a8e6cc6ea67','92f395bf-434f-4ce1-a718-f99e4cd32996'),('Alfa Romeo GT',2500000,'coil-on-plug',1747,'ee6895c9-7a41-4ad7-840a-4436198d811a','abd6727c-5148-4c7c-8252-40c404059633','92340e42-e581-4c14-a036-6a8e6cc6ea67','93dae1f6-99ee-4df2-b59e-b2e8a2980d03'),('Alfa Romeo Junior',4500000,'Mild Hybrid Electric Vehicle System',0,'61f7b7c8-ae84-492a-9539-447aea0ab72d','1a5029c9-a78c-4f4b-89f1-82d909887884','92340e42-e581-4c14-a036-6a8e6cc6ea67','95e713a0-3bfa-444d-a515-aa5fe9ab7025'),('Abarth 600e',4500000,'electric motor',0,'6670a2f6-7af5-4c88-ae2a-5b91a13da275','1a5029c9-a78c-4f4b-89f1-82d909887884','b2ca342f-9267-438f-bf7b-861bf87f4c64','9872e067-fbf3-4e1e-af77-5238cb0b05d3'),('BMW 1-Series',4500000,'coil-on-plug',1499,'7d651926-c178-4614-a0df-d5a6c472ddb4','abd6727c-5148-4c7c-8252-40c404059633','06cdf0c5-38bc-4141-a35e-c43468c64c33','98b3641f-f4e8-4003-8e5a-c14788959e6c'),('BMW 330e',5500000,'coil-on-plug',1998,'e9e81084-b7ee-47fa-80e5-0055142d2170','dca5082a-155f-4c08-a596-2b64978ce9c3','06cdf0c5-38bc-4141-a35e-c43468c64c33','9b7deaa1-9591-4b82-8119-2eb5ed9f2fe2'),('Bugatti Veyron',250000000,'coil-on-plug',7993,'c4a691b2-f6f5-4474-a143-176d68dc428d','abd6727c-5148-4c7c-8252-40c404059633','263da4b3-915a-4f83-9842-4f13aab93cfe','a85b56c8-3274-4c55-9a9c-a1066fe0de5f'),('Alfa Romeo Stelvio',7000000,'coil-on-plug',1995,'130d96fb-db1d-43bb-8da8-0106efefde89','abd6727c-5148-4c7c-8252-40c404059633','92340e42-e581-4c14-a036-6a8e6cc6ea67','ab49455d-c400-45ea-a3d9-4ec36d30ed68'),('Alpine A290',5000000,'electric motor',0,'130d96fb-db1d-43bb-8da8-0106efefde89','abd6727c-5148-4c7c-8252-40c404059633','0228e5aa-4f2b-4aac-a849-8b458865cc5d','b640eb72-a4be-4356-93e9-6ef4c0aca478'),('Audi A8',6000000,'coil-on-plug',2995,'130d96fb-db1d-43bb-8da8-0106efefde89','abd6727c-5148-4c7c-8252-40c404059633','81552096-6bb9-4340-96cd-c1f58ecd334e','c08b8021-fe3a-4669-b382-14e6cd8a3c80'),('BYD Atto 3',12000000,'electric motor',0,'61f7b7c8-ae84-492a-9539-447aea0ab72d','1a5029c9-a78c-4f4b-89f1-82d909887884','49632c36-bc09-4623-88e1-878b80116959','c7ac9d79-a57a-4adb-85d7-09d2d1eae8e5'),('Alfa Romeo Tonale',6500000,'coil-on-plug',1469,'130d96fb-db1d-43bb-8da8-0106efefde89','dca5082a-155f-4c08-a596-2b64978ce9c3','92340e42-e581-4c14-a036-6a8e6cc6ea67','d22334b9-ea38-4ddd-86ff-b0666568e242'),('Alfa Romeo 147',1500000,'coil-on-plug',1598,'7d651926-c178-4614-a0df-d5a6c472ddb4','abd6727c-5148-4c7c-8252-40c404059633','92340e42-e581-4c14-a036-6a8e6cc6ea67','d960a4d5-7571-431b-89e4-91f74dffaf52'),('Bentley Continental GT',33525000,'coil-on-plug',3996,'ee6895c9-7a41-4ad7-840a-4436198d811a','abd6727c-5148-4c7c-8252-40c404059633','982ef209-f1fb-4f5b-b309-b4f701756df3','e0704b58-5936-4687-831b-b6ca7ceb8543'),('Aston Martin DB12',35000000,'coil-on-plug',3982,'9f17bfa8-aa44-41aa-b08f-3c6101302502','abd6727c-5148-4c7c-8252-40c404059633','dea30080-e827-454c-9b44-23fbd9f796ea','e7891d77-704a-4223-a544-39a1d360924b'),('Abarth Punto Evo',2800000,'coil-on-plug',1368,'7d651926-c178-4614-a0df-d5a6c472ddb4','abd6727c-5148-4c7c-8252-40c404059633','b2ca342f-9267-438f-bf7b-861bf87f4c64','ef50094c-f0e0-4d98-8c59-49a2a176d004'),('Bentley Arnage',20000000,'coil-on-plug',6750,'130d96fb-db1d-43bb-8da8-0106efefde89','abd6727c-5148-4c7c-8252-40c404059633','982ef209-f1fb-4f5b-b309-b4f701756df3','f1ccf1c4-6c14-4b35-bd7d-cf6b0f0569c3'),('Alpine A110',8000000,'coil-on-plug',1798,'9f17bfa8-aa44-41aa-b08f-3c6101302502','abd6727c-5148-4c7c-8252-40c404059633','0228e5aa-4f2b-4aac-a849-8b458865cc5d','f4b2b027-d0db-4185-8cec-386ad1e76d8c'),('Alfa Romeo 4C',10000000,'coil-on-plug',1742,'9f17bfa8-aa44-41aa-b08f-3c6101302502','abd6727c-5148-4c7c-8252-40c404059633','92340e42-e581-4c14-a036-6a8e6cc6ea67','f86e6f16-0671-49f2-9181-ede36001dac3');
/*!40000 ALTER TABLE `models` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-20  9:09:11
