# Дана строка-предложение на русском языке и число K (0 < K < 10). Зашифровать строку, выполнив циклическую замену каждой буквы на букву того же регистра, расположенную в алфавите на K-й позиции после шифруемой буквы (например, для K = 2 «А» перейдет в «В», «а» — в «в», «Б» — в «Г», «я» — в «б» и т. д.). Букву «ё» в алфавите не учитывать, знаки препинания и пробелы не заменять.
def encrypt_sentence(sentence, K):
    # Пишем русский алфавит без буквы "ё" 
    lowercase = "абвгдежзийклмнопрстеуфхцчшщъыьэюя"
    capitalletters = lowercase. upper()
