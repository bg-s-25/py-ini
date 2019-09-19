'''
Py-INI: Read/write INI configuration files
Author: Bobby Georgiou
Version: 1.0
Date: Feb 2019
'''
import os.path

class INIFile:
    def __init__(self, filename):
        self.__filename = filename
        self.__index = {}
        
        if not os.path.isfile(filename):
            raise IOError("Cannot open INI file.")

        self.__build_index()

    @property
    def filename(self):
        return os.path._getfullpathname(self.__filename)

    '''
    Read INI file and build an easily accessible index (dictionary)
    '''
    def __build_index(self):
        lines = []
        f = open(self.__filename, 'r')
        for line in f.readlines():
            lines.append(line.strip())
        f.close()

        cur_sec = ''
        cur_key = ''
        cur_val = ''
        put_key = False

        for line in lines:
            if line.startswith(';') or line.startswith('#'): continue
            if line.startswith('[') and line.endswith(']'):
                cur_sec = line[1:][:-1]
                self.__index[cur_sec] = {}
            elif line.__contains__('='):
                kv_pair = line.split('=')
                cur_key = kv_pair[0].strip()
                cur_val = kv_pair[1].strip()
                put_key = True
            if put_key and len(cur_sec) > 0 and len(cur_key) > 0 and len(cur_val) > 0:
                self.__index[cur_sec][cur_key] = cur_val
                put_key = False

    '''
    Export all INI data, including newly added keys, to the file
    '''
    def __export_index(self):
        f = open(self.__filename, 'w')
        for sec in self.__index:
            f.write('[' + sec + ']\n')
            for key in self.__index[sec]:
                f.write(key + '=' + self.__index[sec][key] + '\n')
        f.close()

    '''
    Read value from INI data; return empty string if value was not found
    :param section: section name
    :param key: key name
    '''
    def read_value(self, section, key):
        try:
            return self.__index[section][key]
        except KeyError:
            return ''

    '''
    Read section from INI data, return empty string if section was not found
    :param section: section name
    '''
    def read_section(self, section):
        try:
            return self.__index[section]
        except KeyError:
            return ''

    '''
    Write value to index and INI file; if the specified section/key does not already exist, create it
    :param section: section name
    :param key: key name
    :param value: value name
    '''
    def write_value(self, section, key, value):
        if not isinstance(section, str) or not isinstance(key, str) or not isinstance(value, str):
            raise ValueError("New section, key, and value must be of type str.")
        
        if not section in self.__index: self.__index[section] = {}

        self.__index[section][key] = value
        self.__export_index()

    '''
    Return a string representation of all sections, keys, and values in the index
    '''
    def __str__(self):
        index_str = ''
        for sec in self.__index:
            index_str += '[' + sec + ']\n'
            for key in self.__index[sec]:
                index_str += key + '=' + self.__index[sec][key] + '\n'
        return index_str
