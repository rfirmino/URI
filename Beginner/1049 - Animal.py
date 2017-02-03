v1 = input()
v2 = input()
v3 = input()
l = (v1,v2,v3)
dict = {('vertebrado','mamifero','onivoro'): 'homem', ('vertebrado','mamifero','herbivoro'): 'vaca', 
('vertebrado','ave','carnivoro'): 'aguia', ('vertebrado','ave','onivoro'): 'pomba',
('invertebrado','inseto','hematofago'): 'pulga', ('invertebrado','inseto','herbivoro'): 'lagarta',
('invertebrado','anelideo','hematofago'): 'sanguessuga', ('invertebrado','anelideo','onivoro'): 'minhoca'}
print(dict[l])
