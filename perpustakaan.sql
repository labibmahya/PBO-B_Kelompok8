-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 31 Bulan Mei 2021 pada 07.17
-- Versi server: 10.4.14-MariaDB
-- Versi PHP: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `perpustakaan`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `buku`
--

CREATE TABLE `buku` (
  `kodeBuku` int(10) NOT NULL,
  `judul` varchar(30) NOT NULL,
  `pengarang` varchar(20) NOT NULL,
  `penerbit` varchar(20) NOT NULL,
  `tempatTerbit` varchar(20) NOT NULL,
  `tahunTerbit` varchar(5) NOT NULL,
  `jumlahHalaman` varchar(5) NOT NULL,
  `jumlahBuku` varchar(5) NOT NULL,
  `kategori` varchar(20) NOT NULL,
  `nomorRak` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `buku`
--

INSERT INTO `buku` (`kodeBuku`, `judul`, `pengarang`, `penerbit`, `tempatTerbit`, `tahunTerbit`, `jumlahHalaman`, `jumlahBuku`, `kategori`, `nomorRak`) VALUES
(1, 'Laskar Pelangi', 'Andrea Hirata', 'Bentang Pustaka', 'Yogyakarta', '2005', '529', '5', 'Roman', '100E'),
(12, 'Habis Gelap Terbitlah Terang', 'Kartini', 'Balai Pustaka', 'Indonesia', '2005', '204', '10', 'Biografi', '100E'),
(112, 'Lelaku Harimau', 'Eka Kurniawan', 'PT Gramedia Pustaka ', 'Jakarta', '2016', '190', '10', 'Fiksi', '12A');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `id` int(5) NOT NULL,
  `username` varchar(20) NOT NULL,
  `umur` varchar(5) NOT NULL,
  `alamat` varchar(20) NOT NULL,
  `email` varchar(25) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`id`, `username`, `umur`, `alamat`, `email`, `password`) VALUES
(1, 'labibmahya', '20', 'Banyuwangi', 'labibmahya99@gmail.com', '2020'),
(10, 'rifqi', '21', 'Mojoroto', 'rifqi', 'ahr123');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `buku`
--
ALTER TABLE `buku`
  ADD UNIQUE KEY `kodeBuku` (`kodeBuku`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `user`
--
ALTER TABLE `user`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
