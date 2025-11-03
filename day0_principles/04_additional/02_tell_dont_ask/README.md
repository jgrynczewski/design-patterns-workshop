## Definicja
**Tell**: Mów obiektom co mają robić
**Don't Ask**: Nie pytaj o stan, żeby potem nim manipulować

## Istota zasady
Obiekt sam zarządza swoim stanem i zachowaniem.

## ❌ Violation (ASK):
```python
if account.get_balance() >= amount:
    account.set_balance(account.get_balance() - amount)
```

✅ Solution (TELL):
```python
account.withdraw(amount)
```

Dlaczego lepsze?

- Enkapsulacja — obiekt ukrywa szczegóły implementacji
- Bezpieczeństwo — validation logic w jednym miejscu
- Czytelność — intencja kodu jaśniejsza

Sprawdź przykłady: violation_basic.py kontra solution_basic.py
