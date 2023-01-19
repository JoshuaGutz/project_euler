#include <stdio.h>
#include "gutz_math.h"

void runningNotes()
{
	/*
	THE FOLLOWING FOUR COMMANDS PREPARE AND RUN THIS PROGRAM
		gcc -c gutz_math.c;
		gcc -c 031_coin_sums.c;
		gcc -o 031_coin_sums 031_coin_sums.o gutz_math.o;
		./031_coin_sums;

	*/
}

void pe_031_notes()
{
	/*
	Coin sums
	031_coin_sums.c
	In England the currency is made up of pound, L, and pence, p, and 
	there are eight coins in general circulation:

	1p, 2p, 5p, 10p, 20p, 50p, L1 (100p), and L2 (200p).
	It is possible to make L2 in the following way:

	1*L1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
	How many different ways can L2 be made using any number of coins?
	*/
}

int countWaysToSumCoins(int n, int coins[], int num_coins, int answer[])
{
	//TRIEDTO USE RECURSION ON THIS METHOD
	// Retun How many different ways n can be made using coins
	int different_ways = 0;

	// usable coins are only those where coins[i] <= n
	int i;

	int num_usable_coins = 0;

	for(i = 0; i < num_coins; i++)
	{
		if(coins[i] <= n)
		{
			num_usable_coins++;
		}
	}

	if(num_usable_coins == 0)
	{
		return 0;
	}


	int multiplier;

	for(i = 0; i < num_coins; i++)
	{
		multiplier = 1;
		while(multiplier * coins[i] <= n)
		{
			if(n - multiplier * coins[i] == 0)
			{

			}


			multiplier++;
		}
	}

	return answer[0];
}

int countWaysToSumCoins2(int n, int coins[], int num_coins, int answer[])
{
	// Retun How many different ways n can be made using coins
	int different_ways = 0;

	// usable coins are only those where coins[i] <= n
	int a, b, c, d, e, f, g, h, i;
	int sum = 0;

	int vector[num_coins];

	for(a = 0; a <= 200; a++)
	{
		vector[0] = a;
		sum = 0;
		for(i = 0; i < num_coins; i++)
		{
			sum = sum + vector[i] * coins[i];
			printf("sum,vector,coin=%d,%d,%d\n", sum,vector[i],coins[i]);
		}
		if(sum > n)
		{
			display(a);
			continue;
		}
		if(sum == n)
		{
			different_ways++;
			continue;
		}
		sum = 0;
		for(b = 0; b <= 100; b++)
		{
			vector[1] = b;
			sum = 0;
			for(i = 0; i < num_coins; i++)
			{
				sum = sum + vector[i] * coins[i];
			}
			if(sum > n)
			{
				continue;
			}
			if(sum == n)
			{
				different_ways++;
				continue;
			}
			sum = 0;
			for(c = 0; c <= 40; c++)
			{
				vector[2] = c;
				sum = 0;
				for(i = 0; i < num_coins; i++)
				{
					sum = sum + vector[i] * coins[i];
				}
				if(sum > n)
				{
					continue;
				}
				if(sum == n)
				{
					different_ways++;
					continue;
				}
				sum = 0;
				for(d = 0; d <= 20; d++)
				{
					vector[3] = d;
					sum = 0;
					for(i = 0; i < num_coins; i++)
					{
						sum = sum + vector[i] * coins[i];
					}
					if(sum > n)
					{
						continue;
					}
					if(sum == n)
					{
						different_ways++;
						continue;
					}
					sum = 0;
					for(e = 0; e <= 10; e++)
					{
						vector[4] = e;
						sum = 0;
						for(i = 0; i < num_coins; i++)
						{
							sum = sum + vector[i] * coins[i];
						}
						if(sum > n)
						{
							continue;
						}
						if(sum == n)
						{
							different_ways++;
							continue;
						}
						sum = 0;
						for(f = 0; f <= 5; f++)
						{
							vector[5] = f;
							sum = 0;
							for(i = 0; i < num_coins; i++)
							{
								sum = sum + vector[i] * coins[i];
							}
							if(sum > n)
							{
								continue;
							}
							if(sum == n)
							{
								different_ways++;
								continue;
							}
							sum = 0;
							for(g = 0; g <= 2; g++)
							{
								vector[6] = g;
								sum = 0;
								for(i = 0; i < num_coins; i++)
								{
									sum = sum + vector[i] * coins[i];
								}
								if(sum > n)
								{
									continue;
								}
								if(sum == n)
								{
									different_ways++;
									continue;
								}
								sum = 0;
								for(h = 0; h <= 1; h++)
								{
									vector[7] = h;
									sum = 0;
									for(i = 0; i < num_coins; i++)
									{
										sum = sum + vector[i] * coins[i];
									}
									if(sum > n)
									{
										continue;
									}
									if(sum == n)
									{
										different_ways++;
										continue;
									}
									sum = 0;
//printf("%d,%d,%d,%d,%d,%d,%d,%d\n",
//	vector[0],vector[1],vector[2],vector[3],
//	vector[4],vector[5],vector[6],vector[7]);
								}
							}
						}
					}
				}
			}
		}
	sum = 0;
	}


									//printArray(vector, num_coins);
									//printf("\n");



	return different_ways;
}


int main()
{
	int n = 6;
//	int coins[] = {200, 100, 50, 20, 10, 5, 2, 1};
	int coins[] = {1, 2, 5, 10, 20, 50, 100, 200};
	int num_coins = 8;

	int answer[1] = {0};

	display(countWaysToSumCoins2(n, coins, num_coins, answer));
	n = 200;
//	display(countWaysToSumCoins(n, coins, num_coins, answer));
	return 0;
}
