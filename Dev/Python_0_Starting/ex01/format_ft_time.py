import time as t

s = t.time()
print(f"Seconds since January 1, 1970: {s:,.4f} or {s:.2e} in scientific notation")
print(t.strftime("%b %d %Y", t.localtime()))

# Expected output:
#
# $>python format_ft_time.py | cat -e
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$
# $>
