from pyini import INIFile

# Read sample INI
def test01():
    file = INIFile("ini/test1.ini")
    print('- Filename: "' + file.filename + '"')
    print('- Contents of "test1.ini":')
    print(file)

# Write to sample INI
def test02():
    file = INIFile('ini/test2.ini')
    file.write_value('sec1', 'key2a', 'value2a')
    file.write_value('sec3', 'key5', 'value5')
    print('- Contents of "test2.ini":')
    print(file)

# Read "Skyrim.ini" (Config file for Skyrim)
def test03():
    file = INIFile('ini/Skyrim.ini')
    print('- Contents of "General" section of "Skyrim.ini":')
    print(str(file.read_section('General')))
    print('- Section="General",Key="sTestFile3" = ' + file.read_value('General', 'sTestFile3'))

test01()
test02()
test03()
