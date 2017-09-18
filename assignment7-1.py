text = "X-DSPAM-Confidence:    0.8475"
pos=text.find(' ')
print(pos)
host=text[pos:len(text)]
host=host.strip()
print(host)