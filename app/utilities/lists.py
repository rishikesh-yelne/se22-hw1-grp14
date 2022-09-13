""" Lua code
-- ### Lists
local copy,per,push,csv
-- deepcopy
function copy(t,    u)
  if type(t) ~= "table" then return t end
  u={}; for k,v in pairs(t) do u[k] = copy(v) end
  return setmetatable(u,getmetatable(t))  end

-- Return the `p`-th thing from the sorted list `t`.
function per(t,p)
  p=math.floor(((p or .5)*#t)+.5); return t[math.max(1,math.min(#t,p))] end

-- Add to `t`, return `x`.
function push(t,x) t[1+#t]=x; return x end

-- Call `fun` on each row. Row cells are divided in `the.seperator`.
function csv(fname,fun,      sep,src,s,t)
  sep = "([^" .. the.seperator .. "]+)"
  src = io.input(fname)
  while true do
    s = io.read()
    if not s then return io.close(src) else
      t={}
      for s1 in s:gmatch(sep) do t[1+#t] = coerce(s1) end
      fun(t) end end end
"""
# TODO: Write python for above code


import math
from copy import deepcopy
import csv
from app.utilities.settings import coerce


def per(t, p=0.5):
    p = math.floor(p * len(t))
    return t[max(1, min(len(t), p))]

def copy(t):
	if type(t) is not dict:
		return t
	t_copy = deepcopy(t)
	return t_copy

def csv_func(fname, fun, n):
    with open(fname, mode='r')as file:
        s = list(csv.reader(file))

    for i in range(len(s)):
        t = []
        for word in s[i]:
            t.append(coerce(word))
        fun(t, n)
