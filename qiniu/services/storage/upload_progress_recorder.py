# -*- coding: utf-8 -*-

import json
import os
import tempfile

class UploadProgressRecorder(object):

  def __init__(self, record_folder=tempfile.gettempdir()):
      print record_folder
      self.record_folder = record_folder


  def get_upload_record(self, key):
      upload_record_file_path = os.path.join(self.record_folder, key)
      if not os.path.isfile(upload_record_file_path):
          return None
      with open(upload_record_file_path, 'r') as f:
          json_data = json.load(f)
      return json_data


  def set_upload_record(self, key, data):
      upload_record_file_path = os.path.join(self.record_folder, key)
      folder = os.path.dirname(upload_record_file_path)
      if not os.path.exists(folder):
          os.makedirs(folder)
      with open(upload_record_file_path, 'w') as f:
          json.dump(data, f)


  def delete_upload_record(self, key):
      record_file_path = os.path.join(self.record_folder, key)
      os.remove(record_file_path)
