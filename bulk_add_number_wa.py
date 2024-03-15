# program to create pyQT6
# GUI for bulk adding numbers to
# whatsapp group

import itertools
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog, QComboBox
from PyQt6 import uic
import requests
import json
import pandas as pd

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('main.ui', self)
        self.setFixedSize(512, 640)
        self.setWindowTitle('Bulk Add Participants to WhatsApp')

        self.xor_enc_key = "Asjwu@341SsjcuSduy23"

        try:
            with open('token.wapi', 'rb') as f:
                encrypted_token = f.read().decode()
                self.ui.le_watoken.setText(self.xor_encrypt_decrypt(encrypted_token, self.xor_enc_key))
        except FileNotFoundError:
            pass

        self.ui.pb_savetoken.clicked.connect(self.save_token)
        self.ui.pb_sync.clicked.connect(self.sync_wa_info)
        self.ui.cb_grouplist.currentIndexChanged.connect(self.group_selected)

        self.ui.pb_import.clicked.connect(self.import_csv)

        self.show()

    def save_token(self):
        token = self.ui.le_watoken.text().strip()
        if token:
            encrypted_token = self.xor_encrypt_decrypt(token, self.xor_enc_key)
            with open('token.wapi', 'wb') as f:
                f.write(encrypted_token.encode())
            QMessageBox.information(self, 'Success', 'Token saved successfully')
        else:
            QMessageBox.critical(self, 'Error', 'Please enter a valid token')  

    def xor_encrypt_decrypt(self, text, key):
        return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(text, itertools.cycle(key)))
    
    def sync_wa_info(self):
        self.sync_group_list()
        self.fetch_channel_limits()

    def sync_group_list(self):
        self.ui.pb_sync.setEnabled(False)
        self.ui.pb_sync.setText('Syncing...')
        self.ui.pb_sync.repaint()
        self.fetch_group_list()
        self.ui.pb_sync.setEnabled(True)
        self.ui.pb_sync.setText('Sync')
        self.ui.pb_sync.repaint()

    def fetch_group_list(self):
        # import time
        # time.sleep(3)
        
        group_api_url = 'https://gate.whapi.cloud/groups?count=100'
        headers = { 
            'Authorization': 'Bearer ' + self.ui.le_watoken.text().strip(), 
            'Content-Type': 'application/json', 
            'Accept': 'application/json' 
        }

        response = requests.get(group_api_url, headers=headers)
        if response.status_code == 200:
            group_list = json.loads(response.text)
            print(group_list)
            self.ui.cb_grouplist.clear()
            for group in group_list['groups']:
                self.ui.cb_grouplist.addItem(group['name'], group['id'])
        else:
            QMessageBox.critical(self, 'Error', 'Error fetching group list' + str(response.text))

    def fetch_channel_limits(self):
        channel_api_url = 'https://gate.whapi.cloud/limits'
        headers = { 
            'Authorization': 'Bearer ' + self.ui.le_watoken.text().strip(), 
            'Content-Type': 'application/json', 
            'Accept': 'application/json' 
        }

        response = requests.get(channel_api_url, headers=headers)
        if response.status_code == 200:
            channel_limits = json.loads(response.text)
            self.ui.l_req_left.setText("Req. left: " + str(channel_limits['requests']))
            print(channel_limits)
        else:
            QMessageBox.critical(self, 'Error', 'Error fetching channel limits' + str(response.text))

    def group_selected(self):
        print(self.ui.cb_grouplist.currentData())
    
    def import_csv(self):
        file_name = self.get_file_name()

        if file_name:
            self.ui.l_csvpath.setText(file_name)
            self.ui.l_csvpath.setToolTip(file_name)
            df = pd.read_csv(file_name)
            print(df)
            
    def get_file_name(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)")
        return file_name


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
