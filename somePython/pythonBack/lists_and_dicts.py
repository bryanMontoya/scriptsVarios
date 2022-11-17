def run():
    list = [1, "Hola", True, 4.5]
    dict = {'firstname' : 'brayan','lastname' : 'montoya'}

    superList = [
        {'firstname' : 'brayan1','lastname' : 'montoya1'},
        {'firstname' : 'brayan2','lastname' : 'montoya2'},
        {'firstname' : 'brayan3','lastname' : 'montoya3'}
    ]
    superDict = {
        'naturalNums' : [1,2,4,5],
        'integerNums' : [0,-1,-2],
        'floatingNums': [1.2,4.5,6.7]
    }

    for key, value in superDict.items():
        print(key, "-", value)
    
    for i in superList:
	    print(i.items())


if __name__ == '__main__':
    run()

