
import bot

def test():
    array = []
    fn = 'test.py'
    with open(fn, 'r') as f:
        for line in f:
            str = line.replace('\n','')
            if str != '':
                print str
                array.append(line.replace('\n',""))

    fn = 'wxemoji.em'
    with open(fn, 'w') as f:
        for i in range(0,(len(array)/2),2):
            f.write(array[i+1]+","+array[i])
            f.write('\n')

bb = bot.Bot()