# #Los strings en python 3+ son por defecto unicode. El encabezado uft y los prefijos u son redundantes para el programa. 

def StripPunc(Text,Sig=[u".",u",",u";",u":",u"!",u"¡",u"-",u"?",u"¿",u'"',u"'",u"(",u")",u"[",u"]"]):
    for i in Sig:
        Text=Text.replace(i,u"")
    return Text

def normalize(mystr):
    '''Normalizar las tildes en cadenas de caracteres. 
    Arguments: 
    mystr: str o list. 
    '''
    if type(mystr) is list:
        NewList=[normalize(i) for i in mystr]
        return NewList
    if type(mystr) is str:
        return mystr.lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")

import numpy
import pandas
import nltk
import docx
#NLTK:
nltk.download('punkt')
nltk.download('stopwords')
spanish_stemmer = nltk.stem.SnowballStemmer('spanish')
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
stop_words=set(nltk.corpus.stopwords.words("spanish"))

def PreparacionTexto(Texto,StopWords=stop_words,Stemmer=spanish_stemmer):
    '''Tokenize, stemmed and remove stopwords
    Texto: str
    '''
    StrippedText=StripPunc(Texto)
    tokenized_word=nltk.tokenize.word_tokenize(StrippedText)
    print(tokenized_word)
    filtered_words = [i for i in tokenized_word if i not in StopWords]
    print(filtered_words)
    stemmed_text = [Stemmer.stem(i) for i in filtered_words]
    print(stemmed_text)

#########

def CountingFunction(Text,Pattern):
    '''Contar las ocurrencias de un str dentro de otro str. Ojo: el str pattern se toma sin ninguna modificación.
    Text: str, list of arrtype.
    Pattern: str
    '''
    if type(Text) is not list and type(Text) is not numpy.ndarray and type(Text) is not str:
        print ("Bad usage of this function: CountingFunction(Arr,Pat) Arr: must be a list or an array or string, Pat: must be a string")

        return 
    if type(Text) is str:
        MyArray=numpy.array(StripPunc(Text).split(" "))
    if type(Text) is list:
        MyArray=numpy.array(Text)
    if type(Text) is numpy.ndarray:
        MyArray=Text
    return numpy.count_nonzero(MyArray == Pattern)

#Construccion de Diccionarios

def DictsBuild(CSVFile, StringDeUso='Sinónimos-Palabras'):
    '''Construye el diccionario de palabras para el conteo.
    CSVFile: archivo .csv del diccionario
    StringDeUso: columna a la que se le extrae la información en el archivo.
    '''
    df = pandas.read_csv(CSVFile)
    df = df.replace(numpy.nan, '', regex=True)
    Afectaciones = {}
    for i in range(len(df[StringDeUso])):
        if StringDeUso == 'Sinónimos-Palabras':
            ListaDeAfects=df[StringDeUso][i].replace(", ", ",").split(",")
        if StringDeUso == 'Expresiones':
            ListaDeAfects = df[StringDeUso][i].lower().replace('”','"').replace('“','"').replace('" ,','",').split('",')
            ListaDeAfects = [expr.replace('"','') for expr in ListaDeAfects if expr]
        Afectaciones[normalize(df['Nodos'][i])] = [x.strip() for x in ListaDeAfects if x]
        Afectaciones[normalize(df['Nodos'][i])] = [x for x in Afectaciones[normalize(df['Nodos'][i])] if x]
    return Afectaciones

#Contadores de palabras
def contador(Texto,Diccionarios,ConStem=False):
    '''Cuenta el número de ocurrencias de multiples palabras albergadas en un diccionario construido (DictsBuild) en un texto.
    Texto: str.
    Diccionarios: Dict o DataFrame
    '''
    DFResultado={}
    for i in Diccionarios:
        CurrentFreq=[]
        #print Diccionarios[i]
        for k in Diccionarios[i]:
            #print k
            if ConStem: CurrentFreq.append(CountingFunction(Texto,spanish_stemmer.stem(k)))
            else: CurrentFreq.append(CountingFunction(Texto,k))
        DFResultado[i]=CurrentFreq
    return DFResultado

def ConteoManual(ExlFile,ListaDeAfects,NombreTestimonio,filtradas = True):
    '''Cuenta cuántas ocurrencias reportadas tiene un testimonio en un archivo de Excel. 
    Las ocurrencias deben especificarse en ListaDeAfects.
    ExlFile: path del archivo excel
    ListaDeAfects: list - las afectaciones que quieren ser revisadas
    NombreTestimonio: str - El tesimonio a revisar
    Filtradas: bool - Filtar las afectaciones teniendo en cuenta que sí aparezcan en ListaDeAfects
    '''
    df_manual = pandas.read_excel(ExlFile)
    dfTemp = df_manual.loc[df_manual['TESTIMONIO'] == NombreTestimonio]
    dicc = {k:0 for k in normalize(ListaDeAfects)}
    for i in dfTemp['AFECTACIÓN']:
        j=normalize(i)
        dicc[j] = dicc.get(j, 0) + 1
    SortDic = {k: v for k, v in sorted(dicc.items(), key=lambda item: -item[1])}
    if filtradas:
        return {k:v for k,v in SortDic.items() if k in normalize(ListaDeAfects) }
    else:
        return SortDic

#Lectura de docx
def getText(filename):
    '''Abrir un documento de Word. Retorna el documento en un string
    filename - path al documento
    '''
    doc = docx.Document(filename)   #Abre el documento filename
    fullText = []                   #Lista vacía para ingresar el texto
    for para in doc.paragraphs:     #recorre los paragrafos del texto y los agruega en fulltext
        fullText.append(para.text)
    return '\n'.join(fullText)

def sumador(Dicc):
    '''Suma el total de afectaciones sobre un diccionario
    Dicc: dict - el diccionario que devuelve contador.
    '''      
    total = {k:numpy.sum(v) for (k,v) in Dicc.items()}
    return total


def contador_stemming(Texto, Diccionarios):
    '''Función igual a Contador, pero contiene stemming. 
    '''
    Texto_stem = [spanish_stemmer.stem(word) for word in tokenizer.tokenize(Texto)]
    Dicc_stem = {}
    for i in Diccionarios:
        Dicc_stem[i] = [spanish_stemmer.stem(expr) for expr in Diccionarios[i]]
    DFResultado = {}
    for i in Dicc_stem:
        CurrentFreq = []
        for k in Dicc_stem[i]:
            CurrentFreq.append(Texto_stem.count(k))
        DFResultado[i]=CurrentFreq
    return DFResultado

def contadorExpresiones(Texto,Diccionario,StopWords = False, Stem = False):
    '''Función para el conteo de expresiones, no de palabras. Retorna un diccionario con el conteo.
    Texto: str - texto al que se le cuentan las ocurrencias
    Diccionario: dict - diccionario que devuelve DictBuild(StringDeUso='Expresiones') para las expresiones.
    StopWords: bool - True Si se desea quitar las stopwords
    Stem: bool - True si se desea stemmizar cada palabra en el texto
    '''
    #Stopwords = True: quitar las stopwors. Stem=True: aplicar stem.
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')       #Tokenizador violento (Quita la puntuación)
    stop_words=set(nltk.corpus.stopwords.words("spanish"))  #StopWords en español
    spanish_stemmer = nltk.stem.SnowballStemmer('spanish')
    
    Texto = Texto.lower()
    if (StopWords or Stem): tokenize_text = tokenizer.tokenize(Texto)
    if (StopWords == True and Stem == False): text = ' '.join([word for word in tokenize_text if word not in stop_words])
    if (StopWords == False and Stem == True): text = ' '.join([spanish_stemmer.stem(word) for word in tokenize_text])
    if (StopWords and Stem): text = ' '.join([spanish_stemmer.stem(word) for word in tokenize_text if word not in stop_words])
    #print(text)
    DFResultado = {}
    for key in Diccionario:
        CurrentFreq = []
        for v in Diccionario[key]:
            if StopWords == False and Stem == False:
                CurrentFreq.append(Texto.count(v))
            elif StopWords == True and Stem == False:
                tokenize_Expr = tokenizer.tokenize(v)
                stop_Expr = ' '.join([word for word in tokenize_Expr if word not in stop_words])
                CurrentFreq.append(text.count(stop_Expr))
            elif StopWords == False and Stem == True:
                tokenize_Expr = tokenizer.tokenize(v)
                stem_Expr = ' '.join([spanish_stemmer.stem(word) for word in tokenize_Expr])
                CurrentFreq.append(text.count(stem_Expr))
            else:
                tokenize_Expr = tokenizer.tokenize(v)
                stopstem_Expr = ' '.join([spanish_stemmer.stem(word) for word in tokenize_Expr if word not in stop_words])
                CurrentFreq.append(text.count(stopstem_Expr))        
        DFResultado[key] = CurrentFreq
    return DFResultado

#########
#Si uno corre especificamente este sript, esto corre, si se llama, entonces no. 
if __name__ == '__main__':

    ElEjemploMasSencillo=False

    if ElEjemploMasSencillo:
        Textos=[Texto1,Texto2]

        Dict1=["casa","letra","rato","ojos"]
        Dict2=["signos","concierto","grosor","diablo","patas","vida"]
        Dicts=[Dict1,Dict2]

        Freqs=[]

        for i in Textos:
            for j in range(len(Dicts)):
                CurrentFreq=[]
                for k in Dicts[j]:
                    CurrentFreq.append(CountingFunction(i,k))
                Freqs.append(CurrentFreq)
        print(Freqs)
        
    Texto1 = "Muy lejos, más allá de las montañas de palabras, alejados de los países de las vocales y las consonantes, viven los textos simulados. Viven aislados en casas de letras, en la costa de la semántica, un gran océano de lenguas. Un riachuelo llamado Pons fluye por su pueblo y los abastece con las normas necesarias. Hablamos de un país paraisomático en el que a uno le caen pedazos de frases asadas en la boca. Ni siquiera los todopoderosos signos de puntuación dominan a los textos simulados; una vida, se puede decir, poco ortográfica. Pero un buen día, una pequeña línea de texto simulado, llamada Lorem Ipsum, decidió aventurarse y salir al vasto mundo de la gramática. El gran Oxmox le desanconsejó hacerlo, ya que esas tierras estaban llenas de comas malvadas, signos de interrogación salvajes y puntos y coma traicioneros, pero el texto simulado no se dejó atemorizar. Empacó sus siete versales, enfundó su inicial en el cinturón y se puso en camino. Cuando ya había escalado las primeras colinas de las montañas cursivas, se dio media vuelta para dirigir su mirada por última vez, hacia su ciudad natal Letralandia, el encabezamiento del pueblo Alfabeto y el subtítulo de su propia calle, la calle del renglón. Una pregunta retórica se le pasó por la mente y le puso melancólico, pero enseguida reemprendió su marcha. De nuevo en camino, se encontró con una copia. La copia advirtió al pequeño texto simulado de que en el lugar del que ella venía, la habían reescrito miles de veces y que todo lo que había quedado de su original era la palabra 'y', así que más le valía al pequeño texto simulado volver a su país, donde estaría mucho más seguro. Pero nada de lo dicho por la copia pudo convencerlo, de manera que al cabo de poco tiempo, unos pérfidos redactores publicitarios lo encontraron y emborracharon con Longe y Parole para llevárselo después a su agencia, donde abusaron de él para sus proyectos, una y otra vez. Y si aún no lo han reescrito, lo siguen utilizando hasta ahora.Muy lejos, más allá de las montañas de palabras, alejados de los países de las vocales y las consonantes, viven los textos simulados. Viven aislados en casas de letras, en la costa de la semántica, un gran océano de lenguas. Un riachuelo llamado Pons fluye por su pueblo y los abastece con las normas necesarias. Hablamos de un país paraisomático en el que a uno le caen pedazos de frases asadas en la boca. Ni siquiera los todopoderosos signos de puntuación dominan a los textos simulados; una vida, se puede decir, poco ortográfica. Pero un buen día, una pequeña línea de texto simulado, llamada Lorem Ipsum, decidió aventurarse y salir al vasto mundo de la gramática. El gran Oxmox le desanconsejó hacerlo, ya que esas tierras estaban llenas de comas malvadas, signos de interrogación salvajes y puntos y coma traicioneros, pero el texto simulado no se dejó atemorizar. Empacó sus siete versales, enfundó su"
    Texto2 = "Deterioro económico, Pobreza, molestia, pobreza, pobreza, pobreza"
    #Texto2 = getText('15_TM_HAP (2).docx')
    
    print(CountingFunction(Texto2,'pobreza'))
"""     Afects=DictsBuild('DiccionariosVersionDic1_2020.csv')
    print(Afects)
    ResultadoTexto1=contador(Texto1.replace("a",Afects['proyecto de vida'][6]),Afects)
    print("Conteo del texto 1: \n", ResultadoTexto1)
    print("Total del conteo texto 1: \n", sumador(ResultadoTexto1),"\n")

    ResultadoTexto2=contador(Texto2.replace("a",Afects['socioculturales'][4]),Afects)
    print("Conteo del texto 2: \n: ",ResultadoTexto2)
    print("Total del conteo del texto 2: \n",sumador(ResultadoTexto2))
    
    ResultadoTexto1Stem = contador_stemming(Texto1.replace("a",Afects['proyecto de vida'][6]), Afects)
    print('\n Con Stem: \n Texto 1: \n', ResultadoTexto1Stem)
    print('Total: \n', sumador(ResultadoTexto1Stem))
    
    #ResultadoTexto2Stem = contador_stemming(Texto2.replace("a",Afects['socioculturales'][4]), Afects)
    ResultadoTexto2Stem = contador_stemming(Texto2,Afects)
    print('Texto 2: \n', sumador(ResultadoTexto2Stem))

    dicc = ConteoManual('ReporteTesteoManualTotal.xlsx','DiccionariosVersionDic1_2020.csv','15_TM_HAP (2)',filtradas=True)
    print('Conteo manual: \n',dicc) """