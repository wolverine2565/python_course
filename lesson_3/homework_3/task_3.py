OneScore = {'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'}
TwoScore = {'D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'}
ThreeScore = {'B', 'C','M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'}
FourScore = {'F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'}
FiveScore = {'K', 'Ж', 'З', 'Х', 'Ц', 'Ч'}
EightScore = {'J', 'X', 'Ш', 'Э', 'Ю'}
TenScore = {'Q', 'Z', 'Ф', 'Щ', 'Ъ'}

def ScoreCounter(word):
    score = 0
    LettersArr = [char for char in str.upper(word)]
    for letter in LettersArr:
        if letter in OneScore:
            score += 1
        elif letter in TwoScore:
            score += 2
        elif letter in ThreeScore:
            score += 3
        elif letter in FourScore:
            score += 4
        elif letter in FiveScore:
            score += 5
        elif letter in EightScore:
            score += 8
        elif score in TenScore:
            score += 10

    return(score)
    
print(ScoreCounter(input()))