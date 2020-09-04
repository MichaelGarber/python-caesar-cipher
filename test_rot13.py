from rot13 import  rot13

def test_rot13():
    assert(rot13("SERR PBQR PNZC") == "FREE CODE CAMP")
    assert(rot13("SERR CVMMN!") == "FREE PIZZA!")
    assert(rot13("SERR YBIR?") == "FREE LOVE?")
    assert(rot13("GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT.") == "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.")
    print("YOUR CODE IS CORRECT!")