#!/usr/bin/env python 
import os
cmd = os.system('sudo yum update -y')
if cmd == 0:
   print 'Sucess'
else:
  print 'Something wroung'
