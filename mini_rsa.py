#!/usr/bin/env python3
"""
Mini RSA: expoente `e` pequeno, com M^e so um pouco maior que N.

A ideia: c = M^e mod N = M^e - k*N para algum k pequeno. Entao
M^e = c + k*N. Testamos k = 0, 1, 2, ... ate `c + k*N` ser uma
potencia e-esima perfeita; a raiz e-esima exata e a mensagem M.

Uso:
    1. Preencha N, e, c com os valores do arquivo `values`.
    2. Rode o script.
"""

# ── Preencha com os valores do arquivo `values` ──
N = 0   # TODO: cole o N
e = 0   # TODO: cole o e (normalmente pequeno, tipo 3)
c = 0   # TODO: cole o c


def raiz_inteira(x, n):
    """Maior inteiro r tal que r**n <= x, sem usar float (precisao exata)."""
    if x < 0:
        raise ValueError("x deve ser nao-negativo")
    lo, hi = 0, 1
    while hi ** n <= x:
        hi *= 2
    while lo < hi - 1:
        mid = (lo + hi) // 2
        if mid ** n <= x:
            lo = mid
        else:
            hi = mid
    return lo


def main(limite_k=10_000_000):
    if N == 0 or e == 0 or c == 0:
        raise SystemExit("Preencha N, e e c antes de rodar.")

    for k in range(limite_k):
        alvo = c + k * N
        r = raiz_inteira(alvo, e)
        if r ** e == alvo:
            print("k =", k)
            mensagem = r.to_bytes((r.bit_length() + 7) // 8, "big")
            print("Bytes:", mensagem)
            try:
                print("Mensagem:", mensagem.decode())
            except UnicodeDecodeError:
                print("(nao decodifica como UTF-8 direto; confira os bytes acima)")
            return

    print("Nao encontrou com k ate", limite_k, "- aumente o limite_k.")


if __name__ == "__main__":
    main()