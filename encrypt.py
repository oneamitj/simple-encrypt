#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import os
import array

class secure:
    def delete_event(self, widget, event, data=None):
        print "delete event occurred"
        return False

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()
        

    def encrypt(self, widget, *data):
        f_name = self.entry.get_text()
        result = array.array('i', [0]) * 2
        value = array.array('i', [0]) * 2

        value[0] = self.assign(data[0])
        value[1] = self.assign(data[1])
        
        key = self.key_store('e')
        
        result[0] = (value[0] * key[0][0] + value[1] * key[0][1]) % 41
        result[1] = (value[0] * key[1][0] + value[1] * key[1][1]) % 41
        
        print  "Frist:: ", self.assign(result[0])
        print  "Second:: ", self.assign(result[1])
        
        return result

    def decrypt(self, widget, *data):
        f_name = self.entry.get_text()
        result = array.array('i', [0]) * 2
        value = array.array('i', [0]) * 2

        value[0] = self.assign(data[0])
        value[1] = self.assign(data[1])

        key = self.key_store('d')
        print key

        result[0] = (value[0] * key[0][0] + value[1] * key[0][1]) % 41
        result[1] = (value[0] * key[1][0] + value[1] * key[1][1]) % 41
        
        print  "Frist:: ", self.assign(result[0])
        print  "Second:: ", self.assign(result[1])
        
        return result

    def assign(self, data):
        alpha = " abcdefghijklmnopqrstuvwxyz!,.?0123456789"
        number = 0
        print data
        if type(data) == str:
            return alpha.index(data)

        elif type(data) == int:
            while(number != data):
                number = number + 1
            return alpha[number]


    def select_file(self, widget):
        # input_file = sys.argv[1]
        # data = file(input_file).read()
        filechooser = gtk.FileChooserDialog("Open File",
                               None,
                               gtk.FILE_CHOOSER_ACTION_OPEN,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        filechooser.set_default_response(gtk.RESPONSE_OK)

        # filter = gtk.FileFilter()
        # filter.set_name("All files")
        # filter.add_pattern("*")
        # filechooser.add_filter(filter)

        file_type = gtk.FileFilter()
        file_type.set_name("TXT")
        # file_type.add_mime_type("image/png")
        # file_type.add_mime_type("image/jpeg")
        # file_type.add_mime_type("image/gif")
        file_type.add_pattern("*.txt")
        # file_type.add_pattern("*.jpg")
        # file_type.add_pattern("*.gif")
        # file_type.add_pattern("*.tif")
        # file_type.add_pattern("*.xpm")
        filechooser.add_filter(file_type)

        response = filechooser.run()
        if response == gtk.RESPONSE_OK:
            # self.f_name = filechooser.get_filename()
            self.entry.set_text(filechooser.get_filename())
            filechooser.destroy()
        elif response == gtk.RESPONSE_CANCEL:
            print 'Closed, no files selected'
            filechooser.destroy()
        # print self.f_name


    def key_store(self, data):
        if data == 'e':
            return [[3, -2], [-1, 1]]
        elif data == 'd':
            return [[1, 2], [1, 3]]
        #print e_key[0][1]


    def msg_relay(self, widget, *data):
        pass

    def __init__(self):
        #self.f_name = ""
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", self.delete_event)
        # self.window.set_keep_above(True)
        self.window.set_title("Encrypt")
        self.window.set_default_size(20,50)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)
        # self.window.set_size_request(250,200)

        self.button0 = gtk.Button("Decrypt")
        self.button1 = gtk.Button("Encrypt")
        self.button2 = gtk.Button("Browse")
        self.entry = gtk.Entry()
        self.entry.set_text("...")
        #self.browse = gtk.FileChooserDialog(title=None,action=gtk.FILE_CHOOSER_ACTION_OPEN, buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))

        self.vbox = gtk.VBox(gtk.FALSE, 10)
        self.hbox1 = gtk.HBox(gtk.FALSE, 5)
        self.hbox2 = gtk.HBox(gtk.FALSE, 5)
        
        self.button0.connect("clicked", self.decrypt, 'b', 's')
        self.button1.connect("clicked", self.encrypt, "m", "e")
        self.button2.connect("clicked", self.select_file)

        self.hbox1.pack_start(self.entry, gtk.FALSE, gtk.FALSE, 0)
        self.entry.show()
        self.hbox2.pack_start(self.button1, gtk.FALSE, gtk.FALSE, 0)
        self.button2.show()
        self.hbox1.pack_start(self.button2, gtk.FALSE, gtk.FALSE, 0)
        self.button1.show()
        self.hbox2.pack_start(self.button0, gtk.FALSE, gtk.FALSE, 0)
        self.button0.show()

        self.vbox.pack_start(self.hbox1, gtk.FALSE, gtk.FALSE, 0)
        self.vbox.pack_start(self.hbox2, gtk.FALSE, gtk.FALSE, 0)
        self.hbox1.show()
        self.hbox2.show()
        self.vbox.show()

        self.window.add(self.vbox)
        self.window.show()

    def main(self):
        gtk.main()



if __name__ == "__main__":
    encrypt_main = secure()
    encrypt_main.main()