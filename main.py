import wx
import perpus
import sqlite3

class DataManager:
    def __init__(self):
        self.conn = sqlite3.connect('perpustakaan.db')
        self.cursor = self.conn.cursor()

    def Jalankan(self, query, returnData = False):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.conn.commit()
        if returnData :
            return result

class Main(DataManager, perpus.MyFrame1):
    def __init__(self, parent):
        perpus.MyFrame1.__init__(self, parent)
        self.DM = DataManager()

    def button_login( self, event ):
        username = self.m_textCtrl1.GetValue()
        password = self.m_textCtrl2.GetValue()
        self.query = "SELECT * FROM user where username = '{}' and password = '{}'".format(username, password)
        hasil = self.DM.Jalankan(self.query, returnData = True)

        if hasil is not None and len(hasil) > 0 :
            event = Main3(None)
            event.Show()
            self.Destroy()
            self.DM.conn.close()
            return username
        else:
            wx.MessageBox('Username atau Password yang anda masukkan salah', 'Terjadi Kesalahan')


    def klik_daftar( self, event ):
        event = Main2(None)
        event.Show()
        self.Destroy()

class Main2(Main, perpus.MyFrame2):
    def __init__(self, parent):
        perpus.MyFrame2.__init__(self, parent)
        self.DM = DataManager()
        
    def button_daftar( self, event):
        username = self.m_textCtrl3.GetValue()
        umur = self.m_textCtrl4.GetValue()
        alamat = self.m_textCtrl5.GetValue()
        email = self.m_textCtrl6.GetValue()
        password = self.m_textCtrl7.GetValue()

        if username != "" and umur != "" and alamat != "" and email != "" and password != "":
            self.query = 'INSERT INTO user (username, umur, alamat, email, password) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')'
            self.query= self.query % (username, umur, alamat, email, password)
            self.DM.Jalankan(self.query)
            event = Main(None)
            event.Show()
            self.Destroy()
            self.DM.conn.close()
        else:
            wx.MessageBox('Data tidak boleh kosong', 'Terjadi Kesalahan')

    def klik_login( self, event ):
        event = Main(None)
        event.Show()
        self.Destroy()

class Main3(Main2, perpus.MyFrame3):
    def __init__(self, parent):
        perpus.MyFrame3.__init__(self, parent)
        self.m_grid4.SetColLabelValue(0, "Kode Buku")
        self.m_grid4.SetColLabelValue(1, "Judul")
        self.m_grid4.SetColLabelValue(2, "Pengarang")
        self.m_grid4.SetColLabelValue(3, "Penerbit")
        self.m_grid4.SetColLabelValue(4, "Tempat Terbit")
        self.m_grid4.SetColLabelValue(5, "Tahun Terbit")
        self.m_grid4.SetColLabelValue(6, "Jumlah Halaman")
        self.m_grid4.SetColLabelValue(7, "Jumlah Buku")
        self.m_grid4.SetColLabelValue(8, "Kategori")
        self.m_grid4.SetColLabelValue(9, "Nomor Rak")
        self.m_grid4.SetColLabelValue(10, "Edit")
        self.DM = DataManager()
        self.m = Main(self)
        self.tampil()
        
    def tampil(self):    
        self.query = 'SELECT * FROM buku'
        hasil = self.DM.Jalankan(self.query, returnData=True)
        for a in hasil:
            self.m_grid4.AppendRows(1)
        for b in range (10):
            a = 0
            for row in hasil:
                self.m_grid4.SetCellValue(a, b, str(row[b]))
                a = a + 1

    def m_grid4OnGridCmdSelectCell( self, event ):
        row = event.GetRow()
        self.showTex(row)

    def showTex(self, row):
        kode = self.m_grid4.GetCellValue(row, 0)
        judul = self.m_grid4.GetCellValue(row, 1)
        pengarang = self.m_grid4.GetCellValue(row, 2)
        penerbit = self.m_grid4.GetCellValue(row, 3)
        tmpt_terbit = self.m_grid4.GetCellValue(row, 4)
        thn_terbit = self.m_grid4.GetCellValue(row, 5)
        jml_buku = self.m_grid4.GetCellValue(row, 6)
        jml_Kolom = self.m_grid4.GetCellValue(row, 7)
        kategori = self.m_grid4.GetCellValue(row, 8)
        noRak = self.m_grid4.GetCellValue(row, 9)

        self.m_textCtrl18.SetValue(kode)
        self.m_textCtrl19.SetValue(judul)
        self.m_textCtrl20.SetValue(pengarang)
        self.m_textCtrl21.SetValue(penerbit)
        self.m_textCtrl22.SetValue(tmpt_terbit)
        self.m_textCtrl23.SetValue(thn_terbit)
        self.m_textCtrl24.SetValue(jml_buku)
        self.m_textCtrl25.SetValue(jml_Kolom)
        self.m_textCtrl26.SetValue(kategori)
        self.m_textCtrl27.SetValue(noRak)

    def btn_simpanEdit(self, event):
        kode = self.m_textCtrl18.GetValue()
        judul = self.m_textCtrl19.GetValue()
        pengarang = self.m_textCtrl20.GetValue()
        penerbit = self.m_textCtrl21.GetValue()
        tmpt_terbit = self.m_textCtrl22.GetValue()
        thn_terbit = self.m_textCtrl23.GetValue()
        jml_buku = self.m_textCtrl24.GetValue()
        jml_Kolom = self.m_textCtrl25.GetValue()
        kategori = self.m_textCtrl26.GetValue()
        noRak = self.m_textCtrl27.GetValue()

        self.query = "update buku set judul = \'%s\', pengarang = \'%s\', penerbit = \'%s\', tempatTerbit = \'%s\', tahunTerbit = \'%s\', jumlahHalaman = \'%s\', jumlahBuku = \'%s\', kategori = \'%s\', nomorRak = \'%s\' WHERE kodeBuku = \'%s\'"
        self.query = self.query % (judul, pengarang, penerbit, tmpt_terbit, thn_terbit, jml_buku, jml_Kolom, kategori, noRak, kode)
        self.DM.Jalankan(self.query)
        if kode != "":
            self.refresh(event)

    def refresh( self, event ):
        event = Main3(None)
        event.Show()
        self.Destroy()

    def btn_deleteBuku( self, event ):
        kodeBuku = self.m_textCtrl18.GetValue()
        self.query = "DELETE From buku WHERE kodeBuku = \'%s\'"
        self.query = self.query % (kodeBuku)
        self.DM.Jalankan(self.query)
        if kodeBuku != "":
            self.refresh(event)

    def button_tambah( self, event ):
        event = Main4(None)
        event.Show()
        
    def button_keluar( self, event ):
        self.DM.conn.close()
        event = Main(None)
        event.Show()
        self.Destroy()

class Main4(Main3, perpus.MyFrame4):
    def __init__(self, parent):
        perpus.MyFrame4.__init__(self, parent)
        self.DM = DataManager()

    def button_batal( self, event ):
        self.Destroy()
        
    def button_simpan( self, event ):
        kode = self.m_textCtrl8.GetValue()
        judul = self.m_textCtrl9.GetValue()
        pengarang = self.m_textCtrl10.GetValue()
        penerbit = self.m_textCtrl11.GetValue()
        tmpt_terbit = self.m_textCtrl12.GetValue()
        thn_terbit = self.m_textCtrl13.GetValue()
        jml_halaman = self.m_textCtrl14.GetValue()
        jml_buku = self.m_textCtrl15.GetValue()
        kategori = self.m_textCtrl16.GetValue()
        no_rak = self.m_textCtrl17.GetValue()

        if kode != "" and judul != "" and pengarang != "" and penerbit != "" and tmpt_terbit != "" and thn_terbit != "" and jml_halaman != "" and jml_buku != "" and kategori != "" and no_rak != "":
            self.query = 'INSERT INTO buku (kodeBuku, judul, pengarang, penerbit, tempatTerbit, tahunTerbit, jumlahHalaman, jumlahBuku, kategori, nomorRak) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')'
            self.query = self.query % (kode, judul, pengarang, penerbit, tmpt_terbit, thn_terbit, jml_halaman, jml_buku, kategori, no_rak)
            self.DM.Jalankan(self.query)
            self.Destroy()
            self.DM.conn.close()
        else :
            wx.MessageBox('Data tidak boleh kosong', 'Terjadi Kesalahan')

run = wx.App()
frame = Main(parent=None)
frame.Show()
run.MainLoop()