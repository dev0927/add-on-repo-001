import addons_xml_generator
import zipgen

def make_release():
    addons_xml_generator.Generator()
    zipgen.main("..")

if __name__ == '__main__':
    make_release()