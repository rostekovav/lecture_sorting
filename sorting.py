import os
import csv



def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)

    with open (file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))

    return data

def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_idx = i
        for j in range(i +1, n): #nejdem uplne od zaciaktu ale od toho cisla ktore som este nezoradovala
            if numbers[j] < numbers[min_idx]:
                min_idx = j #minimum nahradim aktualnzm cislom
        #if min_idx != i:
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i] #prehodi prvky
    return numbers

def bubble_sort(zoznam):
    n = len(zoznam)
    for i in range(n):
        for j in range(0, n - i - 1):  # nejdem uplne od zaciaktu ale od toho cisla ktore som este nezoradovala
            if zoznam[j] > zoznam[j + 1]:
                zoznam[j], zoznam[j +1 ] = zoznam[j +1 ], zoznam[j] # prehodi prvky
    return zoznam

def insertion_sort(seznam):
    for i in range(1, len(seznam)):
        kluc = seznam[i]
        j = i -1
        while j >= 0 and seznam[j] > kluc:
            seznam[j + 1] = seznam[j]
            j -= 1
            seznam[j +1] = kluc
    return seznam

def main():
    nactene_sekvence = read_data("numbers.csv")
    print(nactene_sekvence)

    zoradene = selection_sort([33,12,8,27,15,1,4,66,128])
    print(zoradene)

    bubble = bubble_sort([33,12,8,27,15,1,4,66,128,15])
    print(bubble)

    tretie_radenie = insertion_sort([8,13,5,13,25,31,60,100])
    print(tretie_radenie)


if __name__ == '__main__':
    main()
