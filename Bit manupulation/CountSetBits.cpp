#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    int x = n;
    int bits = 0;
    while(x){
        x &= x-1;
        bits++;
    }
    cout<<bits<<endl;
    return 0;
}