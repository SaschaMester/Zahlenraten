// Datei: random.cpp
// Quelle: http://magazin.c-plusplus.de/artikel/Zuf%E4lle%20gibt%60sFragezeichenAusrufezeichen%20-%20Funktionen%20rund%20um%20rand,%20Random%20und%20den%20Zufall

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
   static int rnd_nobias(int lowerbounds, int upperbounds)
   {
      static Random dummy;
      assert(upperbounds - lowerbounds < RAND_MAX);
 
      int rawNumber;
      int count = upperbounds - lowerbounds + 1;
 
      if (count == 2 || count == 4 || count == 8 ||
          count == 16 || count == 32 || count == 64 ||
          count == 128 || count == 256 || count == 512 ||
          count == 1024 || count == 2048 || count == 4096 ||
          count == 8192 || count == 16384)
          return rnd(lowerbounds, upperbounds);
 
      /* dieser Programmabschnitt kann auch noch eleganter formuliert
         werden, allerdings ist dann die Wirkung nicht mehr auf den
         ersten Blick erkennbar:
      if ((count - 1) & count == 0)
          return rnd(lowerbounds, upperbounds);
         erfüllt den Zweck ebenfalls
      */
 
      int ignoreBoundary = (RAND_MAX / count) * count;
 
      do
      {
         rawNumber = std::rand();
      } while (rawNumber > ignoreBoundary);
 
      return lowerbounds + rawNumber % (upperbounds - lowerbounds + 1);
   }
};

#endif
