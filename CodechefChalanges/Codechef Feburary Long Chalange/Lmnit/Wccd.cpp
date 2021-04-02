#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
    ll n;
    cin>>n;
    ll shopes[n];
    ll weights[n];
    ll maxi = 0;
    for(ll i = 0; i < n; i++){
        cin>>shopes[i];
        weights[shopes[i]] = 0;
        weights[shopes[i]] += shopes[i];
        if (weights[shopes[i]] >= maxi){
            maxi = weights[shopes[i]];
        }
    }
    ll index = 0;
    for (ll i = 0; i < n; i++){
        if (weights[i] == maxi){
            index = i;
            break;
        }
    }
    cout<<(maxi/index)<<"\n";
    for (ll i = 0; i < n; i++){
        if (shopes[i] == index){
            cout<<(i+1)<<" ";
        }
    }
    return 0;
}