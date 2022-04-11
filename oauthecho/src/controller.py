"""
Defines the controller layer. 
Author: Thyago Mota
Last Update: April 11, 2022
"""

import sqlite3
import json
import boto3
import secrets
from datetime import datetime

AWS_DEPLOY = True

class Controller: 

    conn = None

    @staticmethod
    def get_connection():
        if not Controller.conn: 
            if AWS_DEPLOY: 
                s3_client = boto3.client("s3")
                database_file = '/tmp/oauthecho.db'
                with open(database_file, 'wb') as f:
                    s3_client.download_fileobj('geostats', 'oauthecho.db', f)
                Controller.conn = sqlite3.connect('/tmp/oauthecho.db')
            else:
                Controller.conn = sqlite3.connect('db/oauthecho.db')
        return Controller.conn

    @staticmethod
    def flush_db():
        conn = Controller.get_connection()
        if AWS_DEPLOY: 
            s3_client = boto3.client("s3")
            database_file = '/tmp/oauthecho.db'
            s3_client.upload_file(database_file, 'geostats', 'oauthecho.db')

    @staticmethod
    def get_token(client_id, client_secret):
        conn = Controller.get_connection()
        cursor = conn.cursor()
        sql = 'SELECT * FROM clients WHERE client_id = ? AND client_secret = ?'
        cursor.execute(sql, [client_id, client_secret])
        row = cursor.fetchone()
        if row:
            access_token = secrets.token_hex(16);
            sql = 'INSERT INTO access_tokens VALUES (?, ?, ?)'
            cursor.execute(sql, [access_token, datetime.now(), 60])
            conn.commit()
            Controller.flush_db()
            return {
                'code': 200, 
                'message': 'successful operation', 
                'body': {
                    'access_token': access_token, 
                    'expires_in': 60, 
                    'token_type': 'client credentials'
                }
            }
        else:
            return {
                'code': 401, 
                'message': 'unauthorized'
            }

    @staticmethod
    def get_echo(access_token, msg):
        conn = Controller.get_connection()
        cursor = conn.cursor()
        sql = 'SELECT * FROM access_tokens WHERE access_token = ?'
        cursor.execute(sql, [access_token])
        row = cursor.fetchone()
        out = 0
        if row:
            date_time = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f')
            tdelta = datetime.now() - date_time
            out = tdelta.total_seconds()
            if tdelta.total_seconds() <= row[2]:
                return {
                    'code': 200, 
                    'message': 'successful operation', 
                    'body': {
                        'msg': msg
                    }
                }

        return {
            'code': 401, 
            'message': 'unauthorized', 
            'out': out
        } 

if __name__ == "__main__":
    # response = Controller.get_token('Articulate Donkeys', 'fx11M43Jvk4THoNCeEDzifEby1hBfUfD')
    # print(response)
    # access_token = response['body']['access_token']
    access_token = '8d95b238dff584a591925c88a49729fe'
    response = Controller.get_echo(access_token, 'Hello!')
    print(response)


