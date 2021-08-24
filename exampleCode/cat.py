class CAT:

  "A class for good cats."

  def __init__(self, name):
    self._name = name
    self._isHungry = True
    self._stomachContents = ""
    print("And the Lord said 'Let there be "+self._name+"'.")

  def __del__(self):
    print(self._name+" has perished.")

  def ignore(self):
    print(self._name+" ignores User...")

  def eat(self, food):
    if(self._isHungry):
      print(self._name+" eats "+food+".")
      self._stomachContents = food
      self._isHungry = False
    else:
      self.ignore()

  def speak(self):
    print(self._name+" says 'meow'.")

  def areYouHungry(self):
    if self._isHungry:
      self.speak()

class MEANCAT(CAT):
  "A class for naughty cats."

  def speak(self):
    print(self._name+" says 'HISS'!")


def roleCall(cat):
  cat.speak()

print(CAT.__doc__)

niclai = CAT("Niclai")
print("User says 'hello' to "+niclai._name+".")
niclai.speak()
print("User asks if "+niclai._name+" is hungry.")
niclai.areYouHungry()
print("User gives "+niclai._name+" some savory salmon.")
niclai.eat("savory salmon")
print(niclai._name+" is full of "+niclai._stomachContents+".")
print("Here "+niclai._name+" have some more fish.")
niclai.eat("savory salmon")
print("Alright then.")

silky=MEANCAT("Silky")
print("User gives "+silky._name+" some tasty tuna.")
silky.eat("tasty tuna")
print(silky._name+" is full of "+silky._stomachContents+".")
print("Cats, sound off!")
roleCall(niclai)
roleCall(silky)
print("Wow "+silky._name+" that's rude. Begone!")
del silky
print("Much better.")
