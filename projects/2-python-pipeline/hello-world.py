from datetime import datetime


def main():
    print('############# Hello Wold #############')
    current_time = datetime.now().strftime('%H:%M:%S')
    
    text_file = open('fileTest.txt','a+')
    text_file.write('\n '+current_time)

    text_file.seek(0)
    print(text_file.read())

    text_file.close()


if __name__ == '__main__':
    main()
