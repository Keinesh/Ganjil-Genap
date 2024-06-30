import datetime

def main():
    date = datetime.datetime.now()
    x = int(date.strftime("%d"))
    if x % 2 == 0:
        print("Genap")
    else:
        print("Ganjil")

if __name__ == "__main__":
    main()
