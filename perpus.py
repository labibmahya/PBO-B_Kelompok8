# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 178, 34, 33 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )


		bSizer1.Add( ( 0, 130), 0, wx.EXPAND, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"APLIKASI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"PERPUSTAKAAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer1.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )


		bSizer1.Add( fgSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.Size( 190,-1 ), 0 )
		self.m_button4.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer3.Add( self.m_button4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Belum punya akun?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer4.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Daftar.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText7.SetForegroundColour( wx.Colour( 5, 109, 224 ) )

		fgSizer4.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer3.Add( fgSizer4, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( bSizer3, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button4.Bind( wx.EVT_BUTTON, self.button_login )
		self.m_staticText7.Bind( wx.EVT_LEFT_UP, self.klik_daftar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def button_login( self, event ):
		event.Skip()

	def klik_daftar( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 178, 34, 33 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 100), 0, wx.EXPAND, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"REGISTRASI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_staticText10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer4.Add( self.m_staticText10, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer5.SetMinSize( wx.Size( -1,170 ) )
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer5.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Umur", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer5.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText13.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer5.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrl5, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer5.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText15.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer5.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrl7, 0, wx.ALL, 5 )


		bSizer4.Add( fgSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Daftar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer5.Add( self.m_button5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		fgSizer51 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer51.SetFlexibleDirection( wx.BOTH )
		fgSizer51.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Sudah punya akun?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText16.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer51.Add( self.m_staticText16, 0, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Login.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		self.m_staticText17.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText17.SetForegroundColour( wx.Colour( 5, 109, 224 ) )

		fgSizer51.Add( self.m_staticText17, 0, wx.ALL, 5 )


		bSizer5.Add( fgSizer51, 1, wx.EXPAND, 5 )


		bSizer4.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.button_daftar )
		self.m_staticText17.Bind( wx.EVT_LEFT_UP, self.klik_login )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def button_daftar( self, event ):
		event.Skip()

	def klik_login( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 178, 34, 33 ) )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer102 = wx.BoxSizer( wx.VERTICAL )

		bSizer102.SetMinSize( wx.Size( -1,50 ) )
		self.m_staticText371 = wx.StaticText( self, wx.ID_ANY, u"Aplikasi Digitalisasi Perpusatakaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText371.Wrap( -1 )

		self.m_staticText371.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Black" ) )
		self.m_staticText371.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer102.Add( self.m_staticText371, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer7.Add( bSizer102, 0, wx.EXPAND, 5 )

		fgSizer7 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Keluar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer7.Add( self.m_button5, 0, wx.ALL, 5 )


		bSizer7.Add( fgSizer7, 0, wx.ALL, 5 )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.m_panel6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid4 = wx.grid.Grid( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )

		# Grid
		self.m_grid4.CreateGrid( 0, 10 )
		self.m_grid4.EnableEditing( False )
		self.m_grid4.EnableGridLines( True )
		self.m_grid4.EnableDragGridSize( False )
		self.m_grid4.SetMargins( 0, 35 )

		# Columns
		self.m_grid4.SetColSize( 0, 80 )
		self.m_grid4.SetColSize( 1, 241 )
		self.m_grid4.SetColSize( 2, 159 )
		self.m_grid4.SetColSize( 3, 159 )
		self.m_grid4.SetColSize( 4, 100 )
		self.m_grid4.SetColSize( 5, 80 )
		self.m_grid4.SetColSize( 6, 112 )
		self.m_grid4.SetColSize( 7, 80 )
		self.m_grid4.SetColSize( 8, 80 )
		self.m_grid4.EnableDragColMove( False )
		self.m_grid4.EnableDragColSize( True )
		self.m_grid4.SetColLabelSize( 30 )
		self.m_grid4.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid4.AutoSizeRows()
		self.m_grid4.EnableDragRowSize( False )
		self.m_grid4.SetRowLabelSize( 80 )
		self.m_grid4.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid4.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_grid4.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer10.Add( self.m_grid4, 1, wx.ALIGN_LEFT|wx.ALL, 5 )

		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button9 = wx.Button( self.m_panel6, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button9.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer9.Add( self.m_button9, 0, wx.ALL, 5 )

		self.m_button91 = wx.Button( self.m_panel6, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button91.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer9.Add( self.m_button91, 0, wx.ALL, 5 )


		bSizer10.Add( fgSizer9, 0, wx.EXPAND, 5 )


		gbSizer1.Add( bSizer10, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		bSizer101 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText28 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"BUKU", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText28.Wrap( -1 )

		self.m_staticText28.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_staticText28.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer101.Add( self.m_staticText28, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		fgSizer10 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText29 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Kode Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		self.m_staticText29.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText29.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer10.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl18, 0, wx.ALL, 5 )

		self.m_staticText30 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Judul", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		self.m_staticText30.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer10.Add( self.m_staticText30, 0, wx.ALL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl19, 0, wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Pengarang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer10.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.m_textCtrl20 = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl20, 0, wx.ALL, 5 )

		self.m_staticText32 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Penerbit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer10.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl21, 0, wx.ALL, 5 )

		self.m_staticText33 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Tempat Terbit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer10.Add( self.m_staticText33, 0, wx.ALL, 5 )

		self.m_textCtrl22 = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl22, 0, wx.ALL, 5 )

		self.m_staticText34 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Tahun Terbit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer10.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.m_textCtrl23 = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl23, 0, wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Jumlah Halaman", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		self.m_staticText35.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer10.Add( self.m_staticText35, 0, wx.ALL, 5 )

		self.m_textCtrl24 = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl24, 0, wx.ALL, 5 )

		self.m_staticText36 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Jumlah Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		self.m_staticText36.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer10.Add( self.m_staticText36, 0, wx.ALL, 5 )

		self.m_textCtrl25 = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl25, 0, wx.ALL, 5 )

		self.m_staticText37 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Kategori", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )

		self.m_staticText37.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer10.Add( self.m_staticText37, 0, wx.ALL, 5 )

		self.m_textCtrl26 = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl26, 0, wx.ALL, 5 )

		self.m_staticText38 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Nomor Rak", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )

		self.m_staticText38.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer10.Add( self.m_staticText38, 0, wx.ALL, 5 )

		self.m_textCtrl27 = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl27, 0, wx.ALL, 5 )


		bSizer101.Add( fgSizer10, 1, wx.EXPAND, 5 )

		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button81 = wx.Button( self.m_panel6, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button81.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer8.Add( self.m_button81, 0, wx.ALL, 5 )

		self.m_button10 = wx.Button( self.m_panel6, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button10.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer8.Add( self.m_button10, 0, wx.ALL, 5 )


		bSizer101.Add( fgSizer8, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gbSizer1.Add( bSizer101, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


		self.m_panel6.SetSizer( gbSizer1 )
		self.m_panel6.Layout()
		gbSizer1.Fit( self.m_panel6 )
		bSizer7.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.button_keluar )
		self.m_grid4.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.m_grid4OnGridCmdSelectCell )
		self.m_button9.Bind( wx.EVT_BUTTON, self.button_tambah )
		self.m_button91.Bind( wx.EVT_BUTTON, self.refresh )
		self.m_button81.Bind( wx.EVT_BUTTON, self.btn_simpanEdit )
		self.m_button10.Bind( wx.EVT_BUTTON, self.btn_deleteBuku )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def button_keluar( self, event ):
		event.Skip()

	def m_grid4OnGridCmdSelectCell( self, event ):
		event.Skip()

	def button_tambah( self, event ):
		event.Skip()

	def refresh( self, event ):
		event.Skip()

	def btn_simpanEdit( self, event ):
		event.Skip()

	def btn_deleteBuku( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 400,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 178, 34, 33 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )


		bSizer9.Add( ( 0, 50), 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Tambah Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		self.m_staticText18.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_staticText18.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer9.Add( self.m_staticText18, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Kode Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText19.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer6.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl8, 0, wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Judul", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		self.m_staticText20.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText20.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer6.Add( self.m_staticText20, 0, wx.ALL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl9, 0, wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Pengarang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText21.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer6.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl10, 0, wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Penerbit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText22.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer6.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl11, 0, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Tempat Terbit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		self.m_staticText23.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText23.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer6.Add( self.m_staticText23, 0, wx.ALL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Tahun Terbit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		self.m_staticText24.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText24.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer6.Add( self.m_staticText24, 0, wx.ALL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl13, 0, wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Jumlah Halaman", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		self.m_staticText25.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText25.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer6.Add( self.m_staticText25, 0, wx.ALL, 5 )

		self.m_textCtrl14 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl14, 0, wx.ALL, 5 )

		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Jumlah Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		self.m_staticText26.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText26.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer6.Add( self.m_staticText26, 0, wx.ALL, 5 )

		self.m_textCtrl15 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl15, 0, wx.ALL, 5 )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Ketegori", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		self.m_staticText27.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText27.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer6.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.m_textCtrl16 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl16, 0, wx.ALL, 5 )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Nomor Rak", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		self.m_staticText28.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText28.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer6.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_textCtrl17 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl17, 0, wx.ALL, 5 )


		bSizer9.Add( fgSizer6, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button10.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer12.Add( self.m_button10, 0, wx.ALL, 5 )


		bSizer12.Add( ( 20, 0), 0, wx.ALL, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button11.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer12.Add( self.m_button11, 0, wx.ALL, 5 )


		bSizer9.Add( bSizer12, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button10.Bind( wx.EVT_BUTTON, self.button_batal )
		self.m_button11.Bind( wx.EVT_BUTTON, self.button_simpan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def button_batal( self, event ):
		event.Skip()

	def button_simpan( self, event ):
		event.Skip()


