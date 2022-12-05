from operaciones import *
import pprint
def main():
    pprint.pprint(sumador.suma(10,5))
    pprint.pprint(restador.resta(10,5))
    pprint.pprint(multiplicador.multiplica(10,5))
    pprint.pprint(divisor.divide(10,5))

if __name__ == "__main__":
    main()