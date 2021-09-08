text = "X-DSPAM-Confidence:    0.8475"

confidence = text.find("0")

confidence = float(text[confidence:])

print(confidence)