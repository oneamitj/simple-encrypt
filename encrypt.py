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
        


    def select_file(self, widget):
        filechooser = gtk.FileChooserDialog("Open File",
                               None,
                               gtk.FILE_CHOOSER_ACTION_OPEN,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        filechooser.set_default_response(gtk.RESPONSE_OK)

        filter = gtk.FileFilter()
        filter.set_name("All files")
        filter.add_pattern("*")
        filechooser.add_filter(filter)

        file_type = gtk.FileFilter()
        file_type.set_name("TXT")
        file_type.add_pattern("*.txt")
        filechooser.add_filter(file_type)

        response = filechooser.run()
        if response == gtk.RESPONSE_OK:
            self.entry.set_text(filechooser.get_filename())
            filechooser.destroy()
            self.label.set_text("File selected!")
        elif response == gtk.RESPONSE_CANCEL:
            print 'Closed, no files selected'
            filechooser.destroy()



    def encrypt(self, *data):
        result = array.array('i', [0]) * 4
        value = array.array('i', [0]) * 4

        value[0] = self.assign(data[0])
        value[1] = self.assign(data[1])
        value[2] = self.assign(data[2])
        value[3] = self.assign(data[3])
        
        key = self.key_store()
        
        result[0] = (value[0] * key[0][0] + value[1] * key[0][1] + value[2] * key[0][2] + value[3] * key[0][3]) % 41
        result[1] = (value[0] * key[1][0] + value[1] * key[1][1] + value[2] * key[1][2] + value[3] * key[1][3]) % 41
        result[2] = (value[0] * key[2][0] + value[1] * key[2][1] + value[2] * key[2][2] + value[3] * key[2][3]) % 41
        result[3] = (value[0] * key[3][0] + value[1] * key[3][1] + value[2] * key[3][2] + value[3] * key[3][3]) % 41
        
        output = self.assign(result[0]) + self.assign(result[1]) + self.assign(result[2]) + self.assign(result[3])
        return output

    def assign(self, data):
        alpha = " abcdefghijklmnopqrstuvwxyz!,.?0123456789"
        number = 0
        if type(data) == str:
            data = data.lower()
            return alpha.index(data)

        elif type(data) == int:
            while(number != data):
                number = number + 1
            return alpha[number]



    def key_store(self):
        return [[19, 18, 29, 0],
                [16, 18, 5, 13],
                [18, 1, 10, 10],
                [15, 19, 8, 9]]


    def msg_relay(self, widget):
        msg = file(self.entry.get_text()).read()
        msg = msg.replace("\n", "")

        sets = (len(msg)) % 4
        if sets != 0:
            msg = msg + " "*(4-sets)
        output = ""

        for i in range(0, len(msg), 4):
                output = output + self.encrypt(msg[i], msg[i+1], msg[i+2], msg[i+3])
                
        f_name = open("encrypted.txt", 'w+')
        f_name.write(str(output))
        f_name.close()
        self.label.set_text("Encrypted message is in encrypted.txt in current directory!")

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", self.delete_event)
        self.window.set_title("Encrypt")
        self.window.set_default_size(20,50)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)

        self.label = gtk.Label("Choose file to encrypt!")
        self.button1 = gtk.Button("Encrypt")
        self.button2 = gtk.Button("Browse")
        self.entry = gtk.Entry()
        self.entry.set_text("/home/wannamit/iVoIP/encrypt/msg.txt")

        self.vbox = gtk.VBox(gtk.FALSE, 10)
        self.hbox1 = gtk.HBox(gtk.FALSE, 5)
        self.hbox2 = gtk.HBox(gtk.FALSE, 5)
        
        self.button1.connect("clicked", self.msg_relay)
        self.button2.connect("clicked", self.select_file)

        self.hbox1.pack_start(self.entry, gtk.FALSE, gtk.FALSE, 0)
        self.entry.show()
        self.hbox2.pack_start(self.button1, gtk.FALSE, gtk.FALSE, 0)
        self.button2.show()
        self.hbox1.pack_start(self.button2, gtk.FALSE, gtk.FALSE, 0)
        self.button1.show()
        self.hbox2.pack_start(self.label, gtk.FALSE, gtk.FALSE, 0)
        self.label.show()

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