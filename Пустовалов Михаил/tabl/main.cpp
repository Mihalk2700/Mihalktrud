#include <iostream>
using namespace std;
int main() {
	int p,n;
	setlocale(LC_ALL,"");
	cout << "¬ведите p (2<p<10)=";
	cin >> p;
	for (int x=1;x<p;x++){
			for (int y=1;y<p;y++){
			n=x*y/p*10+x*y%p;
			cout << n;
		}
		cout << endl;	
	}
	return 0;
}
