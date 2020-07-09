text = "X-DSPAM-Confidence:    0.8475"

com = text.find('0')
com_real = int(com)

text_refine = text[com_real:]

print(float(text_refine))