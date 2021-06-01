import wx
import perpus
import sqlite3

conn = sqlite3.connect('perpustakaan.db')
cursor = conn.cursor()

class Main(perpus.MyFrame1):
    def __init__(self, parent):
        perpus.MyFrame1.__init__(self, parent)
    
    def button_login( self, event ):
        username = self.m_textCtrl1.GetValue()
        password = self.m_textCtrl2.GetValue()

        self.query = 'SELECT * FROM user'
        cursor.execute(self.query)
        hasil = cursor.fetchall()

        for row in hasil:
            if username == row[1] and password == row[5]:
                event = Main3(None)
                event.Show()
                self.Destroy()
                # conn.close()
            else:
                wx.MessageBox('Username atau Password yang anda masukkan salah', 'Terjadi Kesalahan')

    def klik_daftar( self, event ):
        event = Main2(None)
        event.Show()
        self.Destroy()

class Main2(perpus.MyFrame2):
    def __init__(self, parent):
        perpus.MyFrame2.__init__(self, parent)
        
    def button_daftar( self, event):
        username = self.m_textCtrl3.GetValue()
        umur = self.m_textCtrl4.GetValue()
        alamat = self.m_textCtrl5.GetValue()
        email = self.m_textCtrl6.GetValue()
        password = self.m_textCtrl7.GetValue()

        if username != "" and umur != "" and alamat != "" and email != "" and password != "":
            self.query = 'INSERT INTO user (username, umur, alamat, email, password) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')'
            self.value = self.query % (username, umur, alamat, email, password)
            cursor.execute(self.query, self.value)
            conn.commit()
            event = Main(None)
            event.Show()
            self.Destroy()
            conn.close()
        else:
            wx.MessageBox('Data tidak boleh kosong', 'Terjadi Kesalahan')

    def klik_login( self, event ):
        event = Main(None)
        event.Show()
        self.Destroy()

class Main3(perpus.MyFrame1, perpus.MyFrame3):
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

        self.query = 'SELECT * FROM buku'
        cursor.execute(self.query)
        hasil = cursor.fetchall()
        for a in hasil:
            self.m_grid4.AppendRows(1)
        for b in range (9):
            a = 0
            for row in hasil:
                self.m_grid4.SetCellValue(a, b, str(row[b]))
                a = a + 1
                # conn.close()

        jmlKolom = self.m_grid4.GetNumberCols()
        self.m_grid4.AppendCols(2)
        colEdit = jmlKolom
        colDel = jmlKolom + 1

        self.m_grid4.SetColLabelValue(colEdit, '')
        self.m_grid4.SetColLabelValue(colDel, '')

        for row in range (self.m_grid4.GetNumberRows()):
            self.m_grid4.SetCellValue(row, colEdit, 'Edit')
            self.m_grid4.SetCellBackgroundColour(row, colEdit, wx.BLUE)
            self.m_grid4.SetCellTextColour(row, colEdit, wx.WHITE)

            self.m_grid4.SetCellValue(row, colDel, 'Delete')
            self.m_grid4.SetCellBackgroundColour(row, colDel, wx.RED)
            self.m_grid4.SetCellTextColour(row, colDel, wx.WHITE)

        self.m_grid4.Fit()

    def button_tambah( self, event ):
        event = Main4(None)
        event.Show()
        
    def button_keluar( self, event ):
        event = Main(None)
        event.Show()
        self.Destroy()

class Main4(perpus.MyFrame4):
    def __init__(self, parent):
        perpus.MyFrame4.__init__(self, parent)

    def button_batal( self, event ):
        # event = Main3(None)
        # event.Show()
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
            cursor.execute(self.query)
            conn.commit()
            event = Main3(None)
            event.Refresh()
            self.Destroy()
            # conn.close()
        else :
            wx.MessageBox('Data tidak boleh kosong', 'Terjadi Kesalahan')
    
    def cari_grid( self, event ):
        judul = self.m_searchCtrl1.GetValue()
        self.query = "SELECT * FROM buku WHERE judul = \'%s\'"
        self.value = self.query % (judul)
        cursor.execute(self.query, self.value)
        hasil = cursor.fetchall()
        for b in range (9):
            a = 0
            for row in hasil:
                self.m_grid4.SetCellValue(a, b, str(row[b]))
                a = a + 1

run = wx.App()
frame = Main(parent=None)
frame.Show()
run.MainLoop()
# conn.close()