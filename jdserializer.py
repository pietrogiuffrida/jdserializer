#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

def jdserializer(obj):
  """JSON datetime serializer for objects not serializable by default json code"""
  
  if isinstance(obj, (datetime,)):
    return obj.strftime('%Y%m%d %H%M%S')
  raise TypeError ("Type %s not serializable" % type(obj))
