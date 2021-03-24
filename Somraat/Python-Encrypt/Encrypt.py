import os, base64, zlib, marshal, sys
W = '\x1b[1;37m'
RR = '\x1b[1;37m\x1b[31m'
O = '\x1b[1;33m'
B = '\x1b[1;34m'
G = '\x1b[1;32m'
N = '\x1b[1;36m'
os.system('clear')
os.system('figlet -f mini ENCRYPT PYTHON CODE')
print '    Created By HackerFake424 YouTube Channel'
print ('\n{}-=[+]=- {}Menu Encrypt -=[+]=-\n\t\n{}[{}01{}]{} Endcrypt file with base64\n{}[{}02{}]{} Endcrypt file with base64.16\n{}[{}03{}]{} Endcrypt file with base64.32\n{}[{}04{}]{} Endcrypt file with marshal\n{}[{}05{}]{} Endcrypt file with zlib&base64\n{}[{}06{}]{} Endcrypt file with zlib&base64&marshal\n{}[{}07{}]{} Endcrypt file with zlib&base16&marshal\n{}[{}08{}]{} Endcrypt file with zlib&base32&marshal\n{}[{}09{}]{} Exit tool\n{}[{}10{}]{} Programer info\n').format(W, W, B, W, B, B, B, W, B, B, B, W, B, B, B, W, B, B, B, W, B, B, B, W, B, B, B, W, B, B, B, W, B, B, B, W, B, B, B, W, B, B, W, W, W)

def main():
    choice = raw_input(RR + '[++ ' + B + 'Choose: ' + W)
    if choice == '1' or choice == '01':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            a = base64.b64encode(fileopen)
            b = "import base64\nexec(base64.b64decode('" + a + "'))"
            c = file.replace('.py', '_endcrypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print RR + '[*] ' + W + 'OUTPUT:', c
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()

    if choice == '2' or choice == '02':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            a = base64.b16encode(fileopen)
            b = "import base64\nexec(base64.b16decode('" + a + "'))"
            c = file.replace('.py', '_endcrypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print RR + '[*] ' + W + 'OUTPUT:', c
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()

    if choice == '3' or choice == '03':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            a = base64.b32encode(fileopen)
            b = "import base64\nexec(base64.b32decode('" + a + "'))"
            c = file.replace('.py', '_endcrypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print RR + '[*] ' + W + 'OUTPUT:', c
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()

    if choice == '4' or choice == '04':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            a = compile(fileopen, 'dg', 'exec')
            m = marshal.dumps(a)
            s = repr(m)
            b = 'import marshal\nexec(marshal.loads(' + s + '))'
            c = file.replace('.py', '_endcrypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print RR + '[*] ' + W + 'OUTPUT:', c
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()

    if choice == '5' or choice == '05':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            c = zlib.compress(fileopen)
            d = base64.b64encode(c)
            e = 'import marshal,zlib,base64\nexec(zlib.decompress(base64.b64decode("' + d + '")))'
            f = file.replace('.py', '_endcrypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print RR + '[*] ' + W + 'OUTPUT:', f
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()

    if choice == '6' or choice == '06':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            sa = compile(fileopen, 'dg', 'exec')
            sb = marshal.dumps(sa)
            c = zlib.compress(sb)
            d = base64.b64encode(c)
            e = 'import marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("' + str(d) + '"))))'
            f = file.replace('.py', '_endcrypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print RR + '[*] ' + W + 'OUTPUT:', f
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()

    if choice == '7' or choice == '07':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            sa = compile(fileopen, 'dg', 'exec')
            sb = marshal.dumps(sa)
            c = zlib.compress(sb)
            d = base64.b16encode(c)
            e = 'import marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b16decode("' + str(d) + '"))))'
            f = file.replace('.py', '_endcrypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print RR + '[*] ' + W + 'OUTPUT:', f
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()

    if choice == '8' or choice == '08':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            sa = compile(fileopen, 'dg', 'exec')
            sb = marshal.dumps(sa)
            c = zlib.compress(sb)
            d = base64.b32encode(c)
            e = 'import marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b32decode("' + str(d) + '"))))'
            f = file.replace('.py', '_endcrypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print RR + '[*] ' + W + 'OUTPUT:', f
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()

    if choice == '9' or choice == '09':
        sys.exit(RR + '[*] ' + W + 'bye bye!1!1')
    elif choice == '10':
        print "          %sINFORMATION%s------------------------------------------------------\nCreator   :Md.SomRaAt Hossain[Black Hacker]\nYouTube   :HackerFake424\nSupport   :BD Cyber Hacker TeM'\nGitHub  :https://github.com/StHackerFake424\nFacebook  :fb.com/md.somraat.hossain.2\nTwitter   :twitter.com/hackerfake424\nInstagram :instagram.com/md.somraat.hossain.2\nThanks for useing my tool..\n[InFo] if you find any errors or problems   please contact creator------------------------------------------------------"
        main()
    else:
        print RR + '[-] ' + W + 'WRONG INPUT!!'
        sys.exit(RR + '[*] ' + W + 'bye try agin!1!1')


if __name__ == '__main__':
    main()
