import re
list4 = ["으로부터"]
list3 = ["이라서"]
josa1 = ["가" ,"고" ,"과","나" ,"는" ,"니" ,"다" ,"도" ,"든" ,"라" ,"랑" ,"를" ,"만","며" ,"아" ,"야" ,"에" ,"엔" ,"엘" ,"여" ,"와" ,"요" ,"은" ,"을" ,"의" ,"이"]
josa2 = ["같이","같인","라면","과는","과도","과를","과만","과의","까지","까진","나마","는야","다가","다간","대로","더러","든지","라고","라곤","라도","라서","라야","라오","라지","랑은","로고","로군","로다","로되","로세","마다","마저","만도","만에","만은","만을","만의","만이","만치","만큼","말고","밖에","밖엔","보고","보곤","보다","보단","부터","부턴","에게","에겐","에나","에는","에다","에도","에든","에로","에를","에만","에서","에선","에야", "에의", "엔들", "엘랑" ,"와는" ,"와도" ,"와를" ,"와만" ,"와의" ,"으로" ,"으론" ,"이고" ,"이나" ,"이니" ,"이다" ,"이든" ,"이라" ,"이랑" ,"이며" ,"이야" ,"이여" ,"인들" ,"인즉" ,"일랑" ,"조차" ,"처럼" ,"치고" ,"커녕" ,"토록" ,"하고" ,"하곤"]
def func1(list):
    josa = list[-1:]

    if (josa in josa1):

        return list[0:-1]
    else:
        return 0

def func2(list):
    josa = list[-2:]

    if (josa in josa2):

        return list[0:-2]
    else:
        return 0


def func3(list):
    josa = list[-3:]

    if (josa in list3):
        return list[0:-3]
    else:
        return 0

def func4(list):
    josa = list[-4:]

    if (josa in list4):
        return list[0:-4]
    else:
        return 0


def sentence_to_word():
    f = open("synopsis.txt", 'r')
    document = ""
    lines = f.readlines()
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    for line in lines:
        line = hangul.sub('', line)
        document += line
        line = line.strip()


    tokens = document.split()
    token_len = len(tokens)
    for i in range(token_len):
        if(tokens[i][0] == "있"):
            tokens[i] = '#'
    tokens = list(set(tokens))
    tokens.remove('#')
    return tokens

def create_Bow(sen_list):
    bow_dict = {}
    bow = []
    idx=0
    for s in sen_list:
        if s not in bow_dict:
            bow_dict[s] = idx
            bow.insert(idx,1)
            idx=idx+1
        else:
            i = bow_dict.get(s)
            bow[i] = bow[i]+1

    return bow_dict, bow

list = sentence_to_word()

list_len = len(list)

for i in range(list_len):

    length = len(list[i])

    if (length == 3):
        temp = func2(list[i])
        if (temp):
            list[i] = temp
            continue
        temp = func1(list[i])
        if (temp) :
            list[i] = temp
            continue
    elif (length == 4):
        temp = func3(list[i])
        if (temp):
            list[i] = temp
            continue
        temp = func2(list[i])
        if (temp):
            list[i] = temp
            continue
        temp = func1(list[i])
        if (temp):
            list[i] = temp
            continue
    elif (length > 4) :
        temp = func4(list[i])
        if (temp) :
            list[i] = temp
            continue
        temp = func3(list[i])
        if (temp) :
            list[i] = temp
            continue
        temp = func2(list[i])
        if (temp) :
            list[i] = temp
            continue
        temp = func1(list[i])
        if (temp):
            list[i] = temp
            continue

r_dict, r_bow = create_Bow(list)

for key, value in r_dict.items():
    if(r_bow[value] > 10):
        print(key)


print(max(r_bow))


