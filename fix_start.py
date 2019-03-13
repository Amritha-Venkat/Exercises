def fix_start(s):
    first = s[0]
    new_string = s[1:]
    return first + new_string.replace("b",'*')
if __name__=='__main__':
    print(fix_start("babble"))