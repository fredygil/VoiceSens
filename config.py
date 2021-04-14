import os
import sys

# recognize speech using IBM Speech to Text
try:
    APIKEY = os.environ["APIKEY"] 
except:
    print("Error, APIKEY environment variable is not defined")
    sys.exit(1)
    
try:
    URL = os.environ["URL"] 
except:
    print("Error, URL environment variable is not defined")
    sys.exit(1)
