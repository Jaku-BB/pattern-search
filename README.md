# Algorytmy wyszukiwania wzorca w tekście

## Algorytm naiwny

Działa w czasie O((x-y + 1) * y), gdzie **x** to długość tekstu, a **y** to długość wyszukiwanego wzorca.

### Zalety:

- prostota implementacji
- łatwość zrozumienia

### Wady:

- złożoność obliczeniowa
- niska wydajność, zwłaszcza dla długich tekstów

## Algorytm Knutha-Morrisa-Pratta

Działa w czasie O(x + y), gdzie **x** to długość tekstu, a **y** to długość wyszukiwanego wzorca.

### Zalety:

- wysoka wydajność, widoczna zwłaszcza dla długich tekstów, dzięki tablicy LPS
- złożoność obliczeniowa

### Wady:

- skomplikowana implementacja
- konieczność zastosowania dodatkowej tablicy LPS

## Podsumowanie

Algorytm KMP oferuje znacznie lepszą wydajność w porównaniu do algorytmu naiwnego, zwłaszcza dla długich tekstów. 
Jednakże, jeśli tekst i wzorzec są stosunkowo krótkie, różnica w wydajności może być nieznaczna.