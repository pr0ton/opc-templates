#!/usr/bin/env python

import sys
if __name__ == "__main__":
  args = sys.argv[1:]
  fileName =  'template.cpp' if args[0] == 'cpp' else 'template.java'
  libs = args[1:]
  
  with open(fileName) as f:
    code = f.read()
    (startFrag, endFrag) = code.split('//37ae83cb1254dc6d8f3f075ebd91cb')
    
    print startFrag[:-1]
    for lib in libs:
      with open(lib + '.' + args[0]) as libf:
        print libf.read()
    print endFrag[1:]
  # for lib in libs:
    

  
