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
      
    for j in search(query, tld="co.in", num=2, stop=2, pause=2): 
        a.append(j) 

    check = False
    key  = ""
    i = 0
    key = a[0]
        
    
    webbrowser.open(key)


