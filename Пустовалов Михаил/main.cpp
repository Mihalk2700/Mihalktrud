#include <iostream>
using namespace std;
int main() {
	int p,n,d,k;
	cout << "p=";
	cin >> p;
	cout << endl;
	cout << "n=";
	cin >> n;
	cout << endl;
	k=1;
	d=0;
	while(n!=0){
		d+=n%10*k;
		k=k*p;
		n=n/10;
	}
	cout << d;
	return 0;
}
