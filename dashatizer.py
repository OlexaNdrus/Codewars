def dashatize(num):
    if num==None:
        return 'None'
    elif num==0:
        return '0'
    num=str(abs(num))
    if len(num)>1:
        dash=[num[0]]
        if int(num[0])%2!=0:
            dash.append('-')
        for i in num[1:-1]:
            if int(i)%2!=0 and int(i):
                if dash[-1]!='-':
                    dash.append('-')
                dash.append(i)
                dash.append('-')
            else:
                dash.append(i)
        if int(num[-1])%2!=0 and dash[-1]!='-' and int(num[-1]):
            dash.append('-')
        dash.append(num[-1])
    else:
        return num
    return ''.join(dash)

print(dashatize(input()))