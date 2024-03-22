def longestEvenWord(sentence):
#   """
#   Menemukan kata pertama dalam kalimat dengan panjang genap dan lebih besar dari atau sama dengan panjang kata lain yang panjangnya genap.

#   Args:
#     sentence: String yang berisi kalimat.

#   Returns:
#     String yang berisi kata terpanjang dengan panjang genap.
#   """
  words = sentence.split()
  longest_even_word = ""
  for word in words:
    if len(word) % 2 == 0 and len(word) >= len(longest_even_word):
      longest_even_word = word
  return longest_even_word

# Contoh penggunaan
sentence = "Ini adalah kalimat contoh dengan beberapa kata."
longest_even_word = longestEvenWord(sentence)
print(f"Kata terpanjang dengan panjang genap: {longest_even_word}")
