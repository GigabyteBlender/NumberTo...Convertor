class ConvertToRoman:
    def __init__(self):
        self.characters = {1:'I',5:'V',10:'X',50:'L',100:'C',1000:'M'}
    def Convert(self):
        decimal = int(input('Enter the number to convert'))
        decimal = str(decimal)
        
        for x in enumerate(decimal):
            print(x)

if __name__ == '__main__':
    main = ConvertToRoman()
    main.Convert()
    