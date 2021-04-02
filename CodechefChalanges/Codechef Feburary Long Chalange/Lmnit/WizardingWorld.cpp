#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
    int t;
    cin>>t;
    while(t){
        int a,b,c,diamond_count;
        diamond_count = 0;
        cin>>a>>b>>c;

        while(true){
            if ((c >= 2) && (b >= 1)) {
                int x = c/2;
                if (b >= x){
                    c -= x*2;
                    b -= x;
                    diamond_count += 3*x;
                } else {
                    c -= b*2;
                    diamond_count += 3*b;
                    b = 0;
                }
            } else if ((a >= 1) && (b >= 2)){
                int x = b/2;
                if (a >= x){
                    b -= x*2;
                    a -= x;
                    diamond_count += 3*x;
                } else {
                    b -= a*2;
                    diamond_count += 3*a;
                    a = 0;
                }
            } else {
                cout<<diamond_count<<endl;
                break;
            }
        }
        t--;
    }
    return 0;
}