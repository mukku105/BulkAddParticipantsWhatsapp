# GUI for bulk adding numbers to whatsapp group

import itertools
import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog, QScrollArea
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6 import uic
import requests
import json
import pandas as pd

try:
    os.chdir(sys._MEIPASS)
    print(sys._MEIPASS)
except:
    pass

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/main.ui', self)
        self.setFixedSize(512, 540)
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
        self.ui.pb_add.clicked.connect(self.add_participants)
        self.ui.pb_instruct.clicked.connect(self.show_instructions)
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
            self.set_tableview_csv(df)
    
    def set_tableview_csv(self, df):
        model = QStandardItemModel(self)
        model.setHorizontalHeaderLabels(df.columns)
        for i in range(len(df.index)):
            for j in range(len(df.columns)):
                model.setItem(i, j, QStandardItem(str(df.iat[i, j])))
        self.ui.tv_csv.setModel(model)
        # self.ui.tv_csv.selectAll()
        self.ui.tv_csv.resizeColumnsToContents()
        self.ui.tv_csv.show()
    
    def get_file_name(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)")
        return file_name
    
    # def check_phone_number(self, group_id, numbers):
    #     check_phone_api_url = 'https://gate.whapi.cloud/contacts'
    #     headers = { 
    #         'Authorization': 'Bearer ' + self.ui.le_watoken.text().strip(), 
    #         'Content-Type': 'application/json', 
    #         'Accept': 'application/json' 
    #     }

    #     data = {
    #         'blocking': 'wait',
    #         'contacts': numbers
    #     }

    #     response = requests.post(check_phone_api_url, headers=headers, data=json.dumps(data))
    #     if response.status_code == 200:
    #         invalid_numbers = []
    #         for contact in json.loads(response.text)['contacts']:
    #             if contact['status'] == 'invalid':
    #                 invalid_numbers.append(contact['input'])
    #         if invalid_numbers:
    #             QMessageBox.critical(self, 'Error', 'Invalid phone numbers: ' + ', '.join(invalid_numbers) + '<br><strong>Please correct the numbers and try again</strong>')
    #         else:
    #             self.add_numbers_to_group(group_id, numbers)
    #     else:
    #         QMessageBox.critical(self, 'Error', 'Error checking phone numbers' + str(response.text))

    def add_participants(self):
        group_id = self.ui.cb_grouplist.currentData()
        if not group_id:
            QMessageBox.critical(self, 'Error', 'Please select a group')
            return

        model = self.ui.tv_csv.model()
        numbers = []

        for i in range(model.rowCount()):
            number = model.index(i, 1).data()

            if len(number) == 10:
                number = '91' + number
            numbers.append(number)
        df = pd.read_csv(self.ui.l_csvpath.toolTip())
        print(numbers)
        # self.check_phone_number(group_id, numbers)
        self.add_numbers_to_group(group_id, numbers)

    def add_numbers_to_group(self, group_id, numbers):
        group_api_url = 'https://gate.whapi.cloud/groups/' + group_id + '/participants'
        headers = { 
            'Authorization': 'Bearer ' + self.ui.le_watoken.text().strip(), 
            'Content-Type': 'application/json', 
            'Accept': 'application/json' 
        }

        data = {
            'participants': numbers
        }

        response = requests.post(group_api_url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            msg = 'Numbers added successfully'
            if json.loads(response.text)['failed']:
                msg += '<br><strong>Failed to add: </strong>' + ', '.join(json.loads(response.text)['failed'])
            QMessageBox.information(self, 'Success', msg)
            print(response.text)
        elif response.status_code == 409:
            msg = '<strong>Some Participants are already in the Group. Please remove them and try again.</strong>'
            msg += '<br>' + response.text
            QMessageBox.critical(self, 'Error', msg)
        else:
            QMessageBox.critical(self, 'Error', 'Error adding numbers' + str(response.text))

    def show_instructions(self):
            instructions = """
            <p><strong>Instructions:</strong></p>
            <p>
            1. Visit <a href='https://panel.whapi.cloud/login'>https://panel.whapi.cloud/login</a> 
            and login with your credentials or <strong>Sign Up.</strong>
            <br>
            2. Follow the Steps to sign in to your WhatsApp.<br>
            3. Go to Dashboard <a href='https://panel.whapi.cloud/dashboard'>https://panel.whapi.cloud/dashboard</a><br>
            4. Select the channel.
            <br><img src='./imgs/dashboard.jpg' width='200'></img><br>
            5. Grab the API Token <br>
                <img src='./imgs/token.jpg' width='200'></img><br>
            6. Create CSV file containing participants in the format given below and import<br>
                <img src='./imgs/csv_format.jpg' width='180'></img>
            </p>
            """
            # scroll = QScrollArea(self)
            # scroll.setWidgetResizable(T)
            QMessageBox.information(self, 'Markdown Preview Instructions', instructions)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
