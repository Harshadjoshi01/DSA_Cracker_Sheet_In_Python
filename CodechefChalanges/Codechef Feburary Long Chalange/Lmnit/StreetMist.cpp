#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
    int n;
    cin>>n;
    ll tiles[n];
    for(int i=0; i<n; i++){
        cin>>tiles[i];
    }
    for(int i=0; i<n-1; i++){
        ll a = tiles[i] + tiles[i+1];
        cout<<a<<" ";
    }
    cout<<tiles[n-1]<<endl;
    return 0;
}