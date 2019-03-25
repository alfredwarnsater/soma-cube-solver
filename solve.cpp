#include "allmoves.h"
#include <iostream>
#include <bitset>

using namespace std;

int counter = 1;

void print_bits(int a){
	bitset<32> x(a);
	cout << x << endl;
}

vector<vector<int>> solutions;

void solve(int at, int sol, vector<int> moves){
	if(at == 7){
		solutions.push_back(moves);
		return;
	}
	for(auto it : all_moves[at]){
		if((it & sol) == 0){
			moves[at] = it;
			solve(at+1, (it | sol), moves);
		}
	}
}

int main(){	
	vector<int> init_moves(7, 0);
	solve(0, 0, init_moves);
	for(auto move : solutions[0]){
		print_bits(move);
	}
}
