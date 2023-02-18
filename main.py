import argparse

from tester import ODBCTester

if __name__ == '__main__':
    desc = "Usa el comando -p para indicar la ruta a un archivo .mdb (Microsoft Access Database) para comprobar " \
           "que se puede leer/usar odbc. En caso contrario lanzara una excepcion de lo que ha ocurrido.\n"

    parser = argparse.ArgumentParser(description='Comprueba que exista odbc valido instalado.',
                                     epilog=desc)
    parser.add_argument('-p', '--path', help='Ruta a archivo .mdb', required=True)
    args = vars(parser.parse_args())

    if args['path']:
        tester = ODBCTester(args['path'])
        tester.run()
    else:
        print("Falta ruta de archivo .mdb")
