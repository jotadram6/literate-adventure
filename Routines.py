# #Los strings en python 3+ son por defecto unicode. El encabezado uft y los prefijos u son redundantes para el programa. 

import numpy as np

def StripPunc(Text,Sig=[u".",u",",u";",u":",u"!",u"¡",u"-",u"?",u"¿",u'"',u"'",u"(",u")",u"[",u"]"]):
    for i in Sig:
        Text=Text.replace(i,u"")
    return Text

#NLTK utilities

import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
#from nltk.probability import FreqDist
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words=set(stopwords.words("spanish"))
from nltk.stem import SnowballStemmer
spanish_stemmer = SnowballStemmer('spanish')

def PreparacionTexto(Texto,SignosPuntuacion,StopWords=stop_words,Stemmer=spanish_stemmer):
    StrippedText=StripPunc(Texto)
    tokenized_word=word_tokenize(StrippedText)
    print(tokenized_word)
    filtered_words = [i for i in tokenized_word if i not in StopWords]
    print(filtered_words)
    stemmed_text = [Stemmer.stem(i) for i in filtered_words]
    print(stemmed_text)

#########

def CountingFunction(Text,Pattern):
    if type(Text) is not list and type(Text) is not np.ndarray and type(Text) is not str:
        print ("Bad usage of this function: CountingFunction(Arr,Pat) Arr: must be a list or an array or string, Pat: must be a string")

        return 
    if type(Text) is str:
        MyArray=np.array(StripPunc(Text).split(" "))
    if type(Text) is list:
        MyArray=np.array(Text)
    if type(Text) is np.ndarray:
        MyArray=Text
    return np.count_nonzero(MyArray == Pattern)


Texto1 = "Muy lejos, más allá de las montañas de palabras, alejados de los países de las vocales y las consonantes, viven los textos simulados. Viven aislados en casas de letras, en la costa de la semántica, un gran océano de lenguas. Un riachuelo llamado Pons fluye por su pueblo y los abastece con las normas necesarias. Hablamos de un país paraisomático en el que a uno le caen pedazos de frases asadas en la boca. Ni siquiera los todopoderosos signos de puntuación dominan a los textos simulados; una vida, se puede decir, poco ortográfica. Pero un buen día, una pequeña línea de texto simulado, llamada Lorem Ipsum, decidió aventurarse y salir al vasto mundo de la gramática. El gran Oxmox le desanconsejó hacerlo, ya que esas tierras estaban llenas de comas malvadas, signos de interrogación salvajes y puntos y coma traicioneros, pero el texto simulado no se dejó atemorizar. Empacó sus siete versales, enfundó su inicial en el cinturón y se puso en camino. Cuando ya había escalado las primeras colinas de las montañas cursivas, se dio media vuelta para dirigir su mirada por última vez, hacia su ciudad natal Letralandia, el encabezamiento del pueblo Alfabeto y el subtítulo de su propia calle, la calle del renglón. Una pregunta retórica se le pasó por la mente y le puso melancólico, pero enseguida reemprendió su marcha. De nuevo en camino, se encontró con una copia. La copia advirtió al pequeño texto simulado de que en el lugar del que ella venía, la habían reescrito miles de veces y que todo lo que había quedado de su original era la palabra 'y', así que más le valía al pequeño texto simulado volver a su país, donde estaría mucho más seguro. Pero nada de lo dicho por la copia pudo convencerlo, de manera que al cabo de poco tiempo, unos pérfidos redactores publicitarios lo encontraron y emborracharon con Longe y Parole para llevárselo después a su agencia, donde abusaron de él para sus proyectos, una y otra vez. Y si aún no lo han reescrito, lo siguen utilizando hasta ahora.Muy lejos, más allá de las montañas de palabras, alejados de los países de las vocales y las consonantes, viven los textos simulados. Viven aislados en casas de letras, en la costa de la semántica, un gran océano de lenguas. Un riachuelo llamado Pons fluye por su pueblo y los abastece con las normas necesarias. Hablamos de un país paraisomático en el que a uno le caen pedazos de frases asadas en la boca. Ni siquiera los todopoderosos signos de puntuación dominan a los textos simulados; una vida, se puede decir, poco ortográfica. Pero un buen día, una pequeña línea de texto simulado, llamada Lorem Ipsum, decidió aventurarse y salir al vasto mundo de la gramática. El gran Oxmox le desanconsejó hacerlo, ya que esas tierras estaban llenas de comas malvadas, signos de interrogación salvajes y puntos y coma traicioneros, pero el texto simulado no se dejó atemorizar. Empacó sus siete versales, enfundó su"

Texto2 = "Una mañana, tras un sueño intranquilo, Gregorio Samsa se despertó convertido en un monstruoso insecto. Estaba echado de espaldas sobre un duro caparazón y, al alzar la cabeza, vio su vientre convexo y oscuro, surcado por curvadas callosidades, sobre el que casi no se aguantaba la colcha, que estaba a punto de escurrirse hasta el suelo. Numerosas patas, penosamente delgadas en comparación con el grosor normal de sus piernas, se agitaban sin concierto. - ¿Qué me ha ocurrido? No estaba soñando. Su habitación, una habitación normal, aunque muy pequeña, tenía el aspecto habitual. Sobre la mesa había desparramado un muestrario de paños - Samsa era viajante de comercio-, y de la pared colgaba una estampa recientemente recortada de una revista ilustrada y puesta en un marco dorado. La estampa mostraba a una mujer tocada con un gorro de pieles, envuelta en una estola también de pieles, y que, muy erguida, esgrimía un amplio manguito, asimismo de piel, que ocultaba todo su antebrazo. Gregorio miró hacia la ventana; estaba nublado, y sobre el cinc del alféizar repiqueteaban las gotas de lluvia, lo que le hizo sentir una gran melancolía. «Bueno -pensó-; ¿y si siguiese durmiendo un rato y me olvidase de todas estas locuras?» Pero no era posible, pues Gregorio tenía la costumbre de dormir sobre el lado derecho, y su actual estado no le permitía adoptar tal postura. Por más que se esforzara volvía a quedar de espaldas. Intentó en vano esta operación numerosas veces; cerró los ojos para no tener que ver aquella confusa agitación de patas, que no cesó hasta que notó en el costado un dolor leve y punzante, un dolor jamás sentido hasta entonces. - ¡Qué cansada es la profesión que he elegido! -se dijo-. Siempre de viaje. Las preocupaciones son mucho mayores cuando se trabaja fuera, por no hablar de las molestias propias de los viajes: estar pendiente de los enlaces de los trenes; la comida mala, irregular; relaciones que cambian constantemente, que nunca llegan a ser verdaderamente cordiales, y en las que no tienen cabida los sentimientos. ¡Al diablo con todo! Sintió en el vientre una ligera picazón. Lentamente, se estiró sobre la espalda en dirección a la cabecera de la cama, para poder alzar mejor la cabeza. Vio que el sitio que le picaba estaba cubierto de extraños untitos blancos. Intentó rascarse con una pata; pero tuvo que retirarla inmediatamente, pues el roce le producía escalofríos. Una mañana, tras un sueño intranquilo, Gregorio Samsa se despertó convertido en un monstruoso insecto. Estaba echado de espaldas sobre un duro caparazón y, al alzar la cabeza, vio su vientre convexo y oscuro, surcado por curvadas callosidades, sobre el que casi no se aguantaba la colcha, que estaba a punto de escurrirse hasta el suelo. Numerosas patas, penosamente delgadas en comparación con el grosor normal de sus piernas, se agitaban sin concierto. - ¿Qué me ha ocurrido? No estaba soñando. Su habitación, una habitación normal, aunque muy pequeña, tenía el aspecto habitual. Sobre la mesa había"

#Construccion de Diccionarios

import pandas

def DictsBuild(CSVFile,Debug=False):
    #df = pandas.read_csv('DiccionariosVersionDic1_2020.csv')
    df = pandas.read_csv(CSVFile)

    ListaDeAfectaciones = [7,8,9,10,11,13,14,15,16,17,18,19,20]
    Afectaciones = {}
    StringDeUso='Sinónimos-Palabras'
    if Debug:
        print(StringDeUso)
    for i in ListaDeAfectaciones:
        ListaDeAfects=df[StringDeUso][i].replace(", ", ",").split(",")
        Afectaciones[df['Nodos'][i]] = [x.strip() for x in ListaDeAfects if x]
    if Debug:
        print(Afectaciones)
    return Afectaciones

#Contadores de palabras
def contador(Texto,Diccionarios,ConStem=False):
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

#Lectura de docx

import docx

def getText(filename):#
    doc = docx.Document(filename)   #Abre el documento filename
    fullText = []                   #Lista vacía para ingresar el texto
    for para in doc.paragraphs:     #recorre los paragrafos del texto y los agruega en fulltext
        fullText.append(para.text)
    return '\n'.join(fullText)

def sumador(Dicc):      
    #INPUT: Recibe el diccionario que devuelve contador
    #OUTPUT: diccionario con el total de conteos por afectación. 
    total = {k:np.sum(v) for (k,v) in Dicc.items()}
    return total


def contador_stemming(Texto, Diccionarios):
    #Input y output igual a los de la función contador.
    Texto_stem = [spanish_stemmer.stem(word) for word in Texto.split()]
    
    Dicc_stem = {}
    for i in Diccionarios:
        Dicc_stem[i] = [spanish_stemmer.stem(expr) for expr in Diccionarios[i]]

    return contador(Texto_stem, Dicc_stem)

#########

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

ResultadoTexto1Stem = contador_stemming(Texto1.replace("a",Afects['Proyecto de vida'][6]), Afects)
print('\n Con Stem: \n Texto 1: \n', ResultadoTexto1Stem)
print('Total: \n', sumador(ResultadoTexto1Stem))


    Afects=DictsBuild('DiccionariosVersionDic1_2020.csv',Debug=False)
    ResultadoTexto1=contador(Texto1.replace("a",Afects['Proyecto de vida'][6]),Afects)
    print("Conteo del texto 1: \n", ResultadoTexto1)
    print("Total del conteo texto 1: \n", sumador(ResultadoTexto1),"\n")

    ResultadoTexto2=contador(Texto2.replace("a",Afects['Socioculturales'][4]),Afects)
    print("Conteo del texto 2: \n: ",ResultadoTexto2)
    print("Total del conteo del texto 2: \n",sumador(ResultadoTexto2))
    
    ResultadoTexto1Stem = contador_stemming(Texto1.replace("a",Afects['Proyecto de vida'][6]), Afects)
    print('\n Con Stem: \n Texto 1: \n', ResultadoTexto1Stem)
    print('Total: \n', sumador(ResultadoTexto1Stem))
    
    ResultadoTexto2Stem = contador_stemming(Texto2.replace("a",Afects['Socioculturales'][4]), Afects)
    print('\n Texto 2: \n', ResultadoTexto2Stem)
    print('Total: \n', sumador(ResultadoTexto2Stem))
