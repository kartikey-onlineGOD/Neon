import urllib as ur
import webbrowser


def Search( sch ):
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
      
    # to search 
    query = sch
    a =[]
      
    for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
        a.append(j) 
    check = False
    i = 0
    key =""
    while check == False :
        if(a[i].find("youtube") >= 1):
            key = a[i]
            break
        i = i +1
        

    webbrowser.open(key)

Search("Beliver")
