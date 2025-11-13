"""05-palindromes
Permet de vérifier si une chaine est un palindrome ou pas.
"""

def ispalindrome(s):
    """Vérifie si une chaîne est un palindrome ou pas.

    @param s: Chaîne de caractères à tester.
    @type s: str
    @return: True si la chaîne est un palindrome, False sinon.
    @rtype: bool
    """

    s_clean = s.lower()

    not_alpha = "àâäéèêëïîôöùûüçñ"
    to_alpha = "aaaeeeeiioouuucn"

    not_alpha_char = [char for char in s if not char.isalpha() and not char.isalnum()]
    for char in not_alpha_char:
        not_alpha+=char
        to_alpha+=" "

    clean_trans = str.maketrans(not_alpha, to_alpha)

    s_clean = s_clean.translate(clean_trans).replace(" ", "")
    return s_clean == s_clean[::-1]

def main():
    """Fonction principale"""
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(f"{s}: {ispalindrome(s)}")

if __name__ == "__main__":
    main()
