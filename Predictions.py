#import Routines
from Routines import *

if __name__ == '__main__':
    
    Ejemplo1 = "pObreza, pobreza!, Pobreza achaque"
    Ejemplo2 = getText('15_TM_HAP (2).docx')

    Afects = DictsBuild('Diccionario_V2_2CSV.csv')
    AfectsExpr = DictsBuild('Diccionario_V2_2CSV.csv', StringDeUso='Expresiones')
    ResultadoEjemploStem = contador_stemming(Ejemplo1, Afects)
    ResultadoEjemploExpr = contadorExpresiones(Ejemplo1,AfectsExpr,StopWords = True, Stem = True)
    ResultadoTotal = sumador(SumaDeConteos(ResultadoEjemploExpr, ResultadoEjemploStem))
    Porcentajes = DictPercs(ResultadoTotal)
    print('Cantidad total de afectaciones: ', len(Afects))
    print('\nEjemplo 1: \n','Cantidad de afectaciones: ', len( [x for x in Porcentajes.values() if x>0 ]) )
    print(Porcentajes)
    

    Afects = DictsBuild('Diccionario_V2_2CSV.csv')
    AfectsExpr = DictsBuild('Diccionario_V2_2CSV.csv', StringDeUso='Expresiones')
    ResultadoEjemploStem = contador_stemming(Ejemplo2, Afects)
    ResultadoEjemploExpr = contadorExpresiones(Ejemplo2,AfectsExpr,StopWords = True, Stem = True)
    ResultadoTotal = sumador(SumaDeConteos(ResultadoEjemploExpr, ResultadoEjemploStem))
    Porcentajes = DictPercs(ResultadoTotal)
    print('\n Ejemplo 2: \n','Cantidad de afectaciones: ', len( [x for x in Porcentajes.values() if x>0 ]) )
    print(Porcentajes)
    
