#include <iostream>
using namespace std;
int main() {
	int i,c,n;
	bool l;
	i=2;
	cin >> n;
	int d[n-2];
	for (int a=0;a<n-2;a++){
		d[a]=i;
		i++;
		cout << d[a];
	}
	i=0;
	for (int a=0;a<n-2;a++){
		if (d[a]==i*2){
			d[a]=0;
		}
		i++;
		cout << d[a];
	}
	return 0;
}
