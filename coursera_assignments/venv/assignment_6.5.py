text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(':')
new_text = float(text[(pos+1):].strip())
print(new_text)