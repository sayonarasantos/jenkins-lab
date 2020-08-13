from datetime import datetime

def main():
    print '############# Hello Wold #############'
    currentTime = datetime.now().strftime("%H:%M:%S")
    
    fileTxt = open("fileTest.txt","a+")
    fileTxt.write("\n "+currentTime)

    fileTxt.seek(0)
    print fileTxt.read()

    fileTxt.close()

if __name__ == '__main__':
    main()