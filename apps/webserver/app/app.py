from flask import Flask, jsonify, send_file
import shutil
import random
import string
import os
from mcstatus import MinecraftServer
from settings import server_name, server_url, server_port, mods_folder, date

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return jsonify(f'{server_name.capitalize()} Minecraft Server')

@app.route('/api/v1/status', methods=['GET'])
def status():
    conn = MinecraftServer.lookup(f'{server_url}:{server_port}')
    try:
        conn.ping()
    except:
        server = {'status': 'Offline'}
        return jsonify(server)
    else:
        server = {'status': 'Online'}
        return jsonify(server)

@app.route('/api/v1/players', methods=['GET'])
def players():
    conn = MinecraftServer.lookup(f'{server_url}:{server_port}')
    try:
        conn.ping()
        status = conn.status()
    except:
        players = {'players_online': 0, 'players_max': 0}
        return jsonify(players)
    else:
        players = {'players_online': status.players.online, 'players_max': status.players.max}
        return jsonify(players)

@app.route('/download')
def downloadFile ():
    file_path = f'/tmp/{server_name}_mods_{date}'
    shutil.make_archive(file_path, 'zip', mods_folder)
    @app.after_request
    def delete(response):
        os.remove(f'{file_path}.zip')
        return response
    return send_file(f'{file_path}.zip', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
