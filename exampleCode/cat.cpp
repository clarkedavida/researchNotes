#include <string>
#include <iostream>

void narrate(std::string sentence) {
  std::cout << sentence << std::endl;
}

class CAT {
public:

  std::string _name;
  std::string _stomachContents;
  bool _isHungry;

  CAT(std::string name) {
    _name = name;
    _stomachContents = "";
    _isHungry = true;
    narrate("And the Lord said 'Let there be "+_name+"'.");
  };

  ~CAT() { 
    narrate(_name+" has perished."); 
  };

  void ignore() { 
    narrate(_name+" ignores User..."); 
  }

  void eat(std::string food) {
    if(_isHungry) {
      narrate(_name+" eats "+food+".");
      _stomachContents = food;
      _isHungry = false;
    } else {
      ignore();
    }
  }

  void speak() { 
    narrate(_name+" says 'meow'."); 
  }

  void areYouHungry() { 
    if(_isHungry) speak(); 
  }
};

int main () {

  CAT cat("Chooky");
  narrate("User says 'hello' to "+cat._name+".");
  cat.speak();
  narrate("User asks if "+cat._name+" is hungry.");
  cat.areYouHungry();
  narrate("User gives "+cat._name+" some tuna.");
  cat.eat("tuna");
  narrate(cat._name+" is full of "+cat._stomachContents+".");

  return 0;
}
