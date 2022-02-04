#!/usr/bin/env python
# coding: utf-8

# In[1]:


import collections


# In[2]:


def generate_zipf_table(text, top):

    """
    Crear una lista de diccionarios con las palabras más
    palabras más frecuentes, sus frecuencias y
    otros datos zipfianos.
    """

    text = _remove_punctuation(text)

    text = text.lower()

    top_word_frequencies = _top_word_frequencies(text, top)

    zipf_table = _create_zipf_table(top_word_frequencies)

    return zipf_table


def _remove_punctuation(text):

    """
       Elimina los caracteres:
        !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789
        del texto.
    """

    chars_to_remove = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789"

    tr = str.maketrans("", "", chars_to_remove)

    return text.translate(tr)


def _top_word_frequencies(text, top):

    """
    Crear una lista de tuplas que contenga las palabras 
    más frecuentes y sus frecuencias en orden descendente.
    
    """

    # Sin argumento, split() separa la cadena
    # por 1 o más instancias consecutivas de espacios en blanco.
    words = text.split()

    # Crear una colección. Contardor instancia de un
    # iterable, en este caso nuestra lista de palabras.
    word_frequencies = collections.Counter(words)

    # most_common() nos da una lista de tuplas
    # que contenga palabras y sus frecuencias,
    # en orden descendente de frecuencia.
    top_word_frequencies = word_frequencies.most_common(top)

    return top_word_frequencies


def _create_zipf_table(frequencies):

    """
    Toma la lista creada por _top_word_frequencies
    y la inserta en una lista de diccionarios
    junto con los datos de Zipfian.
    """

    zipf_table = []

    top_frequency = frequencies[0][1]

    for index, item in enumerate(frequencies, start=1):

        relative_frequency = "1/{}".format(index)
        zipf_frequency = top_frequency * (1 / index)
        difference_actual = item[1] - zipf_frequency
        difference_percent = (item[1] / zipf_frequency) * 100

        zipf_table.append({"word": item[0],
                           "actual_frequency": item[1],
                           "relative_frequency": relative_frequency,
                           "zipf_frequency": zipf_frequency,
                           "difference_actual": difference_actual,
                           "difference_percent": difference_percent})

    return zipf_table


def print_zipf_table(zipf_table):

    """
    Imprime la lista creada por generate_zipf_table
    en formato de tabla con encabezados de columna.
    """

    width = 80

    print("-" * width)
    print("|Rank|    Word    |Actual Freq | Zipf Frac  | Zipf Freq  |Actual Diff |Pct Diff|")
    print("-" * width)

    format_string = "|{:4}|{:12}|{:12.0f}|{:>12}|{:12.2f}|{:12.2f}|{:7.2f}%|"

    for index, item in enumerate(zipf_table, start=1):

        print(format_string.format(index,
                                   item["word"],
                                   item["actual_frequency"],
                                   item["relative_frequency"],
                                   item["zipf_frequency"],
                                   item["difference_actual"],
                                   item["difference_percent"]))

    print("-" * width)


# In[ ]:




