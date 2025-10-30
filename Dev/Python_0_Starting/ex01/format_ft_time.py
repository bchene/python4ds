import time as t

s = t.time()
print(f"Seconds since January 1, 1970: {s:,.4f} or {s:.2e} \
in scientific notation")
print(t.strftime("%b %d %Y", t.localtime()))
