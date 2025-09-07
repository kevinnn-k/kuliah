from sympy import symbols
from sympy.logic.boolalg import And, Not, Implies
from sympy.logic.inference import satisfiable

def entails(kb, q):
    return not satisfiable(And(*(kb + [Not(q)])))

def show_case(title, kb, q):
    print(f"[n[{title}]")
    print("   KB:", And(*kb))
    print("   q:", q)
    print("   KB = q ?", entails(kb, q))

Manusia, Mortal, Socrates = symbols('Manusia Mortal Socrates')
SocratesManusia, SocratesMortal = symbols('SocratesManusia, SocratesMortal')
KB1 = [Implies(SocratesManusia, SocratesMortal), SocratesManusia]
Q1 = SocratesMortal
show_case("1) Socrates", KB1, Q1)