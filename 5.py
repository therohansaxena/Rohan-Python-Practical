try:    
    fileptr = open("file.txt","r")    
except IOError:    
    print("File not found")    
else:    
    print("The file opened successfully")    
    fileptr.close()    