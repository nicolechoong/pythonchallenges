letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
final=""

enorde=str(input("ENCODE OR DECODE\n   >"))

if str.lower(enorde) in ('encode','e'):
    text=str(input("\nUNCODED TEXT\n   >"))
    key=int(input("\nINSERT SHIFT KEY\n   >"))
    for i in range(0,len(text)):
        x=-1
        while True:
            x=x+1
            if text[i]==letter[x]:
                final+=letter[(x%26)+key]
                break
            else:
                if text[i] in (" "):
                    final+=" "
                    break
    print("\n"+final)

if str.lower(enorde) in ('decode','d'):
    text=str(input("\nCODED TEXT\n   >"))
    key=int(input("\nINSERT SHIFT KEY\n   >"))
    for i in range(0,len(text)):
        x=-1
        while True:
            x=x+1
            if text[i]==letter[x]:
                final+=letter[(x%26)-key]
                break
            else:
                if text[i] in (" "):
                    final+=" "
                    break
    print("\n"+final)
