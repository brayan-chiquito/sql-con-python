-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 29-10-2022 a las 03:05:46
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sistemtravel`
--
CREATE DATABASE IF NOT EXISTS `sistemtravel` DEFAULT CHARACTER SET latin1 COLLATE latin1_spanish_ci;
USE `sistemtravel`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `CODIGO` int(10) NOT NULL,
  `NOMBRE` varchar(30) NOT NULL,
  `APELLIDO` varchar(30) NOT NULL,
  `DIRECCION` varchar(50) NOT NULL,
  `TELEFONO` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`CODIGO`, `NOMBRE`, `APELLIDO`, `DIRECCION`, `TELEFONO`) VALUES
(122, 'brayan', 'chiquito', 'vereda canceles', '3116508052'),
(124, 'alejando', 'chiquito', 'carrera 6 1e 96', '3173802170'),
(125, 'cristian', 'castro', 'barrio las brisas mz1 c2', '3005081831');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contrato_clien`
--

CREATE TABLE `contrato_clien` (
  `CONTRATO` int(11) NOT NULL,
  `CODCLIEN` int(11) NOT NULL,
  `CODSUCURSAL` int(11) NOT NULL,
  `CODVUELO` int(11) NOT NULL,
  `CLASE` varchar(30) NOT NULL,
  `CODHOTEL` int(11) NOT NULL,
  `REGIMEN` varchar(30) NOT NULL,
  `FECHALLEGADA` date NOT NULL,
  `FECHAPARTIDA` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `contrato_clien`
--

INSERT INTO `contrato_clien` (`CONTRATO`, `CODCLIEN`, `CODSUCURSAL`, `CODVUELO`, `CLASE`, `CODHOTEL`, `REGIMEN`, `FECHALLEGADA`, `FECHAPARTIDA`) VALUES
(1, 122, 1, 123455, 'primera', 1122, 'completa', '2022-10-25', '2022-10-26'),
(2, 124, 1, 123444, 'primera', 1122, 'media', '2022-10-26', '2022-10-27');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `hoteles`
--

CREATE TABLE `hoteles` (
  `CODIGOHOT` int(10) NOT NULL,
  `NOMBRE` varchar(30) NOT NULL,
  `DIRECCION` varchar(50) NOT NULL,
  `CIUDAD` varchar(30) NOT NULL,
  `TELEFONO` varchar(30) NOT NULL,
  `NUMPLAZADIS` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `hoteles`
--

INSERT INTO `hoteles` (`CODIGOHOT`, `NOMBRE`, `DIRECCION`, `CIUDAD`, `TELEFONO`, `NUMPLAZADIS`) VALUES
(1122, 'san luis', 'av 30 de agosto', 'pereira', '3317702', 150);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sucursal`
--

CREATE TABLE `sucursal` (
  `CODIGOSU` int(10) NOT NULL,
  `DIRECCION` varchar(30) NOT NULL,
  `TELEFONO` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `sucursal`
--

INSERT INTO `sucursal` (`CODIGOSU`, `DIRECCION`, `TELEFONO`) VALUES
(1, 'carrera 10-23', '3333335');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `usuario` varchar(30) COLLATE latin1_spanish_ci NOT NULL,
  `clave` varchar(50) COLLATE latin1_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`usuario`, `clave`) VALUES
('administrador', '&Ñ­T	ÅÉª`%8=\Z÷w'),
('usuario1', 'úýN2J¸ÍÑŽ•[O');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vuelos`
--

CREATE TABLE `vuelos` (
  `NUMVUE` int(15) NOT NULL,
  `FECHA` date NOT NULL,
  `HORA` time NOT NULL,
  `ORIGEN` varchar(30) NOT NULL,
  `DESTINO` varchar(30) NOT NULL,
  `PLAZASTOTALES` int(10) NOT NULL,
  `PLAZASTURIS` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `vuelos`
--

INSERT INTO `vuelos` (`NUMVUE`, `FECHA`, `HORA`, `ORIGEN`, `DESTINO`, `PLAZASTOTALES`, `PLAZASTURIS`) VALUES
(123444, '2022-10-29', '12:16:00', 'pereira', 'cartagena', 200, 60),
(123455, '2022-10-26', '05:36:00', 'pereira', 'medellin', 150, 20);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`CODIGO`) USING BTREE;

--
-- Indices de la tabla `contrato_clien`
--
ALTER TABLE `contrato_clien`
  ADD PRIMARY KEY (`CONTRATO`);

--
-- Indices de la tabla `hoteles`
--
ALTER TABLE `hoteles`
  ADD PRIMARY KEY (`CODIGOHOT`);

--
-- Indices de la tabla `sucursal`
--
ALTER TABLE `sucursal`
  ADD PRIMARY KEY (`CODIGOSU`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`usuario`);

--
-- Indices de la tabla `vuelos`
--
ALTER TABLE `vuelos`
  ADD PRIMARY KEY (`NUMVUE`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `contrato_clien`
--
ALTER TABLE `contrato_clien`
  MODIFY `CONTRATO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
