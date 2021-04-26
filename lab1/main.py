import numpy as np

FILENAME = "input.txt"

def loadData(fileName: str):
   """
   Загрузить входные данные из файла

   :param fileName: имя файла

   :returns
      matrix: таблица стратегий
      probs: список вероятностей Пj
   """

   matrix = []
   with open(fileName, 'r') as file:
      for line in file:
         matrix.append(list(map(float, line.split())))

   probs = matrix[-1]
   matrix = matrix[:-1]

   return np.array(matrix), probs

def getStrFromNumber(number):
   temp = str(number)
   while len(temp) < 8:
      temp += ' '
   return temp

def getMoreSpaces(msg: str):
   while len(msg) < 12:
      msg += ' '
   return msg
e
def printMatrix(matrix, len, isGurvic=False, isProbs=False, isVald=False, isSavidge=Fals):
   """Красивая печать таблицы"""

  # print('\t', end='')
  # for i in range(len):
  #    print(getMoreSpaces('П{}'.format(i+1)), end='')

  # if isGurvic:
  #    print('min' + ' ' * 9 + 'max' + ' ' * 9 + 'H_i', end='')
  # elif isProbs:
  #    print('r_i', end='')
  # elif isVald:
  #    print('x_min', end='')
  # elif isSavidge:
  #    print('x_max', end='')

  #for i, line in enumerate(matrix):
  #   print('\nА{}'.format(i+1), end='\t')
  #   for element in line:
  #      print(getStrFromNumber(element), end='\t')

  # print('\n')

def makeRiskMatrix(matrix):
   """
   Создать матрицу рисков
   :param matrix: таблица стратегий
   :return risk: таблица рисков
   """

   # транспонирование матрицы для удобного вычисления
   matrix = np.array(matrix)
   tMatrix = matrix.T
   riskMatrix = np.array(tMatrix)

   # в каждой строке находим максимум
   # затем отнимаем от максимума каждый элемент строки
   for i, row in enumerate(tMatrix):
      maxEl = max(row)
      for j, curEl in enumerate(row):
         riskMatrix[i][j] = maxEl - curEl

   # транспонируем обратно, чтобы вернуть исходный вид
   return riskMatrix.transpose()

def getNumberAndPrintResult(curValue, list):
   result = []
   for i, value in enumerate(list):
      if value == curValue:
         #print('Стратегия А{} является оптимальной'.format(i+1))
         result.append(i+1)

   return result


# Критерий по вероятностям
def probsCriterion(riskMatrix, probs):
   #print('\nКритерий, основанный на известных вероятностях:')

   rAVG = []
   # вычисляем средний риск для r_i
   for row in riskMatrix:
      rAVG.append(sum([Qj * Rij for Qj, Rij in zip(row, probs)]))

   # минимизируем математическое ожидание риска
   rMin = min(rAVG)

   # формируем матрицу для наглядного отображения решения
   newMatrix = []
   for i, row in enumerate(riskMatrix):
      newRow = []
      for el in row:
         newRow.append(el)
      newRow.append(rAVG[i])
      newMatrix.append(newRow)

   printMatrix(newMatrix, len(riskMatrix[0]), isProbs=True)
   #print('Минимальное значение в столбце r_i: ', rMin, ' => ')


   # вычислить номер стратегии
   # печать результата на экран
   return getNumberAndPrintResult(rMin, rAVG)


def ValdCriterion(matrix):
   #print('\nКритерий Вальда:')

   # поиск минимумов
   mins = []
   for row in matrix:
      mins.append(min(row))

   # выбор максимального из минимального
   maximin = max(mins)

   # формируем матрицу для наглядного отображения решения
   newMatrix = []
   for i, row in enumerate(matrix):
      newRow = []
      for el in row:
         newRow.append(el)
      newRow.append(mins[i])
      newMatrix.append(newRow)

   printMatrix(newMatrix, len(matrix[0]), isVald=True)
   #print('Максимум среди минимумов в столбце x_min: ', maximin, ' => ')

   # вычислить номер стратегии
   # печать результата на экран
   return getNumberAndPrintResult(maximin, mins)


def SavidgeCriterion(riskMatrix):
   #print('\nКритерий Сэвиджа:')
   # поиск максимальных рисков
   maxs = []
   for row in riskMatrix:
      maxs.append(max(row))

   # выбор минимального риска
   minmax = min(maxs)

   # формируем матрицу для наглядного отображения решения
   newMatrix = []
   for i, row in enumerate(riskMatrix):
      newRow = []
      for el in row:
         newRow.append(el)
      newRow.append(maxs[i])
      newMatrix.append(newRow)

   printMatrix(newMatrix, len(riskMatrix[0]), isSavidge=True)
   #print('Минимальный среди максимумов в столбце x_max: ', minmax, ' => ')

   return getNumberAndPrintResult(minmax, maxs)

def bestResultGurvic(matrix, mins, maxs, Hi, value):
   """
   сформировать матрицу для вывода шага решения и печать результата

   """

   # формируем красивую матрицу
   newMatrix = []
   for i, row in enumerate(matrix):
      newRow = []
      for el in row:
         newRow.append(el)
      newRow.append(mins[i])
      newRow.append(maxs[i])
      newRow.append((Hi[i]))
      newMatrix.append(newRow)

   # печатаем матрицу
   printMatrix(newMatrix, len(matrix[0]), isGurvic=True)

   # запоминаем индексы оптимальных стратегий
   indexes = []
   for i, item in enumerate(Hi):
      if item == value:
         indexes.append(i)

   result = []
   #print('Искомое (мин или макс) значение в столбце H_i: ', value, ' => ')
   for index in indexes:
      #print(' * стратегия A{} является оптимальной'.format(index + 1))
      result.append(index + 1)

   return result

def GurvicCriterion(matrix: list, E):
   #print('\nКритерий Гурвица (коэф = {}):'.format(E))
   # вычисление минимумов и максимумов
   mins = list(map(lambda row: min(row), matrix))
   maxs = list(map(lambda row: max(row), matrix))

   # считаем по формуле исходя из выигрыша
   Hi = [mi+ma for mi, ma in zip(map(lambda x: E * x, mins), map(lambda x: (1 - E) * x, maxs))]
   N = max(Hi)

   return bestResultGurvic(matrix, mins, maxs, Hi, N)


def gurvicRisk(riskMatrix, L):
   #print('\nКритерий Гурвица через риск (коэф = {}):'.format(L))
   # вычисление минимумов и максимумов
   maxs = list(map(lambda row: max(row), riskMatrix))
   mins = list(map(lambda row: min(row), riskMatrix))

   # считаем по формуле исходя из риска
   Hi = [ma+mi for ma, mi in zip(map(lambda x: L * x, maxs), map(lambda x: (1 - L) * x, mins))]
   D = min(Hi)

   return bestResultGurvic(riskMatrix, mins, maxs, Hi, D)

def main():
   # загрузить таблицу стратегий и вероятности
   matrix, probs = loadData(FILENAME)
   #('Таблица стратегий:')
   printMatrix(matrix, len(matrix[0]))

   #print('Вероятности Пj: ', probs)


   # вычисление матрицы рисков
   riskMatrix = makeRiskMatrix(matrix)
   #print('\nМатрица рисков:')
   printMatrix(riskMatrix, len(riskMatrix[0]))

   # заданные коэф-ты для Гурвица
   E = 0.5
   L = 0.5

   # применение всех реализованных методов
   probsCriterion(riskMatrix, probs)
   ValdCriterion(matrix)
   SavidgeCriterion(riskMatrix)
   GurvicCriterion(matrix, E)
   gurvicRisk(riskMatrix, L)
