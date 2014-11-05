// Datei: random.cpp
#ifndef _RANDOM_H
#define _RANDOM_H

#include <cstdlib>
#include <ctime>
#include <cassert>
 
class Random
{
private:
   Random()
   {
      std::srand(static_cast<int>(std::time(NULL)));
   }
public:
   static int rnd(int lowerbounds, int upperbounds)
   {
      static Random dummy;
      assert(upperbounds - lowerbounds < RAND_MAX);
      return lowerbounds + std::rand() % (upperbounds - lowerbounds + 1);
   }
};

#endif
