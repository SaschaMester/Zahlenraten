#include <iostream>
#include "random.cpp"

using namespace std;

int zahl_ausdenken(int minZahl, int maxZahl)
{
   int zahl;
   zahl = Random::rnd(minZahl, maxZahl);
   return zahl;
}

void play(int gedachte_Zahl, int trial)
{
   int i;
   int rateversuch;
   for ( i = 1; i < trial+1; i++)
   {
      cout << "Bitte gebe deinen " << i << ". Rateversuch ein: " << endl;
      cin >> rateversuch;
      if (rateversuch < gedachte_Zahl)
      {
         cout << "Mein Zahl ist größer als " << rateversuch << "." << endl;
      }
      else if (rateversuch > gedachte_Zahl)
      {
         cout << "Meine Zahl ist kleiner als " << rateversuch << "." << endl;
      }
      else
      {
         cout << "Richtig!" << endl;
         break;
      }
   }
}


void raten(int gedachte_Zahl)
{
   cout << "Ich habe mir eine Zahl zwischen 1 und 120 ausgedacht" << endl;
   cout << "Du hast 3 Versuche, meine Zahl zu erraten" << endl;
   play(gedachte_Zahl, 3);
}


int main()
{
   int rateversuch;
   int gedachte_Zahl = zahl_ausdenken(1, 120);
   raten(gedachte_Zahl);
}
