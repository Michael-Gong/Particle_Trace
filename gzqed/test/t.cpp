#include <random>
#include <iostream>

int main(int argc, char **argv)
{
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0, 1);
    double uniform0n01,probability;
	for (int i=0;i<=99;i++)
	{   
	    uniform0n01 = dis(gen);
  	    probability = (rand()/(double)(RAND_MAX));
	    std::cout<<uniform0n01<<" and "<<probability<<std::endl;
        }
}
