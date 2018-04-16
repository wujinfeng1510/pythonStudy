def trim(strIn):
    ''' trim used delete space at the beginning and at the end of str 
    用来删除字符串开始和结尾的空格'''
    length=len(strIn)
    if length==0:
        return ''
    i=0
    j=length-1
    while(strIn[i]==' '):
        i+=1
        if i>j:
            return ''
    while(strIn[j]==' '):
        j-=1
    return(strIn[i:j+1])

def testTrim():
    ''' used to test trim function '''
    print(trim("   hello wujf "))
    if trim('hello  ') != 'hello':
        print('测试失败1!')
    elif trim('  hello') != 'hello':
        print('测试失败2!')
    elif trim('  hello  ') != 'hello':
        print('测试失败3!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败4!')
    elif trim('') != '':
        print('测试失败5!')
    elif trim('    ') != '':
        print('测试失败6!')
    else:
        print('测试成功!')