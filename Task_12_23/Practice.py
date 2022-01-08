import os


# 1 . you have to write a fun which will take string and return a len of it without using inbuilt fun len


def length(s):
    """This Fun return length of given
    string/tuple/set/list/dict."""
    counter = 0
    for _ in s:
        counter += 1
    return counter


length({"R": "rajesh", "k": "kumar"})


# 2 . write a fun which will be able to print an index of all primitive element which you will pass


def PrintIndex(x):
    """This fun return index of which you will pass."""
    for i in range(len(x)):
        print(x[i], i)


PrintIndex("rajesh")


# 3 . Write a fun which will take input as a dict and give me out as a list of all the values
# even in case of 2 level nesting it should work .

def NestedDictValues(d):
    """This fun return value of dict"""
    if type(d) == dict:
        for v in d.values():
            if isinstance(v, dict):
                yield from NestedDictValues(v)
            else:
                yield v
    else:
        return "Please enter Dict"


list(NestedDictValues({"R": "rajesh", "K": "kumar", "J": {"A": {"i": 20, "K": 30}, "B": 30}}))


# 4 . write a fun which will take another function as an input and return me an output

def add(a, b):
    """This fun return sum of both given number"""
    return a + b


def mult(a, b):
    """This Fun return multiply of given number"""
    return a * b


def add_and_mult(a, b):
    """This fun first add and multiply then return sum of added and multiply number"""
    added = add(a, b)
    multed = mult(a, b)
    return add(added, multed)


add_and_mult(5, 10)


# 5. write a function which will take multiple list as input and give me concatenation of all the element as
# and output
def ConcatList(*lists):
    """This function return concatenation list of given list"""
    new_list = []
    for i in lists:
        new_list.extend(i)
    return new_list


list2 = [1, 2, 3, 5, 6, 8]
list3 = [5, 7, 8, 9, 12, 25]
ConcatList(list2, list3)


# 6 . write a function which will be able to take a list as an input return an index of each element
# like  inbuilt index function but even if we have repetitive element it should return index


def getIndex(x, l1):
    """This Fun return index of given element"""
    for i, j in enumerate(l1):
        if j == x:
            print(i)


list1 = [1, 2, 3, 3, 5]
getIndex(3, list1)

# 7 . Write a function which will would return list of all the file name from a directory .


folderPath = os.getcwd()


def ReturnList():
    import os
    """This fun return list of given path"""
    return [os.path.join(path, name) for path, subdir, files in os.walk(folderPath) for name in files]


ReturnList()


# 8  . write a function which will be able to show your system configuration .


def GetSysInfo():
    """This Function return system info"""
    import subprocess
    id_name = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []
    for item in id_name:
        new.append(str(item.split("\r")[:-1]))
    for i in new:
        print(i[2:-2])


GetSysInfo()


# 9 . write a function which will be able to show date and time


def GetDateTime():
    """Return date and time"""
    import datetime
    now = datetime.datetime.now()
    print("Current date and time : ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


GetDateTime()


# 10 . write a function which will be able to read  image file and show it to you .

def ShowImage(image_path):
    """This fun show image of given path"""
    from PIL import Image
    img = Image.open(image_path)
    img.show()


image_name = "image.jpg"
ShowImage(image_name)


# 11 . write a function which can read video file and play for you .


def ReadPlay(filename):
    """this function read and play given video file and press q for exit"""
    import cv2
    file = cv2.VideoCapture(filename)

    if not file.isOpened():
        print("Error opening video file")
    while file.isOpened():
        ret, frame = file.read()
        if ret:
            cv2.imshow("Frame", frame)
            if cv2.waitKey(25) == ord("q"):
                break
        else:
            break
    file.release()
    cv2.destroyAllWindows()


ReadPlay("Sample.mp4")


# 12  . write a function which can move a file from one directory to another directory .
def MoveFile(source_folder, destination_folder):
    """This function used to move file from one to other destination"""
    import os
    import shutil
    all_file = os.listdir(source_folder)
    for file in all_file:
        shutil.move(source_folder + file, destination_folder + file)


source = "D:\\Data_Science\\Ineuron_pycharm\\source\\"
destination = "D:\\Data_Science\\Ineuron_pycharm\\destination\\"

MoveFile(source, destination)
# 13 . write a function which will be able to shut down your system .


def ShutDown():
    """This function make shutdown system within 5 s"""
    import os
    shutdown = input("If you want to shut down your system? Yes Or NO : ")
    if shutdown.lower() == "no":
        exit()
    else:
        os.system("shutdown /s /t 5")


ShutDown()


# 16. write a func to read a complete PDf file .
def ReadPdfFile(file_name):
    """This function return given pdf to line by line"""
    import PyPDF2
    pdf_file = open(file_name, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    page_obj = pdf_reader.getPage(0)
    print(page_obj.extractText())
    pdf_file.close()


ReadPdfFile("sample-pdf-file.pdf")


# 18 . write a function which can help you to filter only word file from a directory .
def FilterByExtension(extension_name, path):
    """This function return list of filter file by given extension"""
    import os
    import fnmatch
    file = fnmatch.filter(os.listdir(path), f"*.{extension_name}")
    print(file)


file_path = os.getcwd()
FilterByExtension("pdf", file_path)


# 19 . write a function by which you can print an ip address of your system .


def GetIp():
    """This function return Ip Address"""
    import socket
    hostname = socket.gethostname()
    ipaddr = socket.gethostbyname(hostname)
    print(f"your computer name is : {hostname}")
    print(f"Your computer Ip Address is : {ipaddr}")


GetIp()


# 20 . write a function by which you will be able to append two PDF files.
def MergePdf(*pdf):
    """This Function return Merge pdf file"""
    import PyPDF2
    combine = PyPDF2.PdfFileMerger()
    for file in pdf:
        combine.append(file, 'rb')
    combine.write("MergePDF.pdf")


MergePdf("sample.pdf", "sample-pdf-file.pdf")
